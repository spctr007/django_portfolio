from django.contrib import admin

from .models import Employee, Portfolio, Skill, Testimonial

admin.site.register(Employee)
admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Testimonial)
