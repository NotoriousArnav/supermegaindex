from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

mega_validator = RegexValidator(
        regex='^(https?:\\/\\/)?(www\\.)?mega\\.nz\\/',
        message='Link must be a valid mega.nz link!'
    )

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    link = models.CharField(max_length=300, primary_key=True, validators=[mega_validator])
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)



