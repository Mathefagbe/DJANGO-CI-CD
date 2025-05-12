from django.shortcuts import render
from django.views.generic import ListView,DetailView,View,TemplateView
from .models import Projects,Skills

class ListGetView(ListView,DetailView):
    pass

# Create your views here.

class HomeView(TemplateView):
    template_name="home.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
    

class ProjectView(ListView):
    model=Projects
    template_name="projects.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["projects"]=self.get_queryset()
        context["skills"]=Skills.objects.all()
        return context

