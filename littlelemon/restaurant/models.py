from django.db.models import Model, CharField, TextField, DateField, IntegerField, SmallIntegerField

# Create your models here.
class Booking(Model):
    first_name = CharField(max_length=200)
    reservation_date = DateField()
    reservation_slot = SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(Model):
   name = CharField(max_length=200) 
   price = IntegerField(null=False) 
   menu_item_description = TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name