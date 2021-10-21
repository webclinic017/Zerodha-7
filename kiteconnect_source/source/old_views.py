from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.defaults import page_not_found
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
import random
import logging
import json
import psycopg2
from itertools import zip_longest
import sys
import threading
import os.path
import enum
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



# @api_view(['GET','POST'])
@login_required(login_url='login_view')
def home(request):
    print("home function")
    user_id = request.user.id
    print("session created")
    current_user = request.user
    print(current_user)
    user_id = request.user.id
    user_id = str(user_id)
    print("------------")
    print(type(user_id), str(user_id))  
    print("=================")     
    # try:
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type,o.is_cancelled FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND t.user_id ="+ user_id)
    rows = cursor.fetchall()
    # print("rowsrowsrowsrowsrowsrows ::",rows[0])
    print("==================",rows)
    # if len(rows) != 0 :
    print("not none")
    dict_result = []
    for row in rows:
        dict_result.append(dict(row))
    # print("dict_result_2[0] :",dict_result)

    # print("dict_result_2[0] :",dict_result[0])


    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id, master_product_type.product_type,o.is_cancelled FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='True' AND t.user_id ="+ user_id)
    rows2 = cursor.fetchall()
    dict_result_2 = []
    for row in rows2:
        dict_result_2.append(dict(row))
        # print(dict_result_2)
    cursor.close()
    connection.close()
    # print("dict_result ",dict_result)
    # print("dict_result_2 ",dict_result_2)
    return render(request, 'index.html',{"content":dict_result,"dict_result_2":dict_result_2,"current_user":current_user,"user_id":user_id})        



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

def fun1(request):
    return render(request,'sort_table.html')

# Collect all the instuments
@api_view(['GET'])
def get_instruments(request):        
    print(" get_instruments function calling ")
    print("request")
    try:        
        print("inside try")    
        exchange=None
        print("===========")
        data = request.query_params.get("exchange")
        print("data ",data)
        print("===========")
        # request.data["trigger"]["trigger_name"]
        if request.query_params.get("exchange") is not None:
            #exchange=request.query_params['exchange']
            switcher={
                '1':'BSE',
                '2':'MCX',
                '3':'NFO',
                '4':'NSE'
            }
            exchange = request.query_params.get("exchange")

            # exchange=switcher.get(request.query_params['exchange'])
            print("exchange == :",exchange)
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
            
            # This is old code
            # postgres_insert_query = "SELECT public.get_instruments_v1('"+symbolName+"','"+exchange+"')"
            
            cursor.execute("SELECT exchange FROM master_exchange where exchange_id ="+str(exchange))
            exchange = cursor.fetchone()
            print("exchange ",exchange)
            postgres_insert_query = "SELECT public.get_instruments_v1('"+symbolName+"','"+exchange[0]+"')"

            # This is an example of exchange
            # postgres_insert_query = "SELECT public.get_instruments_v1('"+symbolName+"','NSE')"

            print("postgres_insert_query :",postgres_insert_query)
        else:
            # postgres_insert_query = "SELECT public.get_instruments('"+symbolName+"','')"  
            # postgres_insert_query="SELECT * FROM public.instruments WHERE items->>'tradingsymbol' LIKE '"+symbolName+"' AND items->>'exchange' =''"
            pass
               

        cursor.execute(postgres_insert_query, (symbolName,exchange,))
        rows = cursor.fetchall()
        # print("-----------------------------------------------------------------------------")
        # print('rows :',rows)
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
        print("order_trigger_name : ",order_trigger_name)
        print("order_trigger_name : ",type(order_trigger_name))
        cursor.execute("SELECT trigger_id from triggers where trigger_name =\'"+order_trigger_name+"\'")
        list_order_trigger_id = cursor.fetchall()
        print('list_order_trigger_id :',list_order_trigger_id)

        list_trigger_id = []
        for i in list_order_trigger_id:
            print("i :==",i[0])
            list_trigger_id.append(i[0])
        print("i :===* ",i)
        print("list_trigger_id ::",list_trigger_id)
        print("----------------------****")

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


        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # postgres_insert_query = """SELECT * from public.get_triggers_orders()"""
        # cursor.execute(postgres_insert_query,()) 
        # rows = cursor.fetchall()

        cursor.execute("SELECT o.order_id, t.trigger_id,t.trigger_criteria,t.symbol,e.exchange_id,e.exchange,c.trigger_condition_id, b.buy_sell_id,o.quantity,p.product_type_id,p.product_type,o.symbol as order_symbol,o.price,o.trigger_price,b.buy_sell, eo.exchange_id as order_exchange_id,eo.exchange as order_exchange, mo.order_type_id,mo.order_type FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id JOIN public.master_exchange eo ON eo.exchange_id=o.exchange_id JOIN public.master_buy_sell b ON o.buy_sell=b.buy_sell_id JOIN public.master_product_type p ON p.product_type_id=o.product_type JOIN public.master_order_type mo ON mo.order_type_id=o.order_type WHERE t.is_active=true order by t.trigger_id asc") 
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
        # print(0/0)
        print("triggers ::::",triggers)
        cursor.close()
        connection.close()
        return triggers
        # new code



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
        schedule.every(15).seconds.do(jobqueue.put,apply_filters(triggers))


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
        # order_ids = cursor.fetchall()

        # print("order_ids :=",order_ids)

        return Response({"status":"success", "message": "success"})        
            
        # return Response({"status":"Success", "message": "Success","content":order_ids})        
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})

jobqueue = multiprocessing.Queue()
# trigger condition
def apply_filters(triggers):

    while True:
        # print('trigger in apply filter fun',triggers)
        print("************apply_filters function*******==************")
        # print(triggers," :  ",type(triggers))
        for i in triggers:
            trigger_id = i['trigger_id']    # trigger_id in list
        # print('trigger_id :',trigger_id)

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
            # print("After if count",order_id)
            order_id =str(order_id)
            print("order_id :===-----------",order_id)
            try:
                cursor.execute("select count(*) from trigger_condition_status where trigger_id ="+triggerId)
                count = cursor.fetchone()

# # new code (14/06/2021)
# # Price
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=1")
#                 price_trigger_count = cursor.fetchone()
#                 print("price_trigger_count :=",price_trigger_count)
#                 price_trigger_count = price_trigger_count[0]
#                 price_trigger = ""
#                 for i in range(price_trigger_count):
#                     price_trigger += "0|"
#                 print("after loop :=",price_trigger)

# # Moving average
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=2")
#                 moving_avg_trigger_count = cursor.fetchone()
#                 print("moving_avg_trigger_count :=",moving_avg_trigger_count)
#                 moving_avg_trigger_count = moving_avg_trigger_count[0]
#                 moving_avg_trigger = ""
#                 for i in range(moving_avg_trigger_count):
#                     moving_avg_trigger += "0|"
#                 print("after loop :=",moving_avg_trigger)

# # Volume
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=3")
#                 volume_trigger_count = cursor.fetchone()
#                 print("volume_trigger_count :=",volume_trigger_count)
#                 volume_trigger_count = volume_trigger_count[0]
#                 volume_trigger = ""
#                 for i in range(volume_trigger_count):
#                     volume_trigger += "0|"
#                 print("after loop :=",volume_trigger)

# # (P2-P1)/P1
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=4")
#                 p2_p1_trigger_count = cursor.fetchone()
#                 print("p2_p1_trigger_count :=",p2_p1_trigger_count)
#                 p2_p1_trigger_count = p2_p1_trigger_count[0]
#                 p2_min_p1_div_p1_trigger = ""
#                 for i in range(p2_p1_trigger_count):
#                     p2_min_p1_div_p1_trigger += "0|"
#                 print("after loop :=",p2_min_p1_div_p1_trigger)

# # RSI
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=6")
#                 rsi_trigger_count = cursor.fetchone()
#                 print("rsi_trigger_count :=",rsi_trigger_count)
#                 rsi_trigger_count = rsi_trigger_count[0]
#                 rsi_trigger = ""
#                 for i in range(rsi_trigger_count):
#                     rsi_trigger += "0|"
#                 print("after loop :=",rsi_trigger)

# # P1 - P2
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=7")
#                 p1_min_p2_trigger_count = cursor.fetchone()
#                 print("p1_min_p2_trigger_count :=",p1_min_p2_trigger_count)
#                 p1_min_p2_trigger_count = p1_min_p2_trigger_count[0]
#                 p1_min_p2 = ""
#                 for i in range(p1_min_p2_trigger_count):
#                     p1_min_p2 += "0|"
#                 print("after loop :=",p1_min_p2)

# # P1 + P2
#                 cursor.execute("select count(*) from triggers where trigger_name=(select trigger_name from triggers where trigger_id="+trigger_id+") and trigger_condition_id=8")
#                 p1_plus_p2_trigger_count = cursor.fetchone()
#                 print("p1_plus_p2_trigger_count :=",p1_plus_p2_trigger_count)
#                 p1_plus_p2_trigger_count = p1_plus_p2_trigger_count[0]
#                 p1_pls_p2 = ""
#                 for i in range(p1_plus_p2_trigger_count):
#                     p1_pls_p2 += "0|"
#                 print("after loop :=",p1_pls_p2)

# for all triggers
                # cursor.execute("INSERT INTO trigger_condition_status VALUES("+triggerId+",\'"+price_trigger+"\',\'"+moving_avg_trigger+"\',\'"+volume_trigger+"\',\'"+p2_min_p1_div_p1_trigger+"\',\'"+rsi_trigger+"\',\'"+p1_min_p2+"\',\'"+p1_pls_p2+"\',"+order_id+")")


                count = int(count[0])
                # print("count[0] :count[0]",count)
                # print("before if count")
                # if count<=0:
                # print("After if count")
                # print("triggerId :===",triggerId)
                # print("order_id :==",order_id)
                # print("inside order if :",order_id)

                order_id = str(order_id)
                


                # price_trigger = "True" # id=\'"+userid+"\'"
                # cursor.execute("INSERT INTO trigger_condition_status VALUES("+triggerId+",\'"+price_trigger+"\',False,False,False,False,False,False,False,"+order_id+")")
                # cursor.execute("INSERT INTO trigger_condition_status VALUES("+triggerId+",'False,False,False,False,False,False,False,False,"+order_id+")")
                cursor.execute("INSERT INTO trigger_condition_status VALUES("+triggerId+",False,False,False,False,False,False,False,"+order_id+",False)")
                connection.commit()
                # print('success===')
                # else:
                #     print("not if ")
            except:
                print("except ",sys.exc_info())

        dic = {}
        count = 0
        print("triggers :=-",triggers)
        for trigger in triggers:
            count += 1
            print("order_id :=---=",order_id)
            print('count@@@@@@@@@@@@@@@@@',count)
            print(trigger["trigger_id"])
            if trigger["trigger_condition_id"]==1:
                dic[1]='criteria_price'
                criteria_price(trigger,triggerId,cursor,trigger_condition_id=0,group_id=0)     
            elif trigger["trigger_condition_id"]==2:
                dic[2]='criteria_moving_average'
                criteria_moving_average(trigger,triggerId,cursor,trigger_condition_id=0,group_id=0)     
            elif trigger["trigger_condition_id"]==3:
                dic[3]='criteria_volume'
                criteria_volume(trigger,triggerId,trigger_condition_id=0,group_id=0)     
            elif trigger["trigger_condition_id"]==4:
                dic[4]='criteria_p2p1'
                criteria_p2p1(trigger,triggerId,trigger_condition_id=0,group_id=0)
            elif trigger["trigger_condition_id"]==5:
                pass  
            elif trigger["trigger_condition_id"]==6:
                dic[6]='criteria_RSI'
                criteria_RSI(trigger,triggerId,cursor,trigger_condition_id=0,group_id=0)       
            elif trigger["trigger_condition_id"]==7:
                dic[7]='criteria_p1_minus_p2'
                criteria_p1_minus_p2(trigger,triggerId,trigger_condition_id=0,group_id=0)  
            elif trigger["trigger_condition_id"]==8:
                dic[8]='criteria_p1_plus_p2'
                criteria_p1_plus_p2(trigger,triggerId,trigger_condition_id=0,group_id=0)  

            id_trigger_condition = trigger_condition_id[0]
            id_trigger_condition = str(id_trigger_condition)

        print("count :=",count)
# New code if(14/06/2021)
        print("order_id ---=-",order_id)
        cursor.execute("SELECT is_executed FROM orders WHERE order_id="+order_id)
        is_executed = cursor.fetchone()
        is_executed = is_executed[0]
        if is_executed == False:
            print("order_idsorder_ids :=",order_ids)

            for order_id in order_ids:
                order_id =str(order_id)
                print("order_id :===",order_id)
                query = "select "
                for key in dic:
                    query += dic[key]+","
                query = query[:-1]
                query += " from trigger_condition_status WHERE trigger_id ="+id_trigger_condition+" and order_id="+order_id
                print('query :',query)
                cursor.execute(query)
                trigger_condition_status = cursor.fetchone()
                print('all query :',trigger_condition_status)

                condition_status = False
                for i in trigger_condition_status:
                    print("iiiiii",i)
                    if i == True:
                        condition_status = True
                    else:
                        condition_status = False
                        print("Unexpected error:", sys.exc_info())   
                        exc_tuple = sys.exc_info()  
                        # trigger_error = count 
                        # return Response({"status":"failure", "message": exc_tuple})
                        break
                print("condition_status ::=",condition_status)

                # if len(order_ids) == 1:   # make order_ids to order_id
                #     print("===========------------------------------------")
                #     order_id = str(order_id[0])
                #     # cursor.execute("SELECT is_executed FROM orders WHERE order_id = "+order_id)
                #     cursor.execute("SELECT is_cancelled FROM orders WHERE order_id = "+order_id)
                #     executed = cursor.fetchone()
                #     if executed[0] == True:
                #         break

                # if condition_status == True:
                #     combine_criteria(triggers,order_id,trigger)
        else:
            break            
                

def combine_criteria(triggers,order_id,trigger,company_name=None):
    # print("this is combine_criteria :" ,triggers)
    # print("=============================")
    print("order_id[0] :",order_id)
    execute_order(triggers,order_id,trigger,company_name)

    
#   criteria_price(trigger,triggerId,cursor,trigger_condition_id=0,group_id=0,order_id=0)     

