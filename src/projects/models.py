from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    tech = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="projects")


    class Meta:
        def __str__(self) -> str:
            return self.title
            
