from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create
def create(request):
    if request.method == "POST":
        resume = Resume.objects.create(
            full_name=request.POST.get('full_name'),
            profile_picture=request.FILES.get('profile_picture'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            summary=request.POST.get('summary'),
            degree=request.POST.get('degree'),
            institute_name=request.POST.get('institute_name'),
            year_of_graduation=request.POST.get('year_of_graduation'),
            company_name=request.POST.get('company_name'),
            position=request.POST.get('position'),
            years_of_experience=request.POST.get('years_of_experience'),
            skills=request.POST.get('skills'),
            hobbies=request.POST.get('hobbies'),
            achievements=request.POST.get('achievements'),
        )
        resume.save()
        return redirect('read')
    
    return render(request, "create.html")


# Read
def read(request):
    resumes = Resume.objects.all()
    return render(request, "read.html", { 'resumes':resumes })


# Update
def update(request, id):
    resume = get_object_or_404(Resume, id=id)

    if request.method == "POST":
        resume.full_name = request.POST.get('full_name')
        
        if request.FILES.get('profile_picture'):
            resume.profile_picture = request.FILES.get('profile_picture')
            resume.email = request.POST.get('email')
            resume.phone = request.POST.get('phone')
            resume.address = request.POST.get('address')
            resume.summary = request.POST.get('summary')
            resume.degree = request.POST.get('degree')
            resume.institute_name = request.POST.get('institute_name')
            resume.year_of_graduation = request.POST.get('year_of_graduation')
            resume.company_name = request.POST.get('company_name')
            resume.position = request.POST.get('position')
            resume.years_of_experience = request.POST.get('years_of_experience')
            resume.skills = request.POST.get('skills')
            resume.hobbies = request.POST.get('hobbies')
            resume.achievements = request.POST.get('achievements')

        resume.save()
        return redirect('read')

    return render(request, "update.html", { 'resume': resume })


# Delete
def delete(request, id):
    resume = get_object_or_404(Resume, id=id)
    resume.delete()
    return redirect('read')



# View
def view(request, id):
    resume = get_object_or_404(Resume, id=id)
    return render(request, 'view.html', {'resume': resume})