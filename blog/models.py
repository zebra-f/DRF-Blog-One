from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):


    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
    ]
    
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    content = models.TextField()

    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    slug = models.SlugField(max_length=250, unique_for_date='published')    
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    objects = models.Manager()  # defualt manager
    postobjects = PostObjects()  # custom manager


    class Meta:
        ordering = ('-published',)
    

    def __str__(self):
        return f'{self.author}- {self.title}'


