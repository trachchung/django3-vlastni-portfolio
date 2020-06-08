from django.db import models

import datetime
class Blog(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    description = models.CharField(max_length = 150)
    date = models.DateField(datetime.date.today)
    url = models.URLField(blank = True)

    def __str__(self): # there is no need to migrate because function doesnt affect the database
        return self.title