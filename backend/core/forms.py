from django import forms

from .models import (
    Competence,
    Department,
    Direction,
    Language,
    Passport,
    Platform,
    Rightholder,
    Stamp,
    StampSubject,
    Subject,
    Publication,
)


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = [
            "title",
            "code",
        ]


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "title",
            "contacts",
        ]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = [
            "title",
            "code",
        ]


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = [
            "title",
            "url",
            "logo",
        ]


class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = [
            "requirements",
            "target",
            "description",
            "structure",
            "interactive",
            "prerequisites",
            "type",
            "results",
            "title",
            "keywords",
            "credits",
            "authors",
            "directions",
            "rightholder",
            "competences",
            "department",
            "subjects",
            "platform",
            "language",
        ]

    def __init__(self, *args, **kwargs):
        super(PassportForm, self).__init__(*args, **kwargs)
        self.fields["directions"].queryset = Direction.objects.all()
        self.fields["rightholder"].queryset = Rightholder.objects.all()
        self.fields["competences"].queryset = Competence.objects.all()
        self.fields["department"].queryset = Department.objects.all()
        self.fields["subjects"].queryset = Subject.objects.all()
        self.fields["platform"].queryset = Platform.objects.all()
        self.fields["language"].queryset = Language.objects.all()


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            "title",
        ]


class RightholderForm(forms.ModelForm):
    class Meta:
        model = Rightholder
        fields = [
            "title",
        ]


class StampSubjectForm(forms.ModelForm):
    class Meta:
        model = StampSubject
        fields = [
            "percentage",
            "subject",
            "direction",
        ]

    def __init__(self, *args, **kwargs):
        super(StampSubjectForm, self).__init__(*args, **kwargs)
        self.fields["subject"].queryset = Subject.objects.all()
        self.fields["direction"].queryset = Direction.objects.all()


class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = [
            "code",
            "title",
            "stamp_subjects",
            "passport",
        ]

    def __init__(self, *args, **kwargs):
        super(CompetenceForm, self).__init__(*args, **kwargs)
        self.fields["stamp_subjects"].queryset = StampSubject.objects.all()
        self.fields["passport"].queryset = Passport.objects.all()


class StampForm(forms.ModelForm):
    class Meta:
        model = Stamp
        fields = [
            "text",
            "before_date",
            "state",
        ]


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = [
            "state",
            "isbn",
            "imprint",
            "reg_num",
            "passport",
        ]

    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)
        self.fields["passport"].queryset = Passport.objects.all()
