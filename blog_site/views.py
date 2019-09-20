from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuModel, HeaderModel, FooterModel, FooterIcon, ArticlesModel, ProfileModel, PostModel, \
    Default_Profile
from .forms import RegisterForm, LoginForm, ContactForm, PostForm, SettingsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
context = {
    'menu': MenuModel.objects.all(),
    'footer': FooterModel.objects.first(),
    'icons': FooterIcon.objects.all(),
    'articles': PostModel.objects.all(),

}


def home_view(request):
    posts = Paginator(PostModel.objects.all(), 2)
    context['posts'] = posts.get_page(request.GET.get('page', 1))
    context['page_range'] = posts.page_range
    context['header'] = MenuModel.objects.get(name='Home').headermodel_set.first()

    if request.user.is_authenticated:
        try:
            context['user_info'] = request.user.profilemodel
        except:
            context['user_info'] = Default_Profile.objects.first()

    return render(request, "index.html", context)


def about_view(request):
    context['header'] = MenuModel.objects.get(name='About').headermodel_set.first()

    if request.user.is_authenticated:
        try:
            context['user_info'] = request.user.profilemodel
        except:
            context['user_info'] = Default_Profile.objects.first()

    return render(request, "about.html", context)


def contact_view(request):
    context['header'] = MenuModel.objects.get(name='Contact').headermodel_set.first()
    context['form'] = ContactForm()
    if request.user.is_authenticated:
        try:
            context['user_info'] = request.user.profilemodel
        except:
            context['user_info'] = Default_Profile.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "We will contact you"
            )

        else:
            context['form'] = form
            messages.error(
                request,
                "Form is not valid"
            )
    return render(request, 'contact.html', context)


def register_view(request):
    form = RegisterForm()
    header = ''
    for i in HeaderModel.objects.all():
        if i.name.name == 'About':
            header = i
    context = {
        'menu': MenuModel.objects.all(),
        'header': header,
        'footer': FooterModel.objects.first(),
        'icons': FooterIcon.objects.all(),
        'form': form,
        'link': 'about-view',
    }
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(request.POST.get('password'))
                user.save()
                user_name = request.POST.get('username')
                messages.success(
                    request, 'you have succesfully signed up'
                )
                return redirect('login-view')
            else:
                context['form'] = form
    else:
        return redirect('home-view')
    return render(request, 'register.html', context)


def login_view(request):
    form = LoginForm()
    header = ''
    for i in HeaderModel.objects.all():
        if i.name.name == 'About':
            header = i
    context = {
        'menu': MenuModel.objects.all(),
        'header': header,
        'footer': FooterModel.objects.first(),
        'icons': FooterIcon.objects.all(),
        'form': form,
        'link': 'about-view',
    }
    if request.user.is_authenticated:
        return redirect('home-view')

    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('home-view')
            else:
                messages.error(
                    request, 'Username or Password is invalid'
                )
                return redirect('login-view')
        else:
            context['form'] = LoginForm(request.POST)
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login-view')


def post_edit_view(request, id):
    form = PostForm(
        initial={'title': PostModel.objects.get(id=id).title, 'subtitle': PostModel.objects.get(id=id).subtitle,
                 'text': PostModel.objects.get(id=id).text})
    context = {
        'form': form,
        'post': PostModel.objects.get(id=id)
    }
    if request.user.is_authenticated:
        try:
            context['user_info'] = request.user.profilemodel
        except:
            context['user_info'] = Default_Profile.objects.first()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = PostModel.objects.get(id=id)
            post.title = request.POST.get('title')
            post.subtitle = request.POST.get('subtitle')
            post.text = request.POST.get('text')
            post.save()
            messages.success(
                request, 'you have succesfully changed settings'
            )
            return redirect('dashboard-view')
        else:
            messages.error(
                request, 'Username or Password is invalid'
            )

    return render(request, 'post_edit.html', context)


def dashboard_view(request):
    posts = Paginator(PostModel.objects.filter(user=request.user), 2)
    context = {
        'menu': MenuModel.objects.all(),
        'footer': FooterModel.objects.first(),
        'icons': FooterIcon.objects.all(),
        'articles': PostModel.objects.all(),
        'posts': posts.get_page(request.GET.get('page', 1)),
        'form': PostForm(),
        'page_range': posts.page_range
    }
    context['header'] = MenuModel.objects.get(name='Home').headermodel_set.first()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(
                request, 'succesfully posted'
            )
            return redirect('dashboard-view')
        else:
            messages.error(
                request, 'Username or Password is invalid'
            )
            context['form'] = form

    if request.user.is_authenticated:
        try:
            context['user_info'] = request.user.profilemodel
        except:
            context['user_info'] = Default_Profile.objects.first()

    return render(request, 'dashboard.html', context)


def delete_view(request, id):
    PostModel.objects.get(id=id).delete()
    return redirect('dashboard-view')


def profile_view(request, slug):
    posts = Paginator(ProfileModel.objects.get(slug=slug).user.postmodel_set.all(), 2)
    context['user'] = ProfileModel.objects.get(slug=slug)
    context['posts'] = posts.get_page(request.GET.get('page', 1))
    return render(request, 'author.html', context)


def post_view(request, slug):
    context['post'] = PostModel.objects.get(slug=slug)

    return render(request, 'post.html', context)


def usersettings_view(request):
    context['header'] = MenuModel.objects.get(name='Home').headermodel_set.first()
    context['form'] = SettingsForm(
        initial={'Ad': request.user.first_name, 'Soyad': request.user.last_name,
                 'Email': request.user.email, 'Image' : ProfileModel.objects.get(user=request.user).profile_image})

    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.first_name = request.POST.get('Ad')
            user.last_name = request.POST.get('Soyad')
            user.email = request.POST.get('Email')
            user.save()
            user.profilemodel.profile_image = request.FILES['Image']
            user.profilemodel.save()
            messages.success(
                request, 'you have succesfully changed settings'
            )
            return redirect('home-view')
        else:
            messages.error(
                request, 'Username or Password is invalid'
            )
    return render(request, 'user-settings.html', context)
