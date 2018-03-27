from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    text = models.CharField(max_length=10000)
    datetime = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User)

    def __str__(self):
        return '{}: {} [{}]'.format(
            self.sender.username,
            self.text[:7] + '...' if len(self.text) >= 10 else self.text,
            self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        )

    class Meta:
        ordering = ('datetime',)
