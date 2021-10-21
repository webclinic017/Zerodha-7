from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.
from rest_framework.response import Response
from rest_framework import serializers, views
from kiteconnect_source.source.testing import dummy 
from rest_framework.decorators import api_view
from kiteconnect import KiteConnect
from django.contrib.sessions.models import Session
from datetime import datetime,timedelta
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponse
# from rest_framework.authentication import BasicAuthentication # SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
import random
import logging
import json
import psycopg2
import sys
import threading
# from psycopg2.extras import Json
import os.path
import enum
# import pandas as pd
import pytz
from pytz import timezone
import sched, time
from decimal import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.template.response import TemplateResponse
import threading
import schedule
from multiprocessing import Queue
import multiprocessing 


s = sched.scheduler(time.time, time.sleep)

logging.basicConfig(level=logging.DEBUG)
_default_login_uri = "https://kite.trade/connect/login/"
global_message=""





# login verification
def login_view(request):
    if request.method == "POST":
        # getting the username and password
        username = request.POST.get('username')
        print("username :",username)
        password = request.POST.get('password', 'false')
        user = authenticate(request, username=username, password=password)
        if user:
            connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM auth_user WHERE username=\'"+username+"\'")
            user_id = cursor.fetchone()
            print('user_id :',user_id)
            userid = 0
            for i in user_id:
                userid +=i
            print("userid :",userid) 
            request.session['user_id'] = userid
            userid = str(userid)
            connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
            cursor = connection.cursor()
            cursor.execute("UPDATE current_login_user SET username = 'vipuljoshi', user_id =\'"+userid+"\'")
            connection.commit()

            print("login success")
            # if login successfull
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            # if no next then resume the render by redirecting it to next possible page
            # return HttpResponseRedirect(reverse('home'))
            print("request :",request)
            return render(request,'callbackurl.html')

        else:
            print("not login")
            messages.error(request, 'Please enter the correct credentials')
            return TemplateResponse(request, "login.html")
    else:
        # if not logged in then
        return render(request, "login.html")
    # if this is not a POST request
    return render(request, "login.html")


def sesion_fun(request):
    # set new data
    user_id = request.user.id
    print("user_id :",user_id)
    request.session['user_id'] = user_id
    return HttpResponse("Session Data Saved")

# def fun2(request):
#     response = ""
#     if request.session.get('user_id'):
#         user_id = request.session.get('user_id')
#         print(user_id)
#     return HttpResponse("Session  get data")



# @api_view(['GET','POST'])
@login_required(login_url='login_view')
def home(request):
    print("home function")
    user_id = request.user.id
    # request.session['current_user_id']= user_id
    # user_id = request.user.id
    # if request.session.get('current_user_id'):
        # print("user_id :=",user_id)
    print("session created")
    current_user = request.user
    print(current_user)
    user_id = request.user.id
    user_id = str(user_id)
    print("------------")
    print(type(user_id), str(user_id))       
    try:
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND t.user_id ="+ user_id)
        rows = cursor.fetchall()
        dict_result = []
        for row in rows:
            dict_result.append(dict(row))
        cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='True' AND t.user_id =1"+ user_id)
        rows2 = cursor.fetchall()
        dict_result_2 = []
        for row in rows2:
            dict_result_2.append(dict(row))
            print(dict_result_2)
        cursor.close()
        connection.close()
        print("dict_result ",dict_result)
        print("dict_result_2 ",dict_result_2)
        return render(request, 'index.html',{"content":dict_result,"dict_result_2":dict_result_2,"current_user":current_user,"user_id":user_id})        

    except:
        print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})

    return render(request, 'index.html')




#  render to krishnas login to page
@api_view(['GET'])
def get_login_url(request):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print("-------------=======-------------------------------===")
    userid = user_id[0]
    userid = str(userid)
    print('idd')
    cursor.execute("SELECT api_key FROM auth_user WHERE id=\'"+userid+"\'")
    api_key = cursor.fetchone()
    api_key = api_key[0]
    kite = KiteConnect(api_key=api_key)
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    # _default_login_uri = "https://kite.trade/connect/login/"
    # global_message=""


    url= kite.login_url()
    print("request :",request)
    print(' login url :',url)
    return Response({"status":"success", "message": "success","content":url})

# Collect all the instuments
@api_view(['GET'])
def get_instruments(request):        
    print(" get_instruments function calling ")
    try:        
        print("inside try")    
        exchange=None
        if request.query_params.get("exchange") is not None:
            #exchange=request.query_params['exchange']
            switcher={
                '1':'BSE',
                '2':'MCX',
                '3':'NFO',
                '4':'NSE'
            }
            exchange=switcher.get(request.query_params['exchange'])
            print("exchange :",exchange)
        if request.query_params.get("symbolName") is not None:
            symbolName=request.query_params['symbolName']
            print("symbolName")
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        if exchange is not None:
            # postgres_insert_query = "SELECT public.get_instruments('"+symbolName+"','"+exchange+"')"
            # postgres_insert_query="SELECT items->'tradingsymbol' AS tradingsymbol,items->'exchange' AS exchange,items->'exchange_token' AS exchange_token,items->'expiry' AS expiry,items->'instrument_token' AS instrument_token,items->'instrument_type' AS instrument_type,items->'last_price' AS last_price,items->'lot_size' AS lot_size,items->'name' AS name,items->'segment' AS segment,items->'strike' AS strike,items->'tick_size' AS tick_size FROM public.instruments WHERE items->>'tradingsymbol' LIKE '"+symbolName+"' AND items->>'exchange' ='"+exchange+"'"
            # postgres_insert_query="SELECT * FROM public.instruments WHERE items->>'tradingsymbol' LIKE '"+symbolName+"' AND items->>'exchange' ='"+exchange+"'"
            # postgres_insert_query="SELECT * FROM public.instruments WHERE "items"::text ILIKE  '%NSE%' AND "items"::text ILIKE  '%CPSE %'"
            postgres_insert_query = "SELECT public.get_instruments_v1('"+symbolName+"','"+exchange+"')"
            print("postgres_insert_query :",postgres_insert_query)
        else:
            # postgres_insert_query = "SELECT public.get_instruments('"+symbolName+"','')"  
            # postgres_insert_query="SELECT * FROM public.instruments WHERE items->>'tradingsymbol' LIKE '"+symbolName+"' AND items->>'exchange' =''"
            pass
               

        cursor.execute(postgres_insert_query, (symbolName,exchange,))
        rows = cursor.fetchall()
        # print("-----------------------------------------------------------------------------")
        print('rows :',rows)
        # for row in rows:
        #     print(row)       
        cursor.close()
        connection.close()
        return Response({"status":"success", "message": "success","content":rows})
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"success", "message": sys.exc_info()[0]})

def save_instruments(instruments):
    print("this is save instruments")
    try:
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()        
        postgres_delete_query = """ Delete from public.instruments"""
        cursor.execute(postgres_delete_query)
        # connection.commit()
        # cursor.close()
        # connection.close()
               
        # connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        # cursor = connection.cursor()

        for item in instruments: 
            instrumentsJson=json.dumps(item, indent=4, sort_keys=True, default=str)
            postgres_insert_query = """ INSERT INTO instruments (items) VALUES (%s)"""
            cursor.execute(postgres_insert_query, (instrumentsJson,))
            # postgres_delete_query = """ Delete from public.instruments  WHERE created_on is null or created_on < (select created_on from public.instruments order by created_on desc LIMIT 1)"""
            # cursor.execute(postgres_delete_query)
        connection.commit()
        cursor.close()
        connection.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
    pass

# Saving all instruments in DB 
@api_view(['GET'])
def sync_instruments(request):  
    try:
        print("inside")
        exchanges=["NSE","BSE","NFO","MCX"]
        # exchanges=["NSE"]
        instrumentsCollection=[]
        # dummyCollection=[]
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()   

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        print("-------------=======-------------------------------===")
        userid = user_id[0]
        userid = str(userid)
        cursor.execute("SELECT api_key FROM auth_user WHERE id=\'"+userid+"\'")
        api_key = cursor.fetchone()
        api_key = api_key[0]
        print("api_key :",api_key)
        print("exchanges :",exchanges)
        kite = KiteConnect(api_key=api_key)
        for exchange in exchanges:
            # print('exchange :',exchange)
            instrument=kite.instruments(exchange)
            # print("instrument :",instrument)
            instrumentsCollection=instrumentsCollection+instrument
            # print("instrumentsCollection :",instrumentsCollection)
            # dummyCollection=instrument
        # instrumentsJson=json.dumps(instrumentsCollection, indent=4, sort_keys=True, default=str)
        save_instruments(instrumentsCollection)        
        return Response({"status":"success", "message": "success"})
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"fail", "message": "failure","content": sys.exc_info()})

import random

from django.shortcuts import redirect

from django.db import connection
# Save data data from the trading form
from django.contrib.auth.models import User

# @api_view(['POST'])
# def save_trigger_order(request):   
#     try:            
#         print("this is trigger funxction")
#         print("___________________________________")
#         user_id = request.session.get('user_id')
#         print("session user_id:========================",user_id)
#         # triggers = {{},{},{}}
#         # orders = {{},{}}
#         print("in save trigger")
#         trigger_name=request.data["trigger"]["trigger_name"]
#         print('trigger_name',trigger_name)
#         symbol=request.data["trigger"]["symbol"]
#         print('symbol',symbol)
#         trigger_condition_id=request.data["trigger"]["trigger_condition_id"]
#         print('trigger_condition_id',trigger_condition_id)
#         trigger_criteria=  json.dumps(request.data["trigger"]["trigger_criteria"])
#         print('trigger_criteria',trigger_criteria)
#         exchange_id=request.data["trigger"]["exchange_id"]
#         print('exchange_id',exchange_id)
#         # exchange_id = str(exchange_id)
#         buy_sell=request.data["order"]["buy_sell"]
#         print('buy_sell :',type(buy_sell))
#         print('buy_sell :',buy_sell)
#         # buy_sell = str(buy_sell)
#         quantity=request.data["order"]["quantity"] 
#         product_type=request.data["order"]["product_type"]
#         order_types=request.data["order"]["order_types"]
#         order_symbol=request.data["order"]["symbol"]
#         order_exchange_id=request.data["order"]["exchange_id"]
#         # order_price=request.data["order"]["price"]
#         # print('order_price :',order_price)
#         # trigger_price=request.data["order"]["trigger_price"]
#         # print('trigger_price :',trigger_price)

#         connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
#         cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
#         print("trigger_id=============================================================")
#         cursor.execute("SELECT MAX(trigger_id) FROM triggers")
#         trigger_id = cursor.fetchall()
#         print("trigger_id :: ",trigger_id)
#         trigger = trigger_id[0]
#         print("trigger :==== ",trigger)
#         triggerId = 0
#         for i in trigger:
#             triggerId +=i
#         triggerId = triggerId+1
#         triggerId = int(triggerId)
#         # print("triggerId : ",triggerId)
#         triggerId = json.dumps(triggerId)

#         cursor.execute("select trigger_name from triggers")
#         rows = cursor.fetchall()
#         trigger_list = []
#         for i in rows:
#             trigger_list.append(i[0])
#         if trigger_name in trigger_list:
#             print("yes exist")
#             messages.error(request, "Trigger name already exist")
#             return redirect('trading/')
#         else:
#             # return Response(serializer.data)
#             print("_________________________________________________________________")
#             user_id = json.dumps(user_id)
#             print("user_id :::::::::::::",type(user_id))
#             print(" before trigger insert ")
#             cursor.execute("INSERT INTO triggers(trigger_name, symbol, trigger_condition_id,trigger_criteria, exchange_id,user_id)VALUES (\'"+trigger_name+"\',\'"+symbol+"\',"+trigger_condition_id+",\'"+trigger_criteria+"\',"+exchange_id+","+user_id+")") 
            
#             cursor.execute("INSERT INTO orders(buy_sell,symbol,exchange_id,quantity,product_type,order_type,trigger_id,user_id)VALUES ("+buy_sell+",\'"+order_symbol+"\',"+order_exchange_id+","+quantity+","+product_type+","+order_types+","+triggerId+","+user_id+")") # 
            
#             print("inserted successfull")
#             connection.commit()
#             # rows = cursor.fetchone()
#             # cursor.close()
#             # connection.close()
#             return Response({"status":"success", "message": "success"})   
            
#     except:
#         # print("Unexpected error:", sys.exc_info()[0])
#         print("except error")
#         return Response({"status":"failure", "message": sys.exc_info()})


@api_view(['POST'])
def save_trigger_order(request):   
    try:            
        
        print("this is trigger funxction")
        print("___________________________________")
        user_id = request.session.get('user_id')
        print("session user_id:========================",user_id)
        # triggers = {{},{},{}}
        # orders = {{},{}}
        print("in save trigger")
        trigger_name=request.data["trigger"]["trigger_name"]
        print('trigger_name',trigger_name)
        symbol=request.data["trigger"]["symbol"]
        print('symbol',symbol)
        trigger_condition_id=request.data["trigger"]["trigger_condition_id"]
        print('trigger_condition_id',trigger_condition_id)
        trigger_criteria=  json.dumps(request.data["trigger"]["trigger_criteria"])
        print('trigger_criteria',trigger_criteria)
        exchange_id=request.data["trigger"]["exchange_id"]
        print('exchange_id',exchange_id)
        # exchange_id = str(exchange_id)
        buy_sell=request.data["order"]["buy_sell"]
        print('buy_sell :',type(buy_sell))
        print('buy_sell :',buy_sell)
        # buy_sell = str(buy_sell)
        quantity=request.data["order"]["quantity"] 
        product_type=request.data["order"]["product_type"]
        order_types=request.data["order"]["order_types"]
        order_symbol=request.data["order"]["symbol"]
        order_exchange_id=request.data["order"]["exchange_id"]
        # order_price=request.data["order"]["price"]
        # print('order_price :',order_price)
        # trigger_price=request.data["order"]["trigger_price"]
        # print('trigger_price :',trigger_price)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        print("trigger_id=============================================================")
        cursor.execute("SELECT MAX(trigger_id) FROM triggers where user_id = "+user_id)
        trigger_id = cursor.fetchall()
        print("trigger_id :: ",trigger_id)
        trigger = trigger_id[0]
        print("trigger :==== ",trigger)
        # triggerId = 0
        # for i in trigger:
        #     triggerId +=i
        # triggerId = triggerId+1
        # triggerId = int(triggerId)
        # print("triggerId : ",triggerId)
        # triggerId = json.dumps(triggerId)

        print("_________________________________________________________________")
        user_id = json.dumps(user_id)
        print("user_id :::::::::::::",type(user_id))
        cursor.execute("INSERT INTO triggers(trigger_name, symbol, trigger_condition_id,trigger_criteria, exchange_id,user_id)VALUES (\'"+trigger_name+"\',\'"+symbol+"\',"+trigger_condition_id+",\'"+trigger_criteria+"\',"+exchange_id+","+user_id+")  RETURNING trigger_id") 
        last_trigger_id = cursor.fetchone()
        print("last_trigger_id :",last_trigger_id)
        last_trigger_id = 925
        cursor.execute("SELECT * FROM trigger_condition_list where trigger_list like '%"+last_trigger_id+"%'")    
        trigger_detail = cursor.fetchone()
        print('trigger_detail :',trigger_detail)

        cursor.execute("UPDATE FROM trigger_condition_list SET trigger_list = '925,'+'926,' WHERE trigger_id = 4")

        # cursor.execute("INSERT INTO trigger_condition_list(trigger_list)VALUES ("+trigger+")") 
        
        # cursor.execute("INSERT INTO orders(buy_sell,symbol,exchange_id,quantity,product_type,order_type,trigger_id,user_id)VALUES ("+buy_sell+",\'"+order_symbol+"\',"+order_exchange_id+","+quantity+","+product_type+","+order_types+","+triggerId+","+user_id+")") # 

        print("inserted successfull")
        connection.commit()
        

        return Response({"status":"success", "message": "success"})   
        
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        print("except error")
        return Response({"status":"failure", "message": sys.exc_info()})


# Testing Purpose

