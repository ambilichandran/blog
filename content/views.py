from django.shortcuts import render,redirect
from.models import Post
from . form import AddPost 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def index(request):
    data=Post.objects .all()
    return render(request,"index.html",{"data":data})
def post(request, id):
    data=Post.objects.get(id=id)
    return render(request,"post.html",{"data":data})

@login_required
def create(request):
    form=AddPost()
    if request.method=='POST':
        form=AddPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"create.html",{"form":form})
@login_required
def edit(request,id):
    data=Post.objects.get(id=id)
    form=AddPost(instance=data) 
    if request.method=='POST':
        form=AddPost(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"edit.html",{"form":form})

@login_required
def delete(request,id):
    data=Post.objects.get(id=id)
    if request.method=='POST':
        data.delete()
        return redirect("/")
    return redirect("/")
def registration(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,"registration.html",{"form":form})
def logout(request):
    logout(request)
    return redirect("/")

