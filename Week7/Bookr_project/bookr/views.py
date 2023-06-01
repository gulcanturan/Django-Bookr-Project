from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




from .models import Book
from .forms import RegistrationForm, LoginForm, SearchForm





def index(request):

    return render(request, "index.html")

def books(request):
   
    books = Book.objects.all()
  
    return render(request, "books.html", {"books": books})




def book_detail(request, pk):
    book = Book.objects.get(id=pk)
   

    return render(request, 'book_detail.html', {"book" :book})






def book_search(request):
    form = SearchForm(request.POST)

    if request.method == 'POST': 
        search_text = form['search'].value()
        search_in = form['search_in'].value()
        print(search_in, search_text)

        if search_in == 'title':
            books = Book.objects.filter(title=search_text)   
        else:  
            print("Contributor" + "#"*10)   
            # books = Book.objects.filter(contributor=search_text)   
 

        return render(request, "search-result.html", {'form': form, 'search_text': search_text, 'books': books})


    else:
        print("*"*100)

    return render(request, "search-result.html", {"form": form})











def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')