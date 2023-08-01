# Generated by Django 4.2.3 on 2023-08-01 02:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('contacts', models.TextField(verbose_name='Контактные данные ответственного лица')),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Наименование')),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirements', models.TextField(verbose_name='Минимальные системные требования')),
                ('target', models.TextField(verbose_name='Целевая аудитория ЭОР')),
                ('description', models.TextField(blank=True, default='', verbose_name='Аннотация ЭОР')),
                ('structure', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None, verbose_name='Перчень разделов (тем) ЭОР')),
                ('interactive', models.CharField(max_length=30, verbose_name='Наличие в ЭОР интерактивных компонентов и степень их автоматизации')),
                ('prerequisites', models.TextField(verbose_name='Пререквизиты ЭОР')),
                ('type', models.CharField(max_length=4, verbose_name='Вид ЭОР')),
                ('results', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None, verbose_name='Результаты освоение ЭОР')),
                ('title', models.TextField(verbose_name='Наименование ЭОР')),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None, verbose_name='Ключевые слова')),
                ('credits', models.PositiveSmallIntegerField(verbose_name='Трудоемкость освоения ЭОР')),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None, verbose_name='Авторы ЭОР')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.department', verbose_name='Подразделение-держатель ЭОР и контактные данные ответственного лица')),
                ('directions', models.ManyToManyField(blank=True, to='core.direction', verbose_name='Направления подготовки, для использования в рамках которых предназначен ЭОР')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.language', verbose_name='Язык контента ЭОР')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('logo', models.ImageField(upload_to='upload/images/platform_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Rightholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('before_date', models.DateField()),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='StampSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveSmallIntegerField(default=0)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.direction')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
                ('isbn', models.CharField(max_length=18, verbose_name='ISBN')),
                ('imprint', models.TextField(verbose_name='Выходные сведения')),
                ('reg_num', models.PositiveIntegerField(verbose_name='Регистрационный номер')),
                ('passport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.passport')),
            ],
        ),
        migrations.AddField(
            model_name='passport',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.platform', verbose_name='Платформа размещения ЭОР'),
        ),
        migrations.AddField(
            model_name='passport',
            name='rightholder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.rightholder', verbose_name='Правообладатель ЭОР'),
        ),
        migrations.AddField(
            model_name='passport',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='core.subject', verbose_name='Дисциплины (модули), для использования в рамках которых предназначен ЭОР'),
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
                ('title', models.TextField(verbose_name='Наименование')),
                ('passport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.passport')),
                ('stamp_subjects', models.ManyToManyField(to='core.stampsubject')),
            ],
        ),
    ]