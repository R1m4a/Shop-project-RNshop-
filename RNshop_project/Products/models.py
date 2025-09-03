from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)
    
    
    def __str__(self):
        return self.name



class Product(models.Model):
    Brand_choices=[("apple","Apple"),
                  ("xiaomi,", "Xiaomi"),
                  ("samsung","Samsung"),
                  ("motorola","Motorola"),
                  ("nokia","Nokia")]
    

    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    name = models.CharField(max_length = 60)

    slug = models.SlugField(unique = True)

    price = models.DecimalField(max_digits = 7, decimal_places = 2)

    photo_presentation = models.ImageField(upload_to='products/Media')

    added_on = models.DateField(auto_now_add = True)

    description = models.TextField(blank = True)

    produced_by = models.CharField(max_length = 20 ,choices = Brand_choices)

    availability = models.BooleanField(default = True)


