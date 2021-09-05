from django.contrib import auth
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
#회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')


# def signup2(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username = request.POST['username'],
#                 password = request.POST['password1'],
#                 email = request.POST['email'],
#             )
#             auth.login(request, user)
#             return redirect('/')
#         return render(request, 'accounts/signup.html')
#     else:
#         form = UserCreationForm
#         context = {
#             'form': form
#         }
#         return render(request, 'accounts/signup.html', context)


#로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:home')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(request.GET.get('next') or 'articles:home')
        else:
            context = {
                'error': 'username or password is incorrect',
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')


#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('articles:home')

#home
# def main(request):
#     return render(request, 'accounts/main.html')