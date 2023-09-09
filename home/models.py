from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name + " - " + self.email

class Poem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    language = models.CharField(max_length=255)
    written_for = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    