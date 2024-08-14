from django_components import component

@component.register("breadcrumbs")
class Breadcrumbs(component.Component):
    template_name = "breadcrumbs/breadcrumbs.html"

    def get_context_data(self, bcs):
        return {
            "bcs": bcs,
        }

    # class Media:
    #     css = "calendar/calendar.css"
    #     js = "calendar/calendar.js"