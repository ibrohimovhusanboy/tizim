# voting/models.py
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    success = models.CharField(max_length=200)
    academic_level = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Voter(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    has_voted = models.BooleanField(default=False)
    vote = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.student_id