@api_view(['GET'])
def place_order(request):
    try:
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = user_id[0]
        userid = str(userid)
        cursor.execute("SELECT token_id FROM auth_user WHERE id = "+userid)
        token_id = cursor.fetchone()
        access_token = token_id[0]
        # file1 = open("accesstoken.txt","r")
        # access_token=file1.read()
        # file1.close()

        cursor.execute("SELECT api_key FROM auth_user WHERE id=\'"+userid+"\'")
        api_key = cursor.fetchone()
        api_key = api_key[0]

        kite = KiteConnect(api_key=api_key)
        # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
        kite.set_access_token(access_token)
        order_id = kite.place_order(
        variety=kite.VARIETY_REGULAR,
        exchange=kite.EXCHANGE_NSE,
        tradingsymbol="INFY",
        transaction_type=kite.TRANSACTION_TYPE_BUY,
        quantity=1,
        product=kite.PRODUCT_CNC,
        order_type=kite.ORDER_TYPE_MARKET
        )
        return Response({"status":"success", "message": "success", "content":order_id})
    except:
        print("Unexpected error:", sys.exc_info()[0])       
        return Response({"status":"failure", "message": "failure"})
# WITH cte_film AS (SELECT json_array_elements(items) token FROM public.instruments ) SELECT  * FROM cte_film WHERE token->>'name' = 'CPSE INDEX';


# getting access token for login
def get_access_token():
    try:

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        print('user_id :',user_id)
        userid = user_id[0]
        print("userid :",userid) 
        userid = str(userid)
        print('userid :',userid)
        cursor.execute("SELECT token_id FROM auth_user WHERE id = "+userid)
        token_id = cursor.fetchone()
        print('token_id :',token_id)
        print('token_id :',type(token_id))
        request_token = token_id[0]

        # file1 = open("accesstoken.txt","r")
        # request_token=file1.read()
        # file1.close()
        return request_token
    except:
        return Response({"status":"failure", "message": "failure"})




# from django.contrib.sessions.models import Session

# def sesion_fun(request):
#     user_id = request.user.id
#     request.session['current_user_id']= user_id
#     # return user_id


# def fun2(request):
#     request.session.get('current_user_id')
#     print(request.session.get('current_user_id'))
#     return HttpResponse('working')




# def sesion_fun(request):
#     # set new data
#     user_id = request.user.id
#     print("user_id :",user_id)
#     request.session['user_id'] = user_id
#     return HttpResponse("Session Data Saved")

# def fun2(request):
#     response = ""
#     if request.session.get('user_id'):
#         user_id = request.session.get('user_id')
#         print(user_id)
#     return HttpResponse("Session  get data")





@api_view(['GET'])
def save_request_token(request):
    message="1"
    # try:
    print('save_request_token function ')

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()

    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print('user_id :',user_id)
    userid = user_id[0]
    print("userid :",userid) 
    userid = str(userid)

    cursor.execute("SELECT api_key FROM auth_user WHERE id=\'"+userid+"\'")
    api_key = cursor.fetchone()
    print('api_key :',api_key)
    api_key = api_key[0]
    print("api_key :",api_key)

    cursor.execute("SELECT secret_key FROM auth_user WHERE id=\'"+userid+"\'")
    secret_key = cursor.fetchone()
    secretkey = secret_key[0]
    print('secretkey :',secretkey)
    print('secretkey :',type(secretkey))

    request_token=request.query_params.get("request_token")
    kite = KiteConnect(api_key=api_key)
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    # secretkey = ''
    # if userid == "1":
    #     print('rsy')34fr
    #     secretkey = 'rl2phtbwxutl1fd2ke6t86z74nq7zl9w'
    # elif userid =='2':
    #     print('no')
    #     secretkey = 'uftaqv4ha7w9qbvvv9r16c7y9nr174va'
    print('secretkey :',secretkey)
    data = kite.generate_session(request_token,secretkey)
    access_token=data["access_token"]
    kite.set_access_token(data["access_token"])
    print("_____________________________________________________________________________________")

    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print('user_id :',user_id)
    userid = 0
    for i in user_id:
        userid +=i
    print("userid :",userid) 
    userid = str(userid)
    print('userid :',userid)

    # access_token = "v12mmmm"
    # print('access_token :',access_token)

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("UPDATE auth_user SET token_id =\'"+access_token+"\' WHERE id =\'"+userid+"\'")        
    connection.commit()
    print("updated")

    # f= open("accesstoken.txt","w+")
    # f.write(access_token)                                
    # f.close()
    return Response({"status":"success", "message": "success"})
    # return HttpResponse("done")
    # except:
    #     return Response({"status":"failure", "message": message,"error":sys.exc_info()})


# @api_view(['POST'])
# def get_dashboard_orders(request): 

#     user_id = request.user.id
#     user_id = str(user_id)
#     print(type(user_id), str(user_id))       
#     try:
#         connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
#         cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         # postgres_insert_query = "SELECT  t.trigger_name,t.symbol,e.exchange,c.trigger_condition,t.created_on,t.is_active, c.trigger_condition,b.buy_sell,o.quantity FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.orders o ON t.trigger_id=o.trigger_id JOIN public.master_buy_sell b ON o.buy_sell=b.buy_sell_id JOIN public.master_product_type p ON p.product_type_id=o.product_type"
#         postgres_insert_query = """SELECT * from public.get_open_orders()""" 
#         cursor.execute(postgres_insert_query,())      
#         rows = cursor.fetchall()
#         # print(rows)

#         dict_result = []
#         for row in rows:
#             dict_result.append(dict(row))
#         cursor.close()
#         connection.close()
#         return Response({"status":"success", "message": "success","content":dict_result})        
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         return Response({"status":"failure", "message": "failure"})




def get_triggers_orders():        
    try:
        print("-------------------------")
        print("get trigger orderf function")
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute("SELECT order_trigger_id FROM current_login_user")
        order_trigger_id = cursor.fetchone()
        print('order_trigger_id :',order_trigger_id)
        order_trigger_id = order_trigger_id[0]
        print("order_trigger_id :",order_trigger_id) 
        order_trigger_id = str(order_trigger_id)

        print('trigger trigger trigger trigger trigger trigger ::::',order_trigger_id)

        cursor.execute("SELECT trigger_name from triggers where trigger_id = "+order_trigger_id)
        order_trigger_name = cursor.fetchone()
        order_trigger_name = order_trigger_name[0]
        
        # order_trigger_names = str(order_trigger_name)
        print("order_trigger_name : ",type(order_trigger_name))
        cursor.execute("SELECT trigger_id from triggers where trigger_name =\'"+order_trigger_name+"\'")
        list_order_trigger_id = cursor.fetchall()
        print('list_order_trigger_id :',list_order_trigger_id)

        list_trigger_id = []
        for i in list_order_trigger_id:
            list_trigger_id.append(i[0])
        print("list_trigger_id ::",list_trigger_id)

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        print('user_id :',user_id)
        user_id = user_id[0]
        print("user_id :",user_id) 
        user_id = str(user_id)    
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id) 
        trigger_names_list = cursor.fetchall()
        print('trigger_names_list-------------------- :',trigger_names_list)
        trigger_names = []
        for i in trigger_names_list:
            trigger_names.append(i[0])
        print("trigger_names ::",trigger_names)
        

        print("trigger_names ::",trigger_names)

        # trigger_names = ['T49','T51']
        # print("before ----------------------------------------------")
        # cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name in %s" % (tuple(trigger_names),))
        # print("after ----------------------------------------------")
        # trigger_id = cursor.fetchall()
        # print("trigger_id :",trigger_id)


        # print("after ----------------------------------------------")
        # trigger = []
        # for i in trigger_id:
        #     trigger.append(i[0])

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        postgres_insert_query = """SELECT * from public.get_triggers_orders()"""
        cursor.execute(postgres_insert_query,()) 
        rows = cursor.fetchall()
        print('rows ::',rows)
        print('rows--------------------------------------------rows')
        order_trigger_id = int(order_trigger_id)
        ordertrigger_id = []
        ordertrigger_id.append(order_trigger_id)
        print('ordertrigger_id',ordertrigger_id)
        print('ordertrigger_id',type(ordertrigger_id))


        print('rows',rows)
        triggers = []
        for row in rows:
            for y in row:
                # print("inside ssecond for ",y)
                if y in list_trigger_id:
                    triggers.append(dict(row))
            # break
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("triggers ::::",triggers)
        cursor.close()
        connection.close()
        return triggers
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})

# import wmi
# After trading function called 
@api_view(['GET'])
def online_trigger(request):        
    try:
        triggers=get_triggers_orders()
        print("triggres ::=",triggers)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('inside onlie_trigger function')
        # print("triggers :",triggers)
        # global multi_cond_check
        multi_cond_check = False 
        # for trigger in triggers:
        #     try:

        print("brforee --")
        # try :
        #     f = wmi.WMI()
        #     for process in f.Win32_Process():
                
        #         # Displaying the P_ID and P_Name of the process
        #         print("--------------------------------")
        #         print(f"{process.ProcessId:<10} {process.Name}") 
        #         print("process name and id ")
        # except:
        #     print("===========================-----------------------------")
        #     print("error :",sys.exc_info)
        # schedule.every(10).seconds.do(jobqueue.put,apply_filters(triggers))


        apply_filters(triggers)
                # print("multi_cond_check :",multi_cond_check)

                # if multi_cond_check == False:
                #     print("if condition multi_cond_check")
                #     break
            # except:
            #     global_message = global_message + sys.exc_info()[0]
            #     pass            
        # if multi_cond_check:
        #     generate_trigger(triggers)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("UPDATE order_response SET active_order = 'inactive' WHERE active_order = 'Active' RETURNING order_id, order_status, status_desc") 
        order_ids = cursor.fetchall()

        print("order_ids :",order_ids)

            
        return Response({"status":"Success", "message": "Success","content":order_ids})        
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})

# jobqueue = multiprocessing.Queue()
# trigger condition
def apply_filters(triggers):
    # while True:
        print('trigger in apply filter fun',triggers)
        print("************apply_filters function*******==************")
        print(triggers," :  ",type(triggers))
        for i in triggers:
            trigger_id = i['trigger_id']    # trigger_id in list
        print('trigger_id :',trigger_id)

        trigger_id = str(trigger_id)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("SELECT trigger_id from trigger_condition_list WHERE trigger_list like  '%"+trigger_id+"%'")
        
        trigger_condition_id = cursor.fetchone()
        # print("trigger_condition_list trigger_id : ",trigger_condition_id)
        trigger = trigger_condition_id[0]
        # print("trigger_condition_id :==== ",trigger)
        # print(type(trigger))
        triggerId = str(trigger)

        cursor.execute("SELECT order_id from orders WHERE trigger_id ="+triggerId)
        order_ids_data = cursor.fetchall()
        # print('order_ids_data :',order_ids_data)
        order_ids = []
        for order in order_ids_data:
            order_ids.append(order[0])
        # print('order_ids :::',order_ids)

        for order_id in order_ids:
            # print("inside for :",order_id)
            order_id =str(order_id)
            try:
                cursor.execute("INSERT INTO trigger_condition_status VALUES("+triggerId+",False,False,False,False,False,False,False,False,"+order_id+")")
                connection.commit()
                # print('success')
            except:
                print("except ",sys.exc_info())

        dic = {}
        count = 0
        for trigger in triggers:
            count += 1
            # print()
            print('count@@@@@@@@@@@@@@@@@',count)
            print(trigger["trigger_id"])
            if trigger["trigger_condition_id"]==1:
                dic[1]='criteria_price'
                criteria_price(trigger,triggerId,cursor)     
            elif trigger["trigger_condition_id"]==2:
                dic[2]='criteria_moving_average'
                criteria_moving_average(trigger,triggerId,cursor)
            elif trigger["trigger_condition_id"]==3:
                dic[3]='criteria_volume'
                criteria_volume(trigger,triggerId,cursor)
            elif trigger["trigger_condition_id"]==4:
                dic[4]='criteria_p2p1'
                criteria_p2p1(trigger,triggerId,cursor)
            elif trigger["trigger_condition_id"]==5:
                pass  
            elif trigger["trigger_condition_id"]==6:
                dic[6]='criteria_RSI'
                criteria_RSI(trigger,triggerId,cursor)  
            elif trigger["trigger_condition_id"]==7:
                dic[7]='criteria_p1_minus_p2'
                criteria_p1_minus_p2(trigger,triggerId,cursor)  
            elif trigger["trigger_condition_id"]==8:
                dic[8]='criteria_p1_plus_p2'
                criteria_p1_plus_p2(trigger,triggerId,cursor)  
            # dict={1:"price"}
            # list = {"price"}
            # print('trigger_condition_id :::::',trigger_condition_id)
            # print('trigger_condition_id :::::',type(trigger_condition_id))
            # print(trigger_condition_id[0])
            id_trigger_condition = trigger_condition_id[0]
            id_trigger_condition = str(id_trigger_condition)
            # print('trigger_condition_id :::::',id_trigger_condition)

        for order_id in order_ids:
            # print("inside for :",order_id)
            order_id =str(order_id)

            query = "select "
            for key in dic:
                query += dic[key]+","
            query = query[:-1]
            query += " from trigger_condition_status WHERE trigger_id ="+id_trigger_condition+" and order_id="+order_id
            print('query :',query)
            cursor.execute(query)
            trigger_condition_status = cursor.fetchone()
            print("trigger_condition_status :",trigger_condition_status)
        condition_status = False
        for i in trigger_condition_status:
            if i == True:
                condition_status = True
            else:
                condition_status = False

                print("Unexpected error:", sys.exc_info())   
                exc_tuple = sys.exc_info()  
                # trigger_error = count 
                return Response({"status":"failure", "message": exc_tuple})
                        # break
        if condition_status == True:
            combine_criteria(triggers,order_id)
            

def combine_criteria(triggers,order_id):
    print("this is combine_criteria :")
    # print("=============================")
    print("order_id[0] :",order_id)
    print("==========================*****************************************************************===")
    execute_order(triggers,order_id)

    

def criteria_price(trigger,triggerId,cursor):
    print("this is criteria price==========")
    try:        
    
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        print('user_id :',user_id)
        userid = user_id[0]
        print("userid :",userid) 
        userid = str(userid)
        print('userid :',userid)
        cursor.execute("SELECT token_id FROM auth_user WHERE id = "+userid)
        token_id = cursor.fetchone()
        print('token_id :',token_id)
        print('token_id :',type(token_id))
        access_token = token_id[0]
        print('toked_id string :',access_token)
        # file1 = open("accesstoken.txt","r")
        # access_token=file1.read()
        print('type of access_token,',type(access_token))
        print(' access_token,',access_token)
        # file1.close() 

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        print('user_id :',user_id)
        userid = user_id[0]
        print("userid :",userid) 
        userid = str(userid)

        cursor.execute("SELECT api_key FROM auth_user WHERE id=\'"+userid+"\'")
        api_key = cursor.fetchone()
        print('api_key :',api_key)
        api_key = api_key[0]
        print("api_key :",api_key)

        kite = KiteConnect(api_key=api_key)
        # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
        kite.set_access_token(access_token)
        print("trigger :::::::::::::::::::::::::::::::::::",trigger)
        exchange_symbol=trigger["exchange"]+":"+trigger["symbol"].strip()
        exchange_symbol = str(exchange_symbol)
        try:
            quote_info=kite.quote(exchange_symbol)
        except:
            print("error ",sys.exc_info())

        # exchange_symbol=trigger["exchange"]+":"+trigger["symbol"]
        # print('exchange_symbol===',type(exchange_symbol))
        # print('exchange_symbol===',exchange_symbol)

        # exchange_symbol  = str(exchange_symbol)
        # print('exchange_symbol===',exchange_symbol)

        # print("=======","'"+trigger["exchange"]+":"+trigger["symbol"].strip() +"'")
        # x  = "'"+trigger["exchange"]+":"+trigger["symbol"].strip() +"'"
        # print()
        # quote_info=kite.quote('BSE:INFY')
        # print("inside criteria price")
        # print('trigger["trigger_criteria"]["operator"] :',trigger)
        print("trigger data",trigger)
        print("quote_info :",quote_info)
        triggerId = str(triggerId)
        print('triggerId :',triggerId)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        print("trigger ------",trigger)
        if trigger is not None:
            print("this is inside IF ")

            # print("==**",quote_info['BSE:INFY'])
            print('trigger["trigger_criteria"]["operator"] :',trigger["trigger_criteria"]["operator"])
            print('quote_info[exchange_symbol]["last_price"] :',quote_info[exchange_symbol]["last_price"])
            print('trigger["trigger_criteria"]["amount"] :',trigger["trigger_criteria"]["amount"])
            if trigger["trigger_criteria"]["operator"]=="5" and quote_info[exchange_symbol]["last_price"]== Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)

                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="3" and quote_info[exchange_symbol]["last_price"]> Decimal(trigger["trigger_criteria"]["amount"]):
                print("operator 3 : ")
                print("triggerId :",type(triggerId))
                # return True
            # cursor.execute("UPDATE auth_user SET token_id =\'"+access_token+"\' WHERE id =\'"+userid+"\'")        

                cursor.execute("UPDATE trigger_condition_status SET criteria_price = True WHERE trigger_id=\'"+triggerId+"\'") 
                print("operator  3 after: ")
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="1" and quote_info[exchange_symbol]["last_price"]>= Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                print("operator 1 : ")
                print("yes ")
                cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="4" and quote_info[exchange_symbol]["last_price"]< Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                print("operator 4 : ")

                cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="2" and quote_info[exchange_symbol]["last_price"] <= Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                print("operator 2 : ")

                cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="6" and ( quote_info[exchange_symbol]["last_price"]> Decimal(trigger["trigger_criteria"]["from_amount"]) and quote_info[exchange_symbol]["last_price"]< Decimal(trigger["trigger_criteria"]["to_amount"])):
                # return True
                print("operator 6 : ")

                cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            connection.commit() 
            print("after commit")

        else:
            print("else ")

            pass    
    except:
        print("this is exept")
        global_message = global_message + sys.exc_info()[0]

