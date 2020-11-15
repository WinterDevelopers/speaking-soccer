from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User





# my status tuples
STATUS = (
    (0,"Darft"), (1,"publish")
     )

# to create categories
TAG = (
    (0,'EPL'), (1,'laliga'), (2,'seria-A'), (3,'bundesliga'), (4, 'league 1'),
)


# Create your models here. 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    display_image = models.ImageField(upload_to = 'static/images', default = 'static/images/head.jpg')
    counts = models.IntegerField(default = 0)
    category = models.IntegerField(choices=TAG, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": str(self.slug)})    

    #def get_absolute_url(self):
        #return reverse_lazy('post_detail', kwargs = {'slug': str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Subscribers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name
    






