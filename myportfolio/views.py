from django.shortcuts import render
from django.views import generic

from myportfolio.models import Employee, Portfolio, Skill


class IndexView(generic.ListView):
    template_name = "myportfolio/index.html"
    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.filter(employee=1)
        context['skills_midcount'] = round(Skill.objects.count() / 2)
        context["skills_count"] = Skill.objects.filter(employee=1).count()
        return context


class PortfolioView(generic.ListView):
    template_name = "myportfolio/portfolio-details.html"

    def get_queryset(self):
        return Portfolio.objects.all()
