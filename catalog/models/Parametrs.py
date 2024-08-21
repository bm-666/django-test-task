from django.db import models


class Parametrs(models.Model):
    id = models.AutoField(prmary_key=True)
    name = models.CharField()