# def generate_trigger(triggers):
#     print("this generate_trigger function ")
#     print("triggers :",generate_trigger)

#     pass

def criteria_moving_average(trigger,triggerId,cursor):
    print('criteria_moving_average function')
    historical_data=None
    from_date=datetime.now()
    current_date=datetime.now()
    from_date_string=""
    to_date_string=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    total=0.00
    instrument_token=trigger["trigger_criteria"]["instrument_token"]
    print('instrument_token :',instrument_token)
    time_frame=trigger["trigger_criteria"]["time_frame"]
    time_frame_type=trigger["trigger_criteria"]["time_frame_type"]
    time_frame_duration=trigger["trigger_criteria"]["time_frame_duration"]
    period=trigger["trigger_criteria"]["period"]

    if trigger["trigger_criteria"]["type"]=="Simple":
        print('first if')
        #if it is MA
        moving_average=0.00
        totalRecords=0
        total=0.00
        totalMA=0.00
        current_moving_average=0.00


        if trigger["trigger_criteria"]["moving_average"]=="MA":
            print('second if')
            pastDays=0
            threshold=1
            startIndex=0
            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
                print('pastDays :;;;;;',pastDays)
                print('pastDays :',type(pastDays))

                #calculate saturday and sunday
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 3)
                # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
                from_date=current_date - timedelta(days=pastDays)
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 2)

                from_date=current_date - timedelta(days=pastDays+1)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            #periodLimit=int(period)
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0
            for data in historical_data:
                if threshold > startIndex:
                    total=total+data["close"]
                    actualCounts=actualCounts+1                   
                threshold=threshold+1
                
            moving_average=total/actualCounts
            

        #If it is MA avg
        elif trigger["trigger_criteria"]["moving_average"]=="MA avg":
           #modification start
            pastDays=0
            threshold=1
            startIndex=0
            current_total=0.00
            averageCountMA=int(trigger["trigger_criteria"]["moving_average_candles"],0)
            #period=int(period,0) + averageCountMA
            recordsNeeded=int(period,0) + averageCountMA

            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0))*(recordsNeeded/375) + 1)
                #calculate saturday and sunday              
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*recordsNeeded) + 50


            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)

            

            #pastDays=pastDays*averageCountMA
            from_date=current_date - timedelta(days=pastDays+1)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            new_historical_data=[]
            actualCounts=0
            outerLoopCount=0
            threshold=0
            startIndex=totalRecords-(int(period,0) + averageCountMA)

            for data in historical_data:                
                if  threshold >= startIndex:
                    new_historical_data.append(data) 
                threshold=threshold+1  


            #totalExpectedCandles = int(period,0) * averageCountMA
            rangeLimit=int(period,0)
            iterationIndex=0
            for i in range(averageCountMA):
                for data in new_historical_data:   
                    total=total+data["close"]
                    iterationIndex=iterationIndex+1
                    actualCounts=actualCounts+1
                    if iterationIndex==rangeLimit:
                        current_moving_average=total/actualCounts
                        #rangeLimit=rangeLimit+1
                        new_historical_data.pop(0)
                        iterationIndex=0
                        totalMA=totalMA+current_moving_average
                        break
                outerLoopCount=outerLoopCount+1
            moving_average=totalMA/outerLoopCount

            #modification end

   
        #If it is (P-MA/MA)
        elif trigger["trigger_criteria"]["moving_average"]=="(P-MA/MA)":
            pastDays=0
            threshold=1
            startIndex=0
            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
                #calculate saturday and sunday
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 3)
                # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
                from_date=current_date - timedelta(days=pastDays)
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 2)

                from_date=current_date - timedelta(days=pastDays+1)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            #periodLimit=int(period)
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0
            for data in historical_data:
                if threshold > startIndex:
                    total=total+data["close"]
                    actualCounts=actualCounts+1                   
                threshold=threshold+1
                
            moving_average=total/actualCounts
            
            #now get quote

            cursor.execute("SELECT user_id FROM current_login_user")
            user_id = cursor.fetchone()
            print('user_id :',user_id)
            userid = user_id[0]
            print("userid :",userid) 
            userid = str(userid)

            cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
            current_token_key = cursor.fetchone()
            print('current_token_key :',current_token_key)
            access_token = current_token_key[0]
            print("token_id :",access_token)
            api_key = current_token_key[1]


            # file1 = open("accesstoken.txt","r")
            # access_token=token_id
            # file1.close() 
            kite = KiteConnect(api_key=api_key)
            # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
            kite.set_access_token(access_token)
            exchange_symbol=trigger["exchange"]+":"+trigger["symbol"].strip()
            exchange_symbol = str(exchange_symbol)
            quote_info=kite.quote(exchange_symbol)
            # exchange_symbol=trigger["exchange"]+":"+trigger["symbol"]
            # quote_info=kite.quote(exchange_symbol)
            # (P-MA/MA) getting value of P
            p_formula=quote_info[exchange_symbol]["last_price"]
            moving_average= (p_formula-moving_average)/moving_average

            

        #If it is (P-MA/MA avg)
        elif trigger["trigger_criteria"]["moving_average"]=="P-MA/MA avg":
             #now get quote

            cursor.execute("SELECT user_id FROM current_login_user")
            user_id = cursor.fetchone()
            print('user_id :',user_id)
            userid = user_id[0]
            print("userid :",userid) 
            userid = str(userid)

            cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
            current_token_key = cursor.fetchone()
            print('current_token_key :',current_token_key)
            access_token = current_token_key[0]
            print("token_id :",access_token)
            api_key = current_token_key[1]


            # file1 = open("accesstoken.txt","r")
            # access_token=file1.read()
            # file1.close() 
            kite = KiteConnect(api_key=api_key)
            # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
            kite.set_access_token(access_token)
            exchange_symbol=trigger["exchange"]+":"+trigger["symbol"].strip()
            exchange_symbol = str(exchange_symbol)
            quote_info=kite.quote(exchange_symbol)
            # exchange_symbol=trigger["exchange"]+":"+trigger["symbol"]
            # quote_info=kite.quote(exchange_symbol)
            # (P-MA/MA) getting value of P
            p_formula=quote_info[exchange_symbol]["last_price"]

            #modified section start
           
           #modification start
            pastDays=0
            threshold=1
            startIndex=0
            current_total=0.00
            averageCountMA=int(trigger["trigger_criteria"]["moving_average_candles"],0)
            recordsNeeded=int(period,0) + averageCountMA -1

            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0)*recordsNeeded)/375) + 1
                #calculate saturday and sunday              
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*recordsNeeded) + 50


            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)

           

            #pastDays=pastDays*averageCountMA
               # from_date=current_date - timedelta(days=pastDays+1)
            from_date=current_date - timedelta(days=pastDays+1)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            new_historical_data=[]
            #periodLimit=int(period)
            # if totalRecords > int(period):
            #     startIndex=totalRecords-int(period)
            # else:
            #     startIndex=0
            actualCounts=0
            threshold=0
            startIndex=totalRecords-(int(period,0) + averageCountMA)
           


            #totalExpectedCandles = int(period,0) * averageCountMA
            for data in historical_data:                
                if  threshold > startIndex:
                    new_historical_data.append(data) 
                threshold=threshold+1      
            
            rangeLimit=int(period,0)
            iterationIndex=0
            
                        ######
            outerLoopCount=0

            for i in range(averageCountMA):
                actualCounts=0
                total=0.00
                current_closing=0.00
                for data in new_historical_data:   
                    total=total+data["close"]
                    iterationIndex=iterationIndex+1
                    actualCounts=actualCounts+1
                    current_closing=data["close"]
                    if iterationIndex==rangeLimit:
                        current_moving_average=total/actualCounts
                        #Now get (P-MA)/MA
                        current_formula=(current_closing-current_moving_average)/current_moving_average
                        print("current_formula :",current_formula)
                        #rangeLimit=rangeLimit+1
                        new_historical_data.pop(0)
                        iterationIndex=0
                        totalMA=totalMA+current_formula
                        break
                outerLoopCount=outerLoopCount+1
            moving_average=totalMA/outerLoopCount
            print("moving_average :",moving_average)
            ######





            # #now we will iterate new_historical_data
            # sub_loop_limit=int(period,0)
            # sub_loop_index=0
            # current_moving_average=0.00            
            # for data in new_historical_data:
            #     if sub_loop_index < sub_loop_limit:
            #         current_total=current_total+data["close"]
            #         sub_loop_index=sub_loop_index+1
            #     if sub_loop_index==sub_loop_limit:
            #         sub_loop_index=0
            #         current_moving_average=current_total/sub_loop_limit
            #         #Now get (P-MA)/MA
            #         current_formula=(p_formula-current_moving_average)/current_moving_average
            #         total=total+current_formula
            #         actualCounts=actualCounts+1 

            # moving_average=total/actualCounts

            
            #modification end

            #modiffied section end

        if trigger["trigger_criteria"]["operator"]=="5" and moving_average== Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and moving_average> Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and moving_average>= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and moving_average< Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="2" and moving_average <= Decimal(trigger["trigger_criteria"]["amount"]):
            print('trigger_criteria 2 ***********')
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="6" and ( moving_average> Decimal(trigger["trigger_criteria"]["from_amount"]) and moving_average< Decimal(trigger["trigger_criteria"]["to_amount"])):
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        connection.commit() 

    elif trigger["trigger_criteria"]["type"]=="Exponential":
        print("exponential :")
        #if it is MA
        moving_average=0.00
        totalRecords=0
        total=0.00
        totalMA=0.00
        current_moving_average=0.00
        total_ema=0.00
        print('trigger["trigger_criteria"]["moving_average"] :',trigger["trigger_criteria"]["moving_average"])

        if trigger["trigger_criteria"]["moving_average"]=="MA":
            print("MA")
            pastDays=0
            threshold=1
            startIndex=0
            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
                #calculate saturday and sunday
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 3)
                pastDays=pastDays*2
                # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
                from_date=current_date - timedelta(days=pastDays)
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 2)
                pastDays=pastDays*2

                from_date=current_date - timedelta(days=pastDays+1)
            print("out if else")
            from_date = datetime.now()-timedelta(15)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            #periodLimit=int(period)
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0

            #to get 1st record for SMA
            start_index_sma=totalRecords-((int(period,0))*2)
            #to get last record for SMA
            end_index_sma=totalRecords-(int(period,0))-1
            sma_counter=1
            sma_counts=0
            sma_total=0.00

            new_historical_data=[]
            #calculate MA that will be used as EMA for 1st record
            for data in historical_data:
                if threshold > startIndex:
                    new_historical_data.append(data)                  
                threshold=threshold+1
                if sma_counter>=start_index_sma and sma_counter <= end_index_sma:
                    sma_total=sma_total+data["close"]
                    sma_counts=sma_counts+1
                sma_counter=sma_counter+1
            exponential_for_first_record=sma_total/sma_counts
                
            #exponential_for_first_record=total/actualCounts
            #exponential_for_first_record=moving_average

            #now calculate EMA for all other records
            actualCounts=0
            previous_period_ema=exponential_for_first_record
            ema_last_record=0.00
            for data in new_historical_data: 
                actualCounts=actualCounts+1
                #price(t)
                current_price=data["close"]
                # N = number of periods in EMA
                N=len(new_historical_data)
                #k = 2/(N+1)
                k=2/(N+1)
                # y = previous period
                y=previous_period_ema
                #(Price(t) * k) + (EMA(y) * (1-k))
                ema_current=(current_price * k) + (previous_period_ema * (1-k))
                total_ema=total_ema+ema_current
                previous_period_ema=ema_current
                ema_last_record=ema_current
            
            moving_average=ema_last_record
                #ema_current=
            print("end MA")
                
                 
         

        #If it is MA avg
        elif trigger["trigger_criteria"]["moving_average"]=="MA avg":
            print("MA AVG")
           #modification start
            pastDays=0
            threshold=1
            startIndex=0
            current_total=0.00
            averageCountMA=int(trigger["trigger_criteria"]["moving_average_candles"],0)
            #period=int(period,0) + averageCountMA
            recordsNeeded=int(period,0) + averageCountMA-1

            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0))*(recordsNeeded/375) + 1)
                #calculate saturday and sunday              
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*recordsNeeded) + 50


            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)

            

            #pastDays=pastDays*averageCountMA
            #just double the value of past date to get extra records
            pastDays=pastDays*2
            from_date=current_date - timedelta(days=pastDays+1)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            try:
                historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
                totalRecords=len(historical_data)
            except:
                print('ERROR ::',sys.exc_info())



            #to get 1st record for SMA

            start_index_sma=totalRecords-recordsNeeded-int(period,0)
            #to get last record for SMA
            end_index_sma=start_index_sma+(int(period,0))-1
            sma_counter=0
            sma_counts=0
            sma_total=0.00

            #####

            
            new_historical_data=[]
            actualCounts=0
            outerLoopCount=0
            threshold=0
            startIndex=totalRecords-(averageCountMA)

            for data in historical_data:                
                if  threshold > end_index_sma:
                    new_historical_data.append(data) 
                threshold=threshold+1 
                if sma_counter>=start_index_sma and sma_counter <= end_index_sma:
                    sma_total=sma_total+data["close"]
                    sma_counts=sma_counts+1
                sma_counter=sma_counter+1
            exponential_for_first_record=sma_total/sma_counts           



            #totalExpectedCandles = int(period,0) * averageCountMA
            rangeLimit=int(period,0)
            iterationIndex=0
            actualCounts=0
            previous_period_ema=exponential_for_first_record
            ema_calculation_index=len(new_historical_data)-averageCountMA
            ema_records_implemented=0
            #for i in range(averageCountMA):
            for data in new_historical_data:  
                #price(t)
                current_price=data["close"] 
                    # N = number of periods in EMA
                N=int(period,0)
                #k = 2/(N+1)
                k=2/(N+1)
                # y = previous period
                y=previous_period_ema
                #(Price(t) * k) + (EMA(y) * (1-k))
                ema_current=(current_price * k) + (previous_period_ema * (1-k)) 
                previous_period_ema=  ema_current
                print(ema_current)              
                if actualCounts>=ema_calculation_index:
                    total_ema=total_ema+ema_current
                    ema_records_implemented=ema_records_implemented+1
                actualCounts=actualCounts+1                        
                
            moving_average=total_ema/ema_records_implemented

            #modification end

   
        #If it is (P-MA/MA)
        

        if trigger["trigger_criteria"]["moving_average"]=="(P-MA/MA)":
            print('inside (P-MA/MA)')
            pastDays=0
            threshold=0
            startIndex=0
            # print('trigger["trigger_criteria"]["time_frame_type"] :',trigger["trigger_criteria"]["time_frame_type"])
            if time_frame_type=="minute":
                print('inside minute')
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
                # pastDays = int(pastDays)
                print("pastDays :",type(pastDays))
                #calculate saturday and sunday
                if pastDays <= 7:
                    pastDays=pastDays+3
                    print('pastDays ;;:',pastDays)
                else:
                    pastDays = pastDays + ((pastDays/7) * 3)
                pastDays=pastDays*2
                # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
                from_date=current_date - timedelta(days=pastDays)
                print('from_date :',from_date)
            elif time_frame=="day":
                print('inside day')
                pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 2)
                pastDays=pastDays*2
                from_date=current_date - timedelta(days=pastDays+1)
            
            from_date = datetime.now() - timedelta(15)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            print('from_date_string :',from_date_string)
            print("before historical_data")
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            #periodLimit=int(period)
            print("after hisorical data")
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0

            #to get 1st record for SMA
            start_index_sma=totalRecords-((int(period,0))*2)
            #to get last record for SMA
            end_index_sma=totalRecords-(int(period,0))-1
            sma_counter=0
            sma_counts=0
            sma_total=0.00

            new_historical_data=[]
            #calculate MA that will be used as EMA for 1st record
            for data in historical_data:
                if threshold >= startIndex:
                    new_historical_data.append(data)                  
                threshold=threshold+1
                if sma_counter>=start_index_sma and sma_counter <= end_index_sma:
                    sma_total=sma_total+data["close"]
                    sma_counts=sma_counts+1
                sma_counter=sma_counter+1
            exponential_for_first_record=sma_total/sma_counts
                
            #exponential_for_first_record=total/actualCounts
            #exponential_for_first_record=moving_average

            #now calculate EMA for all other records
            actualCounts=0
            previous_period_ema=exponential_for_first_record
            ema_last_record=0.00
            last_record_price=0.00
            for data in new_historical_data: 
                actualCounts=actualCounts+1
                #price(t)
                current_price=data["close"]
                last_record_price=current_price
                # N = number of periods in EMA
                N=len(new_historical_data)
                #k = 2/(N+1)
                k=2/(N+1)
                # y = previous period
                y=previous_period_ema
                #(Price(t) * k) + (EMA(y) * (1-k))
                ema_current=(current_price * k) + (previous_period_ema * (1-k))
                total_ema=total_ema+ema_current
                previous_period_ema=ema_current
                ema_last_record=ema_current
            
            moving_average=(last_record_price-ema_last_record)/ema_last_record
                #ema_current=
              


        #If it is (P-MA/MA avg)
        elif trigger["trigger_criteria"]["moving_average"]=="P-MA/MA avg":
           #modification start
            pastDays=0
            threshold=1
            startIndex=0
            current_total=0.00
            averageCountMA=int(trigger["trigger_criteria"]["moving_average_candles"],0)
            #period=int(period,0) + averageCountMA
            recordsNeeded=int(period,0) + averageCountMA-1

            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0))*(recordsNeeded/375) + 1)
                #calculate saturday and sunday              
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*recordsNeeded) + 50


            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)

            

            #pastDays=pastDays*averageCountMA
            #just double the value of past date to get extra records
            pastDays=pastDays*2
            from_date=current_date - timedelta(days=pastDays+1)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)



            #to get 1st record for SMA

            start_index_sma=totalRecords-recordsNeeded-int(period,0)
            #to get last record for SMA
            end_index_sma=start_index_sma+(int(period,0))-1
            sma_counter=0
            sma_counts=0
            sma_total=0.00

            #####

            
            new_historical_data=[]
            actualCounts=0
            outerLoopCount=0
            threshold=0
            startIndex=totalRecords-(averageCountMA)

            for data in historical_data:                
                if  threshold > end_index_sma:
                    new_historical_data.append(data) 
                threshold=threshold+1 
                if sma_counter>=start_index_sma and sma_counter <= end_index_sma:
                    sma_total=sma_total+data["close"]
                    sma_counts=sma_counts+1
                sma_counter=sma_counter+1
            exponential_for_first_record=sma_total/sma_counts           



            #totalExpectedCandles = int(period,0) * averageCountMA
            rangeLimit=int(period,0)
            iterationIndex=0
            actualCounts=0
            previous_period_ema=exponential_for_first_record
            ema_calculation_index=len(new_historical_data)-averageCountMA
            ema_records_implemented=0
            ema_current_formula=0.00
            #for i in range(averageCountMA):
            for data in new_historical_data:  
                #price(t)
                current_price=data["close"] 
                    # N = number of periods in EMA
                N=int(period,0)
                #k = 2/(N+1)
                k=2/(N+1)
                # y = previous period
                y=previous_period_ema
                #(Price(t) * k) + (EMA(y) * (1-k))
                ema_current=(current_price * k) + (previous_period_ema * (1-k))
                ema_current_formula=(current_price-ema_current)/ema_current
                previous_period_ema=ema_current

                if actualCounts>=ema_calculation_index:
                    total_ema=total_ema+ema_current_formula
                    ema_records_implemented=ema_records_implemented+1
                actualCounts=actualCounts+1                        
                
            moving_average=total_ema/ema_records_implemented

            #modification end
        print("befotre conf=ditions")
        if trigger["trigger_criteria"]["operator"]=="5" and moving_average== Decimal(trigger["trigger_criteria"]["amount"]):
            # execute_order(trigger)
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="3" and moving_average> Decimal(trigger["trigger_criteria"]["amount"]):
            # execute_order(trigger)
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="1" and moving_average>= Decimal(trigger["trigger_criteria"]["amount"]):
            # execute_order(trigger)
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="4" and moving_average< Decimal(trigger["trigger_criteria"]["amount"]):
            # execute_order(trigger)
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="2" and moving_average <= Decimal(trigger["trigger_criteria"]["amount"]):
            # execute_order(trigger)
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="6" and ( moving_average> Decimal(trigger["trigger_criteria"]["from_amount"]) and moving_average< Decimal(trigger["trigger_criteria"]["to_amount"])):
            # execute_order(trigger)
            cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        connection.commit()
    print('outside if criteria_moving_average')
        
