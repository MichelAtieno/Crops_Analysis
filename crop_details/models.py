from django.db import models
from django.shortcuts import reverse

# Create your models here.product_variety = models.ManyToManyField(Product_Variety)


class Product_Variety(models.Model):
    variety = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.variety

    def get_variety_absolute_url(self):
        return reverse('csvs:variety_profile', kwargs={
            'id': self.id
        })


UNITS = (
    ('ExtBag', 'Ext Bag'),
    ('MedBunch','Med Bunch' ),
    ('LgBox','Lg Box'),
    ('Bag', 'Bag'),
    ('SmBasket', 'Sm Basket'),
    ('net', 'net'),
    ('Dozen', 'Dozen'),
    ('crate', 'crate')
)


class Crops(models.Model):
    commodity = models.CharField(max_length=100)
    product_variety = models.ManyToManyField(Product_Variety, related_name='produce_variety')
    image = models.ImageField(default='')
    unit = models.CharField(max_length=20, choices=UNITS)
    volume_in_kgs = models.PositiveIntegerField()
    values_in_ksh = models.FloatField(null=True, blank=True, default=0.0)
    date = models.TextField(blank=True, null=True)
    slug = models.SlugField()


    def __str__(self):
        return f"{self.commodity}-{self.slug}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('csvs:crop', kwargs={
            'slug': self.slug
        })

class Commodity_Type(models.Model):
    commodity = models.ForeignKey(Crops, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.commodity
   