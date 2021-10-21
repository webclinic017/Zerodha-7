"""kiteconnect_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from kiteconnect_source.source.views import get_login_url, get_instruments, sync_instruments, save_trigger_order,place_order, save_request_token,online_trigger,update_trigger_order
from kiteconnect_source.source import views
# from .settings.base import ADMIN_URL

# from django.conf.urls import handler404

# handler404 = views.my_error_404
# app_name = 'kiteconnect_source'
urlpatterns = [
    path('', get_login_url),   
    url(r'^login/$', get_login_url, name='login'),
    url(r'^instruments/$', get_instruments, name='instruments'),
    url('syncinst', sync_instruments, name='syncinst'),
    # url('savetriggerorder', save_trigger_order, name='savetriggerorder'),
    url('placeorder', place_order, name='place_order'),
    url('saverequesttoken', save_request_token, name='save_request_token'),
    # url('getdashboardorders', get_dashboard_orders, name='get_dashboard_orders'),
    url('onlinetrigger', online_trigger, name='online_trigger'),
    path('trading/', views.trading, name='trading'),
    path('loginzerodha', views.loginzerodha, name='loginzerodha'),
    path('login_view/',views.login_view,name='login_view'),
    path('login_view/home/', views.home, name='home'),
    path('login_view/home/trigger_order_list/update/<int:id>', views.update,name='update'),

    url('update_order', views.update_trigger_order, name='update_order'),
    path('login_view/home/delete/', views.delete_order,name='delete'),

    path('user_logout/',views.user_logout,name='user_logout'),
    # path('open_order_excel/',views.open_order_excel,name='open_order_excel'),
    # path('execute_order_excel/',views.execute_order_excel,name='execute_order_excel'),
    # path('group_open_order_excel/',views.group_open_order_excel,name='group_open_order_excel'),
    # path('group_executed_order_excel/',views.group_executed_order_excel,name='group_executed_order_excel'),


    path('acess_token/',views.acess_token,name='acess_token'),
    path('admin/', admin.site.urls),
    path("save_multiple_trigger/", views.save_multiple_trigger,name="save_multiple_trigger"),
    path("save_multiple_order/", views.save_multiple_order,name="save_multiple_order"),
    path('trigger_listing/',views.trigger_listing,name="trigger_listing"),
    path('trigger_list/',views.trigger_list,name="trigger_list"),#trigger_id
    path('group_listing/',views.group_listing,name="group_listing"),
    path('group_listing/delete_group/',views.delete_group,name="delete_group"),

    path('groups_order_listing/',views.groups_order_listing,name='groups_order_listing'),
    path('insert_group_order/',views.insert_group_order,name='insert_group_order'),
    # 
    path('groups_order_listing/group_open_trigger_order_list/update_group_order/<str:order_id>',views.update_group_order,name='update_group_order'),
    path('groups_order_listing/delete_group/',views.delete_group_order,name='delete_group_order'),
    path('group_listing/company_add_update/<str:group_name>',views.group_fetch_update,name='group_fetch_update'),
    path('group_order/company_add_update/',views.group_order,name='group_order'),

    path("fetch_trigger/<str:trigger_name>", views.fetch_trigger,name="fetch_trigger"),
    path("fetch_trigger_without_para/<str:trigger_name>", views.fetch_trigger_without_para,name="fetch_trigger_without_para"),


    path("create_group/", views.create_group,name="create_group"),
    path("insert_group_trigger/", views.insert_group_trigger,name="insert_group_trigger"),
    path('save_multiple_order/group_order_fetch/<str:trigger_name>',views.fetch_triggers,name='fetch_triggers'),#fetch_triggers
    path('online_group_order/',views.online_group_order,name='online_group_order'),
    path('insert_group/',views.insert_group,name="insert_group"),
    path('delete_trigger/<int:id>',views.delete_trigger,name="delete_trigger"),
    path('trigger_list/update/<int:trigger_id>',views.update_triggers,name="update_triggers"),#
    path('trigger_list/delete/',views.delete_trigger_from_trigger_list,name="delete_triggers"),#
    path('call_backup/',views.call_backup,name="call_backup"),

    path('login_view/home/cancel_order/',views.cancel_order,name="cancel_order"),
    path('cancel_group_order/cancle_order/<int:order_id>',views.cancel_group_order,name="cancel_group_order"),
    path('group_trigger_listing/update_group_trigger/<int:trigger_id>',views.update_group_trigger,name="update_group_trigger"),

    path("group_trigger_order/",views.group_trigger_order),
    # path("groups_order_listing/group_popup/<str:trigger_name>",views.group_popup,name="group_popup"),
    path("groups_order_listing/cancle_group_order/",views.cancle_group_order,name="cancle_group_order"),
    path("group_trigger_listing/",views.group_trigger_listing,name="group_trigger_listing"),
    path("delete_group_trigger/",views.delete_group_trigger,name="delete_group_trigger"),
    path("groups_order_listing/online_group_order/",views.online_group_order,name="online_group_order/"),
    path("restart_group_order/",views.restart_group_order,name="restart_group_order/"),
    
    path("login_view/home/trigger_order_list/<str:trigger_name>",views.open_trigger_order_list,name="trigger_order_list"),
    path('individual_execute_trigger_excel/',views.individual_execute_trigger_excel,name='individual_execute_trigger_excel'),
    path('groups_order_listing/group_open_trigger_order_list/<str:trigger_name>',views.group_open_trigger_order_list,name= 'individual_executed'),
    path('groups_order_listing/group_executed_trigger_order_list/<str:trigger_name>',views.group_executed_trigger_order_list,name= 'individual_executed'),

    path("login_view/home/deleteTriggerOrder/",views.deleteIndividualTriggerOrder,name='deleteTriggerOrder'),
    path("dummy/",views.dummy),

    path('open_order_excel/',views.open_order_excel,name='open_order_excel'),
    path('trigger_excel/',views.trigger_excel,name='trigger_excel'),
    path('execute_order_excel/',views.execute_order_excel,name='execute_order_excel'),
    path('group_open_order_excel/',views.group_open_order_excel,name='group_open_order_excel'),
    path('group_executed_order_excel/',views.group_executed_order_excel,name='group_executed_order_excel'),
    path('open_trigger_excel/',views.open_trigger_excel,name='open_trigger_excel'),
    path('individual_order_excel/',views.individual_order_excel,name='individual_order_excel'),
    path('group_trigger_excel/',views.group_trigger_excel,name='group_trigger_excel'),
    path('group_order_excel/',views.group_order_excel,name='group_order_excel'),

    path('group_executed_trigger_list/',views.group_executed_trigger_list,name='group_executed_trigger_list'),
    path('group_executed_order_list/',views.group_executed_order_list,name='group_executed_order_list'),
    path('individual_execute_order_excel/',views.individual_execute_order_excel,name='individual_execute_order_excel'),

    path("login_view/home/executed_trigger_order_list/<str:trigger_name>",views.individual_executed_trigger_order_list,name="executed_trigger_order_list"),
    path('thealgotrade.in/sendrequesttoken',views.sendrequesttoken,name='sendrequesttoken'),


]