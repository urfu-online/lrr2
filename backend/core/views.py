from django.shortcuts import render

from lrr.labels import get_label

# Create your views here.


def catalog(request):

    return render(
        request,
        "catalog.html",
        {
            "breadcrumbs": [
                {"name": get_label("HomeLabel"), "url": "", "active": True},
            ],
            "passports": [
                {
                    "id": 1,
                    "type": "Электронный учебный курс",
                    "title": "Основы проектирования интерфейсов",
                    "descr": 'Электронный учебный курс по дисциплине "Основы проектирования интерфейсов"',
                    "platform_logo": "img/hm_logo.png",
                    "platform_name": "Гиперметод",
                    "url": "https://learn.urfu.ru/subject/index/card/subject_id/5284",
                },
                {
                    "id": 2,
                    "type": "Онлайн-курс",
                    "title": "Философия",
                    "descr": "Философия представлена технологиями мышления, которые позволяют ясно мыслить мировоззрение, коммуникацию, свободу выбора, ценности. «Все люди - философы», именно эта фраза Карла Поппера легла в основу создания курса...",
                    "platform_logo": "img/npoo_logo.png",
                    "platform_name": "НПОО",
                    "url": "#",
                },
            ],
        },
    )


def passport(request, passport_id):

    return render(
        request,
        "passport.html",
        {
            "breadcrumbs": [
                {"name": get_label("HomeLabel"), "url": "/", "active": False},
                {
                    "name": "ЭУК" + " " + '"Основы проектирования интерфейсов"',
                    "url": "",
                    "active": False,
                },
                {"name": "Паспорт ЭОР", "url": "", "active": True},
            ],
            "passport": {
                "id": 1,
                "type": "Электронный учебный курс",
                "title": "Основы проектирования интерфейсов",
                "authors": "Карасик А.А.",
                "descr": 'Электронный учебный курс по дисциплине "Основы проектирования интерфейсов"',
                "description": "<ul><li>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.</li><li>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.</li></ul>",
                "prerequisites": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "target": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "direction_tags": [
                    {"name": "Программная инженерия"},
                    {"name": "Прикладная информатика"},
                ],
                "subject_tags": [
                    {"name": "Основы проектирования интерфейсов"},
                    {"name": "Проектирование человеко-машинных интерфейсов"},
                ],
                "competences": [
                    {
                        "name": "Lorem, ipsum dolor sit amet consectetur adipisicing elit"
                    },
                    {
                        "name": "Lorem, ipsum dolor sit amet consectetur adipisicing elit"
                    },
                ],
                "structure": "<ul><li>Lorem, ipsum dolor sit amet consectetur adipisicing elit.</li><li>Lorem, ipsum dolor sit amet consectetur adipisicing elit. </li></ul>",
                "interactive": "Имеются, частично автоматизированы",
                "keywords": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "result_edu": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "credits": "3 з.е.",
                "language": "русский",
                "requirements": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "copyright_holder": 'ФГАОУ ВО "Уральский федеральный университет имнеи первого Президента России Б.Н. Ельцина"',
                "department": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "platform_logo": "img/hm_logo.png",
                "platform_name": "Гиперметод",
                "platform_url": "https://learn.urfu.ru",
                "url": "https://learn.urfu.ru/subject/index/card/subject_id/5284",
                "access_mode": "с аутентификацией пользователя, с ограниченным доступом",
                "resource_state": "Активный",
                "passport_state": "Утвержден",
                "stamp_state": True,
                "stamp_type": "Гриф ЭОР",
                "stamp_before_date": "23.04.2024",
                "stamp_text": 'Рекомендовано Методическим советом УрФУ в качестве электронного учебного курса для студентов, обучающихся по направлению подготовки "Прикладная информатика"',
                "stamp_subjects": [
                    {
                        "subject": "Основы проектирования интерфейсов",
                        "direction": "Программная инженерия",
                        "percentage": "100%",
                    },
                    {
                        "subject": "Проектирование человеко-машинных интерфейсов",
                        "direction": "Прикладная информатика",
                        "percentage": "100%",
                    },
                ],
                "publication_state": True,
                "publication_imprint": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Magni, consectetur eveniet? Voluptas sunt praesentium tenetur? Itaque quam veniam ipsa odit ullam suscipit ducimus molestias qui, iure, ab vero! Excepturi, accusamus.",
                "publication_isbn": "978-5-386-01614-2",
                "publication_reg_num": "9231",
            },
        },
    )


def myresources(request):

    return render(
        request,
        "myresources.html",
        {
            "breadcrumbs": [
                {"name": get_label("MyEORLabel"), "url": "", "active": True},
            ],
        },
    )


def myrequests(request):

    return render(
        request,
        "myrequests.html",
        {
            "breadcrumbs": [
                {"name": get_label("MyRequestsLabel"), "url": "", "active": True},
            ],
        },
    )
