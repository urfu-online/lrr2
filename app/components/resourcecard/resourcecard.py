from django_components import component

@component.register("resourcecard")
class Resourcecard(component.Component):
    template_name = "resourcecard/resourcecard.html"

    def get_context_data(self, res):
        return {
            "res": res,
        }

    # class Media:
    #     css = "calendar/calendar.css"
    #     js = "calendar/calendar.js"