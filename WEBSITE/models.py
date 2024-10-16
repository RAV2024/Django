from django.db import models


class Guitar(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upper_deck_material = models.CharField(max_length=50)
    lower_deck_material = models.CharField(max_length=50)
    fingerboard_material = models.CharField(max_length=50)
    frets = models.IntegerField()
    pickup = models.CharField(max_length=50)
    strings = models.IntegerField()
    image = models.ImageField(upload_to='guitars/')

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name