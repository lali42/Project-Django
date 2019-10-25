from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=200)
    title = models.DateField(auto_now_add=True)
    detail = models.CharField(max_length=1000)
    

    def __str__(self):
        return f'{self.icon} {self.title}'
