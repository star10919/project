'''
from common.models import DataTransferObject
from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')

class CrimeVO(models.Model):
    police = models.TextField()   #CharField는 글자제한이 있을 때 사용/ TextField는 글자제한이 없을 때 사용
    crime = models.TextField()
    create_at = models.DateTimeField()

class CrimeDTO(DataTransferObject):
    police = ''
    crime = ''
    create_at = ''
'''