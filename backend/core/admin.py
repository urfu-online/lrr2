from django.contrib import admin

from . import models


admin.site.register(models.Direction)
admin.site.register(models.Department)
admin.site.register(models.Language)
admin.site.register(models.Platform)
admin.site.register(models.Subject)
admin.site.register(models.Rightholder)
admin.site.register(models.Ums)
admin.site.register(models.ExpertReportType)

admin.site.register(models.ExpertReport)
admin.site.register(models.Competence)


class ExpertiseInLine(admin.StackedInline):
    model = models.Expertise
    extra = 0
    filter_horizontal = ['applicants']

class ResourceStampApplicationInLine(admin.StackedInline):
    model = models.ResourceStampApplication
    extra = 0

class ResourceAdmin(admin.ModelAdmin):
    inlines = (ExpertiseInLine, ResourceStampApplicationInLine)
    filter_horizontal = ['directions', 'subjects', 'competences']

admin.site.register(models.Resource, ResourceAdmin)


class ExpertReportInLine(admin.StackedInline):
    model = models.ExpertReport
    extra = 0

class ExpertiseAdmin(admin.ModelAdmin):
    inlines = (ExpertReportInLine, )
    filter_horizontal = ['applicants']

admin.site.register(models.Expertise, ExpertiseAdmin)
