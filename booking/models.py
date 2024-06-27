from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=10)
    car_name = models.CharField(max_length=20)
    rating = models.IntegerField()
    photo = models.ImageField(upload_to='driver_img/')

    def __str__(self):
        return f"{self.name}"


class Passenger(models.Model):
    name = models.CharField(max_length=10)
    number = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='passenger_img/')

    def __str__(self):
        return f"{self.name}"


class Bookings(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking #{self.pk}"