from django.db import models


class Currency(models.Model):

    type = models.CharField(max_length=20)
    rate = models.FloatField(max_length=20)