def criteria_price(trigger,triggerId,cursor,trigger_condition_id,group_id=0):
    print("this is criteria price==========")
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

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = user_id[0]
        userid = str(userid)

        cursor.execute("SELECT api_key FROM auth_user WHERE id=\'"+userid+"\'")
        api_key = cursor.fetchone()
        api_key = api_key[0]

        kite = KiteConnect(api_key=api_key)
        # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
        kite.set_access_token(access_token)
        # print("trigger :::::::::::::::::::::::::::::::::::",trigger)
        try:
            exchange_symbol=trigger["exchange"]+":"+trigger["symbol"].strip()
            # print("in try")
        except:
            try:
                trigger_id = str(trigger['trigger_id'])
                cursor.execute("select symbol from triggers where trigger_id="+trigger_id)
                company_name = cursor.fetchone()            
                exchange_symbol=trigger["exchange"]+":"+company_name[0]
            except:
                print("error ",sys.exc_info())
        # exchange_symbol=trigger["exchange"]+":"+trigger["symbol"].strip()
        # print("exchange_symbol :",exchange_symbol)
        # exchange_symbol = str(exchange_symbol)
        try:
            # print("before ")
            quote_info=kite.quote(exchange_symbol)
            # print("quote_infoquote_info ::",quote_info)
            # print("after")
        except:
            print("error :=",sys.exc_info())

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
        # print("quote_info :",quote_info)
        triggerId = str(triggerId)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        if trigger is not None:
            print("this is inside IF ")
            if trigger["trigger_criteria"]["operator"]=="5" and quote_info[exchange_symbol]["last_price"]== Decimal(trigger["trigger_criteria"]["amount"]):
                print("True")
                criteria_price_status_update(triggerId,trigger_condition_id,group_id)
                # return True
                # cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)

                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="3" and quote_info[exchange_symbol]["last_price"]> Decimal(trigger["trigger_criteria"]["amount"]):
                print("operator 3 : ")
                # print("triggerId :",type(triggerId))
                # print("triggerId ::",triggerId)
                # return True
                criteria_price_status_update(triggerId,trigger_condition_id,group_id)

                # cursor.execute("UPDATE trigger_condition_status SET criteria_price = True WHERE trigger_id=\'"+triggerId+"\'") 
                print("operator  3 after: ")
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="1" and quote_info[exchange_symbol]["last_price"]>= Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                print("operator 1 : ")
                print("yes ")
                criteria_price_status_update(trigger,triggerId,trigger_condition_id,group_id)

                # cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="4" and quote_info[exchange_symbol]["last_price"]< Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                print("operator 4 : ")
                criteria_price_status_update(triggerId,trigger_condition_id,group_id)
                # cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            elif trigger["trigger_criteria"]["operator"]=="2" and quote_info[exchange_symbol]["last_price"] <= Decimal(trigger["trigger_criteria"]["amount"]):
                # return True
                print("operator 2 : ")
                criteria_price_status_update(triggerId,trigger_condition_id,group_id)

                # cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)

            # elif trigger["trigger_criteria"]["operator"]=="6" and ( quote_info[exchange_symbol]["last_price"]> 440) and quote_info[exchange_symbol]["last_price"]< 450:
            elif trigger["trigger_criteria"]["operator"]=="6" and ( quote_info[exchange_symbol]["last_price"]> Decimal(trigger["trigger_criteria"]["from_amount"]) and quote_info[exchange_symbol]["last_price"]< Decimal(trigger["trigger_criteria"]["to_amount"])):
                # return True
                print("operator 6 : ---------------------------------------")
                criteria_price_status_update(triggerId,trigger_condition_id,group_id)

                # cursor.execute('UPDATE trigger_condition_status SET criteria_price = TRUE WHERE trigger_id= '+triggerId)
                # execute_order(trigger)
            connection.commit() 
            print("after commit")

        else:
            print("else ")

            pass    
    except:
        print("this is exept")
        global_message = sys.exc_info()[0]

def criteria_price_status_update(trigger,triggerId,trigger_condition_id,group_id=0):
    print("criteria_price_status_update")
    print("trigger :==",trigger)
    print("trigger order_id :==",trigger['order_id'])
    order_id = str(trigger['order_id'])
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        # print("group_id==0",group_id)    
        # cursor.execute("SELECT criteria_price from trigger_condition_status where trigger_id="+triggerId)
        # criteria_price = cursor.fetchone() 
        # print("criteria_price :=",criteria_price)
        # criteria_price = criteria_price.split(";")
        # print("criteria_price :===",criteria_price)
        # print("triggerId :==0",triggerId)
        # print("order_id ------",order_id)
# new
        cursor.execute("UPDATE trigger_condition_status SET criteria_price = True WHERE order_id=\'"+order_id+"\'") 


# old
        # cursor.execute("UPDATE trigger_condition_status SET criteria_price = True WHERE trigger_id=\'"+triggerId+"\'") 
        # print("triggerId :==0",triggerId)
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_price = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("errorr",sys.exc_info())
    connection.commit()

# def generate_trigger(triggers):
#     print("this generate_trigger function ")
#     print("triggers :",generate_trigger)

#     pass

def criteria_moving_average(trigger,triggerId,cursor,trigger_condition_id,group_id=0):
    print('criteria_moving_average function')
    historical_data=None
    from_date=datetime.now()
    current_date=datetime.now()
    from_date_string=""
    to_date_string=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    total=0.00
    instrument_token=trigger["trigger_criteria"]["instrument_token"]
    # print('instrument_token :',instrument_token)
    time_frame=trigger["trigger_criteria"]["time_frame"]
    time_frame_type=trigger["trigger_criteria"]["time_frame_type"]
    time_frame_duration=trigger["trigger_criteria"]["time_frame_duration"]
    period=trigger["trigger_criteria"]["period"]
    # print("time_frame ,",time_frame)
    # print("time_frame_type ,",time_frame_type)
    # print("time_frame_duration ,",time_frame_duration)
    # print("period ,",period)

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
                # print("time_frame_duration",time_frame_duration)
                # print("period ",period)
                pastDays= ((int(time_frame_duration,0)*int(period,0))/375) + 1
                # pastDays= ((int(time_frame_duration,0)*int(period,0))/390) + 1

                # print('pastDays :;;;;;',pastDays)
                # print('pastDays :',type(pastDays))

                #calculate saturday and sunday
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 3)
                # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
                # print("current_date ",current_date)
                # print("timedelta(days=pastDays) ",timedelta(days=pastDays))
                from_date=current_date - timedelta(days=pastDays)
                # print("from_date ::",from_date)
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 2)

                from_date=current_date - timedelta(days=pastDays+1)
            # print("from_date ",from_date)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            # print('from_date_string :==',from_date_string)
            # print("to_date_string :==",to_date_string)
            # print("time_frame :=",time_frame)
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            # print('totalRecords :==',totalRecords)
            #periodLimit=int(period)

# vipul

            new_period = int(period)
            # print("new_period ::: ",new_period)
            new_historical_data = historical_data[-new_period:]
            # print("------===")
            # for i in new_historical_data:
            #     print(i)

# end vipul

            # print('period ::::',period)
            # print('totalRecords::::',totalRecords)
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0
            for data in new_historical_data:
                # print("data :==",data)
                total=total+data["close"]
                actualCounts=actualCounts+1  

                # print("threshold :==",threshold)
                # print("total ::==",total)
                # if threshold > startIndex:
                #     total=total+data["close"]
                #     actualCounts=actualCounts+1                   
                # threshold=threshold+1
            # print("total :",total)
            # print('actualCounts ',actualCounts)
            moving_average=total/actualCounts
            print("moving_average :==",moving_average)
            

        #If it is MA avg
        elif trigger["trigger_criteria"]["moving_average"]=="MA avg":
           #modification start
            pastDays=0
            threshold=1
            startIndex=0
            current_total=0.00
            averageCountMA=int(trigger["trigger_criteria"]["moving_average_candles"],0)
            #period=int(period,0) + averageCountMA
            print("averageCountMA ::",averageCountMA)
            recordsNeeded=int(period,0) + averageCountMA
            print('recordsNeeded :',recordsNeeded)

            if time_frame_type=="minute":
                #total minutes in a complete market day=375
                #for 1 minute: day=1/375
                #for fiven minutes: days = (1*given minutes)/375
                #we will add 1 more days for safe side
                pastDays= ((int(time_frame_duration,0))*(recordsNeeded/375) + 1)
                #calculate saturday and sunday              
            elif time_frame=="day":
                pastDays= (int(time_frame_duration,0)*recordsNeeded) + 50
                print("pastDays :--",pastDays)
            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 3)
            print("pastDays :--=",pastDays)
            

            #pastDays=pastDays*averageCountMA
            from_date=current_date - timedelta(days=pastDays+1)
            print("from_date ::",from_date)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            print("from_date_string ::=",from_date_string)
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            print("totalRecords ::==",totalRecords)


# sandeep comment start

            # new_historical_data=[]
            # actualCounts=0
            # outerLoopCount=0
            # threshold=0
            # startIndex=totalRecords-(int(period,0) + averageCountMA)
            # for data in latest_historical_data:                
            #     if  threshold >= startIndex:
            #         new_historical_data.append(data) 
            #     threshold=threshold+1  


            # #totalExpectedCandles = int(period,0) * averageCountMA
            # rangeLimit=int(period,0)
            # iterationIndex=0
            # for i in range(averageCountMA):
            #     for data in new_historical_data:  
            #         print("data :",data) 
            #         # print("total :",total)
            #         # print('data["close"] ',data["close"])
            #         # total=total+data["close"]
            #         iterationIndex=iterationIndex+1
            #         actualCounts=actualCounts+1
            #         # print("actualCounts ",actualCounts)
            #         if iterationIndex==rangeLimit:
            #             # print("data :",data) 
            #             # print("actualCounts :",actualCounts) 
            #             # print("total :",total)
            #             current_moving_average=total/actualCounts

            #             # print("current_moving_average ::",current_moving_average)

            #             #rangeLimit=rangeLimit+1
            #             new_historical_data.pop(0)
            #             iterationIndex=0
            #             totalMA=totalMA+current_moving_average
            #             break
            #     outerLoopCount=outerLoopCount+1
            # moving_average=totalMA/outerLoopCount
            # print("moving_average :",moving_average)
            # # modification end
 
 # comment End            
# Vipul code start

            totalRecords=len(historical_data)
            print('totalRecords :==',totalRecords)
            new_period = int(period)
            print("new_period ::: ",new_period)
            new_period += int(trigger["trigger_criteria"]["moving_average_candles"])
            print("new_period :::=",new_period)
            print("------------------------------")
            new_historical_data = historical_data[-new_period:]
            print("------===")
            print('period ::::',period)
            print('totalRecords::::',totalRecords)
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0
            closing_price = []
            for data in new_historical_data:
                print("data :==",data)
                closing_price.append(data["close"])
                total=total+data["close"]
                actualCounts=actualCounts+1  
            print("total :",total)
            print("closing_price ::::",closing_price)
            closing_price.reverse()
            print("reversed closing_price ::::",closing_price)
            print('actualCounts ',actualCounts)
            # moving_average=total/actualCounts
            # print("moving_average :==",moving_average)

# new code
            print("START")
            print("period ",period)
            print("period type ",type(period))
            print('trigger["trigger_criteria"]["moving_average_candles"]) ::',type(trigger["trigger_criteria"]["moving_average_candles"]))
            moving_average_candles = int(trigger["trigger_criteria"]["moving_average_candles"])
            print("moving_average_candles ",type(moving_average_candles))
            result = [sum(closing_price[i:(i+int(period))]) for i in range(len(closing_price)-5)][:moving_average_candles]
            print(result)

            # result = [sum(l[i:(i+14)]) for i in range(len(l)-5)][:10]
            # print(result)

            list_of_moving_averages = []
            for total in result:
                each_moving_average  = int(total)/int(period)
                # print("each_moving_average ::",each_moving_average)
                list_of_moving_averages.append(each_moving_average)
            moving_average = 0
            len_mva = len(list_of_moving_averages)
            print("len_mva ",len_mva)
            for i in list_of_moving_averages:
                print(' i  ,',i)
                moving_average += i
            print('moving_average after :',moving_average)
            print("len_mva ::==",len_mva)
            moving_average = moving_average/len_mva
            print("moving_average ::===",moving_average)
            print("END")

            


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
            # instrument_token = 969473
            print("instrument_token :==",instrument_token)
            print("time_frame ",time_frame)
            print("from_date_string ",from_date_string)
            print("to_date_string ",to_date_string)
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            # totalRecords=len(historical_data)
            totalRecords = int(period)
            #periodLimit=int(period)
            print("totalRecords ,",totalRecords)

# vipul

            new_period = int(period)
            print("new_period ::: ",new_period)
            new_historical_data = historical_data[-new_period:]
            print("------===")
            print('period ::::',period)
            print('totalRecords::::',totalRecords)
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0
            for data in new_historical_data:
                print("data :==",data)
                total=total+data["close"]
                actualCounts=actualCounts+1  

                # print("threshold :==",threshold)
                # print("total ::==",total)
                # if threshold > startIndex:
                #     total=total+data["close"]
                #     actualCounts=actualCounts+1                   
                # threshold=threshold+1
            print("total :",total)
            print('actualCounts ',actualCounts)
            moving_average=total/actualCounts
            print("Simple moving_average :============================",moving_average)
            

# # end vipul


            # if totalRecords > int(period):
            #     startIndex=totalRecords-int(period)
            # else:
            #     startIndex=0
            # actualCounts=0
            # for data in historical_data:
            #     # print("data ::",data)
            #     if threshold > startIndex:
            #         total=total+data["close"]
            #         actualCounts=actualCounts+1                   
            #     threshold=threshold+1
            # print('total ',total)
            # print('actualCounts ',actualCounts)
            # moving_average=total/actualCounts
            # print("moving_average -==",moving_average)
            
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
            print("exchange_symbol ==:",exchange_symbol)
            exchange_symbol = str(exchange_symbol)
            quote_info=kite.quote(exchange_symbol)
            # exchange_symbol=trigger["exchange"]+":"+trigger["symbol"]
            # quote_info=kite.quote(exchange_symbol)
            # (P-MA/MA) getting value of P
            # print("quote_info ::",quote_info)
            p_formula=quote_info[exchange_symbol]["last_price"]
            print("p_formula ::",p_formula)
            print("moving_average :===",moving_average)
            moving_average= (p_formula-moving_average)/moving_average
            print("moving_average (P-MA)/MA ",moving_average)

            

        #If it is (P-MA/MA avg)
        elif trigger["trigger_criteria"]["moving_average"]=="P-MA/MA avg":
             #now get quote
            print("inside (P-MA)/MA")
            cursor.execute("SELECT user_id FROM current_login_user")
            user_id = cursor.fetchone()
            print('user_id :==',user_id)
            userid = user_id[0]
            print("userid :",userid) 
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
            print("totalRecords ::",totalRecords)
            new_historical_data=[]
            #periodLimit=int(period)
            # if totalRecords > int(period):
            #     startIndex=totalRecords-int(period)
            # else:
            #     startIndex=0
            actualCounts=0
            threshold=0
            startIndex=totalRecords-(int(period,0) + averageCountMA)
            print("startIndex ::",startIndex)
           


