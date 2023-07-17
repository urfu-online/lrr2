from django_components import component
from rolepermissions.roles import get_user_roles
from django.contrib.auth.models import AnonymousUser
import logging

logger = logging.getLogger(__name__)

@component.register("navbar")
class Calendar(component.Component):
    template_name = "navbar/navbar.html"

    def get_context_data(self, user):
        if user.is_anonymous:
            user = None
        return {
            "user": user,
            "role": get_user_roles(user)
        }

    # class Media:
    #     css = "calendar/calendar.css"
    #     js = "calendar/calendar.js"