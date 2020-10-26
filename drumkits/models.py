from django.db import models

# Create your models here.
class Drumkits(models.Model):
    sound = models.CharField(max_length=250)
    url = models.URLField(max_length=200)
    library = models.CharField(max_length=250)
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.sound