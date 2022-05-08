# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthorBackup(models.Model):
    author_id = models.CharField(primary_key=True, max_length=20)
    author_name = models.TextField(blank=True, null=True)
    author_info = models.TextField(blank=True, null=True)
    author_photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_backup'


class AuthorBackup2(models.Model):
    author_id = models.CharField(max_length=20)
    author_name = models.TextField(blank=True, null=True)
    author_info = models.TextField(blank=True, null=True)
    author_photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_backup2'


class AuthorBackup3(models.Model):
    author_id = models.CharField(max_length=20)
    author_name = models.TextField(blank=True, null=True)
    author_info = models.TextField(blank=True, null=True)
    author_photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_backup3'


class Board(models.Model):
    board_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    board_content = models.TextField(blank=True, null=True)
    pubdate = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


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


class BookBackup2(models.Model):
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
        db_table = 'book_backup2'


class BookBackup3(models.Model):
    book_id = models.CharField(primary_key=True, max_length=20)
    title = models.TextField(blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    author_id = models.CharField(max_length=20, blank=True, null=True)
    pubdate = models.DateField(blank=True, null=True)
    translator = models.TextField(blank=True, null=True)
    adult = models.IntegerField(blank=True, null=True)
    author_name = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_backup3'


class BookCover(models.Model):
    book = models.OneToOneField('BookDesc', models.DO_NOTHING, primary_key=True)
    cover = models.TextField(blank=True, null=True)
    cover_large = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_cover'


class BookCoverBackup2(models.Model):
    book_id = models.CharField(max_length=20)
    cover_large = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_cover_backup2'


class BookCoverBackup3(models.Model):
    book_id = models.CharField(max_length=20)
    cover_large = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_cover_backup3'


class BookDesc(models.Model):
    book = models.OneToOneField(Book, models.DO_NOTHING, primary_key=True)
    content = models.TextField(blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_desc'


class BookDescBackup2(models.Model):
    book_id = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_desc_backup2'


class BookDescBackup3(models.Model):
    book_id = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_desc_backup3'


class BookDescPractice(models.Model):
    book_id = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_desc_practice'


class BookGrade(models.Model):
    book = models.OneToOneField(Book, models.DO_NOTHING, primary_key=True)
    score = models.FloatField(blank=True, null=True)
    review_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_grade'


class BookGradeBackup2(models.Model):
    book_id = models.CharField(max_length=20)
    score = models.FloatField(blank=True, null=True)
    review_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_grade_backup2'


class BookGradeBackup3(models.Model):
    book_id = models.CharField(max_length=20)
    score = models.FloatField(blank=True, null=True)
    review_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_grade_backup3'


class BookHistory(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_history'


class BookSize(models.Model):
    book = models.OneToOneField(BookDesc, models.DO_NOTHING, primary_key=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_size'


class BookSizeBackup2(models.Model):
    book_id = models.CharField(max_length=20)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_size_backup2'


class BookSizeBackup3(models.Model):
    book_id = models.CharField(max_length=20)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_size_backup3'


class Comment(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=20)
    board = models.ForeignKey(Board, models.DO_NOTHING, blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    pubdate = models.DateField(blank=True, null=True)
    comment_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class CoverTest(models.Model):
    book_id = models.CharField(max_length=20, blank=True, null=True)
    cover_large = models.TextField(blank=True, null=True)
    cover = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cover_test'


class DislikeTab(models.Model):
    dislike_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dislike_tab'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Isbn(models.Model):
    isbn = models.CharField(primary_key=True, max_length=10)
    isbn13 = models.CharField(max_length=14, blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, db_column='BOOK_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isbn'


class IsbnBackup2(models.Model):
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=14, blank=True, null=True)
    book_id = models.CharField(db_column='BOOK_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isbn_backup2'


class IsbnBackup3(models.Model):
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=14, blank=True, null=True)
    book_id = models.CharField(db_column='BOOK_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isbn_backup3'


class LikeTab(models.Model):
    like_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'like_tab'


class Phrase(models.Model):
    phrase_id = models.CharField(primary_key=True, max_length=20)
    phrase_content = models.TextField(blank=True, null=True)
    book = models.ForeignKey(BookDesc, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phrase'


class PhraseBackup2(models.Model):
    phrase_id = models.CharField(max_length=20)
    phrase_content = models.TextField(blank=True, null=True)
    book_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phrase_backup2'


class PhraseBackup3(models.Model):
    phrase_id = models.CharField(max_length=20)
    phrase_content = models.TextField(blank=True, null=True)
    book_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phrase_backup3'


class Review(models.Model):
    review_id = models.CharField(primary_key=True, max_length=20)
    review_content = models.TextField(blank=True, null=True)
    book = models.ForeignKey(BookDesc, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class ReviewBackup2(models.Model):
    review_id = models.CharField(max_length=20)
    review_content = models.TextField(blank=True, null=True)
    book_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_backup2'


class ReviewBackup3(models.Model):
    review_id = models.CharField(max_length=20)
    review_content = models.TextField(blank=True, null=True)
    book_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_backup3'


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


class Wishlist(models.Model):
    wishlist_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist'


class Yes(models.Model):
    title = models.TextField(blank=True, null=True)
    cover = models.TextField(db_column='COVER', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(blank=True, null=True)
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    author_id = models.CharField(db_column='AUTHOR_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pubdate = models.DateField(db_column='PUBDATE', blank=True, null=True)  # Field name made lowercase.
    translator = models.TextField(db_column='TRANSLATOR', blank=True, null=True)  # Field name made lowercase.
    adult = models.IntegerField(blank=True, null=True)
    author = models.TextField(db_column='AUTHOR', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(blank=True, null=True)
    book_id = models.CharField(db_column='BOOK_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yes'