# #  vipul code start
        #  P-MA/MA Done

            new_period = int(period)
            print("--------------------------------------------")
            print("new_period ::-=---------------------",new_period)
            print('int(trigger["trigger_criteria"]["moving_average_candles"]) ',trigger["trigger_criteria"]["moving_average_candles"])
            new_period += int(trigger["trigger_criteria"]["moving_average_candles"])
            print("new_period ::: ",new_period)
            new_historical_data = historical_data[-new_period:]            

            list_closing_price = []
            for data in new_historical_data:
                print("data :========",data)
                list_closing_price.append(data["close"])
            print("START")

            list_closing_price.reverse()
            print("list_closing_price :: ",list_closing_price)
            period = int(period)
            moving_average_candles = int(trigger["trigger_criteria"]["moving_average_candles"])
            
            # sum of all closing price by example(1-9,2-10,3-11)
            result = [sum(list_closing_price[i:(i+int(period))]) for i in range(len(list_closing_price)-5)][:moving_average_candles]
            print("======================")                
            print("result ::",result)  

            # Simple Moving average AVG
            mv = []
            for i in result:
                mv.append(i/period)

            print("Moving average :",mv)

            # P-MA/MA
            p_ma_div_ma = 0
            for p, m in zip(list_closing_price, mv):
                print("p ::=",p)
                print("m ::=",m)
                print("(p-m)/m ",(p-m)/m)
                p_ma_div_ma += (p-m)/m
            print("=================")
            print("p_ma_div_ma ::", p_ma_div_ma)
            length_list_closing_price = len(list_closing_price)
            print("length_list_closing_price ",length_list_closing_price)
            moving_average = p_ma_div_ma/moving_average_candles
            # Final moving average
            print("moving_average (P-MA/MA) AVG ::",moving_average)

#  end new code
    
# # end vipul


            # totalExpectedCandles = int(period,0) * averageCountMA
            # for data in historical_data:                
            #     if  threshold > startIndex:
            #         new_historical_data.append(data) 
            #     threshold=threshold+1      
            
            # rangeLimit=int(period,0)
            # iterationIndex=0
            
            #             ######
            # outerLoopCount=0

            # for i in range(averageCountMA):
            #     actualCounts=0
            #     total=0.00
            #     current_closing=0.00
            #     for data in new_historical_data:   
            #         print("data ::",data)
            #         total=total+data["close"]
            #         iterationIndex=iterationIndex+1
            #         actualCounts=actualCounts+1
            #         current_closing=data["close"]
            #         if iterationIndex==rangeLimit:
            #             current_moving_average=total/actualCounts
            #             #Now get (P-MA)/MA
            #             current_formula=(current_closing-current_moving_average)/current_moving_average
            #             print("current_formula :",current_formula)
            #             #rangeLimit=rangeLimit+1
            #             new_historical_data.pop(0)
            #             iterationIndex=0
            #             totalMA=totalMA+current_formula
            #             break
            #     outerLoopCount=outerLoopCount+1
            # moving_average=totalMA/outerLoopCount
            # print("moving_average :",moving_average)
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
        print("moving average::=",moving_average)
        if trigger["trigger_criteria"]["operator"]=="5" and moving_average== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)
            
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and moving_average> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and moving_average>= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and moving_average< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="2" and moving_average <= Decimal(trigger["trigger_criteria"]["amount"]):
            print('trigger_criteria 2 ***********')
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="6" and ( moving_average> Decimal(trigger["trigger_criteria"]["from_amount"]) and moving_average< Decimal(trigger["trigger_criteria"]["to_amount"])):

            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
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
                print("=================================================================")
                pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
                print("pastDays ::",pastDays)
                if pastDays <= 7:
                    pastDays=pastDays+3
                else:
                    pastDays = pastDays + ((pastDays/7) * 2)
                # pastDays=pastDays*2
                print("pastDays ::",pastDays)

                from_date=current_date - timedelta(days=pastDays+1)
            print("from_date :::",from_date)
            print("out if else")
            # from_date = datetime.now()-timedelta(15)

            # from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")

            # print("from_date ::::",from_date)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            print('from_date_string ',from_date_string)
            print('to_date_string ',to_date_string)
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            print("totalRecords := ",totalRecords)

# sandeep code            
            periodLimit=int(period)
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
            # #calculate MA that will be used as EMA for 1st record
            # print("threshold ",threshold)
            # print("startIndex ",startIndex)
            for data in historical_data:
                # print("data :: ",data)
                if threshold > startIndex:
                    new_historical_data.append(data)                  
                threshold=threshold+1
                if sma_counter>=start_index_sma and sma_counter <= end_index_sma:
                    # print('data["close"] ::',data["close"])
                    sma_total=sma_total+data["close"]
                    sma_counts=sma_counts+1
                sma_counter=sma_counter+1
            print("sma_total ::",sma_total)
            print("sma_counts ::",sma_counts)
            print("beefore loop")
            # for i in new_historical_data:
            #     print(i)
            exponential_for_first_record=sma_total/sma_counts
            print("exponential_for_first_record ",exponential_for_first_record)    
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
                # print("length of historical data :",N)
                #k = 2/(N+1)
                k=2/(N+1)
                # print("k :",k)
                # y = previous period
                y=previous_period_ema
                #(Price(t) * k) + (EMA(y) * (1-k))
                # print("current_price :",current_price)
                # print("k ",k)
                # print("previous_period_ema ",previous_period_ema)
                
                ema_current=(current_price * k) + (previous_period_ema * (1-k))
                # print("ema_current :",ema_current)
                # print("total_ema ",total_ema)
                total_ema=total_ema+ema_current
                # print("total_ema ",total_ema)
                previous_period_ema=ema_current
                ema_last_record=ema_current
            
            moving_average=ema_last_record
            print('moving_average  : =',moving_average)
                #ema_current=
            print("end MA")
# sandeep code end           

#  Vipul code start

            # new_period=int(period) + int(period)
            # print("period ::",period)
            # # new_period += int(trigger["trigger_criteria"]["moving_average_candles"])
            # print("new_period ::: ",new_period)
            # # new_historical_data = []
            # new_historical_data = historical_data[-new_period:] 

            # # moving_average = new_historical_data[len(new_historical_data)//2:] # C = A[len(A)//2:]

            # # A[:len(A)//2]
            # simple_moving_average_closing_price = new_historical_data[:len(new_historical_data)//2] 

            # print("moving_average ::==")
            # # for i in simple_moving_average_closing_price:
            # #     print("moving_average :",i)
            # print(" ")
            # print(" ")
            # print(" ")
            # print(" ")
            # sma = 0
            # for i in simple_moving_average_closing_price:
            #     sma += i["close"]
            # print("total SMA :",sma)
            # sma = sma / int(period)
            # print("sma :=",sma)   
            # k = 2*(int(period)+1)
            # print("k :: ",k)


 
                 
         

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
                # print("data ::",data)
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
            print("previous_period_ema :: ",previous_period_ema)
            ema_calculation_index=len(new_historical_data)-averageCountMA
            ema_records_implemented=0
            #for i in range(averageCountMA):
            for data in new_historical_data:  
                print("data: ",data)
                #price(t)
                current_price=data["close"] 
                    # N = number of periods in EMA
                N=int(period,0)
                #k = 2/(N+1)
                k=2/(N+1)
                # y = previous period
                y=previous_period_ema
                #(Price(t) * k) + (EMA(y) * (1-k))
                print("previous_period_ema :",previous_period_ema)
                ema_current=(current_price * k) + (previous_period_ema * (1-k)) 
                previous_period_ema=  ema_current
                # print(ema_current)              
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
                    # print('pastDays ;;:',pastDays)
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
            
            from_date = datetime.now() - timedelta(50)
            from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
            print('from_date_string :',from_date_string)
            # print("before historical_data")
            # print('instrument_token :=',instrument_token)
            # print('to_date_string :=',to_date_string)
            historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
            totalRecords=len(historical_data)
            print("historical_data :=",len(historical_data))
            # for i in historical_data:
            #     print('data',i)
            #periodLimit=int(period)
            print("period",period)
            print("totalRecords ",totalRecords)
            print("after hisorical data")
            if totalRecords > int(period):
                startIndex=totalRecords-int(period)
            else:
                startIndex=0
            actualCounts=0

            #to get 1st record for SMA
            start_index_sma=totalRecords-((int(period,0))*2)
            print('start_index_sma ',start_index_sma)
            #to get last record for SMA
            end_index_sma=totalRecords-(int(period,0))-1
            print('end_index_sma ',end_index_sma)
            sma_counter=0
            sma_counts=0
            sma_total=0.00

            new_historical_data=[]
            #calculate MA that will be used as EMA for 1st record
            for data in historical_data:
                # print("inside historical_data")
                # print("data :",data)
                # print('threshold ',threshold)
                # print('startIndex ',startIndex)
                if threshold >= startIndex:
                    new_historical_data.append(data)                  
                threshold=threshold+1
                # print("threshold :",threshold)
                # print("start_index_sma :",start_index_sma)
                # print("sma_counter :",sma_counter)
                # print("end_index_sma :",end_index_sma)
                # print("sma_total :=",sma_total)
                # print("sma_counts :=",sma_counts)    

                if sma_counter>=start_index_sma and sma_counter <= end_index_sma:
                    # print("yes inside if ")
                    sma_total=sma_total+data["close"]
                    sma_counts=sma_counts+1
                sma_counter=sma_counter+1
                # print("sma_counter inside if ",sma_counter)
            # print("after loop :")
            # print("sma_total :",sma_total)
            # print("sma_counts :",sma_counts)
            exponential_for_first_record=sma_total/sma_counts
            # print("exponential_for_first_record ",exponential_for_first_record)
            #exponential_for_first_record=total/actualCounts
            #exponential_for_first_record=moving_average

            #now calculate EMA for all other records
            actualCounts=0
            previous_period_ema=exponential_for_first_record
            ema_last_record=0.00
            last_record_price=0.00
            print("before historial data")
            for data in new_historical_data:
                # print("data 2 :",data) 
                # print("inside new_historical_data")
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
            print("trigger:=================",trigger['trigger_id'])
            moving_average=(last_record_price-ema_last_record)/ema_last_record
            print("moving_average p-ma/ma expo:====",moving_average)
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
                # print("data :",data)             
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
                print("data :",data)             
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
        print("moving average:::=",moving_average)
        print("befotre conf=ditions")#2544
        print('trigger["trigger_id"]',trigger["trigger_id"])

        print('trigger["trigger_criteria"]["operator"]',trigger["trigger_criteria"]["operator"])
        print('Decimal(trigger["trigger_criteria"]["amount"]',trigger["trigger_criteria"]["amount"])
        print("moving_average ",moving_average)
        if trigger["trigger_criteria"]["operator"]=="5" and moving_average== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # execute_order(trigger)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="3" and moving_average> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # execute_order(trigger)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="1" and moving_average>= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # execute_order(trigger)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="4" and moving_average< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # execute_order(trigger)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="2" and moving_average <= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # execute_order(trigger)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)

        elif trigger["trigger_criteria"]["operator"]=="6" and ( moving_average> Decimal(trigger["trigger_criteria"]["from_amount"]) and moving_average< Decimal(trigger["trigger_criteria"]["to_amount"])):
            criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id)

            # execute_order(trigger)
            # cursor.execute('UPDATE trigger_condition_status SET criteria_moving_average = TRUE WHERE trigger_id= '+triggerId)
            # execute_order(trigger)
        connection.commit()
    print('outside if criteria_moving_average')
        

def criteria_moving_average_status_update(triggerId,trigger_condition_id,group_id=0):
    print("criteria_moving_average function",group_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        print("group_id==0",group_id)    
        print("triggerId ==:",triggerId)
        cursor.execute("UPDATE trigger_condition_status SET criteria_moving_average = True WHERE trigger_id=\'"+triggerId+"\'") 
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_moving_average = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("errorr",sys.exc_info())
    print("success UPDATED trigger_condition_status")
    connection.commit()


from django.utils import timezone
# import datetime         
def criteria_volume(trigger,triggerId,trigger_condition_id,group_id=0):
    print('criteria_volume trigger::,',trigger)
    historical_data=None
    from_date=datetime.now()
    current_date=datetime.now()
    from_date_string=""
    to_date_string=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    total=0.00
    print('testing')

    instrument_token=trigger["trigger_criteria"]["instrument_token"]
    time_frame=trigger["trigger_criteria"]["time_frame"]
    time_frame_type=trigger["trigger_criteria"]["time_frame_type"]
    time_frame_duration=trigger["trigger_criteria"]["time_frame_duration"]
    period="1"
    print('testing1')

    # period=trigger["trigger_criteria"]["period"]
    
    moving_average=0.00
    totalRecords=0
    total=0.00
    print('testing2')

    # connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    # cursor = connection.cursor()
    print("before if condition")
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
            print("time_frame_duration ",time_frame_duration)
            print("period ",period)
            pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
            print("pastDays ::::",pastDays)
            if pastDays <= 7:
                pastDays=pastDays+3
            else:
                pastDays = pastDays + ((pastDays/7) * 2)

            from_date=current_date - timedelta(days=pastDays+1)
        from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
        print("from_date_string :=",from_date_string)
        print('time_frame : ',time_frame)
        #     # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')

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
            print("data ",data)
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
        print("this is testing")
        print('current_volume :',current_volume)
        if trigger["trigger_criteria"]["operator"]=="5" and current_volume== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and current_volume> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and current_volume>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("inside operator 1")
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and current_volume< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="2" and current_volume <= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="6" and ( current_volume> Decimal(trigger["trigger_criteria"]["from_amount"]) and current_volume< Decimal(trigger["trigger_criteria"]["to_amount"])):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
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
            print("inside day")
            print("time_frame_duration ",time_frame_duration)
            print("period ",type(time_frame_duration))
            print("period ",period)
            print("period ",type(period))
            period = str(period)
            # try:
            pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
            print("pastDays ",pastDays)
            # except:
            #     print("errorr",sys.exc_info())
            if pastDays <= 7:
                pastDays=pastDays+3
                print("if pastDays ",pastDays)
            else:
                pastDays = pastDays + ((pastDays/7) * 2)
                print("else pastDays ",pastDays)

            from_date=current_date - timedelta(days=pastDays+1)
            print("from_date :",from_date)
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
            print("historical_data :",historical_data)
            if threshold > startIndex:
                new_historical_data.append(data)
                actualCounts=actualCounts+1                   
            threshold=threshold+1
                

        for data in new_historical_data:
            total=total+data["volume"]
        print("actualCounts :",actualCounts)
        print("total ",total)
        volume_average=total/actualCounts 
        print("before if volume")
        print('volume_average :',volume_average)
        print('trigger["trigger_criteria"]["amount"] :',trigger["trigger_criteria"]["amount"])
        print('trigger["trigger_criteria"]["operator"] :',trigger["trigger_criteria"]["operator"])

        if trigger["trigger_criteria"]["operator"]=="5" and volume_average== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and volume_average> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and volume_average>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("operator 1 :::")
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and volume_average< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="2" and volume_average <= Decimal(trigger["trigger_criteria"]["amount"]):
            print("operator 2 ::::")
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="6" and ( volume_average> Decimal(trigger["trigger_criteria"]["from_amount"]) and volume_average< Decimal(trigger["trigger_criteria"]["to_amount"])):
            criteria_volume_status_update(triggerId,trigger_condition_id,group_id)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger) 
        # connection.commit() 
    print('outside if')
              
