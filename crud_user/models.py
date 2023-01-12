from django.db import models
from django.contrib.auth.hashers import make_password



class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null= True)
    date_birth = models.DateField(null= True)
    address =  models.CharField(max_length=50,null= True)
    password = models.CharField(max_length=200)
    mobile_phone = models.IntegerField(null= True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name