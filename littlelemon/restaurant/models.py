from django.db.models import Model, CharField, DateField, SmallIntegerField

# Create your models here.
class Booking(Model):
    first_name = CharField(max_length=200)
    reservation_date = DateField()
    reservation_slot = SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name