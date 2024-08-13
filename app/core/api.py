import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)

api = NinjaAPI(renderer=ORJSONRenderer())


@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/math")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}
from . import models
from ninja import ModelSchema, Schema, Field
from typing import List

api = NinjaAPI(docs_url=None)


class PlatformSchema(ModelSchema):
    class Meta:
        model = models.Platform
        fields = "__all__"

@api.get("/platforms", response=List[PlatformSchema])
def platforms(request):
    qs = models.Platform.objects.all()
    return qs


class ResourceSchema(ModelSchema):
    class Meta:
        model = models.Resource
        fields = "__all__"

@api.get("/resources", response=List[ResourceSchema])
def resources(request):
    qs = models.Resource.objects.all()
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



# class DepartmentUniExportSchema(Schema):
#     name: str

# class PlatformUniExportSchema(Schema):
#     name: str

# class ModuleUniExportSchema(Schema):
#     module_code: str

# class ResourceStampModuleUniExportSchema(Schema):
#     id: int
#     # module_code: str = Field(..., alias="module.module_code")

# class ResourceUniExportSchema(Schema):
#     # resource_code: str
#     title: str
#     credits: int
#     department_name: str = Field(..., alias="department.name")
#     url: str
#     platform_name: str = Field(..., alias="platform.name")
#     stamp_applications: List[ModuleUniExportSchema]

# @api.get("/resources_uni_export", response=List[ResourceUniExportSchema])
# def resources_uni_export(request):
#     qs = models.Resource.objects.all()
#     return qs

# @api.get("/stamp_modules_uni_export", response=List[ResourceStampModuleUniExportSchema])
# def stamp_modules_uni_export(request):
#     qs = models.ResourceStampModule.objects.all()
#     return qs
