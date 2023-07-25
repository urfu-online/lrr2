from django.utils.translation import gettext_lazy as _

labels_data = {
    'HomeLabel': _('Каталог'),
    'MyEORLabel': _('Мои ЭОР'),
    'MyRequestsLabel': _('Мои заявки'),
    'MainTitle': _('Каталог ЭОР'),
}


def get_label(name):
    return labels_data.get(name, '')
