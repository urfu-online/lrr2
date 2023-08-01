from django import forms
from django.contrib import admin

from . import models


class DirectionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Direction
        fields = "__all__"


class DirectionAdmin(admin.ModelAdmin):
    form = DirectionAdminForm
    list_display = [
        "title",
        "code",
    ]


class DepartmentAdminForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = "__all__"


class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm
    list_display = [
        "title",
        "contacts",
    ]


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = "__all__"


class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    list_display = [
        "title",
        "code",
    ]


class PlatformAdminForm(forms.ModelForm):
    class Meta:
        model = models.Platform
        fields = "__all__"


class PlatformAdmin(admin.ModelAdmin):
    form = PlatformAdminForm
    list_display = [
        "title",
        "url",
        "logo",
    ]


class PassportAdminForm(forms.ModelForm):
    class Meta:
        model = models.Passport
        fields = "__all__"


class PassportAdmin(admin.ModelAdmin):
    form = PassportAdminForm
    list_display = [
        "requirements",
        "target",
        "description",
        "structure",
        "interactive",
        "prerequisites",
        "type",
        "results",
        "title",
        "keywords",
        "credits",
        "authors",
    ]


class SubjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = "__all__"


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = [
        "title",
    ]


class RightholderAdminForm(forms.ModelForm):
    class Meta:
        model = models.Rightholder
        fields = "__all__"


class RightholderAdmin(admin.ModelAdmin):
    form = RightholderAdminForm
    list_display = [
        "title",
    ]


class StampSubjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.StampSubject
        fields = "__all__"


class StampSubjectAdmin(admin.ModelAdmin):
    form = StampSubjectAdminForm
    list_display = [
        "percentage",
    ]


class CompetenceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Competence
        fields = "__all__"


class CompetenceAdmin(admin.ModelAdmin):
    form = CompetenceAdminForm
    list_display = [
        "code",
        "title",
    ]


class StampAdminForm(forms.ModelForm):
    class Meta:
        model = models.Stamp
        fields = "__all__"


class StampAdmin(admin.ModelAdmin):
    form = StampAdminForm
    list_display = [
        "text",
        "before_date",
        "state",
    ]


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = models.Publication
        fields = "__all__"


class PublicationAdmin(admin.ModelAdmin):
    form = PublicationAdminForm
    list_display = [
        "state",
        "isbn",
        "imprint",
        "reg_num",
    ]


admin.site.register(models.Direction, DirectionAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Platform, PlatformAdmin)
admin.site.register(models.Passport, PassportAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Rightholder, RightholderAdmin)
admin.site.register(models.StampSubject, StampSubjectAdmin)
admin.site.register(models.Competence, CompetenceAdmin)
admin.site.register(models.Stamp, StampAdmin)
admin.site.register(models.Publication, PublicationAdmin)
