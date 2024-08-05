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


class ResourceCompetenceInLine(admin.TabularInline):
    model = models.ResourceCompetence
    extra = 0

class StampDirSubjInLine(admin.TabularInline):
    model = models.StampDirSubj
    extra = 0

class ExpertiseInLine(admin.StackedInline):
    model = models.Expertise
    extra = 0
    filter_horizontal = ['applicants']

class ResourceAdmin(admin.ModelAdmin):
    inlines = (ResourceCompetenceInLine, StampDirSubjInLine, ExpertiseInLine, )
    filter_horizontal = ['directions', 'subjects']

admin.site.register(models.Resource, ResourceAdmin)


class ExpertReportInLine(admin.StackedInline):
    model = models.ExpertReport
    extra = 0

class ExpertiseAdmin(admin.ModelAdmin):
    inlines = (ExpertReportInLine, )
    filter_horizontal = ['applicants']

admin.site.register(models.Expertise, ExpertiseAdmin)
