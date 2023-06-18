from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.name