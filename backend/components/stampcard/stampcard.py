from django_components import component

@component.register("stampcard")
class Stampcard(component.Component):
    template_name = "stampcard/stampcard.html"

    def get_context_data(self, pas):
        return {
            "pas": pas,
        }

    # class Media:
    #     css = "calendar/calendar.css"
    #     js = "calendar/calendar.js"
