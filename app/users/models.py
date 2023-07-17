import re

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_person(self):
        person = Person.objects.filter(user=self)
        try:
            return person.first()
        except MultipleObjectsReturned:
            raise person


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='person')

    location = models.CharField("Адрес проживания", max_length=150, null=True, blank=True)
    date_birthday = models.DateTimeField("Дата рождения", null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    middle_name = models.CharField("Отчество", max_length=100, null=True, blank=True)
    country = models.CharField("Страна", max_length=100, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=45, null=True, blank=True)
    avatar = models.ImageField("Изображение профиля", upload_to="upload/images/", null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    @property
    def short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    @property
    def full_name_display(self):
        full_name = f"{self.last_name if self.last_name else ''} {self.first_name if self.first_name else ''} {self.middle_name if self.middle_name else ''}"
        return re.sub(" +", " ", full_name)

    def get_absolute_url(self):
        return reverse("repository_Person_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Person_update", args=(self.pk,))

    @classmethod
    def get_or_create(cls, user):
        try:
            obj = cls.objects.get(user=user)
        except cls.DoesNotExist:
            obj = cls(user=user)
            obj.save()

        return obj

    @classmethod
    def get_person(cls, user):
        try:
            obj = cls.objects.get(user=user)
        except cls.DoesNotExist:
            obj = None
        return obj
