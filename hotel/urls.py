from django.urls import path
from . import views

urlpatterns=[
    path('api/create_room/', views.create_room_api , name = "create_room_api"),
    path('api/list_room/', views.list_room_api , name = "list_room_api"),
    path('api/detail_room/<int:id>/', views.detail_room_api , name = "detail_room_api"),
    path('api/update_room/<int:id>/', views.update_room_api , name = "update_room_api"),
    path('api/delete_room/<int:id>/', views.delete_room_api , name = "delete_room_api"),

    
    path('api/create_customer/', views.create_customer_api , name = "create_customer_api"),
    path('api/list_customer/', views.list_customer_api , name = "list_customer_api"),
    path('api/detail_customer/<int:id>/', views.detail_customer_api , name = "detail_customer_api"),
    path('api/update_customer/<int:id>/', views.update_customer_api , name = "update_customer_api"),
    path('api/delete_customer/<int:id>/', views.delete_customer_api , name = "delete_customer_api"),

    
    path('api/create_booking/', views.create_booking_api , name = "create_booking_api"),
    path('api/list_booking/', views.list_booking_api , name = "list_booking_api"),
    path('api/detail_booking/<int:id>/', views.detail_booking_api , name = "detail_booking_api"),
    path('api/update_booking/<int:id>/', views.update_booking_api , name = "update_booking_api"),
    path('api/delete_booking/<int:id>/', views.delete_booking_api , name = "delete_booking_api"),

    
    path('api/create_invoice/<int:id>/', views.create_invoice_api , name = "create_invoice_api"),
    path('api/list_invoice/', views.list_invoice_api , name = "list_invoice_api"),
    path('api/detail_invoice/<int:id>/', views.detail_invoice_api , name = "detail_invoice_api"),
    path('api/update_invoice/<int:id>/', views.update_invoice_api , name = "update_invoice_api"),
    path('api/delete_invoice/<int:id>/', views.delete_invoice_api , name = "delete_invoice_api"),

]