from django.db import models
from BimsCharity.userApp.models import Profile

# Create your models here.

class Cause(models.Model):
    cause_id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=50,null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    price_raised = models.DecimalField( max_digits=9, decimal_places=2)
    price_target = models.DecimalField( max_digits=9, decimal_places=2)
    details = models.TextField(null=True)
    cause_image = models.ImageField(upload_to='cause_images/', null=True)
    date_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
    












    