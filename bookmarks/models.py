from django.db import models

class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=16)
    description = models.TextField()

    def __str__(self):
        return self.group

class Folders(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True, blank=True)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Create your models here.
class Bookmarks(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True, blank=True)
    folder = models.ForeignKey(Folders, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=400)

    def __str__(self):
        return self.name