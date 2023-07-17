from django.apps import AppConfig


# from watson import search as watson

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    # def ready(self):
    #     YourModel = self.get_model("YourModel")
    #     watson.register(YourModel)
