from django.shortcuts import redirect, render
from .forms import RegisterForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }

    return render(request, "registration/register.html", context)


@login_required(login_url=("/login"))
def edit_view(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('/profile')
    else:
        form = UpdateUserForm(instance=request.user)
        context = {
            'form': form
        }

        return render(request, "registration/edit.html", context)