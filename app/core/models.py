from django.contrib.postgres import fields as postgres_fields
from django.db import models
from django.urls import reverse


class Direction(models.Model):
    title = models.CharField("Наименование", max_length=30)
    code = models.CharField("Код", max_length=8)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Direction_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Direction_update", args=(self.pk,))


class Department(models.Model):
    title = models.TextField()
    contacts = models.TextField("Контактные данные ответственного лица")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Department_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Department_update", args=(self.pk,))


class Language(models.Model):
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Language_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Language_update", args=(self.pk,))


class Platform(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    logo = models.ImageField(upload_to="upload/images/platform_logo")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Platform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Platform_update", args=(self.pk,))


class Passport(models.Model):

    directions = models.ManyToManyField(
        "core.Direction",
        verbose_name="Направления подготовки, для использования в рамках которых предназначен ЭОР",
        blank=True,
    )
    rightholder = models.ForeignKey(
        "core.Rightholder", verbose_name="Правообладатель ЭОР", on_delete=models.PROTECT
    )
    # competences = models.ManyToManyField("core.Competence", verbose_name="Перечень компетенций, в формировании которых участвует ЭОР", blank=True)
    department = models.ForeignKey(
        "core.Department",
        verbose_name="Подразделение-держатель ЭОР и контактные данные ответственного лица",
        on_delete=models.PROTECT,
    )
    subjects = models.ManyToManyField(
        "core.Subject",
        verbose_name="Дисциплины (модули), для использования в рамках которых предназначен ЭОР",
        blank=True,
    )
    platform = models.ForeignKey(
        "core.Platform",
        verbose_name="Платформа размещения ЭОР",
        on_delete=models.PROTECT,
    )
    language = models.ForeignKey(
        "core.Language", verbose_name="Язык контента ЭОР", on_delete=models.PROTECT
    )

    requirements = models.TextField("Минимальные системные требования")
    target = models.TextField("Целевая аудитория ЭОР")
    description = models.TextField("Аннотация ЭОР", blank=True, default="")
    structure = postgres_fields.ArrayField(
        models.TextField(),
        verbose_name="Перчень разделов (тем) ЭОР",
    )
    interactive = models.CharField(
        "Наличие в ЭОР интерактивных компонентов и степень их автоматизации",
        max_length=30,
    )
    prerequisites = models.TextField("Пререквизиты ЭОР")
    type = models.CharField("Вид ЭОР", max_length=4)
    results = postgres_fields.ArrayField(
        models.CharField(max_length=100), verbose_name="Результаты освоение ЭОР"
    )
    title = models.TextField("Наименование ЭОР")
    keywords = postgres_fields.ArrayField(
        models.CharField(max_length=100), verbose_name="Ключевые слова"
    )
    credits = models.PositiveSmallIntegerField("Трудоемкость освоения ЭОР")
    authors = postgres_fields.ArrayField(
        models.CharField(max_length=100), verbose_name="Авторы ЭОР"
    )

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Passport_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Passport_update", args=(self.pk,))


class Subject(models.Model):
    title = models.CharField("Наименование", max_length=255, db_index=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Subject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Subject_update", args=(self.pk,))


class Rightholder(models.Model):
    title = models.CharField(max_length=512)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Rightholder_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Rightholder_update", args=(self.pk,))


class StampSubject(models.Model):

    subject = models.ForeignKey("core.Subject", on_delete=models.PROTECT)
    direction = models.ForeignKey("core.Direction", on_delete=models.PROTECT)

    percentage = models.PositiveSmallIntegerField(default=0)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_StampSubject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_StampSubject_update", args=(self.pk,))


class Competence(models.Model):
    # Это справочник?

    stamp_subjects = models.ManyToManyField("core.StampSubject")
    passport = models.ForeignKey("core.Passport", on_delete=models.CASCADE)

    code = models.CharField("Код", max_length=8)
    title = models.TextField("Наименование")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Competence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Competence_update", args=(self.pk,))


class Stamp(models.Model):
    text = models.TextField()
    before_date = models.DateField()
    state = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Stamp_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Stamp_update", args=(self.pk,))


class Publication(models.Model):

    passport = models.ForeignKey("core.Passport", on_delete=models.CASCADE)

    state = models.BooleanField(default=False)
    isbn = models.CharField("ISBN", max_length=18)
    imprint = models.TextField("Выходные сведения")
    reg_num = models.PositiveIntegerField("Регистрационный номер")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_Publication_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_Publication_update", args=(self.pk,))