from django.utils import timezone
# import datetime         

def criteria_volume(trigger,triggerId,cursor):
    print('criteria_volume trigger::,',trigger)
    historical_data=None
    from_date=datetime.now()
    current_date=datetime.now()
    from_date_string=""
    to_date_string=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    total=0.00

    instrument_token=trigger["trigger_criteria"]["instrument_token"]
    time_frame=trigger["trigger_criteria"]["time_frame"]
    time_frame_type=trigger["trigger_criteria"]["time_frame_type"]
    time_frame_duration=trigger["trigger_criteria"]["time_frame_duration"]
    period="1"

    # period=trigger["trigger_criteria"]["period"]
    
    moving_average=0.00
    totalRecords=0
    total=0.00

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if (trigger["trigger_criteria"]["type"]).lower()=="volume":
               
        pastDays=0
        threshold=1
        startIndex=0
        if time_frame_type=="minute":
            #total minutes in a complete market day=375
            #for 1 minute: day=1/375
            #for fiven minutes: days = (1*given minutes)/375
            #we will add 1 more days for safe side
            pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
            print("error line")
            #calculate saturday and sunday
            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)
            # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
            from_date=current_date - timedelta(days=pastDays)
        elif time_frame=="day":
            pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 2)

            from_date=current_date - timedelta(days=pastDays+1)
        from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
        historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
        totalRecords=len(historical_data)
        new_historical_data=[]
        #periodLimit=int(period)
        if totalRecords > int(period):
            startIndex=totalRecords-int(period)
        else:
            startIndex=0
        actualCounts=0
        for data in historical_data:
            if threshold > startIndex:
                new_historical_data.append(data)
                actualCounts=actualCounts+1                   
            threshold=threshold+1
            
        ####
      
        #historical_data[0]["close"]
        print("before_condition")
        print('trigger["trigger_criteria"]["operator"] :',trigger["trigger_criteria"]["operator"])
        print('trigger["trigger_criteria"]["amount"] :',trigger["trigger_criteria"]["amount"])
        current_volume=new_historical_data[0]["volume"]

        # ----------------- ---------------------------                  ---------
        print('current_volume :',current_volume)
        if trigger["trigger_criteria"]["operator"]=="5" and current_volume== Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and current_volume> Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and current_volume>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("inside operator 1")
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and current_volume< Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="2" and current_volume <= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="6" and ( current_volume> Decimal(trigger["trigger_criteria"]["from_amount"]) and current_volume< Decimal(trigger["trigger_criteria"]["to_amount"])):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
        connection.commit() 
            # execute_order(trigger)
        
    #If it is Volume avg
    elif (trigger["trigger_criteria"]["type"]).lower()=="volume_avg":

        print("inside elif**")

        period=int(trigger["trigger_criteria"]["volume_average_candles"],0)       
        pastDays=0
        threshold=1
        startIndex=0
        print("before if")
        if time_frame_type=="minute":
            #total minutes in a complete market day=375
            #for 1 minute: day=1/375
            #for fiven minutes: days = (1*given minutes)/375
            #we will add 1 more days for safe side
            # pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
            pastDays= (int(time_frame_duration,0)*period/375) + 1
            #calculate saturday and sunday
            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)
            # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
            from_date=current_date - timedelta(days=pastDays)
        elif time_frame=="day":
            pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 2)

            from_date=current_date - timedelta(days=pastDays+1)
        print("after if")
        from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
        historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
        # print('historical_data',historical_data)
        totalRecords=len(historical_data)
        new_historical_data=[]
        #periodLimit=int(period)
        print("second if")
        if totalRecords > int(period):
            startIndex=totalRecords-int(period)
        else:
            startIndex=0
        actualCounts=0
        for data in historical_data:
            if threshold > startIndex:
                new_historical_data.append(data)
                actualCounts=actualCounts+1                   
            threshold=threshold+1
                

        for data in new_historical_data:
            total=total+data["volume"]
        volume_average=total/actualCounts 
        print("before if volume")
        print('volume_average :',volume_average)
        print('trigger["trigger_criteria"]["amount"] :',trigger["trigger_criteria"]["amount"])
        print('trigger["trigger_criteria"]["operator"] :',trigger["trigger_criteria"]["operator"])

        if trigger["trigger_criteria"]["operator"]=="5" and volume_average== Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and volume_average> Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and volume_average>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("operator 1 :::")
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and volume_average< Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="2" and volume_average <= Decimal(trigger["trigger_criteria"]["amount"]):
            print("operator 2 ::::")
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="6" and ( volume_average> Decimal(trigger["trigger_criteria"]["from_amount"]) and volume_average< Decimal(trigger["trigger_criteria"]["to_amount"])):
            cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger) 
        connection.commit() 
    print('outside if')
              
def criteria_p2p1(trigger,triggerId,cursor):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    userid = user_id[0]
    userid = str(userid)
    cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
    current_token_key = cursor.fetchone()
    access_token = current_token_key[0]
    api_key = current_token_key[1]

    # file1 = open("accesstoken.txt","r")
    # access_token=file1.read()
    # file1.close() 

    kite = KiteConnect(api_key=api_key)
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    kite.set_access_token(access_token)
    exchange1_symbol=trigger["exchange"] +":"+ trigger["trigger_criteria"]["symbol1_exchange"]
    quote_info_exchange1=kite.quote(exchange1_symbol)
    exchange2_symbol=trigger["exchange"] +":"+trigger["trigger_criteria"]["symbol2_exchange"]
    quote_info_exchange2=kite.quote(exchange2_symbol)

    calculated_criteria= ( quote_info_exchange2[exchange2_symbol]["last_price"]- quote_info_exchange1[exchange1_symbol]["last_price"])/quote_info_exchange1[exchange1_symbol]["last_price"]

    if trigger is not None:
        if trigger["trigger_criteria"]["operator"]=="5" and calculated_criteria== Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and calculated_criteria> Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and calculated_criteria>= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and calculated_criteria< Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="2" and calculated_criteria <= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="6" and ( calculated_criteria> Decimal(trigger["trigger_criteria"]["from_amount"]) and calculated_criteria< Decimal(trigger["trigger_criteria"]["to_amount"])):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 
        connection.commit() 
            # execute_order(trigger)
    else:
        pass
              
def criteria_p1_minus_p2(trigger,triggerId,cursor):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()

    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print('user_id :',user_id)
    userid = user_id[0]
    print("userid :",userid) 
    userid = str(userid)

    cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
    current_token_key = cursor.fetchone()
    print('current_token_key :',current_token_key)
    access_token = current_token_key[0]
    print("token_id :",access_token)
    api_key = current_token_key[1]
    
    # file1 = open("accesstoken.txt","r")
    # access_token=file1.read()
    # file1.close() 
    kite = KiteConnect(api_key=api_key)
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    kite.set_access_token(access_token)
    exchange1_symbol=trigger["exchange"] +":"+ trigger["trigger_criteria"]["symbol1_exchange"]
    quote_info_exchange1=kite.quote(exchange1_symbol)
    exchange2_symbol=trigger["exchange"] +":"+trigger["trigger_criteria"]["symbol2_exchange"]
    quote_info_exchange2=kite.quote(exchange2_symbol)

    calculated_criteria= ( quote_info_exchange1[exchange1_symbol]["last_price"] - quote_info_exchange2[exchange2_symbol]["last_price"])

    if trigger is not None:
        if trigger["trigger_criteria"]["operator"]=="5" and calculated_criteria== Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="3" and calculated_criteria> Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="1" and calculated_criteria>= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'")
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="4" and calculated_criteria< Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger

        elif trigger["trigger_criteria"]["operator"]=="2" and calculated_criteria <= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="6" and ( calculated_criteria> Decimal(trigger["trigger_criteria"]["from_amount"]) and calculated_criteria< Decimal(trigger["trigger_criteria"]["to_amount"])):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        connection.commit() 
    else:
        pass
              
def criteria_p1_plus_p2(trigger,triggerId,cursor):
    print("inside criteria_p1_plus_p2 function")
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print('user_id :',user_id)
    userid = user_id[0]
    print("userid :",userid) 
    userid = str(userid)

    cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
    current_token_key = cursor.fetchone()
    print('current_token_key :',current_token_key)
    access_token = current_token_key[0]
    print("token_id ::",access_token)
    api_key = current_token_key[1]
    print('api key',api_key)
    # file1 = open("accesstoken.txt","r")
    # access_token=file1.read()
    # file1.close() 
    kite = KiteConnect(api_key=api_key)
    print("kite ")
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    try:
        kite.set_access_token(access_token)
        print('1')
        print('trigger["exchange"] ',trigger["exchange"])
        print('trigger["trigger_criteria"]["symbol1_exchange"] :',trigger["trigger_criteria"])
        exchange1_symbol=trigger["exchange"] +":"+ trigger["trigger_criteria"]["symbol1_exchange"]
        print('exchange1_symbol :',exchange1_symbol)
        quote_info_exchange1=kite.quote(exchange1_symbol)
        print('quote_info_exchange1 :',quote_info_exchange1)
        exchange2_symbol=trigger["exchange"] +":"+trigger["trigger_criteria"]["symbol2_exchange"]
        print('exchange2_symbol :',exchange2_symbol)
        quote_info_exchange2=kite.quote(exchange2_symbol)
        print("quote_info_exchange2 :",quote_info_exchange2)
    except:
        print('error ::::',sys.exc_info())
    print("before calculated_criteria")
    print('quote_info_exchange1[exchange1_symbol]["last_price"]',quote_info_exchange1[exchange1_symbol])
    print('quote_info_exchange2[exchange2_symbol]["last_price"]',quote_info_exchange2[exchange2_symbol])
    calculated_criteria= ( quote_info_exchange1[exchange1_symbol]["last_price"]+ quote_info_exchange2[exchange2_symbol]["last_price"])
    print("before if else condition")
    if trigger is not None:
        print("insidee conditions")
        print('trigger["trigger_criteria"]',trigger["trigger_criteria"])
        print('calculated_criteria :',calculated_criteria)
        if trigger["trigger_criteria"]["operator"]=="5" and calculated_criteria== Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="3" and calculated_criteria> Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="1" and calculated_criteria>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("true condition")
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="4" and calculated_criteria< Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="2" and calculated_criteria <= Decimal(trigger["trigger_criteria"]["amount"]):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="6" and ( calculated_criteria> Decimal(trigger["trigger_criteria"]["from_amount"]) and calculated_criteria< Decimal(trigger["trigger_criteria"]["to_amount"])):
            cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        connection.commit() 
    else:
        print("this is else")
        pass

