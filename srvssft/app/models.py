from django.db import models

# Create your models here.

# class User(models.Model):
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)


class Audio(models.Model):
    name = models.CharField(max_length=30)
    mp3 = models.CharField(max_length=300)


class AudioFile(models.Model):
  # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  record_id = models.FileField(upload_to='film_help/%Y-%m-%d/')


