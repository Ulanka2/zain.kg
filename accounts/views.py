from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def jobs(request):
    return render(request, 'jobs.html')

def candidate(request):
    return render(request, 'candidate.html')

def job_details(request):
    return render(request, 'job_details.html')

def blog(request):
    return render(request, 'blog.html')