from django import forms
from .models import (
    Projects,
    AboutMe,
    WorkExperience,
    Experience
)
class InputProjectsForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields=[
            "image_url",
            "tags",
            "title",
            "body"
        ]

class OutputProjectsForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields="__all__"

class AboutMeForm(forms.ModelForm):
    class Meta:
        model=AboutMe
        fields="__all__"

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        fields=[
            "title"
        ]

class OutputWorkExperienceForm(forms.ModelForm):
    experiences=ExperienceForm(many=True)
    class Meta:
        model=WorkExperience
        fields="__all__"

class InputWorkExperienceForm(forms.ModelForm):
    class Meta:
        model=WorkExperience
        fields="__all__"