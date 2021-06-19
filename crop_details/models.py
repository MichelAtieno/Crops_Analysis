from django.db import models

# Create your models here.

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
    product_variety = models.CharField(max_length=200)
    commodity_type = models.CharField(max_length=200)
    unit = models.CharField(max_length=20, choices=UNITS)
    volume_in_kgs = models.PositiveIntegerField()
    values_in_ksh = models.FloatField(null=True, blank=True, default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commodity_type}-{self.product_variety}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
