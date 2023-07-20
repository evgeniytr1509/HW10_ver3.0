from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserLoginForm
from .models import Quote, Author
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quotes')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# def quotes(request):
#     # Получаем список всех цитат из базы данных
#     all_quotes = Quote.objects.all()

#     # Передаем список цитат в шаблон 'quotes.html'
#     return render(request, 'quotes.html', {'quotes': all_quotes})

def quotes(request):
    # Получаем список всех цитат из базы данных
    all_quotes = Quote.objects.all()

    # Получаем список всех уникальных тегов из всех цитат
    all_tags = Quote.objects.values_list('tags', flat=True).distinct()

    # Создаем объект Paginator, указывая список и количество элементов на странице
    paginator = Paginator(all_quotes, 10)  # Показывать 10 цитат на странице

    # Получаем текущую страницу из GET-параметра 'page'
    page_number = request.GET.get('page')
    page_quotes = paginator.get_page(page_number)


    return render(request, 'quotes.html', {'quotes': all_quotes, 'tags': all_tags})




def quotes(request):
    # Получаем список всех авторов из базы данных
    all_authors = Author.objects.all()

    # Передаем список авторов в шаблон 'quotes.html'
    return render(request, 'quotes_app/quotes.html', {'authors': all_authors})



def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes')  
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})


def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'all_authors.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})




def quotes_by_tag(request, tag):
    # Получаем список всех цитат с выбранным тегом из базы данных
    quotes_with_tag = Quote.objects.filter(tags__contains=tag)

    return render(request, 'quotes_by_tag.html', {'quotes': quotes_with_tag, 'tag': tag})