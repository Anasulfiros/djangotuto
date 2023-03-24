from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Departments,Doctors
from .forms import BookingForm,UserForm,UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form':form
    }
    return render(request,"booking.html",dict_form)

def doctors(request):
    dict_docs = {
        "doctors" : Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_docs)

def department(request):
    dict_dept = {
        "dept":Departments.objects.all()
    }
    return render(request,"department.html",dict_dept)


@login_required
def special(request):
    return HttpResponse('You are logged in , Nice !')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("Someone tried to login and failed !")
            print("Username : {} and Password : {}".format(username,password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'login.html')