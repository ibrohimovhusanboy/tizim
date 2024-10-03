# voting/views.py
from django.shortcuts import render, redirect
from .models import Candidate, Voter

import os
from .forms import UploadFileForm

def index(request):
    candidates = Candidate.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        candidate_id = request.POST.get('candidate_id')

        try:
            voter = Voter.objects.get(student_id=student_id)
            if voter.has_voted:
                return render(request, 'index.html', {'candidates': candidates, 'error': 'Siz allaqachon ovoz bergansiz.'})
            else:
                candidate = Candidate.objects.get(id=candidate_id)
                voter.vote = candidate
                voter.has_voted = True
                voter.save()
                return render(request, 'index.html', {'candidates': candidates, 'success': 'Ovoz muvaffaqiyatli berildi!'})
        except Voter.DoesNotExist:
            return render(request, 'index.html', {'candidates': candidates, 'error': 'Talaba ID raqami noto‘g‘ri.'})

    return render(request, 'index.html', {'candidates': candidates})

def upload_voters(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # Process the uploaded file
            if file.name.endswith('.txt'):
                # Read lines from the file and create voters
                for line in file:
                    student_id = line.decode('utf-8').strip()  # Remove whitespace and decode
                    if student_id:  # Ensure it's not empty
                        Voter.objects.get_or_create(student_id=student_id)
                return render(request, 'upload_success.html')  # Render a success template
            else:
                return render(request, 'upload_voters.html', {'form': form, 'error': 'File must be a .txt file.'})
    else:
        form = UploadFileForm()
    return render(request, 'upload_voters.html', {'form': form})