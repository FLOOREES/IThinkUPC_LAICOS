from django.db import models

class Member(models.Model):
  username = models.CharField(max_length=255)
  firstname = models.CharField(max_length=255)
  age = models.IntegerField(null=True)
  degree = models.CharField(max_length=255, null=True)
  music = models.CharField(max_length=255, null=True)
  sport = models.IntegerField(null=True)
  read = models.IntegerField(null=True)
  board_games= models.IntegerField(null=True)
  cluster = models.IntegerField(null=True)
  slug = models.SlugField(default='', null=False)
  def __str__(self):
    return f"{self.firstname} {self.music}"
  def delete_everything(self):
    Member.objects.all().delete()