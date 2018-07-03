from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
from apps.courses_app.models import Course


def index(request):
    print('on index')
    all_courses = Course.objects.all()
    print(all_courses)
    l = len(all_courses)
    for i in range(l):
        course = all_courses[i]
        print(course.name, course.description)
    context = {
        'all_courses': all_courses, 
    }

    return render(request, 'courses_app/index.html', context)


def add(request):
    
    
    request.session['name'] = request.POST['name']
    name = request.session['name']
    request.session['description'] = request.POST['description']
    description = request.session['description']
    print('went to add', request.session['name'], request.session['description'])
    # request.session['courses'] = Course.objects.all()
    Course.objects.create(name=name, description=description)
    course_added = Course.objects.last()
    print(course_added, course_added.name, course_added.description)
    # course = Course.objects.get(id=1)
    # print(course, course.name, course.description)
    return redirect('/')


def delete(request):
    print('went to delete')
    course_id = request.POST['confirm_delete']
    print(course_id)
    Course.objects.get(id = course_id).delete()


    return redirect('/')


def destroy(request, id):
    course_id = request.POST['course_id']
    course_name = request.POST['course_name']
    course_description = request.POST['course_description']

    print('on destroy', course_id, course_name, course_description)
    context = {
        'course_id': course_id,
        'course_name': course_name,
        'course_description': course_description,
    }


    return render(request, 'courses_app/destroy.html', context)
