from django_components import component

@component.register("publcard")
class Stampcard(component.Component):
    template_name = "publcard/publcard.html"

    def get_context_data(self, pas):
        return {
            "pas": pas,
        }

    # class Media:
    #     css = "calendar/calendar.css"
    #     js = "calendar/calendar.js"