def criteria_volume_status_update(triggerId,trigger_condition_id,group_id=0):
    print("criteria_volume_status_update",group_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        print("group_id==0",group_id)    
        cursor.execute("UPDATE trigger_condition_status SET criteria_volume = True WHERE trigger_id=\'"+triggerId+"\'") 
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_volume = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("errorr",sys.exc_info())
    connection.commit()

# def criteria_price(trigger,triggerId,cursor,trigger_condition_id,group_id=0):

def criteria_p2p1(trigger,triggerId,trigger_condition_id,group_id=0):

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

    print('quote_info_exchange2[exchange2_symbol]["last_price"] :=',quote_info_exchange2[exchange2_symbol]["last_price"])
    print('quote_info_exchange1[exchange1_symbol]["last_price"] :==',quote_info_exchange1[exchange1_symbol]["last_price"])
    calculated_criteria= ( quote_info_exchange2[exchange2_symbol]["last_price"]- quote_info_exchange1[exchange1_symbol]["last_price"])/quote_info_exchange1[exchange1_symbol]["last_price"]
    print('calculated_criteria ',calculated_criteria)
    if trigger is not None:
        if trigger["trigger_criteria"]["operator"]=="5" and calculated_criteria== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="3" and calculated_criteria> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="1" and calculated_criteria>= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="4" and calculated_criteria< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="2" and calculated_criteria <= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 

            # execute_order(trigger)
        elif trigger["trigger_criteria"]["operator"]=="6" and ( calculated_criteria> Decimal(trigger["trigger_criteria"]["from_amount"]) and calculated_criteria< Decimal(trigger["trigger_criteria"]["to_amount"])):
            criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 
        connection.commit() 
            # execute_order(trigger)
    else:
        pass
              
def criteria_p2p1_status_update(triggerId,trigger_condition_id,group_id=0):
    print("criteria_p2p1_status_update :",group_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        print("group_id==0",group_id)    
        cursor.execute("UPDATE trigger_condition_status SET criteria_p2p1 = True WHERE trigger_id=\'"+triggerId+"\'") 
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_p2p1 = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("errorr",sys.exc_info())
    connection.commit()



def criteria_p1_minus_p2(trigger,triggerId,trigger_condition_id,group_id=0):

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
    print("quote_info_exchange1 ",quote_info_exchange1)
    exchange2_symbol=trigger["exchange"] +":"+trigger["trigger_criteria"]["symbol2_exchange"]
    quote_info_exchange2=kite.quote(exchange2_symbol)
    print("quote_info_exchange2 ",quote_info_exchange2)
    print('quote_info_exchange1[exchange1_symbol]["last_price"] ',quote_info_exchange1[exchange1_symbol]["last_price"])
    print('quote_info_exchange2[exchange2_symbol]["last_price"] ',quote_info_exchange2[exchange2_symbol]["last_price"])
    calculated_criteria= ( quote_info_exchange1[exchange1_symbol]["last_price"] - quote_info_exchange2[exchange2_symbol]["last_price"])
    print("calculated_criteria :=",calculated_criteria)
    print('trigger["trigger_criteria"]["amount"] ',trigger["trigger_criteria"]["amount"])
    if trigger is not None:
        if trigger["trigger_criteria"]["operator"]=="5" and calculated_criteria== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="3" and calculated_criteria> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="1" and calculated_criteria>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("yes true")
            criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'")
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="4" and calculated_criteria< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger

        elif trigger["trigger_criteria"]["operator"]=="2" and calculated_criteria <= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)

        elif trigger["trigger_criteria"]["operator"]=="6" and ( calculated_criteria> Decimal(trigger["trigger_criteria"]["from_amount"]) and calculated_criteria< Decimal(trigger["trigger_criteria"]["to_amount"])):
            criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        connection.commit() 
    else:
        print("else ")
        # return 
        pass


def criteria_p1_minus_p2_status_update(triggerId,trigger_condition_id,group_id=0):
    print("criteria_p1_minus_p2_status_update :",group_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        print("group_id==0",group_id)    
        cursor.execute("UPDATE trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_p1_minus_p2 = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("errorr",sys.exc_info())
    connection.commit()


              
def criteria_p1_plus_p2(trigger,triggerId,trigger_condition_id=0,group_id=0):
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
    print("calculated_criteria :",calculated_criteria)
    if trigger is not None:
        print("insidee conditions")
        print('trigger["trigger_criteria"]',trigger["trigger_criteria"])
        print('calculated_criteria :',calculated_criteria)
        if trigger["trigger_criteria"]["operator"]=="5" and calculated_criteria== Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="3" and calculated_criteria> Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="1" and calculated_criteria>= Decimal(trigger["trigger_criteria"]["amount"]):
            print("true condition")
            criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="4" and calculated_criteria< Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="2" and calculated_criteria <= Decimal(trigger["trigger_criteria"]["amount"]):
            criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
            
        elif trigger["trigger_criteria"]["operator"]=="6" and ( calculated_criteria> Decimal(trigger["trigger_criteria"]["from_amount"]) and calculated_criteria< Decimal(trigger["trigger_criteria"]["to_amount"])):
            criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0)
            # cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
            # execute_order(trigger)
        connection.commit() 
    else:
        print("this is else")
        pass


def criteria_p1_plus_p2_status_update(triggerId,trigger_condition_id,group_id=0):
    print("criteria_p1_plus_p2_status_update :",group_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        print("group_id==0",group_id)    
        cursor.execute("UPDATE trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_id=\'"+triggerId+"\'") 
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_p1_plus_p2 = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("error",sys.exc_info())
    connection.commit()


#criteria RSI start

def criteria_RSI(trigger,triggerId,cursor,trigger_condition_id,group_id=0):
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
        print('pastDays',pastDays)
        #calculate saturday and sunday
        if pastDays <= 7:
            pastDays=pastDays+3
            print(" if pastDays :=",pastDays)
        else:
            pastDays = pastDays + ((pastDays/7) * 3)
            print(" else pastDays :=",pastDays)
        # from_date=current_date - timedelta(minutes=int(time_frame_duration,0)*int(period,0))
        from_date=current_date - timedelta(days=pastDays)
        print("from_date ::",from_date)
        print('from_date :=',from_date)
    elif time_frame=="day":
        print("inside day")
        pastDays= (int(time_frame_duration,0)*int(period,0)) + 50
        print("pastDays elif",pastDays)
        if pastDays <= 7:
            pastDays=pastDays+3
            print("pastDays if",pastDays)
        else:
            pastDays = pastDays + ((pastDays/7) * 2)
            print("pastDays else",pastDays)

        from_date=current_date - timedelta(days=pastDays+2)
        print("from_date ",from_date)
    print("no if no else ::")
    from_date_string=from_date.strftime("%Y-%m-%d %H:%M:%S")
    print('from_date_string :',from_date_string)
    #     # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')

    try:
        # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')
        print("to_date_string  :==",to_date_string)
        # historical_data=get_historical_data(instrument_token,'day','2021-03-24 10:10:10',to_date_string)
        historical_data=get_historical_data(instrument_token,time_frame,from_date_string,to_date_string)
        print('type historical_data',type(historical_data))
        # print('first_previous_date ',first_previous_date)
        # first_previous_historical_data=get_historical_data(instrument_token,time_frame,first_previous_date,to_date_string)

        # for i in historical_data:
        #     print("---------------")
        #     print("historical_data :i ",i)

        # print('historical_data :',historical_data)

        new_period = int(period)+1
        print("new_period ::: ",new_period)
        new_historical_data = historical_data[-new_period:]
        print("------===")
        for i in new_historical_data:
            print(i)
        # for i in historical_data:
        #     print("historical_data :",i)
    except:
        print("Error")
        print("Except : ",sys.exc_info())
        
    totalRecords=len(new_historical_data)
    print('totalRecords :',totalRecords)
    print("no if no else")
    #periodLimit=int(period)
    if totalRecords > int(period):
        startIndex=totalRecords-int(period)
        print('startIndex :=',startIndex)
    else:
        startIndex=0
    actualCounts=0
    
    #######
   
    previous_close=new_historical_data[0]["close"]
    # previous_close=new_historical_data[0]["close"]

    print("previous_close :====== ",previous_close)

    total_upward_price_change=0.00
    total_downward_price_change=0.00
    total_upward_count=0
    total_downward_count=0
    print("before for loop")
    for data in new_historical_data:
        print("historical_data :=",data)
        # print("threshold :=",threshold)
        # print("startIndex :=",startIndex)
        if threshold > startIndex:
            actualCounts=actualCounts+1
            current_close=data["close"]
            print('previous_close :=',previous_close)
            print("current_close :",current_close)
            if current_close>=previous_close:
                print('total_upward_count :=',total_upward_count)
                total_upward_count=total_upward_count+1
                print('total_upward_count :=',total_upward_count)
                total_upward_price_change +=current_close-previous_close
                print('total_upward_price_change',total_upward_price_change)
                previous_close=current_close
                print("if previous_close ::",previous_close)
            else:
                print('total_downward_count :=',total_downward_count)
                total_downward_count=total_downward_count+1
                print('total_downward_count :=',total_downward_count)
                print('current_close :=',current_close)
                print('previous_close :=',previous_close)
                total_downward_price_change += previous_close - current_close
                print('total_downward_price_change :=',total_downward_price_change)
                previous_close=current_close
                print("else previous_close ::",previous_close)
        threshold=threshold+1


    print("total_upward_count ",total_upward_count)
    print("total_downward_count ",total_downward_count)
    total_period = total_upward_count+total_downward_count
    print("total_upward_price_change ",total_upward_price_change)
    print("total_downward_price_change ",total_downward_price_change)
    print('total_period == ',total_period)
    average_upward_price_change=total_upward_price_change/total_period # total no of period
    # average_upward_price_change=total_upward_price_change/total_upward_count # total no of period
    print('average_upward_price_change ',average_upward_price_change)
    average_downward_price_change=total_downward_price_change/total_period
    print('average_downward_price_change ',average_downward_price_change)
    # average_downward_price_change = 30.5045
    # average_upward_price_change  = 19.3818
    rsi = Decimal( 100-(100 / ( 1 + (average_upward_price_change / average_downward_price_change ) ) ))
        
    print("before condition")
    print('trigger["trigger_id"] ',trigger["trigger_id"])
    print("check trigger :",trigger)
    print('trigger["trigger_criteria"]["operator"] ',trigger["trigger_criteria"]["operator"])
    print('trigger["trigger_criteria"]["amount"] ',trigger["trigger_criteria"]["amount"])
    print("rsi :=",rsi)


    if trigger["trigger_criteria"]["operator"]=="5" and rsi== Decimal(trigger["trigger_criteria"]["amount"]):
        # cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
        criteria_rsi_status_update(triggerId,trigger_condition_id,group_id)

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="3" and rsi> Decimal(trigger["trigger_criteria"]["amount"]):
        # cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
        criteria_rsi_status_update(triggerId,trigger_condition_id,group_id)

        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="1" and rsi>= Decimal(trigger["trigger_criteria"]["amount"]):
        # cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
        criteria_rsi_status_update(triggerId,trigger_condition_id,group_id)
        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="4" and rsi< Decimal(trigger["trigger_criteria"]["amount"]):
        # cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
        criteria_rsi_status_update(triggerId,trigger_condition_id,group_id)
        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="2" and rsi <= Decimal(trigger["trigger_criteria"]["amount"]):
        # cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
        criteria_rsi_status_update(triggerId,trigger_condition_id,group_id)
        # execute_order(trigger)
    elif trigger["trigger_criteria"]["operator"]=="6" and ( rsi> Decimal(trigger["trigger_criteria"]["from_amount"]) and rsi< Decimal(trigger["trigger_criteria"]["to_amount"])):
        # cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
        criteria_rsi_status_update(triggerId,trigger_condition_id,group_id)        
    connection.commit() 
    print("after committ")
        # execute_order(trigger)
    
#criteris RSI end
def criteria_rsi_status_update(triggerId,trigger_condition_id,group_id=0):
    print("criteria_volume_status_update",group_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if group_id == 0:
        print("group_id==0",group_id)    
        cursor.execute("UPDATE trigger_condition_status SET criteria_rsi = True WHERE trigger_id=\'"+triggerId+"\'") 
    else:
        print("group_id!=0",group_id)
        print("trigger_condition_id ::::",trigger_condition_id)
        trigger_condition_id = str(trigger_condition_id)
        try:
            cursor.execute("UPDATE group_trigger_condition_status SET criteria_rsi = True WHERE trigger_condition_id=\'"+trigger_condition_id+"\'") 
        except:
            print("errorr",sys.exc_info())
    connection.commit()




def execute_order(order_condition,orderid,trigger,company_name=None):
    print("this is execute_order function :")
    print("trigger ::[ ",trigger)
    try:
        print('orderid :',orderid)
    
        print("----------------")
        # print(order_condition)
        print("company_name::==",company_name)

        
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
        # print('order_condition :',order_condition)
        # file1 = open("accesstoken.txt","r")
        # access_token=file1.read()
        # file1.close() 

        kite = KiteConnect(api_key=api_key)
        # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
        kite.set_access_token(access_token)
        print("-------------------------------------------")
        trigger_id = []
        for order in order_condition:
            trigger_id.append(order['trigger_id'])
        # print('trigger_id :',trigger_id)
        trigger_id = trigger_id[0]

        orders = []
        for row in order_condition:
            # print('row ::',row)
            # print('trigger_id :',trigger_id)
            # for y in row:
            #     print("inside ssecond for ",y)
            # if row['trigger_id'] == trigger_id:
            orders.append(dict(row))
        # print('orders :::=',orders)
        # print("------------------",order_condition['trigger_criteria'])
        # print(order_condition['symbol1_exchange'])
        print("company_name ",company_name)
        if company_name is not None:
            company_name = company_name[0]
        # else:
        #     company_name = trigger['symbol']
        #     print("else:company_name ",company_name)
        # try:
        #     cursor.execute("SELECT trigger_id from triggers WHERE symbol=\'"+company_name+"\'") # empty company name
        #     trigger_id = cursor.fetchone()
        #     print('trigger_id ":',trigger_id)
        #     print("trigger",trigger)
        # except:
        #     pass
        for order in orders:
            print("inside order")
            print('trigger_id[0] ',trigger_id)

            print("order['trigger_id']",order['trigger_id'])
            print('trigger_id[0] ',trigger_id)
            if order['trigger_id'] == trigger['trigger_id']:
                print("trigger_id[0]",trigger_id)
                limit_price=None
                trigger_price=None
                # print('order :::::::::::::::::',order)
                if order["order_type"]=="LIMIT" or order["order_type"]=="SL":
                    limit_price=order["price"]
                if order["order_type"]=="LIMIT" or order["order_type"]=="SL":
                    trigger_price=order["trigger_price"]
                
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
                print("before execute ::")
                print("company_name ",company_name)
                # company_name = company_name[0]
                print("full company_name",company_name)

                error =''
                quantity=0
                if company_name == None:
                    print("this is if condition")
                    company_name=order["order_symbol"]
                    quantity=order["quantity"]
                else:
                    print("else ::")
                    amount=order["amount"]
                    print("amount",amount)

                    exchange = str(order["order_exchange"])
                    company_name = str(company_name)
                    print('company_name',company_name)
                    quote_info=kite.quote(exchange+':'+company_name)
                    # print("quote_info ::",quote_info[exchange+':'+company_name]['last_price'])
                    print("type :",type(quote_info[exchange+':'+company_name]['last_price']))
                    quantity = amount//int(quote_info[exchange+':'+company_name]['last_price'])
                print("quantity ",quantity)
                    # print("quote_info :",quote_info['NSE:INFY']['last_price'])

                    # quote_info=kite.quote("NSE:INFY")
                    # print("quote_info :",quote_info['NSE:INFY']['last_price'])

                try :
                    if quantity > 0:
                        order_id = kite.place_order(
                        variety=kite.VARIETY_REGULAR,
                        exchange=order["order_exchange"],
                        # tradingsymbol= order["symbol1_exchange"],#order_symbol
                        tradingsymbol= company_name,#order_symbol
                        transaction_type=order["buy_sell"],
                        quantity=quantity,
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
                            print("inside tryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                            orderid = str(orderid)
                            print('orderid :',orderid)
                            
                            # false = False
                            status = "Active"
                            print("company_name ===",company_name)
                            
                            # new code 
                            cursor.execute("SELECT COUNT(*) FROM orders where order_id="+orderid)
                            count = cursor.fetchone()
                            print("count :=",count)
                            # if group_or_not[0] == False:    # Company name is None so it will go else and giving error
                            # # if company_name == None:    # Company name is None so it will go else and giving error
                            #     print("company name ==========",company_name)
                            #     cursor.execute("INSERT INTO order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,'success',"+userid+",\'"+status+"\')")
                            # elif company_name != None:
                            #     print("company_name IS None")
                            #     cursor.execute("INSERT INTO group_order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,'success',"+userid+",\'"+status+"\')")
                            #     cursor.execute("UPDATE group_trigger_status SET status = True WHERE trigger_id="+str(trigger['trigger_id']))

                        # Old Code
                            print("company name ==========",company_name)
                            print("count[0] :",count[0])
                            
                            # if len(count) > 0 :    # Company name is None so it will go else and giving error
                            if company_name != "":
                                cursor.execute("INSERT INTO order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,'success',"+userid+",\'"+status+"\')")
                            else:
                                print("company_name IS not None")
                                cursor.execute("INSERT INTO group_order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,'success',"+userid+",\'"+status+"\')")
                                cursor.execute("UPDATE group_trigger_status SET status = True WHERE trigger_id="+str(trigger['trigger_id']))
                            connection.commit()
                            print("after commit :::====")
                            print("trigger_id': ==============",order['trigger_id'])
                            print("orderid :=",orderid)
                            cursor.execute("UPDATE orders set is_executed=True WHERE order_id="+orderid)
                            connection.commit()
                            
                            schedule.CancelJob
                        except:
                            print("except blockkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                            print("except",sys.exc_info())
                            schedule.CancelJob
                    else:
                        print("elseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                        error_VALUE = "Quantity must be greater than zero."
                        status = "Active"
                        if company_name != None:
                            cursor.execute("INSERT INTO order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,\'"+error_VALUE+"\',"+userid+",\'"+status+"\')")
                        else:
                            cursor.execute("INSERT INTO group_order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,\'"+error_VALUE+"\',"+userid+",\'"+status+"\')")
                        connection.commit()
                        schedule.CancelJob
                        # return Response({"status":"Error", "message": "Quantity is 0"})
                except:
                    print("except block")
                    print("orderid :===",orderid)
                    types, value, traceback = sys.exc_info()
                    print('Error opening %s:' % (value))
                    error = str(value)
                    error_VALUE = error[:50]
                    print('error sliced :',error_VALUE)
                    schedule.CancelJob
                    print("before break")
                    break
                    try:
                        orderid = str(orderid)
                        print('orderid :',orderid)
                        status = "Active"
                        # false = False

                        if company_name == None:
                            cursor.execute("INSERT INTO order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,\'"+error_VALUE+"\',"+userid+",\'"+status+"\')")
                        else:
                            cursor.execute("INSERT INTO group_order_response(order_id,order_status,status_desc,user_id,active_order)VALUES("+orderid+",True,\'"+error_VALUE+"\',"+userid+",\'"+status+"\')")
                        connection.commit()
                        print("after commit")
                        # schedule.CancelJob
                    except:
                        print("except",sys.exc_info())
                # return Response({"status":"error", "message": "error", "content":error})
    except:
        print("last except")
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
    # print('time_frame :',time_frame)
    # print('from_date_string :',from_date_string)
    # print('to_date_string :',to_date_string)
    # print('instrument_token :',instrument_token)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    # print('user_id :',user_id)
    userid = user_id[0]
    # print("userid ::=",userid) 
    userid = str(userid)

    cursor.execute("SELECT token_id,api_key FROM auth_user WHERE id=\'"+userid+"\'")
    current_token_key = cursor.fetchone()
    # print('current_token_key :',current_token_key)
    access_token = current_token_key[0]
    # print("token_id :",access_token)
    api_key = current_token_key[1]

    # file1 = open("accesstoken.txt","r")
    # access_token=file1.read()
    # file1.close() 
    kite = KiteConnect(api_key=api_key)
    # print('kite :',kite)
    # kite = KiteConnect(api_key="ib196gkbrmuqnoer")
    kite.set_access_token(access_token)
    #quote_info=kite.quote("NSE:INFY")
    # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')
    # historical_data=kite.historical_data('408065','2020-04-18 10:10:10','2020-04-22 12:50:00','day')

    try:
        # time_framee = 'minute'
        # print("from_date_string :",from_date_string)
        historical_data= kite.historical_data(instrument_token, from_date_string ,to_date_string,time_frame)
        # print('historical_data :',historical_data)
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
@api_view(['POST','GET'])
def update(request,id):
    if request.method=='POST':
        print("this is update function")
        # order_id = 1215
        order_id = str(id)
        print("order_id :",order_id)
        # order_iddd=request.data["order"]["order_id"]
        # print("order_iddd :==",order_iddd)
        buy_sell=request.data["order"]["buy_sell"]
        buy_sell = str(buy_sell)
        print('buy_sell :',buy_sell)
        quantity=request.data["order"]["quantity"] 
        print('quantity :',quantity)
        product_type=request.data["order"]["product_type"]
        print('product_type :',product_type)
        order_type=request.data["order"]["order_types"]
        # print('order_types :',order_types)
        symbol=request.data["order"]["symbol"]
        # print('order_symbol :',order_symbol)
        exchange_id=request.data["order"]["exchange_id"]
        price=request.data["order"]["price"]
        print(price)
        trigger_price=request.data["order"]["trigger_price"]
        print("trigger_price",trigger_price)
        # price = "10"
        
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        print("order_id :====",order_id)        
        cursor.execute("UPDATE orders SET buy_sell="+buy_sell+", quantity=\'"+quantity+"\',product_type="+product_type+",order_type="+order_type+",symbol=\'"+symbol+"\',exchange_id=\'"+exchange_id+"\',price=\'"+price+"\' WHERE order_id="+order_id)
        # # cursor.execute("UPDATE orders SET buy_sell="+buy_sell+", quantity ="+quantity+",product_type =\'"+product_type +"\',symbol =\'"+order_symbol+"\',order_type=\'"+order_types+"\',exchange_id="+order_exchange_id+" WHERE trigger_id="+trigger_id)
        connection.commit()
        print("success")
        print("post end :")
        return HttpResponseRedirect(reverse('home'))

    else:
        print("get :")
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        order_id = str(id)
        print("order_id :",order_id)
        cursor.execute("SELECT b.buy_sell,eo.exchange,o.symbol,o.quantity,p.product_type,mo.order_type,o.order_id FROM orders o JOIN public.master_exchange eo ON eo.exchange_id=o.exchange_id JOIN public.master_buy_sell b ON o.buy_sell=b.buy_sell_id JOIN public.master_product_type p ON p.product_type_id=o.product_type JOIN public.master_order_type mo ON mo.order_type_id=o.order_type WHERE order_id="+order_id)
        order = cursor.fetchone()
        print('order :',order)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()        
        cursor.execute("SELECT username FROM current_login_user")
        current_user = cursor.fetchone()
        current_user = current_user[0]
        print('current_user :',current_user)
        current_user = str(current_user)   
        print("get end :")
        return render(request, 'update-order.html',{'order':order,'current_user':current_user})

# @login_required(login_url='login_view')
@api_view(['GET','POST'])
def delete_order(request):
    print("delete_order function -----------------------")
    order_id=request.data["data"]["id"]

    print("order_i0d ::",order_id)
    # user_id = request.user.id
    order_trigger_id = str(order_id)
    print("order_trigger_id :==",order_trigger_id)

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 

    cursor.execute("DELETE from trigger_condition_status WHERE trigger_id ="+ order_trigger_id)
    connection.commit()

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("DELETE from order_response WHERE order_id ="+ order_trigger_id)
    connection.commit()

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("DELETE FROM orders WHERE order_id="+ order_trigger_id)
    connection.commit()
    print("successfully deleted")

    # return HttpResponseRedirect(reverse('home'))
    return Response({"status":"success", "message": "success"})


@login_required(login_url='login_view')
def trigger_listing(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 

    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print('user_id :',user_id)
    userid = user_id[0]
    print("userid :",userid) 
    userid = str(userid)
    # cursor.execute("SELECT * from triggers WHERE user_id="+userid)
    # cursor.execute("SELECT t.trigger_id, t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,e.exchange FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id JOIN public.master_exchange e ON t.exchange_id=e.exchange_id Where t.user_id ="+userid)

    data = cursor.fetchall()
    print("data :",data)
    return HttpResponse(data)


@login_required(login_url='login_view')
def delete_trigger(request,id):
    print("delete_order function -----------------------")

    trigger_id = str(id)
    # print(order_trigger_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("DELETE FROM triggers WHERE trigger_id="+ trigger_id)
    connection.commit()
    print("success")
    return HttpResponse("delete success")


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

@login_required(login_url='login_view')
def open_oreder_excel(request):
    print("open_oreder_excel")
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



def download_csv():
    print("download_csv")
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

def testing():
    print("testing function")

import schedule
import time
schedule.every(3).hours.do(testing)
def call_backup(request):
    
    schedule.every().wednesday.at("12:50").do(testing)
    # schedule.every().friday.at(jobqueue2.put,group_apply_filters())
    # schedule.every().friday.at("23:41").do(jobqueue2.put,open_oreder_excel(request))
    while True:
        schedule.run_pending()
        time.sleep(1)

# schedule.every().monday.at("23:59").do(open_oreder_excel)
# name = "working"
# schedule.every().friday.at("23:55").do(download_csv)



@login_required(login_url='login_view')
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
@login_required(login_url='login_view')
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

        print("success")
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

@login_required(login_url='login_view')
@api_view(['POST','GET'])
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

@login_required(login_url='login_view')
@api_view(['POST','GET'])
def save_multiple_trigger(request):   
    if request.method == "POST":
        try:            
            print("this is trigger funxction")
            print("___________________________________")
            # user_id = request.session.get('user_id')
            # print("session user_id:========================",user_id)
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

            cursor.execute("SELECT user_id FROM current_login_user")
            user = cursor.fetchone()
            # print("user ::=",user)
            # print("user ::=",user[0])
            user_id = user[0]

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
            cursor.execute("INSERT INTO triggers(trigger_name, symbol, trigger_condition_id,trigger_criteria, exchange_id,user_id,is_group_trigger)VALUES (\'"+trigger_name+"\',\'"+symbol+"\',"+trigger_condition_id+",\'"+trigger_criteria+"\',"+exchange_id+","+user_id+",False)  RETURNING trigger_id") 
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
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()        
        cursor.execute("SELECT username FROM current_login_user")
        current_user = cursor.fetchone()
        current_user = current_user[0]
        print('current_user :',current_user)
        current_user = str(current_user)   
        return render(request,'add-multiple-trigger.html',{'current_user':current_user})



# function to save multiple orders
@login_required(login_url='login_view')
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
            cursor.execute("INSERT INTO orders(buy_sell,symbol,exchange_id,quantity,product_type,order_type,trigger_id,user_id,group_or_not)VALUES ("+i['buy_sell']+",\'"+i['symbol']+"\',"+i['exchange_id']+","+i['quantity']+","+i['product_type']+","+i['order_types']+","+triggerId+","+userid+", False)") 
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
        # new
        # cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id where t.user_id ="+user_id+" and is_group_trigger = False and o.is_executed= False") 
        # Old
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id+" and is_group_trigger = False") 

        data = cursor.fetchall()
        print("data :",data)
        triggers = []
        for row in data:
            triggers.append(row[0])
        print('triggers :',triggers)
        print(triggers)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()        
        cursor.execute("SELECT username FROM current_login_user")
        current_user = cursor.fetchone()
        current_user = current_user[0]
        print('current_user :',current_user)
        current_user = str(current_user)   
        # return render(request,'add-multiple-order.html',{'triggers':triggers})
        return render(request,'new-add-multiple-order.html',{'triggers':triggers,'current_user':current_user})


def get_mul(request):
    if request.method == 'POST': 
        username = request.POST.getlist("name")
        print(username)
        symbol = request.POST.getlist("symbol")
        print(symbol)

        # user_password = request.POST.get("name")
        # print()
    return render(request, 'multi.html')

from django.http import JsonResponse

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def create_group(request):
    if request.method == "POST":
        print("create group")

        group_instrument_token=request.data["group"]["group_instrument_token"] 
        print("group_instrument_token",group_instrument_token)
        print("group_instrument_token type",type(group_instrument_token))
        group_instrument_token = ','.join(group_instrument_token)
        print("group_instrument_token================",group_instrument_token)


        group_symbol=request.data["group"]["group_symbol"] 
        print("group_symbol ",group_symbol)
        print("group_symbol type",type(group_symbol))
        group_symbol = ','.join(group_symbol)


        group_name=request.data["group"]["group_name"] 
        print("group_name",group_name)
        print("group_name type",group_name)

        group_exchange=request.data["group"]["group_exchange"] 
        group_exchange = str(group_exchange)
        print("group_exchange ",group_exchange)
        print("group_exchange type",group_exchange)

        # order=request.data["order"]["form_data"] 
        # print("order ",order)
        # json_string = json.loads(order)
        # print("json_string ",json_string)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        # cursor.execute("SELECT group_name from master_company_group")    
        # group_name = cursor.fetchall()
        # group_list = []
        # for row in group_name:
        #     group_list.append(row[0])

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        userid = 0
        for i in user_id:
            userid +=i
        userid = str(userid)


        cursor.execute("INSERT INTO master_company_group(group_name,company_list,exchange,user_id,instrument) VALUES(\'"+group_name+"\',\'"+group_symbol+"\',\'"+group_exchange+"\','"+userid+"',\'"+group_instrument_token+"\')")
        print("inserted successfull")
        connection.commit()
        return Response({"status":"success", "message": "success"})        

        # if group not in group_list:
        #     print("create")
        #     # group_id =1
        #     # # group_id = str(group_id)
        #     print('json_string ',json_string)
        #     symbol = []
        #     for item in json_string:
        #         company = item['group_symbol']
        #         print("company ",company)
        #         symbol.append(company)
        #         # # group_id = str(group_id)
        #         group_exchange = str(group_exchange)
        #     print("symbol :",symbol)
        #     s = ","
        #     company_list = s.join(symbol) 
        #     print("added :::::",company_list)

        #     instrumen_tokens = []
        #     for i in json_string:
        #         instrumen = i['instrument_token']
        #         print('instrumen ',instrumen)
        #         instrumen_tokens.append(instrumen)
        #     print("instrumen_tokens :",instrumen_tokens)
        #     # s = ","
        #     instrumen_tokens = s.join(instrumen_tokens) 
        #     print("instrum
        #     cursor.execute("INSERT INTO master_company_group(group_name,company_list,exchange,user_id,instrument) VALUES(\'"+group+"\',\'"+company_list+"\',\'"+group_exchange+"\','"+userid+"',\'"+str(instrumen_tokens)+"\')")
        #     # cursor.execute("INSERT INTO master_company_group(id,group_name,company_list,exchange) VALUES("+id+",\'"+group_name+"\',\'"+company+"\',\'"+exchange+"\')")
        #     print("inserted successfull")
        #     connection.commit()
        #     # group_id = int(group_id)
        #     # group_id += 1
        #     # messages.success(request, 'Group created successfully')
        #     # return TemplateResponse(request, "create_group.html")
        #     # return JsonResponse({"status":"success", "message": "success"})
            # return Response({"status":"success", "message": "success"})en_tokens :::::",instrumen_tokens)
            

        return Response({"status":"success", "message": "success"})
        # else:
        #     print("===========================================")
        #     cursor.execute("select group_name from master_company_group where group_name= \'"+group+"\'")
        #     groups = cursor.fetchall()
        #     groups = groups[0]
        #     group_db = groups[0]
        #     print('groups :',group_db)
        #     if group_db == group:
        #         print("same")
        #         return Response({"status":"failure", "message": "failure"})
    else:
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()        
        cursor.execute("SELECT username FROM current_login_user")
        current_user = cursor.fetchone()
        current_user = current_user[0]
        print('current_user :',current_user)
        current_user = str(current_user)   
        return render(request,'add-group.html',{'current_user':current_user})

    # return Response({"status":"success", "message": "success"})
    # return render(request,'add-group.html')

@login_required(login_url='login_view')
def group_listing(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT group_name,company_list,me.exchange FROM master_company_group INNER JOIN master_exchange as me ON master_company_group.exchange = me.exchange_id")
    groups = cursor.fetchall()
    connection.commit()
    cursor.execute("SELECT username FROM current_login_user")
    current_user = cursor.fetchone()
    current_user = current_user[0]
    print('current_user :',current_user)
    current_user = str(current_user)   
    
    return render(request,'group_listing.html',{'groups_list':groups,'current_user':current_user})

from django.contrib import messages

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def delete_group(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    try :
        g_name=request.data["data"]["id"] 
        print("g_name :=",g_name)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM master_company_group WHERE group_name=\'"+g_name+"\'")
        connection.commit()
        print("deleted")
        # return HttpResponseRedirect(reverse('group_listing'))
        return Response({"status":"success", "message": "success"})
    except:
        # messages.error(request, 'Some trigger is assigned to this Group.')
        # messages.add_message(request, messages.SUCCESS, 'Failed... trigger is assigne to this group.')
        # return HttpResponseRedirect(reverse('group_listing'))
        return Response({"status":"failure", "message": "Error"})


@api_view(['GET','POST'])
def company_add_update(request,group_name):

    if request.method == "GET":
        print("company_add_update functoin")
        print("=============--------------------------==========================================")
    # company = request.POST.get("company")
        # trigger_name=request.data["trigger"]["trigger_name"]
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

@login_required(login_url='login_view')
def group_order(request):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()        
    cursor.execute("SELECT username FROM current_login_user")
    current_user = cursor.fetchone()
    current_user = current_user[0]
    print('current_user :',current_user)
    current_user = str(current_user)   
    return render(request,'update-group.html',{'current_user':current_user})

@login_required(login_url='login_view')
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
        print("symbols ::",symbols)
        group_name = company_list[1]
        # symbol = {'group_name':group_name}

        exchange = company_list[2]
        symbols = symbols.split(',')
        print('symbols ::::',symbols)
        print('symbols ::::',type(symbols))
        # data = {'group_name':group_name,'exchange':exchange ,'symbol':symbols}
        return render(request,'update-group.html',{'group_name':group_name,'exchange':exchange ,'symbol':symbols})
    else:
        print("company_add_update functoinn")
        print("=========================================")
    # company = request.POST.get("company")
        company_name =request.data["order"]["form_data"] 
        company_name = json.loads(company_name)
        print("company_name :=",company_name) 
        print("company_name :::type ::",type(company_name))  

        for i in company_name:
            print("i :=",i['group_symbol'])

        symbol_list = []
        instrument_list = []
        for i in company_name:
            instrument_list.append(i['instrument_token'])
            symbol_list.append(i['group_symbol'])
            print(symbol_list)
            print(instrument_list)


        # company = "VM ware"
        # # group_name ='Group2'
        # # print("group_name ",group_name)

        # group_name =request.data["group"]["group_name"] 
        # print('group_name :--',group_name)
        # # group_exchange=request.data["group"]["group_exchange"]
        # # print('group_exchange :',group_exchange)
        # form_data=request.data["order"]["form_data"] 
        
        # uncommint  

        # connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        # cursor = connection.cursor()
        # cursor.execute("UPDATE master_company_group SET company_list=\'"+symbol_list+"\' WHERE group_name=\'"+group_name+"\'")
        # cursor.execute("UPDATE master_company_group SET instrument=\'"+instrument_list+"\' WHERE group_name=\'"+group_name+"\'")
        # connection.commit()

        # till here

        
        # # cursor.execute("SELECT company_list FROM master_company_group WHERE group_name=\'"+group_name+"\'")
        # # company_list = cursor.fetchone()
        # # print("company_list :",company_list)
        # # print("update")
        # # company_list = company_list[0]
        # # if company_list == None:
        # #     cursor.execute("UPDATE master_company_group SET company_list=\'"+company+"\' WHERE group_name=\'"+group_name+"\'")
        # #     connection.commit()
        # # else:
        # #     company_list = company_list + "," + company
        # #     print("company_list :::",company_list)
        # #     cursor.execute("UPDATE master_company_group SET company_list=\'"+company_list+"\' WHERE group_name=\'"+group_name+"\'")
        # #     connection.commit()
        # #     print("inserted successfull")
        return Response({"status":"success", "message": "success"})  

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def insert_group_order(request):
    print("inside insert_group_order function ")
    if request.method=="POST":
        print("inside insert_group_order post")
        # trigger_name =request.data["trigger"]["trigger_name"] 
        # print('trigger_name :------------------------------',trigger_name)
        group_name =request.data["trigger"]["group_name"] 
        print('group_name :------------------------------',group_name)

        buy_sell=request.data["order"]["buy_sell"]
        print('buy_sell :',type(buy_sell))
        print('buy_sell :',buy_sell)
        amount=request.data["order"]["order_amount"] 
        print('amount : ',amount)
        product_type=request.data["order"]["product_type"]
        print('product_type : ',product_type)
        order_type=request.data["order"]["order_types"]
        print('order_type :',order_type)
        # order_exchange_id=request.data["order"]["exchange_id"]
        # print('order_exchange_id :',order_exchange_id)
        order_price=request.data["order"]["price"]
        print('order_price :',order_price)
        trigger_price=request.data["order"]["trigger_price"]
        print('trigger_price :',trigger_price)
        print("-------------------------======================================-----------")
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
        # group_name = 'group'
        cursor.execute("SELECT exchange FROM master_company_group Where group_name=\'"+group_name+"\'")
        exchange = cursor.fetchone()
        exchange = str(exchange[0])
        print("exchange ",exchange)
        


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
        group_name = str(group_name)
        cursor.execute("SELECT distinct(trigger_condition_list.trigger_id) FROM trigger_condition_list join triggers ON trigger_condition_list.trigger_list like '%' || triggers.trigger_id || '%' and triggers.trigger_name=\'"+group_name+"\'")
        trigger_ids = cursor.fetchone()
        trigger_id = 0
        for i in trigger_ids:
            trigger_id +=i
        trigger_id = str(trigger_id)
        cursor.execute("INSERT INTO group_order(group_id,buy_sell,exchange_id,amount,product_type,order_type,trigger_id,trigger_price,user_id)VALUES ("+group_id+","+buy_sell+","+exchange+","+amount+","+product_type+","+order_type+","+trigger_id+","+trigger_price+","+userid+")") 

        cursor.execute("SELECT trigger_id FROM triggers WHERE trigger_name = \'"+group_name+"\' AND user_id = "+userid+"")
        trigger_order_id = cursor.fetchone()
        print('trigger_order_id :',trigger_order_id)
        trigger_order_id = trigger_order_id[0]
        print("trigger_order_id :",trigger_order_id) 
        trigger_order_id = str(trigger_order_id)
        print('trigger_order_id kkkkk:',trigger_order_id)

        cursor.execute("UPDATE current_login_user SET order_trigger_id = "+trigger_order_id+" WHERE user_id="+userid+"")

        connection.commit()
        print("success")
        # return render(request,'insert-group-order.html')
        return Response({"status":"success", "message": "success"})  
        # return HttpResponse("working")
    else:
        print("------------------------------------------------------------------------")
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        print('user_id :',user_id)
        user_id = str(user_id)    
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id+" and is_group_trigger") 
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
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()        
        cursor.execute("SELECT username FROM current_login_user")
        current_user = cursor.fetchone()
        current_user = current_user[0]
        print('current_user :',current_user)
        current_user = str(current_user)   
        return render(request,'place-group.html',{'triggers':triggers,"group_names":group_names,'current_user':current_user})

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def update_group_order(request,order_id):
    print("inside update_group_order function ")
    if request.method=="POST":
        print("inside update_group_order post")
        buy_sell=request.data["order"]["buy_sell"]
        print('buy_sell :',type(buy_sell))
        print('buy_sell :',buy_sell)
        amount=request.data["order"]["amount"] 
        print('amount : ',amount)
        product_type=request.data["order"]["product_type"]
        print('product_type : ',product_type)
        order_type=request.data["order"]["order_types"]
        print('order_type :',order_type)
        order_exchange_id=request.data["order"]["exchange_id"]
        print('order_exchange_id :',order_exchange_id)
        order_price=request.data["order"]["price"]
        print('order_price :',order_price)
        trigger_price=request.data["order"]["trigger_price"]
        print('trigger_price :',trigger_price)
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
        order_id = str(order_id)
        print("order_id ",order_id)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        order_id = str(order_id)
        # cursor.execute("SELECT * FROM group_order WHERE order_id="+order_id+"")
        # group_order = cursor.fetchone()
        # print('group_order :',group_order)
        
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        print('user_id :',user_id)
        user_id = str(user_id)    
        cursor.execute("SELECT group_order.order_id,group_order.trigger_id,mcg.group_name,bs.buy_sell,mex.exchange,amount,mpt.product_type,opt.order_type,executed_on,price,group_order.trigger_price FROM group_order INNER JOIN master_company_group as mcg ON group_order.group_id = mcg.id INNER JOIN master_product_type as mpt ON group_order.product_type = mpt.product_type_id INNER JOIN master_order_type as opt ON group_order.order_type = opt.order_type_id INNER JOIN master_buy_sell as bs ON group_order.buy_sell = bs.buy_sell_id INNER JOIN master_exchange as mex ON group_order.exchange_id = mex.exchange_id JOIN public.trigger_condition_list tcl ON tcl.trigger_id= group_order.trigger_id JOIN public.triggers tr ON tcl.trigger_list like '%' || tr.trigger_id || '%' WHERE group_order.order_id ="+order_id) 
        group_order = cursor.fetchone()
        print("group_order :",group_order)
        return render(request,'update-group-order.html',{'group_order':group_order})


@login_required(login_url='login_view')
@api_view(['GET','POST'])
def insert_group_trigger(request):
    print("inside insert_group_trigger function ")
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    # if request.method=="GET": #change to POST
    if request.method=="POST": #change to POST
        print("inside insert_group_trigger post")
        print("--------------------------------------------------------------------------------------")
        group_name =request.data["group"]["group_name"] 
        print('group_name',group_name)
        trigger_condition_id=request.data["group"]["trigger_condition_id"]
        trigger_condition_id = str(trigger_condition_id)
        print('trigger_condition_id',trigger_condition_id) 
        trigger_criteria=  json.dumps(request.data["group"]["trigger_criteria"])
        # trigger_criteria.trigger_data = 123

        print('trigger_criteria ::',type(trigger_criteria))

        cursor.execute("select instrument,group_name from master_company_group where group_name=\'"+group_name+"\'") 
        group_record = cursor.fetchall()
        instrument = group_record[0]
        cursor.execute("select exchange,company_list from master_company_group where group_name=\'"+group_name+"\'") 
        group_record = cursor.fetchall()
        group_data = group_record
        exchange_id = str(group_data[0][0])
        company_list = group_data[0][1]
        company_list = company_list.split(',')

        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        # print('user_id :',user_id)
        user_id = str(user_id)
        trigger_name = group_name
        for record,instrument in zip(company_list, instrument[0].split(',')):
            if record != "":
                trigger_criteria = json.loads(trigger_criteria)
                trigger_criteria['instrument_token']=instrument
                trigger_criteria = json.dumps(trigger_criteria)
                cursor.execute("INSERT INTO triggers(trigger_name, symbol, trigger_condition_id,trigger_criteria, exchange_id,user_id,is_group_trigger)VALUES (\'"+trigger_name+"\',\'"+record+"\',"+trigger_condition_id+",\'"+trigger_criteria+"\',"+exchange_id+","+user_id+",True)") 
                connection.commit()                
            else:
                print("pass")
                pass
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
        connection.commit()
        cursor.execute("Update master_company_group SET trigger_id=\'"+trigger+"\' WHERE group_name =\'"+group_name+"\'")
        connection.commit()
        print("successss")
        return Response({"status":"success", "message": "success"})        

        # return HttpResponse("done")
        # return HttpResponseRedirect(reverse('group_trigger'))

    else:
        print("GET ===============================")
        cursor.execute("SELECT user_id FROM current_login_user")
        user_id = cursor.fetchone()
        user_id = user_id[0]
        user_id = str(user_id)

        # cursor.execute("select group_name from master_company_group where trigger_id is null and user_id="+user_id) 
        cursor.execute("select group_name from master_company_group where user_id="+user_id) 

        group_order = cursor.fetchall()
        group_list = []
        for i in group_order:
            group_list.append(i[0])
        print("group_list ::::",group_list)
        return render(request,'group_trigger.html',{'group_list':group_list})
        # return HttpResponse(group_order)

@login_required(login_url='login_view')
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
@login_required(login_url='login_view')
def groups_order_listing(request):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    user_id = user_id[0]
    user_id = str(user_id) 
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    # add group_name
    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,p.product_type, b.buy_sell,o.amount,o.trigger_id,o.order_id, master_product_type.product_type,o.is_cancelled FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.group_order o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id JOIN public.master_product_type p ON p.product_type_id=o.product_type INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type JOIN public.master_buy_sell b ON o.buy_sell=b.buy_sell_id WHERE t.user_id ="+user_id+" order by t.user_id desc limit 1")
    rows = cursor.fetchall()
    open_group_order = []
    for row in rows:
        open_group_order.append(dict(row))
    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='True' AND t.user_id ="+ user_id)
    rows2 = cursor.fetchall()
    executed_trigger_order = []
    for row in rows2:
        executed_trigger_order.append(dict(row))
        print(executed_trigger_order)    
    # new
    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition, o.buy_sell,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.group_order o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE t.user_id ="+user_id)
    # old
    # cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,t.trigger_criteria,o.symbol, o.buy_sell, o.quantity,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND trigger_name=\'"+trigger_name+"\'") 
    triggers = cursor.fetchall()
    print("triggers ",triggers)     
    cursor.execute("SELECT username FROM current_login_user")
    current_user = cursor.fetchone()
    current_user = current_user[0]
    print('current_user :',current_user)
    current_user = str(current_user)   

    # return render(request, 'groups_order_listing.html',{"content":open_group_order,"executed_trigger_order":executed_trigger_order,"triggers":triggers,"current_user":current_user})        
    return render(request, 'groups_order_listing.html',{"content":open_group_order,"executed_trigger_order":executed_trigger_order,"current_user":current_user})        

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def delete_group_order(request):
    print("*****************************************************************************")
    if request.method == "POST":
        trigger_id =request.data["data"]["id"] 
        print("trigger_id :==",trigger_id)

        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()
        print('type:=',type(trigger_id))
        print('type:=',trigger_id)
        trigger_id = str(trigger_id)
        print("trigger_id :==",trigger_id)
        cursor.execute("SELECT group_name FROM master_company_group WHERE trigger_id="+trigger_id)
        group_name = cursor.fetchone()

        print('group_name ="" ',group_name)
        groupname = group_name[0]
        groupname = str(groupname)
        print('type:=groupname',type(groupname))
        print('type:=groupname',groupname)
        

        # cursor.execute("SELECT exchange FROM master_company_group Where group_name=\'"+group_name+"\'")

        cursor.execute("DELETE FROM triggers WHERE trigger_name = \'"+groupname+"\'")
        connection.commit()
        print("deleted")
        # # return HttpResponseRedirect(reverse('group_listing'))
        return Response({"status":"success", "message": "success"})
    else:
        print("else")
        return Response({"status":"error", "message": "invalid request"})




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
        print("start --------------------------------------------------------------------------------------------------------")
        cursor.execute("SELECT distinct trigger_name FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' where t.user_id ="+user_id) 
        trigger_names_list = cursor.fetchall()
        print('trigger_names_list----------------=---- :',trigger_names_list)
        print("End--------------------------------------------------------------------------------------------------------")
        trigger_names = []
        for i in trigger_names_list:
            trigger_names.append(i[0])
            print("trigger_names ::====",trigger_names)
        
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
        # schedule.every(10).seconds.do(jobqueue.put,group_apply_filters(triggers))
        group_apply_filters(triggers)
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
        print("order_ids ::",order_ids)            
        return Response({"status":"Success", "message": "Success","content":order_ids})        
    except:
        # print("Unexpected error:", sys.exc_info()[0])
        return Response({"status":"failure", "message": "failure"})





# jobqueue = multiprocessing.Queue()
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
        print("trigger_id -=",trigger_id)
        connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
        cursor = connection.cursor()

        cursor.execute("SELECT trigger_id from trigger_condition_list WHERE trigger_list like  '%"+trigger_id+"%'") # error return null
        
        trigger_condition_id = cursor.fetchone()
        print("trigger_condition_list trigger_id ::= ",trigger_condition_id)
        trigger = trigger_condition_id[0]
        print("trigger_condition_id :==== ",trigger)
        # print(type(trigger))
        triggerId = str(trigger)

        cursor.execute("SELECT id from master_company_group WHERE trigger_id ="+triggerId)
        group_id = cursor.fetchone()
        group_id = str(group_id[0])
        print("group_id ",group_id)

        cursor.execute("SELECT order_id from group_order WHERE group_id ="+group_id)
        order_id_data = cursor.fetchone()
        order_id_data = str(order_id_data[0])
        print("order_id_data ",order_id_data)
        print("triggerId ",triggerId)
        # cursor.execute("SELECT trigger_list from trigger_condition_list WHERE trigger_id ="+triggerId)
        # triggers_list = cursor.fetchall()
        # print('triggers_list :',triggers_list)
        
        # order_ids = []
        # for order in order_id_data:
        #     order_ids.append(order[0])
        # print('order_ids :::',order_ids)

        for trigger_condtion_id in trigger_ids:
            # print("inside for :",order_id)
            trigger_condtion_id =str(trigger_condtion_id)
            try:
                # order_id trigger_condition_id 
                cursor.execute("INSERT INTO group_trigger_condition_status VALUES("+order_id_data+","+triggerId+","+trigger_condtion_id+","+group_id+",False,False,False,False,False,False,False,False)")
                connection.commit()
                print('success')
            except:
                print("except ",sys.exc_info())
        
        count = 0
        trigger_combine_status = True
        is_cancelled_request = False
        
        for trigger in triggers:
            print("trigger loop :",trigger)
            count += 1
            # group_cron_apply_filter(trigger,triggerId,cursor,count,group_id,order_id_data,triggers)
            try:
                # print("str(trigger['trigger_id']",str(trigger['trigger_id'])
                cursor.execute("SELECT count(trigger_id) FROM group_trigger_status WHERE trigger_id="+str(trigger['trigger_id']) )
                Count = cursor.fetchone()
                print("Count :",Count)
                print("Count[0]",Count[0])
                if Count[0] != 0:
                    
                    cursor.execute("SELECT status FROM group_trigger_status WHERE trigger_id="+str(trigger['trigger_id']) )
                    status = cursor.fetchone()
                    print("status ",status)
                    if status[0] == True:
                        print("inside true")
                        continue
                    print("trigger[trigger_id]::=",trigger['trigger_id'])

                if Count[0] == 0:

                    group_id = str(group_id)
                    cursor.execute("INSERT INTO group_trigger_status(trigger_id,group_id,status)values("+str(trigger['trigger_id'])+","+group_id+",false)")
                    connection.commit()
                    print("success")
            except:
                print("errorr :",sys.int_info())
            

            cursor.execute("SELECT is_cancelled FROM group_order WHERE order_id="+order_id_data)
            is_cancelled_request = cursor.fetchone()
            is_cancelled_request = is_cancelled_request[0]
            if is_cancelled_request == True:
                break

            schedule.every(10).seconds.do(jobqueue.put,group_cron_apply_filter(trigger,triggerId,cursor,count,group_id,order_id_data,triggers))
        # update trigger status(True/False) every time in new table
        # check for every entry in dict if we get all true then break while loop else continue until all conditions get fullfill.
        if is_cancelled_request == True:
            break
        print("group_id :=",group_id)
        cursor.execute("SELECT status FROM group_trigger_status WHERE group_id="+group_id )
        status = cursor.fetchall()
        print("status :::",status)
        for i in status:
            if i[0] == False:
                trigger_combine_status = False
        if trigger_combine_status == True:
            break


            
def group_cron_apply_filter(trigger,triggerId,cursor,count,group_id,order_id_data,triggers):
        dic = {}
        print("trigger::: ",trigger)
        print("trigger id :::",trigger['trigger_id'])
        print('trigger["trigger_condition_id"] ',trigger["trigger_condition_id"])
        print('count@@@@@@@@@@@@@@@@@',count)
        print(trigger["trigger_id"])
        if trigger["trigger_condition_id"]==1:
            dic[1]='criteria_price'
            criteria_price(trigger,triggerId,cursor,trigger['trigger_id'],group_id)     
        elif trigger["trigger_condition_id"]==2:
            dic[2]='criteria_moving_average'
            criteria_moving_average(trigger,triggerId,cursor,trigger['trigger_id'],group_id)
        elif trigger["trigger_condition_id"]==3:
            print("calling criteria_volume ")
            dic[3]='criteria_volume'
            print("trigger['trigger_id'] :",trigger['trigger_id'])
            criteria_volume(trigger,triggerId,trigger['trigger_id'],group_id)
        elif trigger["trigger_condition_id"]==4:
            dic[4]='criteria_p2p1'
            criteria_p2p1(trigger,triggerId,cursor)
        elif trigger["trigger_condition_id"]==5:
            pass  
        elif trigger["trigger_condition_id"]==6:
            dic[6]='criteria_RSI'
            criteria_RSI(trigger,triggerId,cursor,trigger['trigger_id'],group_id)  
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
        # id_trigger_condition = trigger_condition_id[0]
        # id_trigger_condition = str(id_trigger_condition)
        # print('trigger_condition_id :::::',id_trigger_condition)

    # for order_id in order_ids:
        # print("inside for :",order_id)
        # order_id =str(order_id)
        print("before query")
        print("trigger['trigger_id'] ",trigger['trigger_id'])
        query = "select "
        try:    
            for key in dic:
                query += dic[key]+","
            query = query[:-1]
            query += " from group_trigger_condition_status WHERE trigger_condition_id ="+ str(trigger['trigger_id'])
            print('query :',query)
            cursor.execute(query)
            trigger_condition_status = cursor.fetchone()
            print("trigger_condition_status :::",trigger_condition_status)
        except:
            print("errorr :",sys.exc_info())

# cancle cron job for group
        # print("order_id ========= ",order_id)
        # if order_ids:   # make 
        #     print("===========------------------------------------")
        #     order_id = str(order_ids[0])
        #     cursor.execute("SELECT is_executed FROM group_order WHERE order_id = "+order_id)
        #     executed = cursor.fetchone()
        #     print("executed ",executed[0])
        #     if executed[0] == True:
        #         break



        if trigger_condition_status[0] == True:
            print("yes true")
            trigger_id = trigger['trigger_id']
            print("trigger_id",trigger_id)
            cursor.execute("SELECT symbol from triggers where trigger_id="+str(trigger_id))
            company_name = cursor.fetchone()
            print("company_name",company_name)
            print("calling combine criteria")
            combine_criteria(triggers,order_id_data,trigger,company_name) 
        else:
            print("not true") 
  

            # condition_status = False
            # for i in trigger_condition_status:
            #     if i == True:
            #         condition_status = True
            #     else:
            #         condition_status = False

            #         print("Unexpected error:", sys.exc_info())   
            #         exc_tuple = sys.exc_info()  
            #         # trigger_error = count 
            #         return Response({"status":"failure", "message": exc_tuple})
                            # break
            # if condition_status == True:
            #     combine_criteria(triggers,order_id)






@login_required(login_url='login_view')
def trigger_list(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    print("==================")
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print("-------------=======-------------------------------===")
    userid = user_id[0]
    userid = str(userid)
    # cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,t.trigger_id FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.trigger_condition_list tcl ON trigger_list not like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id WHERE t.is_active=true and t.user_id ="+userid+" and is_group_trigger = false order by t.trigger_id asc ")
    cursor.execute("select created_on,trigger_name,symbol,trigger_criteria,trigger_id from triggers where user_id ="+userid+" and is_group_trigger = False")
    triggers = cursor.fetchall()
    print("trigger_condition_list trigger_id : ",triggers)       
    cursor.execute("SELECT username FROM current_login_user")
    current_user = cursor.fetchone()
    current_user = current_user[0]
    print('current_user :',current_user)
    current_user = str(current_user)   
    return render(request,'trigger_listing.html',{'triggers':triggers,'current_user':current_user})

# ------------------
@login_required(login_url='login_view')
@api_view(['GET','POST'])
def update_triggers(request,trigger_id):
    print("trigger_idtrigger_idtrigger_idtrigger_idtrigger_idtrigger_id",trigger_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if request.method =='POST':
        print("session update_triggers:========================")
        trigger_name=request.data["trigger"]["trigger_name"]
        print('trigger_name',trigger_name)
        symbol=request.data["trigger"]["symbol"]
        print('symbol',symbol)
        trigger_condition_id=request.data["trigger"]["trigger_condition_id"]
        trigger_condition_id = str(trigger_condition_id)
        print('trigger_condition_id',trigger_condition_id)
        trigger_criteria=  json.dumps(request.data["trigger"]["trigger_criteria"])
        print('trigger_criteria ::',trigger_criteria)
        exchange_id=request.data["trigger"]["exchange_id"]
        exchange_id = str(exchange_id)
        print('exchange_id',exchange_id)
        trigger_id = str(trigger_id)
        print('trigger_id === ',trigger_id)
        # trigger_id=request.data["trigger"]["trigger_id"]
        # print('trigger_id',trigger_id)
        # trigger_name = "Dummy"
        # symbol = "Dummy_symbol"
        # trigger_condition_id = "1"
        # trigger_criteria = "3"
        # trigger_criteria = '{"type": "volume_avg", "volume_average_candles": "50", "time_frame": "5minute", "time_frame_type": "minute", "time_frame_duration": "5", "operator": "1", "amount": "5000", "instrument_token": "1076225"}'

        # exchange_id = '3'
        # trigger_id = '1743'
        cursor.execute("UPDATE triggers set trigger_name = \'"+trigger_name+"\', symbol=\'"+symbol+"\',trigger_condition_id=\'"+trigger_condition_id+"\',trigger_criteria=\'"+trigger_criteria+"\',exchange_id=\'"+exchange_id+"\' WHERE trigger_id=\'"+trigger_id+"\'")
        connection.commit()
        print("succeeeeeeeeeeeeeeeeeeeeeees")
        return Response({"status":"success", "message": "success"})
    else:    
        print("GET")
        trigger_id = str(trigger_id)
        print("trigger_id ",trigger_id)
        cursor.execute("SELECT t.trigger_id,t.trigger_name,t.symbol,e.exchange,c.trigger_condition,t.trigger_criteria FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.master_exchange eo ON eo.exchange_id=t.exchange_id WHERE t.trigger_id="+trigger_id+" order by t.trigger_id asc")
        triggers = cursor.fetchall()
        print("triggers",triggers)
        # 
        cursor.execute("SELECT t.trigger_criteria FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.master_exchange eo ON eo.exchange_id=t.exchange_id WHERE t.trigger_id="+trigger_id+" order by t.trigger_id asc")
        trigger_criteria = cursor.fetchall()
        # print("triggers : ",triggers)

        print("trigger_condition_list trigger_id : ",trigger_criteria)
        # trigger_criteria = json.loads(trigger_criteria)

        # print("trigger_criteria ============================",type(trigger_criteria))

        return render(request,'update_trigger.html',{'triggers':triggers,'trigger_criteria':trigger_criteria,"trigger_id":trigger_id})
        # return HttpResponse(triggers)

@api_view(['GET','POST'])
@login_required(login_url='login_view')
def delete_trigger_from_trigger_list(request):
    print("delete_order function -----------------------")
    trigger_id=request.data["data"]["id"]

    trigger_id = str(trigger_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("DELETE FROM triggers WHERE trigger_id="+ trigger_id)
    connection.commit()
    print("success")
    return Response({"status":"success", "message": "success"})
    # return HttpResponseRedirect(reverse('trigger_list'))

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def fetch_trigger(request,trigger_name):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print("-------------=======-------------------------------===")
    userid = user_id[0]
    userid = str(userid)
    # trigger_name = "T51"
    print("trigger_name ==========",trigger_name)
    # cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND t.user_id ="+user_id+" AND trigger_name="+trigger_name)
    
    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell, o.quantity,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND trigger_name=\'"+trigger_name+"\'")

    triggers = cursor.fetchall()
    print("triggers ",triggers)
    return render(request,'popup.html',{'triggers':triggers})

def test(request):
    return render(request,'listing.html')

@login_required(login_url='login_view')#cancel order
def cancel_group_order(request,order_id):
    
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
# new
    cursor.execute("UPDATE group_order SET is_executed=True WHERE order_id="+str(order_id))
# old
    # cursor.execute("UPDATE group_order SET is_cancelled=False WHERE order_id="+str(order_id))
    connection.commit()
    print("cancle")
    print("update again")
    time.sleep(5)
    cursor.execute("UPDATE group_order SET is_executed=False WHERE order_id="+str(order_id))
    #  sleep 10 sec and update same order is_executed= False
    return HttpResponseRedirect(reverse('home'))
    # return render(request,)

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def cancel_order(request,order_id):
    print("order_id :",order_id)
    print("cancle_order function")
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("UPDATE orders SET is_cancelled=True WHERE order_id="+str(order_id))
    connection.commit()

    # print("cancle")
    # print("update again")
    # time.sleep(5)
    # cursor.execute("UPDATE orders SET is_executed=False WHERE order_id="+str(order_id))
    # connection.commit()
    print("cancle")
    # return HttpResponseRedirect(reverse('home'))
    return Response({"status":"success", "message": "success"})




def demo1(request):

    l = [36.9,
    36.85,
    33.3,
    34,
    35.2,
    35.6,
    33.5,
    33.65,
    33.35,
    33.55,
    34,34.1,34.65,36.9,36.85,33.3,34,35.2,35.6,33.5,33.65,33.35,33.55,34,34.1,34.65,35.05,36.85]

    result = [sum(l[i:(i+6)]) for i in range(len(l)-5)][:10]
    # for i in range(0,5):
        
    #     print(result[i]/5)
    print(result)

    return HttpResponse(result)

# Remove this code
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    print("response ",response)
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    print("tutorial ",tutorial)
    return HttpResponse("java tutorials @: "+  tutorial)

import json
def test12(request):
    return render(request,"sidebar.html")

@login_required(login_url='login_view')
def group_trigger_order(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("SELECT group_name FROM master_company_group ")
    group_list = cursor.fetchall()
    # trigger_criteria = group_list[0]
    print("trigger_criteria :",group_list)
    return HttpResponse(group_list)

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def group_popup(request,trigger_name):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print("-------------=======-------------------------------===")
    userid = user_id[0]
    userid = str(userid)
    print("trigger_name ==========",trigger_name)

    # trigger_name = "T51"
    print("trigger_name ==========",trigger_name)
    # cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,o.symbol, o.buy_sell,  o.quantity,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND t.user_id ="+user_id+" AND trigger_name="+trigger_name)
    
    cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,t.trigger_criteria,o.symbol, o.buy_sell, o.quantity,o.product_type,o.trigger_id,o.order_id, master_product_type.product_type FROM triggers t JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id INNER JOIN master_product_type ON master_product_type.product_type_id = o.product_type WHERE o.is_executed='False' AND trigger_name=\'"+trigger_name+"\'")

    triggers = cursor.fetchall()
    print("triggers ",triggers)
    return render(request,'grouppopup.html',{'triggers':triggers})

@api_view(['GET','POST'])
def cancle_group_order(request):

    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    trigger_id=request.data["data"]["id"]
    print('trigger_id :=',trigger_id)
    print('trigger_id :=',trigger_id)
    # data['id]
    # trigger_id = '201'
    cursor.execute("update group_order set is_cancelled=True WHERE trigger_id="+str(trigger_id))
    connection.commit()
    print("success")
    return Response({"status":"success", "message": "success"})


# restart group cronjob

@api_view(['GET','POST'])
def restart_group_order(request):
    print("restart_group_order function")
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    trigger_id=request.data["data"]["id"]
    print('trigger_id :=',trigger_id)
    print('trigger_id :=',trigger_id)
    # data['id]
    # trigger_id = '201'
    cursor.execute("update group_order set is_cancelled=False and is_executed=False WHERE trigger_id="+str(trigger_id))
    # cursor.execute("update group_order set is_executed=False WHERE trigger_id="+str(trigger_id))

    connection.commit()
    print("success after commit")
    return Response({"status":"success", "message": "success"})

    
# ID needed
@login_required(login_url='login_view')
def group_trigger_listing(request):
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    print("==================")
    cursor.execute("SELECT user_id FROM current_login_user")
    user_id = cursor.fetchone()
    print("-------------=======-------------------------------===")
    userid = user_id[0]
    userid = str(userid)
    # cursor.execute("SELECT t.created_on, t.trigger_name,t.symbol, master_trigger_conditions.trigger_condition,t.trigger_id FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.trigger_condition_list tcl ON trigger_list not like '%' || t.trigger_id || '%' JOIN public.orders o ON tcl.trigger_id=o.trigger_id INNER JOIN master_trigger_conditions ON t.trigger_condition_id = master_trigger_conditions.trigger_condition_id WHERE t.is_active=true and t.user_id ="+userid+" and is_group_trigger = false order by t.trigger_id asc ")
    cursor.execute("select created_on,trigger_name,symbol,trigger_criteria,trigger_id from triggers where user_id ="+userid+" and is_group_trigger = True")
    triggers = cursor.fetchall()
    print("trigger_condition_list trigger_id : ",triggers)       
    cursor.execute("SELECT username FROM current_login_user")
    current_user = cursor.fetchone()
    current_user = current_user[0]
    print('current_user :',current_user)
    current_user = str(current_user)   
    return render(request,'group_trigger_listing.html',{'triggers':triggers,'current_user':current_user})

# @login_required(login_url='login_view')
# def update_group_trigger(request,trigger_id):
#     if request.method=="POST":
#         pass
#     else:
#         return render(request,'update_group_trigger.html')
# 

@login_required(login_url='login_view')
@api_view(['GET','POST'])
def update_group_trigger(request,trigger_id):
    print("trigger_idtrigger_idtrigger_idtrigger_idtrigger_idtrigger_id",trigger_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor()
    if request.method =='POST':
        print("session update_triggers:========================")
        trigger_name=request.data["trigger"]["trigger_name"]
        print('trigger_name',trigger_name)
        symbol=request.data["trigger"]["symbol"]
        print('symbol',symbol)
        trigger_condition_id=request.data["trigger"]["trigger_condition_id"]
        trigger_condition_id = str(trigger_condition_id)
        print('trigger_condition_id',trigger_condition_id)
        trigger_criteria=  json.dumps(request.data["trigger"]["trigger_criteria"])
        print('trigger_criteria ::',trigger_criteria)
        exchange_id=request.data["trigger"]["exchange_id"]
        exchange_id = str(exchange_id)
        print('exchange_id',exchange_id)
        trigger_id = str(trigger_id)
        print('trigger_id === ',trigger_id)
        cursor.execute("UPDATE triggers set trigger_name = \'"+trigger_name+"\', symbol=\'"+symbol+"\',trigger_condition_id=\'"+trigger_condition_id+"\',trigger_criteria=\'"+trigger_criteria+"\',exchange_id=\'"+exchange_id+"\' WHERE trigger_id=\'"+trigger_id+"\'")
        connection.commit()
        print("succeeeeeeeeeeeeeeeeeeeeeees")
        return Response({"status":"success", "message": "success"})
    else:    
        print("GET")
        trigger_id = str(trigger_id)
        print("trigger_id ",trigger_id)
        cursor.execute("SELECT t.trigger_id,t.trigger_name,t.symbol,e.exchange,c.trigger_condition,t.trigger_criteria FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.master_exchange eo ON eo.exchange_id=t.exchange_id WHERE t.trigger_id="+trigger_id+" order by t.trigger_id asc")
        triggers = cursor.fetchall()
        print("triggers : ",triggers)

        # 
        cursor.execute("SELECT t.trigger_criteria FROM public.triggers t JOIN public.master_exchange e ON t.exchange_id=e.exchange_id JOIN public.master_trigger_conditions c ON t.trigger_condition_id=c.trigger_condition_id JOIN public.trigger_condition_list tcl ON trigger_list like '%' || t.trigger_id || '%' JOIN public.master_exchange eo ON eo.exchange_id=t.exchange_id WHERE t.trigger_id="+trigger_id+" order by t.trigger_id asc")
        trigger_criteria = cursor.fetchall()
        print("trigger_criteria : ",trigger_criteria)

        # print("trigger_condition_list trigger_id : ",trigger_criteria)
        # print("trigger_criteria ============================",type(trigger_criteria))
        return render(request,'update_group_trigger.html',{'triggers':triggers,'trigger_criteria':trigger_criteria,"trigger_id":trigger_id})
        # return render(request,'update_group_trigger.html',{'triggers':triggers,"trigger_id":trigger_id})


@login_required(login_url='login_view')
@api_view(['GET','POST'])
def delete_group_trigger(request):
    print("delete_order function -----------------------")

    trigger_id=request.data["data"]["id"]

    trigger_id = str(trigger_id)
    print("trigger_id =",trigger_id)
    connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursor.execute("DELETE FROM triggers WHERE trigger_id="+ trigger_id)
    connection.commit()
    print("success")
    return Response({"status":"success", "message": "success"})

"""

#error

company_name IS None
except blockkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
except (<class 'psycopg2.errors.ForeignKeyViolation'>, ForeignKeyViolation('insert or update on table "group_order_response" 
violates foreign key constraint "fk_order_id"\nDETAIL:  Key (order_id)=(976) is not present in table "group_order".\n'), 
<traceback object at 0x00000273A2A0B948>)

 """

def dumm(request):
    time.sleep(5)
    print("hhhhhhhhhhhhhhhhhhhhhhhhh")
    return HttpResponse("done")
    