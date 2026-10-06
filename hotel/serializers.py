from rest_framework import serializers
from .models import Room , Customer , Booking , Invoice

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields=['room_no' , 'room_type' , 'price' , 'available' , 'id']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields=['name' , 'phone' , 'email'  , 'id']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields=['customer' ,'room' , 'check_in' , 'check_out' , 'status'  , 'id']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields=['booking' , 'total_amount' , 'generated_date'  , 'id']
