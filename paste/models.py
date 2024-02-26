from django.db import models


class File(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    file = models.FileField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    visited = models.IntegerField(default=0)
    password = models.CharField(max_length=1024, null=True, blank=False)


class Username(models.Model):
    name = models.CharField(max_length=255)
    file = models.ForeignKey(File, on_delete=models.CASCADE)


class Limit(models.Model):
    view = models.IntegerField()
    time = models.IntegerField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)