#criteria RSI start

def criteria_RSI(trigger,triggerId,cursor):
    historical_data=None
    from_date=datetime.now()
    current_date=datetime.now()
    from_date_string=""
    to_date_string=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    total=0.00
    print("____________________________________________________________")
    print('instrument_token')
    instrument_token=trigger["trigger_criteria"]["instrument_token"]
    print('instrument_token',instrument_token)
    time_frame=trigger["trigger_criteria"]["time_frame"]
    print('time_frame :',time_frame)
    time_frame_type=trigger["trigger_criteria"]["time_frame_type"]
    print('time_frame_type :',time_frame_type)
    time_frame_duration=trigger["trigger_criteria"]["time_frame_duration"]
    print('time_frame_duration :',time_frame_duration)

    period=trigger["trigger_criteria"]["period"]
    print(period)
    # period = 1
    # period = str(period)
    moving_average=0.00
    totalRecords=0
    total=0.00
    

    pastDays=0
    threshold=1
    startIndex=0
    print("before first if ")
    if time_frame_type=="minute":
        print("inside minute")
        #total minutes in a complete market day=375
        #for 1 minute: day=1/375
        #for fiven minutes: days = (1*given minutes)/375
        #we will add 1 more days for safe side
        pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
        #calculate saturday and sunday
        if pastDays <= 7:
            pastDays=pastDays+3
        else:
            pastDays = pastDays + ((pastDays/7) * 3)
        # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
        from_date=current_date - timedelta(days=pastDays)
    elif time_frame=="day":
        print("inside day")
        pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
        if pastDays <= 7:
            pastDays=pastDays+3
        else:
            pastDays = pastDays + ((pastDays/7) * 2)

        from_date=current_date - timedelta(days=pastDays+1)
    print("no if no else ::")
    from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
    print('from_date_string :',from_date_string)
    try:
        historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
        # print('historical_data :',historical_data)
    except:
        print("Error")
        print("Except : ",sys.exc_info())
        
    totalRecords=len(historical_data)
    print('totalRecords :',totalRecords)
    print("no if no else")
    #periodLimit=int(period)
    if totalRecords > int(period):
        startIndex=totalRecords-int(period)
    else:
        startIndex=0
    actualCounts=0
    
    #######
   
    print("previous_close")
    previous_close=historical_data[0]["close"]
    total_upward_price_change=0.00
    total_downward_price_change=0.00
    total_upward_count=0
    total_downward_count=0
    print("before for loop")
    for data in historical_data:
        if threshold > startIndex:
            actualCounts=actualCounts+1
            current_close=data["close"]
            if current_close>=previous_close:
                total_upward_count=total_upward_count+1
                total_upward_price_change=current_close-previous_close
                previous_close=current_close
            else:
                total_downward_count=total_downward_count+1
                total_downward_price_change=previous_close - current_close
                previous_close=current_close
        threshold=threshold+1


        
    average_upward_price_change=total_upward_price_change/total_upward_count
    average_downward_price_change=total_downward_price_change/total_downward_count
    rsi = Decimal( 100-(100 / ( 1 + (average_upward_price_change / average_downward_price_change ) ) ))
        
    print("before condition")
    if trigger["trigger_criteria"]["operator"]=="5" and rsi== Decimal(trigger["trigger_criteria"]["amount"]):
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="3" and rsi> Decimal(trigger["trigger_criteria"]["amount"]):
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="1" and rsi>= Decimal(trigger["trigger_criteria"]["amount"]):
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="4" and rsi< Decimal(trigger["trigger_criteria"]["amount"]):
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="2" and rsi <= Decimal(trigger["trigger_criteria"]["amount"]):
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="6" and ( rsi> Decimal(trigger["trigger_criteria"]["from_amount"]) and rsi< Decimal(trigger["trigger_criteria"]["to_amount"])):
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
    connection.commit() 
    print("after committ")
        # execute_order(trigger)
    
#criteris RSI end

def execute_order(order_condition,orderid):
    print("this is execute_order function :",order_condition)
    try:
        print('orderid :',orderid)
    
        print("----------------")
        # print(order_condition)
        
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        # print('user_id :',user_id)
        userid = user_id[0]
        print("userid ::::::",userid) 
        userid = str(userid)

        cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
        current_token_key = cursor.fetchone()
        print('current_token_key :',current_token_key)
        access_token = current_token_key[0]
        print("token_id :",access_token)
        api_key = current_token_key[1]
        print('order_condition :',order_condition)
        # file1 = open("accesstoken.txt","r")
        # access_token=file1.read()
        # file1.close() 

        kite = KiteConnect(api_key=api_key)
        # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
        kite.set_access_token(access_token)
        print("-------------------------------------------")
        orders_ids = []
        for order in order_condition:
            orders_ids.append(order['trigger_id'])
        print('orders_ids :',orders_ids)
        orders_ids = orders_ids[0]

        orders = []
        for row in order_condition:
            print('row ::',row)
            # print('orders_ids :',orders_ids)
            # for y in row:
            #     print("inside ssecond for ",y)
            if row['trigger_id'] == orders_ids:
                orders.append(dict(row))
        print('orders :::=',orders)


        # print("------------------",order_condition['trigger_criteria'])
        # print(order_condition['symbol1_exchange'])

        for order in orders:
            print("inside order for")
            limit_price=None
            trigger_price=None
            print('order :::::::::::::::::',order)
            if order["order_type"]=="LIMIT" or order["order_type"]=="SL":
                limit_price=order["price"]
            if order["order_type"]=="LIMIT" or order["order_type"]=="SL":
                trigger_price=order["trigger_price"]
            print("ordersssssssss")
            # order_id = kite.place_order(
            # variety=kite.VARIETY_REGULAR,
            # exchange=kite.EXCHANGE_NSE,
            # tradingsymbol="INFY",    ib196gkbrmuqnoer
            # transaction_type=kite.TRANSACTION_TYPE_BUY,
            # quantity=1,
            # product=kite.PRODUCT_CNC,
            # order_type=kite.ORDER_TYPE_MARKET
            # )     
            # order_id="test"
            # print('order["order_condition"]',order["order_condition"])
            print("before execute")
            error =''
            try :
                print("")
                order_id = kite.place_order(
                variety=kite.VARIETY_REGULAR,
                exchange=order["order_exchange"],
                # tradingsymbol= order["symbol1_exchange"],#order_symbol
                tradingsymbol= order["order_symbol"],#
                transaction_type=order["buy_sell"],
                quantity=order["quantity"],
                product=order["product_type"],
                order_type=order["order_type"],
                price=limit_price,
                trigger_price=trigger_price
                )
                print("order_id :",order_id)
                if order_id is not None:
                    order_status=kite.order_history(order_id)
                    if order_status[len(order_status)-1]["status"]=="COMPLETE":
                        mark_order_executed(order["trigger_id"])     
                print("successsss") 
                try:
                    orderid = str(orderid)
                    print('orderid :',orderid)
                    # false = False
                    status = "Active"
                    cursor.execute("INSERT INTO order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,'success',"+userid+",\'"+status+"\')")
                    connection.commit()
                    print("after commit")
                    schedule.CancelJob
                except:
                    print("except",sys.exc_info())
                    # schedule.CancelJob

                # return Response({"status":"success", "message": "success", "content":orderid})
            except:
                print("except block")
                print("errorrrr :",sys.exc_info())
                value = sys.exc_info()
                print('Error opening %s:' % (value))
                error = str(value)
                error_VALUE = error[:50]
                print('error sliced :',error_VALUE)

                try:
                    orderid = str(orderid)
                    print('orderid :',orderid)
                    status = "Active"
                    # false = False
                    cursor.execute("INSERT INTO order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",False,\'"+error_VALUE+"\',"+userid+",\'"+status+"\')")
                    connection.commit()
                    print("after commit")
                    # schedule.CancelJob
                except:
                    print("except",sys.exc_info())
                # return Response({"status":"error", "message": "error", "content":error})
    except:
        # print("Unexpected error :::::::::::", sys.exc_info())       
        # return Response({"status":"failure", "message": sys.exc_info()})
        # raise Response({"status":"failure", "message": "failure","message":"'something bad happened!"})
        return Response({"status":"failure", "message": "failure"})
# WITH cte_film AS (SELECT json_array_elements(items) token FROM public.instruments ) SELECT  * FROM cte_film WHERE token->>'name' = 'CPSE INDEX';

def mark_order_executed(execited_trigger_id):
    try:
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        postgres_update_query = """Update  triggers set is_active=%s WHERE trigger_id=%s"""
        cursor.execute(postgres_update_query, (False,execited_trigger_id,))
        postgres_update_query = """Update  orders set is_executed=%s WHERE trigger_id=%s"""
        cursor.execute(postgres_update_query, (True,execited_trigger_id,))
        connection.commit()
        count = cursor.rowcount
        print(count)
        cursor.close()
        connection.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])    

def get_historical_data(instrument_token,time_frame,from_date_string,to_date_string):
    print('time_frame :',time_frame)
    print('from_date_string :',from_date_string)
    print('to_date_string :',to_date_string)
    print('instrument_token :',instrument_token)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print('user_id :',user_id)
    userid = user_id[0]
    print("userid :",userid) 
    userid = str(userid)

    cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
    current_token_key = cursor.fetchone()
    print('current_token_key :',current_token_key)
    access_token = current_token_key[0]
    print("token_id :",access_token)
    api_key = current_token_key[1]

    # file1 = open("accesstoken.txt","r")
    # access_token=file1.read()
    # file1.close() 
    kite = KiteConnect(api_key=api_key)
    print('kite :',kite)
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    kite.set_access_token(access_token)
    #quote_info=kite.quote("NSE:INFY")
    # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')
    # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')

    try:
        # time_framee = 'minute'
        print("from_date_string :",from_date_string)
        historical_data= kite.historical_data(instrument_token, from_date_string ,to_date_string,time_frame)
        print('historical_data :',historical_data)
    except:
        print("ERROR at historical :::",sys.exc_info())
    #a=1
    return historical_data



# section for enums and constants
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3

# # @api_view(['GET','POST'])
# @login_required(login_url='login_view')
# def home(request):

#     user_id = request.user.id
#     request.session['current_user_id']= user_id
#     user_id = request.user.id
#     print("user_id : =================",user_id)

#     current_user = request.user
#     print(current_user)
#     user_id = request.user.id
#     user_id = str(user_id)
#     print("------------")
#     print(type(user_id), str(user_id))       
#     try:
#         connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
#         cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
#         cursor.execute("SELECT triggers.created_on, triggers.trigger_name,triggers.symbol, master_trigger_conditions.trigger_condition, orders.symbol, orders.buy_sell,  orders.quantity,orders.product_type,orders.trigger_id, master_product_type.product_type FROM triggers INNER JOIN orders ON triggers.trigger_id=orders.trigger_id INNER JOIN master_trigger_conditions ON triggers.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = orders.product_type WHERE orders.is_executed='False' AND triggers.user_id ="+ user_id)
#         rows = cursor.fetchall()
#         dict_result = []
#         for row in rows:
#             dict_result.append(dict(row))
#         cursor.execute("SELECT triggers.created_on, triggers.trigger_name,triggers.symbol, master_trigger_conditions.trigger_condition, orders.symbol, orders.buy_sell,  orders.quantity,orders.product_type ,orders.trigger_id, master_product_type.product_type FROM triggers INNER JOIN orders ON triggers.trigger_id=orders.trigger_id INNER JOIN master_trigger_conditions ON triggers.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = orders.product_type WHERE orders.is_executed='True' AND triggers.user_id ="+ user_id)
#         rows2 = cursor.fetchall()
#         dict_result_2 = []
#         for row in rows2:
#             dict_result_2.append(dict(row))
#             print(dict_result_2)
#         cursor.close()
#         connection.close()
#         return render(request, 'index.html',{"content":dict_result,"dict_result_2":dict_result_2,"current_user":current_user,"user_id":user_id})        

#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         return Response({"status":"failure", "message": "failure"})

#     return render(request, 'index.html')


@login_required(login_url='login_view')
def update(request,id):
    current_user = request.user
    print("this is update function")
    trigger_id = 1215
    trigger_id = str(id)
    print("trigger_id :",trigger_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("SELECT triggers.created_on, triggers.trigger_name,triggers.symbol, master_trigger_conditions.trigger_condition, orders.symbol, orders.buy_sell, orders.quantity,orders.product_type,orders.trigger_id, master_product_type.product_type,master_exchange.exchange,master_buy_sell.buy_sell FROM triggers INNER JOIN orders ON triggers.trigger_id=orders.trigger_id INNER JOIN master_exchange ON triggers.exchange_id = master_exchange.exchange_id INNER JOIN master_trigger_conditions ON triggers.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = orders.product_type INNER JOIN master_buy_sell ON master_buy_sell.buy_sell_id=orders.buy_sell WHERE orders.is_executed='False' AND triggers.trigger_id ="+ trigger_id)
    rows = cursor.fetchall()
    dict_result = []
    for row in rows:
        dict_result.append(dict(row))
    print("dict_result ",dict_result)

    # cursor.execute("SELECT master_exchange.exchange, orders.buy_sell FROM master_exchange INNER JOIN orders ON orders.exchange_id=master_exchange.exchange_id WHERE trigger_id="+ trigger_id)
    # exchanges = cursor.fetchall()
    # # exchang = []
    # # for row in exchanges:
    # #     exchang.append(dict(row))
    # exchanges = list(exchanges[0])
    # exchanges = exchanges[0]
    # print("exchanges : ",exchanges)

    # cursor.execute("SELECT orders.buy_sell FROM master_exchange INNER JOIN orders ON orders.exchange_id=master_exchange.exchange_id WHERE trigger_id="+ trigger_id)
    # buy_sell_id = cursor.fetchall()
    # buy_sell_id = list(buy_sell_id[0])
    # buy_sell_id = buy_sell_id[0]
    # print("buy_sell_id : ",buy_sell_id)

    # # cursor.execute("SELECT master_order_type.order_type FROM master_order_type INNER JOIN orders ON orders.order_type=master_order_type.order_type_id WHERE trigger_id="+ trigger_id)
    # cursor.execute("SELECT master_order_type.order_type, orders.order_type FROM master_order_type INNER JOIN orders ON orders.order_type=master_order_type.order_type_id WHERE trigger_id="+ trigger_id)

    # order = cursor.fetchall()
    # print("order : ",order)

    # order_name = []
    # for row in order:
    #     order_name.append(dict(row))
    # order_name = list(order[0])
    # order_name = order_name[0]
    # print("order_name : ",order_name)

    # cursor.execute("SELECT orders.exchange_id FROM orders WHERE trigger_id="+ trigger_id)
    # exchange_id = cursor.fetchall()
    # print("exchange_id :: ",exchange_id)

    # exchange = []
    # for row in exchange_id:
    #     exchange.append(dict(row))
    # exchange = exchange[0]
    # print("exchange : ",exchange)

    # cursor.execute("SELECT orders.product_type FROM orders WHERE trigger_id="+ trigger_id)
    # product_type_id = cursor.fetchall()
    # product_type = []
    # for row in product_type_id:
    #     product_type.append(dict(row))
    # product_type = product_type[0]
    # print("product_type : ",product_type)

    # cursor.execute("SELECT orders.order_type FROM orders WHERE trigger_id="+ trigger_id)
    # order_type_id = cursor.fetchall()
    # order_type = []
    # for row in order_type_id:
    #     order_type.append(dict(row))
    # order_type = order_type[0]
    # print("order_type : ",order_type)

    # cursor.execute("SELECT triggers.exchange_id FROM triggers WHERE trigger_id="+ trigger_id)
    # trigger_exchange_id = cursor.fetchall()
    # print("exchange_id :: ",trigger_exchange_id)

    # trigger_exchange = []
    # for row in trigger_exchange_id:
    #     trigger_exchange.append(dict(row))
    # trigger_exchange = trigger_exchange[0]
    # print("trigger_exchange : ",trigger_exchange)

    # cursor.execute("SELECT triggers.exchange_id FROM triggers WHERE trigger_id="+ trigger_id)
    # trigger_exchange_id = cursor.fetchall()
    # print("exchange_id :: ",trigger_exchange_id)

    # trigger_exchange = []
    # for row in trigger_exchange_id:
    #     trigger_exchange.append(dict(row))
    # trigger_exchange = trigger_exchange[0]
    # print("trigger_exchange : ",trigger_exchange)


    # cursor.execute("SELECT triggers.trigger_criteria FROM triggers WHERE trigger_id="+ trigger_id)
    # trigger_criteria = cursor.fetchall()
    # criteria = []
    # for row in trigger_criteria:
    #     criteria.append(dict(row))
    # criteria = criteria[0]
    # print("criteria : ",criteria)       # trigger criteria RSI MOVING AVERAGE ETC



    # cursor.close()
    # connection.close()
    # # return render(request, 'update.html',{'dict_result':dict_result,'current_user':current_user,'exchanges':exchanges,'order_list':order,'order_name':order_name,'buy_sell_id':buy_sell_id,'exchange_id':exchange,'product_type_id':product_type,'order_type_id':order_type,'trigger_exchange_id':trigger_exchange})
    return render(request, 'update.html')

@login_required(login_url='login_view')
def delete(request,id):

    # user_id = request.user.id
    id = str(id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("DELETE FROM triggers WHERE trigger_id="+ id)
    cursor.execute("DELETE FROM orders WHERE trigger_id="+ id)

    connection.commit()
    # cursor.close()
    # connection.close()
    # return HttpResponse(id)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='login_view')
def trading(request):
    return render(request, 'trading.html')   

def loginzerodha(request):
    return render(request, 'loginzerodha.html')    


def demo(request):
    max = 11
    l = list(range(1, max))  # the cast to list is optional in Python 2
    random.shuffle(l)
    print(l)
    return HttpResponse(l)

def function(request):
    return render(request,'login.html')

@login_required(login_url='login')
def user_logout(request):
    # Take the request and pass it to logout
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))

