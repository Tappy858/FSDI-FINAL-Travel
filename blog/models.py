from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img')
    repository = models.URLField()
    

    def __str__(self):
        return f"{self.name} - ({self.year})"
