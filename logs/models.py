from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)
SLUG_TYPE = (
    ('S', 'Statement'),
    ('D', 'Doubt'),
    ('I', 'Imp'),
    ('W', 'Work')
)

class Post(models.Model):
    slug = models.SlugField(max_length=200, unique=False, choices=SLUG_TYPE, default='W')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', default='subodhk')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    

class Meta:
    ordering = ['-created_on']

def __str__(self):
    return self.content