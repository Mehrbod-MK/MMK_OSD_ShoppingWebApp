from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def index(request):
    index_Metas = ''

    # Check user authentication.
    if request.user.is_authenticated:
        index_Metas = {
            'is_UserLoggedIn': 'yes',
            'user_FirstName': request.user.first_name,
            'user_Username': request.user.get_username(),

            'user_ItemsInCart': 0,
        }

    return render(request, 'shop/index.html', context= index_Metas)

def login(request):
    return render(request, 'registration/login.html')

def userAuth(request):
    user_Username = request.POST["user_Username"]
    user_Password = request.POST["user_Password"]

    metas =  '';

    user = authenticate(request=request, username=user_Username, password=user_Password)
    if(user is not None):
        auth_login(request, user)
        metas = { 'msgTitle': 'ورود موفقیت‌آمیز!', 'msgType': 'MSG_SUCCESS', 
                 'msgText': f'کاربر گرامی، {user.get_username()} بزرگوار، خوش آمدید.',
                 'msgRedirectURL': '/'}
    else:
        metas = { 'msgTitle': 'ورود ناموفق!', 'msgType': 'MSG_ERROR',
                 'msgText': 'نام کاربری/کلمه عبور اشتباه است.',
                'msgRedirectURL': '/login' }
        
    return render(request, 'registration/msgDisplay.html', context= metas)
