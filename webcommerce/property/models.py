from django.db import models


RENT_SALE = ((0, 'Rent'),(1, 'Sale'))
LATEST_OFFER = ((0, 'Latest'), (1, 'Offer'))

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='property_pics')
    description = models.TextField(default='')
    price = models.IntegerField(default='0')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(choices=RENT_SALE, default=0)
    uniqueness = models.IntegerField(choices=LATEST_OFFER, default=0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name 
