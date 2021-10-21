def dummy():
    print("this is dummy function")

# from django.shortcuts import render

# # Create your views here.
# from rest_framework.response import Response
# from rest_framework import serializers, views
# from rest_framework.decorators import api_view
# from kiteconnect import KiteConnect
# from datetime import datetime,timedelta
# import logging
# import json
# import psycopg2
# import sys
# import threading
# # from psycopg2.extras import Json
# import os.path
# import enum
# # import pandas as pd
# import pytz
# from pytz import timezone
# import sched, time
# from decimal import *
# from django.contrib.auth.decorators import login_required


# def get_triggers_orders():        
#     try:
#         connection = psycopg2.connect(user="postgres", password="root", host="localhost", port="5432", database="Kite")
#         cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         postgres_insert_query = """SELECT * from public.get_triggers_orders()"""
#         cursor.execute(postgres_insert_query,()) 
#         rows = cursor.fetchall()
#         triggers = []
#         for row in rows:
#             triggers.append(dict(row))
#         cursor.close()
#         connection.close()
#         return triggers
#     except:
#         # print("Unexpected error:", sys.exc_info()[0])
#         return Response({"status":"failure", "message": "failure"})


# def online_trigger(request):        
#     try:
#         triggers=get_triggers_orders()
#         for trigger in triggers:
#             try:
#                 apply_filters(trigger)
#             except:
#                 global_message = global_message + sys.exc_info()[0]
#                 pass            
#         return Response({"status":"success", "message": "success","content":triggers})        
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         return Response({"status":"failure", "message": "failure"})

# def criteria_price(trigger):
#     try:        
#         file1 = open("accesstoken.txt","r")
#         access_token=file1.read()
#         file1.close() 
#         kite = KiteConnect(api_key="ib196gkbrmuqnoer")
#         kite.set_access_token(access_token)
#         exchange_symbol=trigger["exchange"]+":"+trigger["symbol"]
#         quote_info=kite.quote(exchange_symbol)
#         if trigger is not None:
#             if trigger["trigger_criteria"]["operator"]=="5" and quote_info[exchange_symbol]["last_price"]== Decimal(trigger["trigger_criteria"]["amount"]):
#                 execute_order(trigger)
#             elif trigger["trigger_criteria"]["operator"]=="3" and quote_info[exchange_symbol]["last_price"]> Decimal(trigger["trigger_criteria"]["amount"]):
#                 execute_order(trigger)
#             elif trigger["trigger_criteria"]["operator"]=="1" and quote_info[exchange_symbol]["last_price"]>= Decimal(trigger["trigger_criteria"]["amount"]):
#                 execute_order(trigger)
#             elif trigger["trigger_criteria"]["operator"]=="4" and quote_info[exchange_symbol]["last_price"]< Decimal(trigger["trigger_criteria"]["amount"]):
#                 execute_order(trigger)
#             elif trigger["trigger_criteria"]["operator"]=="2" and quote_info[exchange_symbol]["last_price"] <= Decimal(trigger["trigger_criteria"]["amount"]):
#                 execute_order(trigger)
#             elif trigger["trigger_criteria"]["operator"]=="6" and ( quote_info[exchange_symbol]["last_price"]> Decimal(trigger["trigger_criteria"]["from_amount"]) and quote_info[exchange_symbol]["last_price"]< Decimal(trigger["trigger_criteria"]["to_amount"])):
#                 execute_order(trigger)
#         else:
#             pass    
#     except:
#         global_message = global_message + sys.exc_info()[0]