from distutils.command.build import build
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class Classroom(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    period = models.CharField(max_length=64)
    teacher = models.CharField(max_length=64, default="- Teacher -")
    room = models.CharField(max_length=64, default="- Room -")
    building = models.CharField(max_length=64, default="- Building -")

    def __str__(self):
        return f"{self.name}, Period: {self.period}, Building: {self.building}, Room: {self.room}"

class Student(AbstractUser):

    class YearInSchool(models.TextChoices):
        CHOOSE = '', _('- Choose Grade -')
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')

    grade = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.CHOOSE,
    )

    classes = models.ManyToManyField(Classroom, blank=True , related_name="students")

    def __str__(self):
        return f"{self.username}, {self.grade}"