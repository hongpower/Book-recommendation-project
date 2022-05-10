from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(primary_key=True, max_length=20)
    title = models.TextField(blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    author_id = models.CharField(max_length=20, blank=True, null=True)
    pubdate = models.DateField(blank=True, null=True)
    translator = models.TextField(blank=True, null=True)
    adult = models.IntegerField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'

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

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    book_id = models.CharField(max_length=20, blank=True, null=True)
    board_content = models.TextField(blank=True, null=True)
    pubdate = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'

