# voting/admin.py
from django.contrib import admin
from .models import Candidate, Voter

admin.site.register(Candidate)
admin.site.register(Voter)
