from django.db import models


class Measurers(models.Model):
    """ Замерщики """

    measurer = models.CharField(max_length=255, unique=True)                                 # Замерщик
    objects = models.Manager()

    def __str__(self):
        return self.measurer


class Installers(models.Model):
    """ Монтажники """

    installer = models.CharField(max_length=255, unique=True)                               # Монтажник
    objects = models.Manager()

    def __str__(self):
        return self.installer