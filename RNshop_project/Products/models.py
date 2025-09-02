from django.db import models

class Product(models.Model):
    Brand_choices=[("apple","Apple"),
                  ("xiaomi,", "Xiaomi"),
                  ("samsung","Samsung"),
                  ("motorola","Motorola"),
                  ("nokia","Nokia")]
    


    name = models.CharField(max_length=60)

    price = models.DecimalField(max_digits=7, decimal_places= 2)

    photo_presentation = models.ImageField(upload_to='products/Media')

    added_on = models.DateField(auto_now_add = True)

    description = models.TextField(blank=True)

    produced_by = models.CharField(max_length = 20 ,choices = Brand_choices)

    availability = models.BooleanField(default=True)
