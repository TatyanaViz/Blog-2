from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    date_of_publication = models.DateField()
    def __str__(self):
        return self.text

