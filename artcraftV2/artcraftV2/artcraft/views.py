from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class homeView(View):
    def get(self, request):
        
        return render(request, 'home.html')

class aboutView(View):
    def get(self, request):
        
        return render(request, 'about.html')

class artworkView(View):
    def get(self, request):
        
        return render(request, 'artwork.html')

class contactView(View):
    def get(self, request):
        
        return render(request, 'contact.html')      

class dashboardView(View):
    def get(self, request):
        qs_artist = Artist.objects.all()
        qs_customer = Customer.objects.all()
    
        context = {
            'artist' : qs_artist,
            'customer' : qs_customer
        }
        
        return render(request, 'dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            # Artist
            if 'btnUpdate' in request.POST:
                print('update button clicked')
                id = request.POST.get("id")
                fname = request.POST.get("firstName")
                lname = request.POST.get("lastName")
                bDate = request.POST.get("birthDate")
                address = request.POST.get("address")
                phone = request.POST.get("phoneNumber")

                update_artist = Artist.objects.filter(id = id).update(firstName = fname, lastName = lname, birthDate=bDate, address=address, phoneNumber=phone)

                print(update_artist)
                return redirect('artcraft:dashboard')

            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                artist = Artist.objects.filter(id = id).delete()

                return redirect('artcraft:dashboard')

            # Customer
            elif 'btnUpdate2' in request.POST:
                print('update button clicked')
                id = request.POST.get("id")
                fname = request.POST.get("firstName")
                lname = request.POST.get("lastName")
                email = request.POST.get("email")
                address = request.POST.get("address")
                phone = request.POST.get("phoneNumber")

                update_customer = Customer.objects.filter(id = id).update(firstName = fname, lastName = lname, email=email, address=address, phoneNumber=phone)

                print(update_customer)
                return redirect('artcraft:dashboard')

            elif 'btnDelete2' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                customer = Customer.objects.filter(id = id).delete()

                return redirect('artcraft:dashboard')

class loginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if Customer.objects.filter(username=uname).count() != 0:
            account = Customer.objects.get(username=uname)

            if account.password == pwd:
                return redirect('artcraft:home')
            else:
                messages.error(request, 'Incorrect Password')
        else:
            messages.error(request, 'Username Does Not Exist')

        return render(request, 'login.html')

def LogoutView(request):
	logout(request)
	return redirect('artcraft:login')


class registerView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            fname = request.POST.get("firstName")
            lname = request.POST.get("lastName")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone = request.POST.get("phoneNumber")
            uname = request.POST.get("username")
            passw = request.POST.get("password")
            cpassw = request.POST.get("cpassword")
            
            if passw == cpassw:
                if Customer.objects.filter(username=uname).exists():
                    messages.info(request,'Username already taken')
                    return redirect('register.html')
                elif Customer.objects.filter(email=email).exists():
                    messages.info(request, 'Email already used')
                    return redirect('register.html')
                else:
                    form = Customer(firstName=fname, lastName=lname, email=email, address=address, phoneNumber=phone, username=uname, password=passw)
                    form.save()
            else:
                return HttpResponse('Password not match')

            # return HttpResponse('Record Saved')
            # print('success')
            return redirect('artcraft:login')
        else:
            # messages.info(request, 'one or more fields are missing inputs')
            return redirect('artcraft:register')
            # return HttpResponse('Not Saved')

class registerArtistView(View):
    def get(self, request):
        return render(request, 'registerArtist.html')
    
    def post(self, request):
        form = ArtistForm(request.POST)

        if form.is_valid():
            fname = request.POST.get("firstName")
            lname = request.POST.get("lastName")
            bDate = request.POST.get("birthDate")
            address = request.POST.get("address")
            phone = request.POST.get("phoneNumber")
            uname = request.POST.get("username")
            passw = request.POST.get("password")

            form = Artist(firstName=fname, lastName=lname, birthDate=bDate, address=address, phoneNumber=phone, username=uname, password=passw)
            form.save()
            

            # return HttpResponse('Record Saved')
            # print('success')
            return redirect('artcraft:login')
        else:
            # messages.info(request, 'one or more fields are missing inputs')
            # return redirect('artcraft:register')
            return HttpResponse('Not Saved')