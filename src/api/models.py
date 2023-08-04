from django.db import models


# Create your models here.
categorie = ( (1,'front'), (2,'back'))

class Skill(models.Model):
    owner = models.ForeignKey('auth.User', related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=100 , blank=False, null=False)
    description = models.TextField(default='', max_length=400, null=True, )
    categorie = models.CharField(choices=categorie, max_length=100, default='back')
    image = models.ImageField(blank=True, upload_to="media/skill/", validators="", height_field=None, width_field=None, max_length=100) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Project(models.Model):
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=100, blank=False, null=False)
    description = models.TextField(default='', max_length=400, null=True, )
    created = models.DateTimeField(auto_now_add=True)
    iniciate = models.DateField(blank=False, null=False)
    conclusion = models.DateField(blank=True)
    link = models.CharField(default='', max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="media/skill/", height_field=None, width_field=None, max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
