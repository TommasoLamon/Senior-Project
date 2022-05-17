from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Classroom, Student
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        tmp = request.user.classes.all()
        print(request.user.classes.all())

        context = {
           'classes': tmp 
        }

        return render(request, "main/index.html", context)
    else:
        return redirect("/login")
@login_required(login_url=("/login"))
def contacts(request):
    return render(request, "main/contacts.html")

def profile(request):
    if request.user.is_authenticated:
        return render(request, "main/profile.html")
    else:
        return redirect("/login")

@login_required(login_url=("/login"))
def classroom(request, class_id):
    class_var = Classroom.objects.get(id = class_id)
    students = class_var.students.all()

    context = {
        'class': class_var,
        'students': students
    }

    return render(request, "main/classroom.html", context)

@login_required(login_url=("/login"))
def enroll(request, class_id):
    if request.method == "GET":
        class_var = Classroom.objects.get(pk = class_id)
        user = Student.objects.get(pk = request.user.id)
        user.classes.add(class_var)
        print(user.classes.all())
        return redirect("index")

@login_required(login_url=("/login"))
def drop(request, class_id):
    if request.method == "GET":
        class_var = Classroom.objects.get(pk = class_id)
        user = Student.objects.get(pk = request.user.id)
        user.classes.remove(class_var)
        print(user.classes.all())
        return redirect("index")


def search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = request.POST['query']
            results = Classroom.objects.filter(name__contains=form)
            if not results:
                results = Classroom.objects.filter(teacher__contains=form)

            context = {
                'results': results,
                'search': form
            }

            return render(request, "main/search.html", context)

    else:
        return redirect("/login")


@login_required(login_url=("/login"))
def explore(request):

    classes = Classroom.objects.all()
    user = Student.objects.get(pk = request.user.id)
    user_classes = user.classes.all()

    context = {
        'classes': classes,
        'already_in': user_classes
    }

    return render(request, "main/explore.html", context)

def friends(request, class_id):
    class_var = Classroom.objects.get(pk = class_id)
    student_list = class_var.students.all()

    context = {
        'friends': student_list
    }

    return render(request, "main/participants.html", context)
