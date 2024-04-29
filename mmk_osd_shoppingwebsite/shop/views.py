from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from shop.models import Product, CategoryEnum

# My functions (Mehrbod M.K.)
def __Generate_AuthenticatedUser_Metas(request):
    auth_Metas = ''

    # Check user authentication.
    if request.user.is_authenticated:
        auth_Metas = {
            'is_UserLoggedIn': 'yes',
            'user_FirstName': request.user.first_name,
            'user_Username': request.user.get_username(),

            'user_ItemsInCart': 0,
        }
    else:
        auth_Metas= {
            'is_UserLoggedIn': 'no'
        }

    return auth_Metas

# Create your views here.
def index(request):
    index_Metas = __Generate_AuthenticatedUser_Metas(request)

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

def logout(request):
    if(request.user.is_authenticated):
        auth_logout(request)
    
    return HttpResponse('OK')

@login_required(login_url="/login")
def products(request):
    # Check user.
    index_Metas = __Generate_AuthenticatedUser_Metas(request)
    
    # Fetch products.
    productsQuery = Product.objects.all()
    metas_Products = {};
    products_List = [];

    for productGet in productsQuery:
        dict_Product = {}
        dict_Product['Product_Name'] = productGet.name
        dict_Product['Product_Price'] = f'{productGet.price:,}'
        dict_Product['Product_Category'] = productGet.category.name
        if(productGet.thumbnailImagePath != 'blank' and productGet.thumbnailImagePath != ''):
            dict_Product['Product_ThumbImage'] = productGet.thumbnailImagePath
        products_List.append(dict_Product)
    
    metas_Products['products'] = products_List
    metas_Products.update(index_Metas)

    return render(request, 'shop/products.html', context= metas_Products)
