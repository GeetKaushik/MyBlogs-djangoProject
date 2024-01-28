from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Blog_Category, Query, Subscription, Blog_Post
from .form import Blog_Form, Blogpost_form



# Create your views here.
def home(request):
    # return HttpResponse("<h1>This is a Home page 👾</h1 >")

    ##fetching data from db
    x = Blog_Category.objects.all()
    print(x)
    return render(request, 'my_blogs/home.html', {"category":x})

def about(request):
    # return HttpResponse("<h1>This is a About page 🙂</h1>")
    return render(request, 'my_blogs/about.html')

def services(request):
    # return HttpResponse("<h1>This is a Services page ⭐️ </h1>")
    return render(request, 'my_blogs/about.html')

def contact(request):
    # return HttpResponse("<h1>This is a Contact page 🤙 </h1>")
    if request.method == 'GET':
        return render(request, 'my_blogs/contact.html')
    elif request.method == 'POST':
        name = request.POST.get('usrname')
        email = request.POST.get('usremail')
        query = request.POST.get('usrquery')
        ##fetching data from db
        x = Query(u_name=name, u_email=email, u_query=query)
        x.save()
        print(x)
        print(name)
        print(email)
        print(query)
        return render(request, 'my_blogs/contact.html', {'feedback' :'Thankyou, We will get back to you soon 😊'})

def subcription(request):
    # return HttpResponse("<h1>this is subscription page 👾<h1>")
    if request.method == 'GET':
        return render(request, 'my_blogs/subscription.html')
    elif request.method == 'POST':
        email = request.POST.get('usremail')
        membership = request.POST.get('usrmembership')

        if(Subscription.objects.filter(u_email = email).exists()): 
            return render(request, 'my_blogs/subscription.html', {'feedback' : "Already Exists 😇"})
        else:
            x = Subscription(u_email=email, u_membership=membership)
            x.save()
            print(x)
            print(email)
            print(membership)
            return render(request, 'my_blogs/subscription.html', {'feedback' : "Thankyou for taking our subscription 😇"})

def blog(request):
    x = Blog_Form()
    if request.method == "GET":
        return render(request, 'my_blogs/blog.html', {"x" : x})
    else:
        print("Processing...")
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Saving...")
            return redirect('/')
        else:
            return render(request,'my_blogs/blog.html', {"x" : x})

def ck(request):
    x = Blogpost_form()
    if request.method == "GET":
        return render(request, 'my_blogs/ck.html', {"x" : x})
    else:
        print("Processing...")
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Saving...")
            return redirect('/')
        else:
            return render(request,'my_blogs/ck.html', {"x" : x})

@login_required(login_url="loginusr")      
def allBlogs(request):
    y = Blog_Post.objects.all()
    return render(request, 'my_blogs/allblogs.html', {"y" : y} )

def blogDetails(request, blog_id):
    obj = get_object_or_404(Blog_Post, pk=blog_id)
    print(obj)
    print(blog_id)
    return render(request,'my_blogs/blogDetails.html', {"obj":obj})

def loginusr(request):
    if request.method == 'GET':
        return render(request, 'my_blogs/loginusr.html', {'LoginForm': AuthenticationForm()})
    else:
        usr = request.POST.get('username')
        pas = request.POST.get('password')
        user = authenticate(request, username=usr,password=pas)
        if user is None:
            return render(request, 'my_blogs/loginusr.html', {'LoginForm' : AuthenticationForm(), 'Error': "Invalid Credentials"})
        else:
            login(request, user)
            return redirect('/')

def signupusr(request):
    if request.method == 'GET':
        return render(request, 'my_blogs/signupusr.html', {'SignupForm': UserCreationForm()})
    else:
        usr = request.POST.get('username')
        pas = request.POST.get('password1')
        pasv = request.POST.get('password2')
        if pas == pasv:
            # Check wether user exists
            if (User.objects.filter(username = usr)):
                return render(request, 'my_blogs/signupusr.html', {'SignupForm': UserCreationForm(), 'Error': "Username already exist! (Try again with different username)"})
            else:
                user = User.objects.create_user(username = usr, password = pas)
                user.save()
                login(request, user)
                return redirect('/')
        else:
            # if password verification fails
            return render(request, 'my_blogs/signupusr.html', {'SignupForm': UserCreationForm(), 'Error': "Make sure both password is same!"})



def logoutusr(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')