from django.views.defaults import page_not_found

def my_error_404(request, exception):
    template_name = '404.html'
    if request.path.startswith('/trading/'):
        print("inside if")
        template_name='404.html'
    elif request.path.startswith('/home/'):
        template_name='404.html'
    elif request.path.startswith('/login_view/home/'):
        template_name='404.html'     
    # elif request.path.startswith('/'):
    #     template_name=''   
    return page_not_found(request, exception, template_name=template_name)


# import schedule
# import time

# def job():
#     print("I'm working...")

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1) 


from django.http import HttpResponse
import tablib
import pyexcel.ext.xls 
import csv

def open_oreder_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Open orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['Created On', 'Trigger Name','Symbol','Trigger Condition ID', 'Orders Symbol','Buy & Sell', 'Quantity','Product Type'])
    # data = stu_details.objects.filter()

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    # cursor.execute("select trigger_name,symbol,exchange_id,trigger_id,trigger_condition_id,created_on from triggers")

    cursor.execute("SELECT triggers.created_on, triggers.trigger_name,triggers.symbol, master_trigger_conditions.trigger_condition, orders.symbol, orders.buy_sell, orders.quantity,orders.product_type FROM triggers INNER JOIN orders ON triggers.trigger_id=orders.trigger_id INNER JOIN master_trigger_conditions ON triggers.trigger_condition_id = master_trigger_conditions.trigger_condition_id WHERE orders.is_executed='False'")

    data = cursor.fetchall()
    dict_result = []
    for row in data:
        dict_result.append(row)
    row = []
    for row in dict_result:
        row = list(row)
        # print(row[3]," : ",type(row))
        if row[7] == 1:
            row[7] = "NRML"
        elif row[7] == 2:
            row[7] = "MIS"
        elif row[7] == 3:
            row[7] = "CNC"

        if row[5] == 1:
            row[5] = 'Buy'
        else:
            row[5] = 'Sell'
        rowobj = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
        writer.writerow(rowobj)
        # row = tuple(row[3])
    return response 

def execute_oreder_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Execute orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['Created On', 'Trigger Name','Symbol','Trigger Condition ID', 'Orders Symbol','Buy & Sell', 'Quantity','Product Type'])
    # data = stu_details.objects.filter()

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    # cursor.execute("select trigger_name,symbol,exchange_id,trigger_id,trigger_condition_id,created_on from triggers")

    cursor.execute("SELECT triggers.created_on, triggers.trigger_name,triggers.symbol, master_trigger_conditions.trigger_condition, orders.symbol, orders.buy_sell,  orders.quantity,orders.product_type FROM triggers INNER JOIN orders ON triggers.trigger_id=orders.trigger_id INNER JOIN master_trigger_conditions ON triggers.trigger_condition_id = master_trigger_conditions.trigger_condition_id WHERE orders.is_executed='TRUE'")

    data = cursor.fetchall()
    dict_result = []
    for row in data:
        dict_result.append(row)
    row = []
    for row in dict_result:
        row = list(row)
        # print(row[3]," : ",type(row))
        if row[7] == 1:
            row[7] = "NRML"
        elif row[7] == 2:
            row[7] = "MIS"
        elif row[7] == 3:
            row[7] = "CNC"

        if row[5] == 1:
            row[5] = 'Buy'
        else:
            row[5] = 'Sell'
        rowobj = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
        writer.writerow(rowobj)
    return response 

def sort(request):
    return render(request,'sort_table.html')

def sort2(request):
    return render(request,'sort.html')




# def get_dashboard_orders(request):

#     user_id = request.user.id
#     user_id = str(user_id)
#     print("------------")
#     print(type(user_id), str(user_id))       
#     try:
#         connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
#         cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
#         cursor.execute("SELECT triggers.created_on, triggers.trigger_name,triggers.symbol, master_trigger_conditions.trigger_condition, orders.symbol, orders.buy_sell,  orders.quantity,orders.product_type FROM triggers INNER JOIN orders ON triggers.trigger_id=orders.trigger_id INNER JOIN master_trigger_conditions ON triggers.trigger_condition_id = master_trigger_conditions.trigger_condition_id WHERE orders.is_executed='TRUE' AND public.triggers.user_id ="+ user_id)
#         rows = cursor.fetchall()
#         # print(rows)

#         dict_result = []
#         for row in rows:
#             dict_result.append(dict(row))
#         cursor.close()
#         connection.close()
#         return render(request, 'index.html',{"content":dict_result})        
#         # return render(request, 'listing.html',{"content":dict_result})        

#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         return Response({"status":"failure", "message": "failure"})

@api_view(['POST','GET'])
def update_trigger_order(request):   
    try:
        print('update_trigger_order function')
        print('update_trigger_order :',update_trigger_order)
        trigger_name=request.data["trigger"]["trigger_name"]
        print(trigger_name,' : trigger_name')
        symbol=request.data["trigger"]["symbol"]
        print('symbol :',symbol)
        trigger_condition_id=request.data["trigger"]["trigger_condition_id"]
        # trigger_condition_id = str(trigger_condition_id)
        print('trigger_condition_id :',trigger_condition_id)
        trigger_criteria=  json.dumps(request.data["trigger"]["trigger_criteria"])
        print('trigger_criteria :',trigger_criteria)
        exchange_id=request.data["trigger"]["exchange_id"]
        # exchange_id = str(exchange_id)
        buy_sell=request.data["order"]["buy_sell"]
        # buy_sell = str(buy_sell)
        print('buy_sell :',buy_sell)
        quantity=request.data["order"]["quantity"] 
        print('quantity :',quantity)
        product_type=request.data["order"]["product_type"]
        print('product_type :',product_type)
        order_types=request.data["order"]["order_types"]
        print('order_types :',order_types)
        order_symbol=request.data["order"]["symbol"]
        print('order_symbol :',order_symbol)
        order_exchange_id=request.data["order"]["exchange_id"]
        print('order_exchange_id :',order_exchange_id)
        trigger_id=request.data["order"]["trigger_id"]        
        print("trigger_id : ",trigger_id)

        # order_price=request.data["order"]["price"]
        # print(order_price)
        # trigger_price=request.data["order"]["trigger_price"]
        # print("trigger_price",trigger_price)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 

        cursor.execute("UPDATE triggers SET trigger_name =\'"+trigger_name+"\',symbol =\'"+symbol+"\',trigger_condition_id ="+trigger_condition_id+",trigger_criteria=\'"+trigger_criteria+"\',exchange_id="+exchange_id+" WHERE trigger_id="+trigger_id)
        cursor.execute("UPDATE orders SET buy_sell="+buy_sell+", quantity ="+quantity+",product_type =\'"+product_type +"\',symbol =\'"+order_symbol+"\',order_type=\'"+order_types+"\',exchange_id="+order_exchange_id+" WHERE trigger_id="+trigger_id)


        connection.commit()
        # return redirect("trading")
        # return render(request,'sort_table.html')
        return Response({"status":"success", "message": "success"})   

            
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": sys.exc_info()})

def user_fun(request):
    user_id = request.user.id
    user_id = str(user_id)
    print(user_id)
    return HttpResponse(user_id)

def acess_token(request):

    print("user = ",user_fun)
    current_date = datetime.date.today()
    print("current_date :",current_date)
    access_token = '5qxZY4HaZpIstFWh5PxQNIeWKdtP866Q'
    user_id = request.user.id
    user_id = str(user_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    
    print("started")
    cursor.execute("UPDATE auth_user SET token_id =\'"+access_token+"\' WHERE id="+user_id)        
    connection.commit()
    print("updated")
    return HttpResponse("working")

def fetch_triggers(request,trigger_name):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("SELECT t.trigger_name,master_exchange.exchange,t.symbol,t.trigger_criteria FROM triggers t INNER JOIN master_exchange ON t.exchange_id = master_exchange.exchange_id where trigger_name=\'"+trigger_name+"\'")    
    trigger_detail = cursor.fetchall()
    # print("before trigger_detail",trigger_detail)

    for i in trigger_detail:
        print(i[3]['operator'])
        if i[3]['operator'] == '1':
            i[3]['operator'] = ">="
        elif i[3]['operator'] == '2':
            i[3]['operator'] = "<="
        elif i[3]['operator'] == '3':
            i[3]['operator'] = ">"
        elif i[3]['operator'] == '<':
            i[3]['operator'] = "="
        elif i[3]['operator'] == '5':
            i[3]['operator'] = "Between"
    return render(request,'group.html',{'trigger_detail':trigger_detail})
    # return HttpResponse(trigger_detail)

# def create_multiple_trigger(request):
#     return render(request,'add-multiple-trigger.html')

@api_view(['POST','GET'])
def save_multiple_trigger(request):   
    if request.method == "POST":
        try:            
            print("this is trigger funxction")
            print("___________________________________")
            user_id = request.session.get('user_id')
            print("session user_id:========================",user_id)
            print("in save trigger")
            trigger_name=request.data["trigger"]["trigger_name"]
            print('trigger_name',trigger_name)
            symbol=request.data["trigger"]["symbol"]
            print('symbol',symbol)
            trigger_condition_id=request.data["trigger"]["trigger_condition_id"]
            print('trigger_condition_id',trigger_condition_id)
            trigger_criteria=  json.dumps(request.data["trigger"]["trigger_criteria"])
            print('trigger_criteria ::',trigger_criteria)
            exchange_id=request.data["trigger"]["exchange_id"]
            print('exchange_id',exchange_id)

            connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
            cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 

            print("trigger_id=============================================================")
            user_id = json.dumps(user_id)
            cursor.execute("SELECT MAX(trigger_id) FROM triggers where user_id = "+user_id+" and trigger_name = '"+trigger_name+"'")

            # SELECT MAX(trigger_id) FROM triggers where user_id =1 and trigger_name = 'A11'

            # cursor.execute("SELECT MAX(trigger_id) FROM triggers where user_id = "+user_id)
            trigger_id = cursor.fetchone()
            print("trigger_id :: ",trigger_id)
            trigger = trigger_id[0]
            print("trigger :==== ",trigger)
            trigger = str(trigger)
            
            trigger_id = str(trigger_id)


            print("_________________________________________________________________")
            cursor.execute("INSERT INTO triggers(trigger_name, symbol, trigger_condition_id,trigger_criteria, exchange_id,user_id)VALUES (\'"+trigger_name+"\',\'"+symbol+"\',"+trigger_condition_id+",\'"+trigger_criteria+"\',"+exchange_id+","+user_id+")  RETURNING trigger_id") 
            connection.commit()

            last_trigger_id = cursor.fetchone()

            print("last_trigger_id :",last_trigger_id)

            last_trigger_id = str(last_trigger_id[0])
            last_trigger_id = last_trigger_id+","
            print('last_trigger_id :',last_trigger_id)
            print('trigger ,',trigger)
            print('trigger ,',type(trigger))
            if trigger != 'None':
                cursor.execute("SELECT * FROM trigger_condition_list where trigger_list like '%"+trigger+"%'")    
                trigger_detail = cursor.fetchone()
                print("hii div")
                print(" len(trigger_detail) ",trigger_detail)
                if trigger_detail is not None:
                    print('trigger_detail :',trigger_detail)
                    trigger_list = trigger_detail[1]
                    print('trigger_list :',trigger_list)

                    trigger_detail_id = str(trigger_detail[0])
                    print('trigger_detail_id',trigger_detail_id)
                    # cursor.execute("UPDATE trigger_condition_list SET trigger_list = '"+trigger_list+"'"+"'"+last_trigger_id+"' WHERE trigger_id = "+trigger_detail_id)

                    cursor.execute("UPDATE trigger_condition_list SET trigger_list = '"+trigger_list+last_trigger_id+"' WHERE trigger_id = "+trigger_detail_id)

                    print('update success')
                    connection.commit()
                    return Response({"status":"success", "message": "success"})   
            else:
                print("else")
                cursor.execute("INSERT INTO trigger_condition_list(trigger_list)VALUES('"+last_trigger_id+"')") 
                print('inserted success')
            print("inserted successfull")
            connection.commit()
            return Response({"status":"success", "message": "success"})   
            
        except:
            # print("Unexpected error:", sys.exc_info()[0])
            print("except error")
            return Response({"status":"failure", "message": sys.exc_info()})
    else:
        return render(request,'add-multiple-trigger.html')



# function to save multiple orders
@api_view(['GET','POST'])
def save_multiple_order(request):

    if request.method =='POST':
        print("======================================================")
        trigger_name=request.data["trigger"]["trigger_name"]
        multi_order=request.data["order"]["form_data"]
        multi_order = json.loads(multi_order)
        print('multi_order json :',multi_order)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = 0
        for i in user_id:
            userid +=i
        userid = str(userid)
    # trigger_name
        cursor.execute("SELECT tcl.trigger_id from trigger_condition_list tcl join triggers t on tcl.trigger_list like '%' || t.trigger_id ||'%' and t.user_id = "+userid+" and t.trigger_name='"+trigger_name+"'")
        trigger_id = cursor.fetchall()
        print("trigger_id ::::: ",trigger_id)
        trigger = trigger_id[0][0]
        print('trigger ::',trigger)

        request.session['trigger'] = trigger
        triggerId = str(trigger) 
        print("before")
        for i in multi_order:
            cursor.execute("INSERT INTO orders(buy_sell,symbol,exchange_id,quantity,product_type,order_type,trigger_id,user_id)VALUES ("+i['buy_sell']+",\'"+i['symbol']+"\',"+i['exchange_id']+","+i['quantity']+","+i['product_type']+","+i['order_types']+","+triggerId+","+userid+")") 
        print("after")
        
        cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name = \'"+trigger_name+"\' AND user_id = "+userid+"")
        trigger_order_id = cursor.fetchone()
        print('trigger_order_id :',trigger_order_id)
        trigger_order_id = trigger_order_id[0]
        print("trigger_order_id :",trigger_order_id) 
        trigger_order_id = str(trigger_order_id)
        print('trigger_order_id kkkkk:',trigger_order_id)

        cursor.execute("UPDATE current_login_user SET order_trigger_id = "+trigger_order_id+" WHERE user_id="+userid+"")

        connection.commit()

        print("inserted success")
        # return render(request,'add-multiple-order.html')
        return Response({"status":"success", "message": "success"})   
    else:

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        # user_id = request.user.id
        
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        print('user_id :',user_id)
        user_id = str(user_id)    
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id) 
        data = cursor.fetchall()
        print("data :",data)
        triggers = []
        for row in data:
            triggers.append(row[0])
        print('triggers :',triggers)
        print(triggers)
        # return render(request,'add-multiple-order.html',{'triggers':triggers})
        return render(request,'new-add-multiple-order.html',{'triggers':triggers})


