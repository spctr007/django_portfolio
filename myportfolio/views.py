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
        context["portfolios"] = Portfolio.objects.filter(employee=1)
        return context


class PortfolioView(generic.DetailView):
    model = Portfolio
    template_name = "myportfolio/portfolio-details.html"
