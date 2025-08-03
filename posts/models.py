from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status = 'pu')

class Article(models.Model):

    STATUS_OF_ARTICLE = [
        ('ch','Checking'),
        ('re','Rejected'),
        ('pu','published'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_OF_ARTICLE, max_length=20, default='ch')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Articles')
    slug = models.SlugField(unique=True,null=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return f'writed by {self.author}'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            self.save()

    objects = models.Manager()
    publish = ArticleManager()