def get_mul(request):
    if request.method == 'POST': 
        username = request.POST.getlist("name")
        print(username)
        symbol = request.POST.getlist("symbol")
        print(symbol)

        # user_password = request.POST.get("name")
        # print()
    return render(request, 'multi.html')

@api_view(['GET','POST'])
def create_group(request):
    if request.method == "POST":
        group=request.data["group"]["group_name"] 
        group_exchange=request.data["group"]["group_exchange"] 
        order=request.data["order"]["form_data"] 
        json_string = json.loads(order)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT group_name from master_company_group")    
        group_name = cursor.fetchall()
        group_list = []
        for row in group_name:
            group_list.append(row[0])

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = 0
        for i in user_id:
            userid +=i
        userid = str(userid)

        if group not in group_list:
            print("create")
            # group_id =1
            # # group_id = str(group_id)
            symbol = []
            for item in json_string:
                company = item['group_symbol']
                print("company ",company)
                symbol.append(company)
                # # group_id = str(group_id)
                group_exchange = str(group_exchange)
            print("symbol :",symbol)
            s = ","
            company_list = s.join(symbol) 
            print("added :::::",company_list)

            cursor.execute("INSERT INTO master_company_group(group_name,company_list,exchange,user_id) VALUES(\'"+group+"\',\'"+company_list+"\',\'"+group_exchange+"\','"+userid+"')")
            # cursor.execute("INSERT INTO master_company_group(id,group_name,company_list,exchange) VALUES("+id+",\'"+group_name+"\',\'"+company+"\',\'"+exchange+"\')")
            print("inserted successfull")
            connection.commit()
            # group_id = int(group_id)
            # group_id += 1
            # messages.success(request, 'Group created successfully')
            # return TemplateResponse(request, "create_group.html")
            return Response({"status":"success", "message": "success"})
        else:
            print("===========================================")
            cursor.execute("select group_name from master_company_group where group_name= \'"+group+"\'")
            groups = cursor.fetchall()
            groups = groups[0]
            group_db = groups[0]
            print('groups :',group_db)
            if group_db == group:
                print("same")
                return Response({"status":"failure", "message": "failure"})
    # else:
    #     print("else")
    #     return render(request,'add-group.html')

    return render(request,'add-group.html')

def group_listing(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    
    cursor.execute("SELECT group_name,company_list,me.exchange FROM master_company_group INNER JOIN master_exchange as me ON master_company_group.exchange = me.exchange_id")
    groups = cursor.fetchall()
    # print("groups ::",groups)
    connection.commit()
    return render(request,'group_listing.html',{'groups_list':groups})

from django.contrib import messages

def delete_group(request,g_name):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    try :
        cursor = connection.cursor()
        cursor.execute("DELETE FROM master_company_group WHERE group_name=\'"+g_name+"\'")
        connection.commit()
        print("deleted")
        return HttpResponseRedirect(reverse('group_listing'))
    except:
        messages.error(request, 'Some trigger is assigned to this Group.')

        # messages.add_message(request, messages.SUCCESS, 'Failed... trigger is assigne to this group.')
        return HttpResponseRedirect(reverse('group_listing'))

@api_view(['GET','POST'])
def company_add_update(request,group_name):

    if request.method == "GET":
        print("company_add_update functoin")
        print("=============--------------------------==========================================")
    # company = request.POST.get("company")
        company = "VM ware"
        # group_name ='Group2'
        print("group_name ",group_name)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT company_list FROM master_company_group WHERE group_name=\'"+group_name+"\'")
        company_list = cursor.fetchone()
        print("company_list :",company_list)
        print("update")
        company_list = company_list[0]
        if company_list == None:
            cursor.execute("UPDATE master_company_group SET company_list=\'"+company+"\' WHERE group_name=\'"+group_name+"\'")
            connection.commit()
        else:
            company_list = company_list + "," + company
            print("company_list :::",company_list)
            cursor.execute("UPDATE master_company_group SET company_list=\'"+company_list+"\' WHERE group_name=\'"+group_name+"\'")
            connection.commit()
        print("Update successfull")
    # return Response({"status":"success", "message": "success"})  
    else:
        print("post")
    # return HttpResponseRedirect(reverse('group_listing'))
    return render(request,'update-group.html')

def group_order(request):
    return render(request,'update-group.html')

@api_view(['GET','POST'])
def group_fetch_update(request,group_name):
    if request.method=="GET":
        print("group_order_fetch functoin")
        # group_name = "group"
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT company_list,group_name,exchange FROM master_company_group WHERE group_name=\'"+group_name+"\'")
        company_list = cursor.fetchone()
        symbols = company_list[0]
        # symbol = {'symbol':symbols}
        # print("symbols ::",symbol)
        group_name = company_list[1]
        symbol = {'group_name':group_name}

        exchange = company_list[2]
        symbols = symbols.split(',')
        print('symbols ::::',symbols)
        print('symbols ::::',type(symbols))
        # data = {'group_name':group_name,'exchange':exchange ,'symbol':symbols}
        return render(request,'update-group.html',{'group_name':group_name,'exchange':exchange ,'symbol':symbols})
    else:
        print("company_add_update functoin")
        print("=============--------------------------==========================================")
    # company = request.POST.get("company")
        company = "VM ware"
        # group_name ='Group2'
        print("group_name ",group_name)

        # group_name =request.data["group"]["group_name"] 
        # print('group_name :--',group_name)
        # exchange=request.data["group"]["exchange"]
        # print('exchange :',type(exchange))
        # print('exchange :',exchange)
        # amount=request.data["group"]["amount"] 
        # print('amount : ',amount)
        # product_type=request.data["group"]["product_type"]
        # print('product_type : ',product_type)
        # order_type=request.data["group"]["order_types"]
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT company_list FROM master_company_group WHERE group_name=\'"+group_name+"\'")
        company_list = cursor.fetchone()
        print("company_list :",company_list)
        print("update")
        company_list = company_list[0]
        if company_list == None:
            cursor.execute("UPDATE master_company_group SET company_list=\'"+company+"\' WHERE group_name=\'"+group_name+"\'")
            connection.commit()
        else:
            company_list = company_list + "," + company
            print("company_list :::",company_list)
            cursor.execute("UPDATE master_company_group SET company_list=\'"+company_list+"\' WHERE group_name=\'"+group_name+"\'")
            connection.commit()
        print("inserted successfull")
        return Response({"status":"success", "message": "success"})  

@api_view(['GET','POST'])
def insert_group_order(request):
    print("inside insert_group_order function ")
    if request.method=="POST":
        print("inside insert_group_order post")
        trigger_name =request.data["trigger"]["trigger_name"] 
        print('trigger_name :------------------------------',trigger_name)
        buy_sell=request.data["order"]["buy_sell"]
        print('buy_sell :',type(buy_sell))
        print('buy_sell :',buy_sell)
        amount=request.data["order"]["amount"] 
        print('amount : ',amount)
        product_type=request.data["order"]["product_type"]
        print('product_type : ',product_type)
        order_type=request.data["order"]["order_types"]
        print('order_type :',order_type)
        group_name=request.data["order"]["group_name"]
        print('group_name :',group_name)
        order_exchange_id=request.data["order"]["exchange_id"]
        print('order_exchange_id :',order_exchange_id)
        order_price=request.data["order"]["price"]
        print('order_price :',order_price)
        trigger_price=request.data["order"]["trigger_price"]
        print('trigger_price :',trigger_price)
        # print("-------------------------=======================================---------------------------")
        # # buy_sell = True
        # # product_type = '2'
        # # order_type =  '3'
        # # order_exchange_id = '2'
        # trigger_id = '160' 
        # # trigger_price = '200'  
        # # amount= '2000'
        # order_id = '6621'
        # group_id = '2'

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = 0
        for i in user_id:
            userid +=i
        userid = str(userid)

        cursor.execute("SELECT id FROM master_company_group Where group_name=\'"+group_name+"\'")
        group_ids = cursor.fetchone()
        group_id = 0
        for i in group_ids:
            group_id +=i
        group_id = str(group_id)

        cursor.execute("SELECT distinct(trigger_condition_list.trigger_id) FROM trigger_condition_list join triggers ON trigger_condition_list.trigger_list like '%' || triggers.trigger_id || '%' and triggers.trigger_name=\'"+trigger_name+"\'")
        trigger_ids = cursor.fetchone()
        trigger_id = 0
        for i in trigger_ids:
            trigger_id +=i
        trigger_id = str(trigger_id)
        cursor.execute("INSERT INTO group_order(group_id,buy_sell,exchange_id,amount,product_type,order_type,trigger_id,trigger_price,user_id)VALUES ("+group_id+","+buy_sell+","+order_exchange_id+","+amount+","+product_type+","+order_type+","+trigger_id+","+trigger_price+","+userid+")") 

        cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name = \'"+trigger_name+"\' AND user_id = "+userid+"")
        trigger_order_id = cursor.fetchone()
        print('trigger_order_id :',trigger_order_id)
        trigger_order_id = trigger_order_id[0]
        print("trigger_order_id :",trigger_order_id) 
        trigger_order_id = str(trigger_order_id)
        print('trigger_order_id kkkkk:',trigger_order_id)

        cursor.execute("UPDATE current_login_user SET order_trigger_id = "+trigger_order_id+" WHERE user_id="+userid+"")

        connection.commit()
        print("success")
        return render(request,'group_order.html')

    # return HttpResponse("working")
    else:
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        print('user_id :',user_id)
        user_id = str(user_id)    
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id) 
        data = cursor.fetchall()
        print("data :",data)
        triggers = []
        for row in data:
            triggers.append(row[0])
        print('triggers :',triggers)
        print(triggers)
        # select group_name from master_company_group where user_id = 1
        cursor.execute("select group_name from master_company_group where user_id = "+user_id)
        data = cursor.fetchall()
        group_names = []
        for row in data:
            group_names.append(row[0])
        print('group_names :',group_names)
        print(group_names)
        return render(request,'insert-group-order.html',{'triggers':triggers,"group_names":group_names})


@api_view(['GET','POST'])
def update_group_order(request,order_id):
    print("inside update_group_order function ")
    if request.method=="POST":
        print("inside update_group_order post")

        trigger_name =request.data["trigger"]["trigger_name"] 
        print('trigger_name :==========----------------==-',trigger_name)
        buy_sell=request.data["order"]["buy_sell"]
        print('buy_sell :',type(buy_sell))
        print('buy_sell :',buy_sell)
        amount=request.data["order"]["amount"] 
        print('amount : ',amount)
        product_type=request.data["order"]["product_type"]
        print('product_type : ',product_type)
        order_type=request.data["order"]["order_types"]
        print('order_type :',order_type)
        group_name=request.data["order"]["group_name"]
        print('group_name :',group_name)
        order_exchange_id=request.data["order"]["exchange_id"]
        print('order_exchange_id :',order_exchange_id)
        order_price=request.data["order"]["price"]
        print('order_price :',order_price)
        trigger_price=request.data["order"]["trigger_price"]
        print('trigger_price :',trigger_price)
        # print("-------------------------=======================================---------------------------")
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = 0
        for i in user_id:
            userid +=i
        userid = str(userid)
        order_id = str(order_id)
        cursor.execute("UPDATE group_order SET buy_sell="+buy_sell+",amount="+amount+",product_type="+product_type+",order_type="+order_type+",trigger_price="+trigger_price+" WHERE order_id="+order_id+"") 
        connection.commit()
        print("updated")
        return Response({"status":"success", "message": "success"})  
        # return render(request,'group_order.html')
    else:
        print("order_id ",order_id)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        order_id = str(order_id)
        cursor.execute("SELECT * FROM group_order WHERE order_id="+order_id+"")
        group_order = cursor.fetchone()
        print('group_order :',group_order)
        
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        print('user_id :',user_id)
        user_id = str(user_id)    
        cursor.execute("SELECT group_order.order_id,group_order.trigger_id,mcg.group_name,bs.buy_sell,mex.exchange,amount,mpt.product_type,opt.order_type,executed_on,price,group_order.trigger_price FROM group_order INNER JOIN master_company_group as mcg ON group_order.group_id = mcg.id INNER JOIN master_product_type as mpt ON group_order.product_type = mpt.product_type_id INNER JOIN master_order_type as opt ON group_order.order_type = opt.order_type_id INNER JOIN master_buy_sell as bs ON group_order.buy_sell = bs.buy_sell_id INNER JOIN master_exchange as mex ON group_order.exchange_id = mex.exchange_id JOIN public.trigger_condition_list tcl ON tcl.trigger_id= group_order.trigger_id JOIN public.triggers tr ON tcl.trigger_list like '%' || tr.trigger_id || '%' WHERE group_order.order_id ="+order_id) 
        group_order = cursor.fetchall()
        print("group_order :",group_order)
        return render(request,'update-group-order.html',{'group_order':group_order})



# @api_view(['GET','POST'])
def insert_group_trigger(request):
    print("inside update_group_order function ")
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if request.method=="GET": #change to POST
        print("inside update_group_order post")

        # group_name =request.data["group"]["group_name"] 
        # trigger_name=request.data["group"]["trigger_name"]
        # trigger_condition_id=request.data["group"]["trigger_condition_id"]
        # print('trigger_condition_id',trigger_condition_id)
        # trigger_criteria=  json.dumps(request.data["group"]["trigger_criteria"])
        # print('trigger_criteria ::',trigger_criteria)
        # exchange_id=request.data["group"]["exchange_id"]
        # print('exchange_id',exchange_id) 
        group_name = "group"
        cursor.execute("select exchange,company_list from master_company_group where group_name=\'"+group_name+"\'") 
        group_record = cursor.fetchall()
        exchange = group_record[0][0]
        print("exchange",exchange)
        company_list = group_record[0][1]
        company_list = company_list.split(',')
        print("company_list",company_list)

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        # print('user_id :',user_id)
        user_id = str(user_id)
        trigger_name = "test1"
        # symbol = "TCS"
        trigger_condition_id = "4"
        trigger_criteria = '{"type": "volume_avg", "volume_average_candles": "50", "time_frame": "5minute", "time_frame_type": "minute", "time_frame_duration": "5", "operator": "1", "amount": "5000", "instrument_token": "1076225"}'
        exchange_id = '3'
        for record in company_list:
            cursor.execute("INSERT INTO triggers(trigger_name, symbol, trigger_condition_id,trigger_criteria, exchange_id,user_id)VALUES (\'"+trigger_name+"\',\'"+record+"\',"+trigger_condition_id+",\'"+trigger_criteria+"\',"+exchange_id+","+user_id+")") 
        connection.commit()

        cursor.execute("select trigger_id from triggers where trigger_name =\'"+trigger_name+"\'") 
        trigger_id = cursor.fetchall()
        print("trigger_id ::::",trigger_id[0])
        trigger_ids = ""
        for i in trigger_id:
            # i = str(i)
            print(i," ",type(i))
            trigger_ids += str(i[0])+","
            # print(i[0]
        print("trigger_ids",trigger_ids)
        cursor.execute("INSERT INTO trigger_condition_list(trigger_list)VALUES (\'"+trigger_ids+"\') RETURNING trigger_id") 
        trigger = cursor.fetchone()
        trigger = str(trigger[0])
        
        print("trigger ",trigger)
        connection.commit()
        cursor.execute("Update master_company_group SET trigger_id=\'"+trigger+"\' WHERE group_name =\'"+group_name+"\'")
        connection.commit()

        return HttpResponse("done")

    else:

        # order_id = str(order_id)
        cursor.execute("select group_name from master_company_group where trigger_id is null") 
        group_order = cursor.fetchall()
        print("group_order ::::",group_order)
        # return render(request,'')
        return HttpResponse(group_order)

