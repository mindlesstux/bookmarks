from django.db import models

# Create your models here.
class Folder(models.Model):
        id = models.IntegerField(primary_key=True)
        parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
        name = models.CharField(max_length=128)