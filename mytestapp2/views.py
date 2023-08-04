from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def homepage(request):
    post= NewPost.objects.order_by('-publication_time')
    user=request.user
    context= {'user':user,'posts':post}
    return render(request, "home.html", context)

def addpost(request):
    if request.method =="POST":
        title=request.POST['title']
        content=request.POST['content']
        author=request.POST['author']
        date=request.POST['date']
        categories=request.POST['categories']
        upload=request.POST['upload']
        
        author=request.user
        newpost=NewPost(title=title, content=content,author=author,publication_time=date,categories=categories,image=upload)
        newpost.save()
        return redirect('home')
        
    return render(request, "addpost.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname 
        myuser.save()
        profile = Profile(user=myuser)
        profile.save()
        messages.success(request, "You have Successfully Signed up")
        return redirect("login")
    
    return render(request, "signup.html")

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        print(username,pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "You have Entered the wrong Username or Password")
    
    return render(request, "login.html")

def logoutpage(request):       
    logout(request)
    return redirect('home')

def profilepage(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile(user=user)
    
    if request.method == "POST":
        aboutme = request.POST['aboutme']
        profile.aboutme = aboutme
        profile.save()
        messages.success(request, "You have saved your form")
    else:
        messages.error(request, "It's an error")
    
    content = {'user': user, 'profile': profile}
    return redirect('profileappear')
    return render(request, "profile.html", content)


def contactpage(request):
    return render (request, "contact.html")


def articlepage(request,pk):
    post=NewPost.objects.get(pk=pk)
    return render (request, "article.html", {'posts': post})

def updatepost(request,pk):
    post = NewPost.objects.get(pk=pk)
    if request.method=="POST":
        post.title= request.POST['title']
        post.content= request.POST['content']
        post.save()
        return redirect('home')

    return render (request, 'update_page.html', {'posts':post})

def deletepost(request,pk):
    post=NewPost.objects.get(pk=pk)
    if request.method=="POST":
        post.delete()
        
        return redirect('home')
        
    return render (request,"delete_post.html" ,{'post': post})

def profileappear(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None
    
    return render(request, 'profile_appear.html', {'profile': profile})

def categoriespage(request, cats):
    categoriess = NewPost.objects.filter(categories=cats)
    content = {'categoriess': categoriess , 'cats':cats}
    return render(request, "categories.html", content)

def likespage(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(NewPost, pk=pk)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
    return redirect('article', pk=pk)
    
    
    
    