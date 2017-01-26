from django.shortcuts import render, redirect

from .models import Course

# Create your views here.
def index(request):
    context = {'courses':Course.objects.all()}
    print context
    return render(request, 'course/index.html', context)

def add_course(request):
    Course.objects.create(name=request.POST['course_name'],description=request.POST['course_description'])
    return redirect('/')

def drop_course(request, id):
    dropping = Course.objects.get(id = id)
    name = dropping.name
    description = dropping.description
    context = {'name': name, 'description':description, 'id':id}
    return render(request, 'course/drop.html', context)

def final_drop(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
