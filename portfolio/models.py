from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    description = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='portfolio/images/', height_field=None, width_field=None, max_length=100)
    url = models.URLField(blank = True)

    def __str__(self): # there is no need to migrate because function doesnt affect the database
        return self.title









