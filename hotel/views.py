from rest_framework.decorators import api_view
from .models import Room , Customer , Booking , Invoice
from rest_framework.response import Response
from .serializers import RoomSerializer , CustomerSerializer , BookingSerializer , InvoiceSerializer


@api_view(['POST'])
def create_room_api(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_room_api(request):
    h = Room.objects.all()
    serializer=RoomSerializer(h , many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_room_api(request,id):
    h = Room.objects.get(id=id)
    serializer = RoomSerializer(h)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_room_api(request,id):
    h = Room.objects.get(id=id)
    serializer = RoomSerializer(h, data=request.data ,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_room_api(request,id):
    h = Room.objects.get(id=id)
    h.delete()
    return Response(status=204)




@api_view(['POST'])
def create_customer_api(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_customer_api(request):
    h = Customer.objects.all()
    serializer=CustomerSerializer(h , many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_customer_api(request,id):
    h = Customer.objects.get(id=id)
    serializer = CustomerSerializer(h)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_customer_api(request,id):
    h = Customer.objects.get(id=id)
    serializer = CustomerSerializer(h, data=request.data ,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_customer_api(request,id):
    h = Customer.objects.get(id=id)
    h.delete()
    return Response(status=204)






@api_view(['POST'])
def create_booking_api(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.errors , status=400)


@api_view(['GET'])
def list_booking_api(request):
    h = Booking.objects.all()
    serializer= BookingSerializer(h , many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_booking_api(request,id):
    h = Booking.objects.get(id=id)
    serializer = BookingSerializer(h)
    return Response(serializer.data , status=200)



@api_view(['PATCH'])
def update_booking_api(request,id ):
    h = Booking.objects.get(id=id)
    serializer = BookingSerializer(h, data=request.data ,partial=True)
    if serializer.is_valid():
        serializer.save()

        if h.status == "Acc":
          h.room.available = False
          h.room.save()

        elif h.status == "Cancel":
            h.room.available = True
            h.room.save()

        elif h.status == "Out":
            h.room.available = True
            h.room.save()

        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_booking_api(request, id):
    h = Booking.objects.get(id=id)
    if h.status == "Acc":
        h.room.available = True
        h.room.save()
    h.delete()
    return Response(status=204)





@api_view(['POST'])
def create_invoice_api(request,id):
    h = Booking.objects.get(id=id)

    if h.status != "Out":
      return Response({"error": "Abhi checkout nahi hua"}, status=400)   # sirf galat case

    nights = (h.check_out - h.check_in).days          # Out hone pe yahan se chalta hai
    total = nights * h.room.price
    inv = Invoice.objects.create(booking=h, total_amount=total)
    return Response(InvoiceSerializer(inv).data, status=201)


@api_view(['GET'])
def list_invoice_api(request):
    h = Invoice.objects.all()
    serializer = InvoiceSerializer(h ,  many=True)
    return Response(serializer.data, status = 200)


@api_view(['GET'])
def detail_invoice_api(request,id):
    h = Invoice.objects.get(id=id)
    serializer = InvoiceSerializer(h)
    return Response(serializer.data , status=200)


@api_view(['PATCH'])
def update_invoice_api(request,id):
    h = Invoice.objects.get(id=id)
    serializer = InvoiceSerializer(h , data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status =206)
    return Response(serializer.errors , status = 400)


@api_view(['DELETE'])
def delete_invoice_api(request,id):
    h = Invoice.objects.get(id = id)
    h.delete()
    return Response(status=204)





@api_view(['GET'])
def search_room_api(request):
    j =request.query_params.get('type')
    rooms = Room.objects.filter(room_type=j)
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def sort_room_api(request):
   order = request.query_params.get('order')
   if order == "low":
       rooms = Room.objects.all().order_by('price')
   elif order == "high":
       rooms = Room.objects.all().order_by('-price')
   else:
       return Response({"error": "Check The Option"}, status=400)
   serializer = RoomSerializer(rooms , many=True)
   return Response(serializer.data , status=200)

       
