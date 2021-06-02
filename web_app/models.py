from django.db import models


class PublicChat(models.Model):
  title = models.CharField(max_length=100)


class Message(models.Model):
  chat = models.ForeignKey(PublicChat, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  text = models.CharField(max_length=500)
  created_date = models.DateTimeField(auto_now_add=True)
