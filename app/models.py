from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models

# Create your models here.


# disease outbreak
class Hostel(models.Model):

    GENDER=[('Male','Male'),('Female','Female'),('Both Male & Female','Both Male & Female')]

    hostel_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50,choices=GENDER)
    maximum_capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    location = models.PointField(srid=4326)
    objects = GeoManager()


    def _str_(self):
        return self.hostel_name

    class Meta:
        verbose_name_plural="Hostel"

