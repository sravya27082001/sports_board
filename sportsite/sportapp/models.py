from django.db import models

# Create your models here.
class equipments(models.Model):
    name = models.CharField(max_length=30)
    quantity=models.IntegerField()
    sport= models.CharField(max_length=50)
    Image= models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.name