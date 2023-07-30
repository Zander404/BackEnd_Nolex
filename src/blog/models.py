from django.db import models

# Create your models here.

class Post(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=False, default='')
    owner =  models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateField(auto_now_add=True)
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    


class Categorie(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'
