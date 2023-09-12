from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



from user.forms import BaseUserForm, LoginForm

# Create your views here.



def register(request):

    context = {

        'title': 'Register',

        'form': BaseUserForm()

    }

    if request.method == 'POST':

        if request.POST['password'] != request.POST['confirm_password']:

            context['error'] = 'Passwords do not match'

            return render(request, 'register.html', context)

        else:

            form = BaseUserForm(request.POST, request.FILES)

            if form.is_valid():

                user = form.save()

                user.set_password(user.password)

                user.save()

                return redirect('home')

    return render(request, 'register.html', context)



def login(request):

    context = {

        'title': 'Login',

        'form': LoginForm()



    }

    if request.method == 'POST':

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:

            auth_login(request, user)

            return redirect('home')

        else:

            context['error'] = 'Username or password is incorrect'

    return render(request, 'login.html', context)



def logout_view(request):

    auth_logout(request)

    return redirect('home')