@api_view(['GET','POST'])
def insert_group(request):
    if request.method =="POST":

        print("hii")

        group_name =request.data["trigger"]["group_name"] 
        print('group_name',group_name)
        trigger_name=request.data["trigger"]["trigger_name"]
        print('trigger_name',trigger_name)
        trigger_condition_id=request.data["order"]["buy_sell"]
        print('trigger_condition_id',trigger_condition_id)
        trigger_criteria=  json.dumps(request.data["order"]["order_amount"])
        print('trigger_criteria ::',trigger_criteria)
        # exchange_id=request.data["group"]["exchange_id"]
        # print('exchange_id',exchange_id) 
        return render(request,'place-group.html')    
    else:
        print("calling get")

        # group_name =request.data["trigger"]["group_name"] 
        # print('group_name',group_name)
        # trigger_name=request.data["trigger"]["trigger_name"]
        # print('trigger_name',trigger_name)
        # trigger_condition_id=request.data["order"]["buy_sell"]
        # print('trigger_condition_id',trigger_condition_id)
        # trigger_criteria=  json.dumps(request.data["order"]["order_amount"])
        # print('trigger_criteria ::',trigger_criteria)
        # exchange_id=request.data["group"]["exchange_id"]
        # print('exchange_id',exchange_id) 
        # return render(request,'place-group.html') 
        return render(request,'place-group.html')


# def login_user_triggers(request):
def groups_order_listing(request):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    user_id = user_id[0]
    # print('user_id :',user_id)
    user_id = str(user_id) 
    cursor.execute("SELECT group_order.order_id,group_order.trigger_id,mcg.group_name,bs.buy_sell,amount,mpt.product_type,opt.order_type,executed_on,price,group_order.trigger_price FROM group_order INNER JOIN master_company_group as mcg ON group_order.group_id = mcg.id INNER JOIN master_product_type as mpt ON group_order.product_type = mpt.product_type_id INNER JOIN master_order_type as opt ON group_order.order_type = opt.order_type_id INNER JOIN master_buy_sell as bs ON group_order.buy_sell = bs.buy_sell_id JOIN public.trigger_condition_list tcl ON tcl.trigger_id= group_order.trigger_id JOIN public.triggers tr ON tcl.trigger_list like '%' || tr.trigger_id || '%' WHERE group_order.user_id = "+user_id)
    groups_records = cursor.fetchall()
    # print("groups_records :",groups_records)
    connection.commit()
    return render(request,'groups_order_listing.html',{'groups_records':groups_records})


def delete_group_order(request,id):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    order_id = str(id)
    cursor.execute("DELETE FROM group_order WHERE order_id="+order_id+"")
    connection.commit()
    print("deleted")
    return HttpResponseRedirect(reverse('group_listing'))

# @api_view(['GET','POST'])
# def update_group(request):
#     # print("inside update_group function ")
#     # if request.method=="POST":
#         print("inside update_group post")

#         # trigger_name =request.data["trigger"]["trigger_name"] 
#         # print('trigger_name :',trigger_name)
#         # buy_sell=request.data["order"]["buy_sell"]
#         # print('buy_sell :',buy_sell)
#         # amount=request.data["order"]["quantity"] 
#         # print('amount : ',amount)
#         # product_type=request.data["order"]["product_type"]
#         # print('product_type : ',product_type)
#         # order_type=request.data["order"]["order_types"]
#         # print('order_type :',order_type)
#         # order_exchange_id=request.data["order"]["exchange_id"]
#         # print('order_exchange_id :',order_exchange_id)
#         # order_price=request.data["order"]["price"]
#         # print('order_price :',order_price)
#         # trigger_price=request.data["order"]["trigger_price"]
#         # print('trigger_price :',trigger_price)
#         print("-------------------------=======================================---------------------------")
#         buy_sell = '2'
#         product_type = '3'
#         order_type =  '3'
#         order_exchange_id = '2'
#         trigger_id = '160' 
#         trigger_price = '500'  
#         amount= '2000'
#         order_id = '662'
#         group_id = '2'

#         connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
#         cursor = connection.cursor()
#         cursor.execute("UPDATE group_order set buy_sell="+buy_sell+",exchange_id="+order_exchange_id+",amount="+amount+",product_type="+product_type+",order_type="+order_type+" WHERE order_id="+order_id+"") 
#         connection.commit()
#         return render(request,'new-add-multiple-order.html')

# def save_group(request):
#     print("working")
#     return render(request,'add-group.html')




def get_group_triggers_orders():        
    try:
        print("-------------------------")
        print(" get_group_triggers_orders function")
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute("SELECT order_trigger_id FROM current_login_user")
        order_trigger_id = cursor.fetchone()
        print('order_trigger_id :',order_trigger_id)
        order_trigger_id = order_trigger_id[0]
        print("order_trigger_id :",order_trigger_id) 
        order_trigger_id = str(order_trigger_id)

        print('trigger trigger trigger trigger trigger trigger ::::',order_trigger_id)

        cursor.execute("SELECT trigger_name from triggers where trigger_id = "+order_trigger_id)
        order_trigger_name = cursor.fetchone()
        order_trigger_name = order_trigger_name[0]
        
        # order_trigger_names = str(order_trigger_name)
        print("order_trigger_name : ",type(order_trigger_name))
        cursor.execute("SELECT trigger_id from triggers where trigger_name =\'"+order_trigger_name+"\'")
        list_order_trigger_id = cursor.fetchall()
        print('list_order_trigger_id :',list_order_trigger_id)

        list_trigger_id = []
        for i in list_order_trigger_id:
            list_trigger_id.append(i[0])
        print("list_trigger_id ::",list_trigger_id)

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        print('user_id :',user_id)
        user_id = user_id[0]
        print("user_id :",user_id) 
        user_id = str(user_id)    
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id) 
        trigger_names_list = cursor.fetchall()
        print('trigger_names_list-------------------- :',trigger_names_list)
        trigger_names = []
        for i in trigger_names_list:
            trigger_names.append(i[0])
        print("trigger_names ::",trigger_names)
        
        # trigger_names = tuple(trigger_names)
        # print(" => ",trigger_names)
        # trigger_names = ['T49','T51']
        # trigger_names = "test1"
        print("before ----------------------------------------------")
        # try:
        #     # cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name = "+trigger_names+"")
        #     print("tuple(trigger_names[0]",tuple(trigger_names))
        #     cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name in %s" % (tuple(trigger_names),))
        #     # 
        #     # cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name in ('T51')" % (tuple(trigger_names),))
        #     trigger_id = cursor.fetchall()
        #     print("trigger_id :",trigger_id)
        # except:
        #     print("error",sys.exc_info())
        print("after ----------------------------------------------")

        # trigger = []
        # for i in trigger_id:
        #     trigger.append(i[0])
        # print('trigger :',trigger)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cursor.execute("SELECT  t.trigger_id,mcg.company_list,t.trigger_criteria,e.exchange_id,e.exchange,c.trigger_condition_id,b.buy_sell_id,o.amount,p.product_type_id,p.product_type,o.price,o.trigger_price,b.buy_sell,eo.exchange_id as order_exchange_id,eo.exchange as order_exchange, mo.order_type_id,mo.order_type FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' Join public.master_company_group mcg ON tcl.trigger_id = mcg.trigger_id JOIN public.group_order o ON mcg.id=o.group_id JOIN public.master_exchange eo ON eo.exchange_id=o.exchange_id JOIN public.master_buy_sell b ON o.buy_sell=b.buy_sell_id JOIN public.master_product_type p ON p.product_type_id=o.product_type JOIN public.master_order_type mo ON mo.order_type_id=o.order_type WHERE t.is_active=true order by t.trigger_id asc")
            # cursor.execute(postgres_insert_query,()) 
            rows = cursor.fetchall()
            print('rows ::',rows)
        except:
            print("error =",sys.exc_info())
        print('rows--------------------------------------------rows')
        order_trigger_id = int(order_trigger_id)
        ordertrigger_id = []
        ordertrigger_id.append(order_trigger_id)
        print('ordertrigger_id',ordertrigger_id)
        print('ordertrigger_id',type(ordertrigger_id))


        print('rows',rows)
        triggers = []
        for row in rows:
            for y in row:
                # print("inside ssecond for ",y)
                if y in list_trigger_id:
                    triggers.append(dict(row))
            # break
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("triggers ::::",triggers)
        cursor.close()
        connection.close()
        return triggers
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})


@api_view(['GET','POST'])
def online_group_order(request):        
    try:
        print("calling get_group_triggers_orders ")
        try:
            triggers=get_group_triggers_orders()

            print('inside online_group_order function')
            print("triggers :",triggers)
        except:
            print("error ::",sys.exc_info())
        # global multi_cond_check
        multi_cond_check = False 
        # for trigger in triggers:
        #     try:
        print("brforee --")
        schedule.every(10).seconds.do(jobqueue.put,group_apply_filters(triggers))
        # apply_filters(triggers)
                # print("multi_cond_check :",multi_cond_check)
                # if multi_cond_check == False:
                #     print("if condition multi_cond_check")
                #     break
            # except:
            #     global_message = global_message + sys.exc_info()[0]
            #     pass            
        # if multi_cond_check:
        #     generate_trigger(triggers)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("UPDATE order_response SET active_order = 'inactive' WHERE active_order = 'Active' RETURNING order_id, order_status, status_desc") 
        order_ids = cursor.fetchall()
        print("order_ids :",order_ids)            
        return Response({"status":"Success", "message": "Success","content":order_ids})        
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})





jobqueue = multiprocessing.Queue()
# trigger condition
def group_apply_filters(triggers):

    while True:
        print('trigger in apply filter fun',triggers)
        print("************apply_filters function*******************")
        print(triggers," :  ",type(triggers))
        trigger_ids = []
        print("//////////////////")
        for i in triggers:
            trigger_id = i['trigger_id']    # trigger_id in list
            trigger_ids.append(i['trigger_id'])
        # print('trigger_id :',trigger_id)
        print('trigger_ids :',trigger_ids)

        trigger_id = str(trigger_id)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("SELECT trigger_id from trigger_condition_list WHERE trigger_list like  '%"+trigger_id+"%'")
        
        trigger_condition_id = cursor.fetchone()
        print("trigger_condition_list trigger_id : ",trigger_condition_id)
        trigger = trigger_condition_id[0]
        print("trigger_condition_id :==== ",trigger)
        # print(type(trigger))
        triggerId = str(trigger)

        cursor.execute("SELECT group_id from master_company_group WHERE trigger_id ="+triggerId)
        group_id = cursor.fetchone()
        group_id = str(group_id[0])
        print("group_id ",group_id)

        cursor.execute("SELECT order_id from group_orders WHERE group_id ="+group_id)
        order_id_data = cursor.fetchone()
        order_id_data = str(order_id_data[0])
        print("order_id_data ",order_id_data)

        cursor.execute("SELECT trigger_list from trigger_condition_list WHERE trigger_id ="+triggerId)
        order_ids_data = cursor.fetchall()
        print('order_ids_data :',order_ids_data)
        
        order_ids = []
        for order in order_ids_data:
            order_ids.append(order[0])
        print('order_ids :::',order_ids)

        for trigger_condtion_id in trigger_ids:
            # print("inside for :",order_id)
            trigger_condtion_id =str(trigger_condtion_id)
            try:
                # order_id trigger_condition_id 
                cursor.execute("INSERT INTO group_trigger_condition_status VALUES("+order_id_data+","+triggerId+","+trigger_condtion_id+","+group_id+",False,False,False,False,False,False,False,False,"+order_id+")")
                connection.commit()
                print('success')
            except:
                print("except ",sys.exc_info())

        dic = {}
        count = 0
        for trigger in triggers:
            count += 1
            # print()
            print('count@@@@@@@@@@@@@@@@@',count)
            print(trigger["trigger_id"])
            if trigger["trigger_condition_id"]==1:
                dic[1]='criteria_price'
                criteria_price(trigger,triggerId,cursor)     
            elif trigger["trigger_condition_id"]==2:
                dic[2]='criteria_moving_average'
                criteria_moving_average(trigger,triggerId,cursor)
            elif trigger["trigger_condition_id"]==3:
                dic[3]='criteria_volume'
                criteria_volume(trigger,triggerId,cursor)
            elif trigger["trigger_condition_id"]==4:
                dic[4]='criteria_p2p1'
                criteria_p2p1(trigger,triggerId,cursor)
            elif trigger["trigger_condition_id"]==5:
                pass  
            elif trigger["trigger_condition_id"]==6:
                dic[6]='criteria_RSI'
                criteria_RSI(trigger,triggerId,cursor)  
            elif trigger["trigger_condition_id"]==7:
                dic[7]='criteria_p1_minus_p2'
                criteria_p1_minus_p2(trigger,triggerId,cursor)  
            elif trigger["trigger_condition_id"]==8:
                dic[8]='criteria_p1_plus_p2'
                criteria_p1_plus_p2(trigger,triggerId,cursor)  
            # dict={1:"price"}
            # list = {"price"}
            # print('trigger_condition_id :::::',trigger_condition_id)
            # print('trigger_condition_id :::::',type(trigger_condition_id))
            # print(trigger_condition_id[0])
            id_trigger_condition = trigger_condition_id[0]
            id_trigger_condition = str(id_trigger_condition)
            # print('trigger_condition_id :::::',id_trigger_condition)

        for order_id in order_ids:
            # print("inside for :",order_id)
            order_id =str(order_id)

            query = "select "
            for key in dic:
                query += dic[key]+","
            query = query[:-1]
            query += " from trigger_condition_status WHERE trigger_id ="+id_trigger_condition+" and order_id="+order_id
            print('query :',query)
            cursor.execute(query)
            trigger_condition_status = cursor.fetchall()
            print("trigger_condition_status :",trigger_condition_status)
        condition_status = False
        for i in trigger_condition_status:
            if i == True:
                condition_status = True
            else:
                condition_status = False

                print("Unexpected error:", sys.exc_info())   
                exc_tuple = sys.exc_info()  
                # trigger_error = count 
                return Response({"status":"failure", "message": exc_tuple})
                        # break
        if condition_status == True:
            combine_criteria(triggers,order_id)
            







def apply_filters_2(trigger):
    print('trigger :',trigger)
    # return HttpResponse("working")

# ------------------



# def job(trigger):
#     try:
#         print("trigger:")
#         print("trigg :",trigger)
#         print("I'm running on thread " )
#     except:
#         print('error in job')
#     # return schedule.CancelJob
        
# # def job2():
# #     print("running job2 function %s" % threading.current_thread())

# # def run_threaded(job_func):
# #     job_thread = threading.Thread(target=job_func)
# #     job_thread.start()



# def worker_main():
#     print("this is worker main function")
#     print("job :")
#     while True:
#         time.sleep(2)
#         try:
#             print("inside try",jobqueue.qsize())
#             print('jobqueue :',jobqueue)
#             print('jobqueue.get() :',jobqueue.get())
            
#             job_func, job_arg = jobqueue.get()
#             print('job_func ',jobqueue.qsize())
#             job_func(*job_arg)
#         except Exception as e:
#             print("worker error",e)
#             print(sys.exc_info)


# worker_thread = threading.Thread(target=worker_main)
# worker_thread.start()
# # schedule.CancelJob

# def other(request):
#     print("this is other function()")
#     trigger = "this is trgger!!!!!"
#     # schedule.every(10).seconds.do(run_threaded,job)
#     # jobqueue = Queue.Queue()
#     # jobqueue = multiprocessing.Queue()
#     print('jobqueue ',jobqueue.qsize())
#     schedule.every(1).seconds.do(jobqueue.put,job(trigger))
#     # schedule.every(10).minutes.do(job('do something', 'like this'))
#     # time.sleep(2)

#     # newjob = schedule.every(10).seconds.do(run_threaded,job2)
#     # schedule.cancel_job(newjob)
#     # schedule.every(10).seconds.do(run_threaded, job)
#     # schedule.every(10).seconds.do(run_threaded, job)
#     # schedule.every(10).seconds.do(run_threaded, job)
#     while 1:
#         schedule.run_pending()
#         time.sleep(1)
#     return schedule.CancelJob

#     # return HttpResponse('this is other function()') 

# threading.active_count() 


# -------------------------


# import schedule
# import time
# running = True
# def test():
#     global running
#     running = False
#     print("Stopped")
#     return schedule.CancelJob
# schedule.every(10).seconds.do(test)
# while running:
#     print("test")
#     schedule.run_pending()
#     time.sleep(1)