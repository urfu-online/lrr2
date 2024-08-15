import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer

from . import models
from ninja import ModelSchema, Schema, Field
from typing import List, Optional

from datetime import date


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)

api = NinjaAPI(renderer=ORJSONRenderer(), docs_url=None)


class DepartmentSchema(Schema):
    id: int
    name: str
    value: str = Field(..., alias="name")
    label: str = Field(..., alias="name")

@api.get("/departments", response=List[DepartmentSchema])
def departments(request):
    qs = models.Department.objects.all()
    return qs


class DirectionSchema(Schema):
    id: int
    code: str
    name: str
    degree: str
    merged_name: str
    value: str = Field(..., alias="merged_name")
    label: str = Field(..., alias="merged_name")

@api.get("/directions", response=List[DirectionSchema])
def directions(request):
    qs = models.Direction.objects.all()
    return qs


class PlatformSchema(Schema):
    id: int
    name: str
    url: str
    logo: str
    value: str = Field(..., alias="name")
    label: str = Field(..., alias="name")

@api.get("/platforms", response=List[PlatformSchema])
def platforms(request):
    qs = models.Platform.objects.all()
    return qs


class SubjectSchema(Schema):
    id: int
    name: str
    value: str = Field(..., alias="name")
    label: str = Field(..., alias="name")

@api.get("/subjects", response=List[SubjectSchema])
def subjects(request):
    qs = models.Subject.objects.all()
    return qs


class CompetenceSchema(Schema):
    name: str

class LanguageSchema(ModelSchema):
    class Meta:
        model = models.Language
        fields = "__all__"

class RightholderSchema(ModelSchema):
    class Meta:
        model = models.Rightholder
        fields = "__all__"

class ResourceSchema(Schema):
    id: int
    resource_code: str
    type: str
    title: str
    authors_text: str
    description: str
    prerequisites: str
    target: str
    directions: List[DirectionSchema]
    subjects: List[SubjectSchema]
    competences: List[CompetenceSchema]
    structure: str
    interactive: str
    keywords: str
    results: str
    credits: int
    language: LanguageSchema
    requirements: str
    rightholder: RightholderSchema
    department: DepartmentSchema
    contacts: str
    platform: PlatformSchema
    access_mode: str
    url: str
    resource_state: str
    passport_state: str
    stamp_state: str
    stamp_text: str
    stamp_expiration: Optional[date] = None
    pub_state: str
    pub_imprint: str
    pub_isbn: str
    pub_regnum: str

@api.get("/resources", response=List[ResourceSchema])
def resources(request):
    qs = models.Resource.objects.all()
    return qs


class ResourceStampApplicationSchema(Schema):
    resource_id: int = Field(..., alias="resource.pk")
    direction: DirectionSchema
    subject: SubjectSchema
    module_code: str
    percentage: int
    
@api.get("/resource_stamp_applications", response=List[ResourceStampApplicationSchema])
def resource_stamp_applications(request):
    qs = models.ResourceStampApplication.objects.all()
    return qs


class ResourceApplicationUniExportSchema(Schema):
    resource_type: str = Field(..., alias="resource.type")
    resource_title: str = Field(..., alias="resource.title")
    resource_credits: int = Field(..., alias="resource.credits")
    resource_department_name: str = Field(..., alias="resource.department.name")
    resource_url: str = Field(..., alias="resource.url")
    resource_platform_name: str = Field(..., alias="resource.platform.name")
    module_code: str
    subject_name: str = Field(..., alias="subject.name")
    application_models: List[str]

@api.get("/resource_application_uni_export", response=List[ResourceApplicationUniExportSchema])
def resource_application_uni_export(request):
    qs = models.ResourceStampApplication.objects.all()
    return qs
