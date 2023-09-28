from django.db import models

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.num_of_products}'
