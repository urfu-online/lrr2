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