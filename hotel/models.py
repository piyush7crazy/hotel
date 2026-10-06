from django.db import models 

class Room(models.Model):
    room_no = models.IntegerField(unique = True)
    room_type = models.CharField(max_length=100 , choices = [("Slng" , "Single") , ("Dou" , "Double") , ("Su" , "Suite")])
    price = models.IntegerField()
    available = models.BooleanField(default=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    

class Booking(models.Model):
    customer = models.ForeignKey(Customer , on_delete = models.CASCADE)
    room = models.ForeignKey(Room , on_delete = models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=100 , choices = [("Pen" , "Pending") , ("Acc" , "Accepted") , ("Cancel" , "Cancelled") , ("Out" , "Checked_Out")])


class Invoice(models.Model):
    booking = models.OneToOneField(Booking , on_delete = models.CASCADE)
    total_amount = models.DecimalField(max_digits=12 , decimal_places=2)
    generated_date = models.DateTimeField(auto_now_add=True)
