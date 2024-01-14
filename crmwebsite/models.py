from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=20, blank=False, null=False)
    state = models.CharField(max_length=30, blank=False, null=False)
    zipcode = models.IntegerField(blank=False, null=False,validators=[MaxValueValidator(999999)])

    class Meta:
        db_table = "customer"

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")