from django.db import models

# Create your models here.

class Posts(models.Model):
    post_date = models.DateTimeField(auto_now=True)
    post_author = models.CharField(max_length=25)
    post_title = models.CharField(max_length=40)
    post_content = models.TextField(max_length=1000)


class Comments(models.Model):
    comment_date = models.DateTimeField(auto_now=True)
    comment_author = models.CharField(max_length=25)
    comment_content = models.TextField(max_length=300)
    # comment_post_id = models.IntegerField()  // A implementar
    


class Users(models.Model):
    user_name = models.CharField(max_length=25)
    user_pass = models.CharField(max_length=40)
    user_email = models.EmailField()