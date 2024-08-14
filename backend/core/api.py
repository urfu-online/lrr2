import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer

from . import models
from ninja import ModelSchema, Schema, Field
from typing import List


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)

api = NinjaAPI(renderer=ORJSONRenderer())
# api = NinjaAPI(docs_url=None)


class DepartmentSchema(ModelSchema):
    class Meta:
        model = models.Department
        fields = "__all__"

@api.get("/departments", response=List[DepartmentSchema])
def departments(request):
    qs = models.Department.objects.all()
    return qs


class DirectionSchema(ModelSchema):
    class Meta:
        model = models.Direction
        fields = "__all__"

@api.get("/directions", response=List[DirectionSchema])
def directions(request):
    qs = models.Direction.objects.all()
    return qs


class LanguageSchema(ModelSchema):
    class Meta:
        model = models.Language
        fields = "__all__"

@api.get("/languages", response=List[LanguageSchema])
def languages(request):
    qs = models.Language.objects.all()
    return qs


class PlatformSchema(ModelSchema):
    class Meta:
        model = models.Platform
        fields = "__all__"

@api.get("/platforms", response=List[PlatformSchema])
def platforms(request):
    qs = models.Platform.objects.all()
    return qs


class ResourceCompetenceSchema(Schema):
    resource_id: int = Field(..., alias="resource.pk")
    competence: str

@api.get("/resource_competences", response=List[ResourceCompetenceSchema])
def resource_competences(request):
    qs = models.ResourceCompetence.objects.all()
    return qs


class ResourceSchema(ModelSchema):
    class Meta:
        model = models.Resource
        fields = "__all__"

@api.get("/resources", response=List[ResourceSchema])
def resources(request):
    qs = models.Resource.objects.all()
    return qs


class ResourceStampApplicationSchema(ModelSchema):
    class Meta:
        model = models.ResourceStampApplication
        fields = "__all__"

@api.get("/resource_stamp_applications", response=List[ResourceStampApplicationSchema])
def resource_stamp_applications(request):
    qs = models.ResourceStampApplication.objects.all()
    return qs


class RightholderSchema(ModelSchema):
    class Meta:
        model = models.Rightholder
        fields = "__all__"

@api.get("/rightholders", response=List[RightholderSchema])
def rightholders(request):
    qs = models.Rightholder.objects.all()
    return qs


class SubjectSchema(ModelSchema):
    class Meta:
        model = models.Subject
        fields = "__all__"

@api.get("/subjects", response=List[SubjectSchema])
def subjects(request):
    qs = models.Subject.objects.all()
    return qs


class ModuleResourceApplicationUniExportSchema(Schema):
    module_code: str
    resource_type: str = Field(..., alias="resource.type")
    resource_title: str = Field(..., alias="resource.title")
    resource_credits: int = Field(..., alias="resource.credits")
    resource_department_name: str = Field(..., alias="resource.department.name")
    resource_url: str = Field(..., alias="resource.url")
    resource_platform_name: str = Field(..., alias="resource.platform.name")
    subject_name: str = Field(..., alias="subject.name")
    application_models: List[str]

@api.get("/module_resource_appl_uni_export", response=List[ModuleResourceApplicationUniExportSchema])
def module_resource_appl_uni_export(request):
    qs = models.ResourceStampApplication.objects.all()
    return qs
