from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_pwd = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'