from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog_Category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blog_cat_img = models.ImageField(upload_to="images/")
    blog_cat_description = models.CharField(max_length=200)
    def __str__(self):
        return self.blog_cat
    
class Query(models.Model):
    u_email = models.EmailField()
    u_name = models.CharField(max_length=200)
    u_query = models.CharField(max_length=200)
    def __str__(self):
        return self.u_email
    
class Subscription(models.Model):
    u_email = models.EmailField(unique=True)
    u_membership = models.CharField(max_length=60)
    def __str__(self):
        return self.u_email
    
class Blog_Post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField()

    def __str__(self):
        return self.blog_name
