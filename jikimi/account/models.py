from django.db import models
from django.contrib.auth.models import AbstractUser
from cctv_page.models import School 

# Create your models here.

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    user_phone = models.CharField(unique=True, max_length=11, blank=True, null=True)
    user_school = models.ForeignKey(School, models.DO_NOTHING, db_column='user_school', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'User'