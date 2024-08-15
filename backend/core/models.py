from django.db import models


class Direction(models.Model):
    DEGREES_CHOICES = (
        ("бакалавриат", "бакалавриат"),
        ("специалитет", "специалитет"),
        ("магистратура", "магистратура"),
        ("аспирантура", "аспирантура"),
    )
    code = models.CharField("Код направления подготовки", max_length=8, blank=True)
    name = models.CharField("Наименование направления подготовки", max_length=255)
    degree = models.CharField("Уровень образования направления подготовки", max_length=12, choices=DEGREES_CHOICES)

    def merged_name(self):
        if self.code:
            code = self.code
        else:
            code = ""
        return (code + " " + self.name + " (" + self.degree + ")").strip()

    def __str__(self):
        if self.code:
            code = self.code
        else:
            code = ""
        return (code + " " + self.name + " (" + self.degree + ")").strip()

    class Meta:
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"


class Department(models.Model):
    name = models.CharField("Наименование подразделения", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


class Language(models.Model):
    name = models.CharField("Наименование языка", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


class Platform(models.Model):
    name = models.CharField("Наименование платформы", max_length=255)
    url = models.URLField("URL платформы")
    logo = models.ImageField("Логотип платформы", upload_to="platform_logo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Платформа"
        verbose_name_plural = "Платформы"


class Subject(models.Model):
    name = models.CharField("Наименование дисциплины", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Rightholder(models.Model):
    name = models.CharField("Наименование правообладателя", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Правообладатель"
        verbose_name_plural = "Правообладатели"


class Competence(models.Model):
    name = models.TextField("Наименование компетенции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"


class Resource(models.Model):
    resource_code = models.CharField("Код ЭОР", max_length=10, unique=True, blank=True)
    TYPE_CHOICES = (
        ("Электронный образовательный контент", "Электронный образовательный контент"),
        ("Электронный учебный курс", "Электронный учебный курс"),
        ("Онлайн-курс", "Онлайн-курс"),
    )
    type = models.CharField("Вид ЭОР", max_length=35, choices=TYPE_CHOICES)
    title = models.TextField("Наименование ЭОР")
    authors_text = models.TextField("Авторы ЭОР")
    description = models.TextField("Аннотация ЭОР")
    prerequisites = models.TextField("Пререквизиты ЭОР", blank=True)
    target = models.TextField("Целевая аудитория ЭОР", blank=True)
    directions = models.ManyToManyField(
        Direction,
        verbose_name="Направления подготовки, для использования в рамках которых предназначен ЭОР",
        blank=True,
    )
    subjects = models.ManyToManyField(
        Subject,
        verbose_name="Дисциплины (модули), для использования в рамках которых предназначен ЭОР",
        blank=True,
    )
    competences = models.ManyToManyField(
        Competence,
        verbose_name="Компетенции, в формировании которых участвует ЭОР",
        blank=True,
    )
    structure = models.TextField("Перчень разделов (тем) ЭОР", blank=True)
    INTERACTIVE_CHOICES = (
        ("Все интерактивные компоненты автоматизированы", "Все интерактивные компоненты автоматизированы"),
        ("Некоторые интерактивные компоненты требуют участия преподавателя", "Некоторые интерактивные компоненты требуют участия преподавателя"),
        ("Интерактивные компоненты отсутствуют", "Интерактивные компоненты отсутствуют"),
    )
    interactive = models.CharField(
        "Наличие в ЭОР интерактивных компонентов и степень их автоматизации",
        max_length=64,
        choices=INTERACTIVE_CHOICES
    )
    keywords = models.TextField("Ключевые слова", blank=True)
    results = models.TextField("Результаты освоения ЭОР", blank=True)
    credits = models.PositiveSmallIntegerField("Трудоемкость освоения ЭОР", blank=True, null=True)
    language = models.ForeignKey(
        Language, verbose_name="Язык контента ЭОР", on_delete=models.PROTECT, blank=True, null=True
    )
    requirements = models.TextField("Минимальные системные требования", blank=True)
    rightholder = models.ForeignKey(
        Rightholder, verbose_name="Правообладатель ЭОР", on_delete=models.PROTECT
    )
    department = models.ForeignKey(
        Department,
        verbose_name="Подразделение-держатель ЭОР",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    contacts = models.TextField("Контактные данные ответственного лица", blank=True)
    platform = models.ForeignKey(
        Platform,
        verbose_name="Платформа размещения ЭОР",
        on_delete=models.PROTECT
    )
    ACCESS_MODE_CHOICES = (
        ("анонимный, открытый", "анонимный, открытый"),
        ("анонимный, ограниченный (прямой ссылкой)", "анонимный, ограниченный (прямой ссылкой)"),
        ("с аутентификацией пользователя, с открытой регистрацией", "с аутентификацией пользователя, с открытой регистрацией"),
        ("с аутентификацией пользователя, с ограниченным доступом", "с аутентификацией пользователя, с ограниченным доступом"),
    )
    access_mode = models.CharField(
        "Режим доступа",
        max_length=55,
        choices=ACCESS_MODE_CHOICES
    )
    url = models.URLField("URL ЭОР")
    RESOURCE_STATE_CHOICES = (
        ("Активный", "Активный"),
        ("Архивный", "Архивный"),
    )
    resource_state = models.CharField(
        "Состояние ЭОР",
        max_length=8,
        choices=RESOURCE_STATE_CHOICES,
        default="Активный"
    )
    PASSPORT_STATE_CHOICES = (
        ("Утвержден", "Утвержден"),
        ("Не утвержден", "Не утвержден"),
    )
    passport_state = models.CharField(
        "Состояние Паспорта ЭОР",
        max_length=12,
        choices=PASSPORT_STATE_CHOICES,
        default="Не утвержден"
    )
    STAMP_STATE_CHOICES = (
        ("Имеется", "Имеется"),
        ("Отсутствует", "Отсутствует"),
    )
    stamp_state = models.CharField(
        "Гриф ЭОР",
        max_length=11,
        choices=STAMP_STATE_CHOICES,
        default="Отсутствует"
    )
    stamp_text = models.TextField("Текст Грифа ЭОР", blank=True)
    stamp_date = models.DateField("Дата присвоения Грифа ЭОР", blank=True, null=True)
    stamp_expiration = models.DateField("Дата истечения срока действия Грифа ЭОР", blank=True, null=True)
    PUB_STATE_CHOICES = (
        ("Является изданием", "Является изданием"),
        ("Не является изданием", "Не является изданием"),
    )
    pub_state = models.CharField(
        "Статус издания",
        max_length=20,
        choices=PUB_STATE_CHOICES,
        default="Не является изданием"
    )
    pub_imprint = models.TextField("Выходные сведения издания", blank=True)
    pub_isbn = models.CharField("ISBN издания", max_length=17, blank=True)
    pub_regnum = models.CharField("Регистрационный номер издания", max_length=10, blank=True)
    notes = models.TextField("Примечания (не публикуются в Паспорте ЭОР)", blank=True)

    def __str__(self):
        return self.resource_code + " " + self.title

    class Meta:
        verbose_name = "ЭОР"
        verbose_name_plural = "ЭОРы"


class Ums(models.Model):
    name = models.CharField("Наименование УМС института", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "УМС института"
        verbose_name_plural = "УМС института"


class Expertise(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT, verbose_name="ЭОР")
    ums = models.ForeignKey(Ums, on_delete=models.PROTECT, verbose_name="УМС института", blank=True, null=True)
    applicants = models.ManyToManyField("users.Person", verbose_name="Заявитель", blank=True)
    applicant_contacts = models.TextField("Контактные данные заявителя", blank=True)
    expert_access_details = models.TextField("Режим доступа к ЭОР для эксперта", blank=True)
    TYPE_CHOICES = (
        ("Полная", "Полная"),
        ("Расширение области применения", "Расширение области применения"),
        ("Отзыв Грифа МС", "Отзыв Грифа МС"),
    )
    type = models.CharField("Вид экспертизы ЭОР", max_length=29, choices=TYPE_CHOICES)
    application_date = models.DateField("Дата заявки", blank=True, null=True)
    STATE_CHOICES = (
        ("В процессе", "В процессе"),
        ("Завершена (положительный результат)", "Завершена (положительный результат)"),
        ("Завершена (отрицательный результат)", "Завершена (отрицательный результат)"),
    )
    state = models.CharField(
        "Состояние экспертизы",
        max_length=35,
        choices=STATE_CHOICES,
        default="В процессе"
    )
    notes = models.TextField("Примечания", blank=True)


    def __str__(self):
        return self.resource.title + " (" + self.type + ")"

    class Meta:
        verbose_name = "Экспертиза ЭОР"
        verbose_name_plural = "Экспертизы ЭОР"


class ResourceStampApplication(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT, verbose_name="ЭОР")
    direction = models.ForeignKey(Direction, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Направление подготовки")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Дисциплина")
    module_code = models.CharField("Код модуля", max_length=7, blank=True)
    percentage = models.PositiveSmallIntegerField("Процент соответствия")
    expertise = models.ForeignKey(Expertise, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Экспертиза ЭОР")

    def application_models(self):
        if self.percentage >= 100 and self.resource.interactive == "Все интерактивные компоненты автоматизированы":
            return ["Модель 2", "Модель 3"]
        else:
            return ["Модель 1", "Модель 4", "Модель 5"]

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Соответвствие ЭОР направлению, дисциплине и модулю, установленное Грифом ЭОР"
        verbose_name_plural = "Соответвствия ЭОР направлениям, дисциплинам и модулям, установленные Грифом ЭОР"


class ExpertReportType(models.Model):
    name = models.CharField("Наименование вида экспертного заключения", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид экспертного заключения"
        verbose_name_plural = "Виды экспертного заключения"


class ExpertReport(models.Model):
    expertise = models.ForeignKey(Expertise, on_delete=models.PROTECT, verbose_name="Экспертиза ЭОР")
    type = models.ForeignKey(ExpertReportType, on_delete=models.PROTECT, verbose_name="Вид экспертного заключения")
    expert = models.ForeignKey("users.Person", on_delete=models.PROTECT, verbose_name="Эксперт", blank=True, null=True)
    expert_contacts = models.TextField("Контактные данные эксперта", blank=True)
    report_pdf = models.FileField("Файл экспертного заключения в PDF", upload_to="reports", blank=True, null=True)
    report_doc = models.FileField("Файл экспертного заключения в DOC", upload_to="reports", blank=True, null=True)
    notes = models.TextField("Примечания", blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Экспертное заключение"
        verbose_name_plural = "Экспертные заключения"

