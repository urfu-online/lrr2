from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/math")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}