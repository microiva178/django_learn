from django.db import models
from django.conf import settings

class fortest(models.Model):
    testlogin = models.CharField(max_length=30)
    testpassword = models.CharField(max_length=30)

    def saveit(self):
        self.save()
