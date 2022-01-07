from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Job
from django.views import generic
from application.forms import ApplicationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 5) # 3 posta na kajdoi str
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    context = {
        'jobs': jobs,
        'page': page,
    }
    return render(request, 'index.html', context=context)


def job_details(request, pk):
    job_details = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        comment_form = ApplicationForm(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.job = job_details
            new_comment.save()
            return redirect('jobs')
    else:
        comment_form = ApplicationForm()
    return render(request, 'job_details.html', {'job_details': job_details,'comment_form': comment_form},)


def jobs(request):
    return render(request, 'jobs.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def base(request):
    return render(request, 'base.html')


# class ApplicationView(generic.FormView):
#     form_class = ApplicationForm
#     template_name = 'job_details.html'

#     def get_success_url(self):
#         return reverse("job_details")

#     def get(self, request, pk):
#         job_details = get_object_or_404(Job, pk=pk)
#         return render(request, self.template_name, {'job_details': job_details})

    
#     def post(self, request, pk):
#         job_details = get_object_or_404(Job, pk=pk)
#         form = ApplicationForm(request.POST)
#         if request.method == 'POST':
#             if form.is_valid():
#                 new_application = form.save(commit=False)
#                 new_application.application = job_details
#                 new_application.save()
#         else:
#             form = ApplicationForm()
        
#         return render(request, self.template_name, {'job_details': job_details, 'form': form})
    