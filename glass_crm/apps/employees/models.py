from django.db import models


class Measurers(models.Model):
    """ Замерщики """

    name = models.CharField(max_length=255, unique=True)                                 # Замерщик.

    objects = models.Manager()

    def __str__(self):
        return self.name


class Installers(models.Model):
    """ Монтажники """

    name = models.CharField(max_length=255, unique=True)                               # Монтажник.

    objects = models.Manager()

    def __str__(self):
        return self.name
