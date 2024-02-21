from django.db import models


class Measurer(models.Model):
    """ Замерщики """

    name = models.CharField(max_length=255, unique=True, verbose_name='Имя замерщика')      # Замерщик.

    objects = models.Manager()

    def __str__(self):
        return self.name


class Installer(models.Model):
    """ Монтажники """

    name = models.CharField(max_length=255, unique=True, verbose_name='Имя монтажника')     # Монтажник.

    objects = models.Manager()

    def __str__(self):
        return self.name
