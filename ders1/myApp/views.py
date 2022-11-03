from django.shortcuts import render, get_object_or_404, redirect
from myApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    
    return render(request,'index.html',context)

def detail(request,id):
    post = get_object_or_404(Post,id=id)
    
    if request.method == "POST":
        adet=int(request.POST['number'])
        if Shop.objects.filter(product=post, user=request.user):
            buy = Shop.objects.filter(user=request.user).get(product=post)
            buy.user = request.user
            buy.adet += adet
            buy.fiyat += adet*post.fiyat
            buy.save()
        else:
            buy=Shop(user=request.user,product=post,fiyat=post.fiyat*adet, adet=adet, image=post.image)
            buy.save()    
    
    context={
        "post":post
    }
    return render(request,'detail.html',context)

def shoping(request):
    shop = Shop.objects.filter(user=request.user)
    toplamfiyat = 0
    if request.method == "POST":
        # if shop:
            adetkey = list(request.POST)[1]
            print('POST içerisinden gelen',request.POST)
            print('list POST', list(request.POST))
            print('adetkey',adetkey)
            adetid = adetkey[6:] # ürünün id değerini çekmek için
            adet = int(request.POST[adetkey])
            print(adetkey, adetid)
            buy = Shop.objects.get(id=adetid)
            buy.adet = adet
            buy.fiyat = adet* buy.product.fiyat
            buy.save()
            print(buy.adet, "asd")
            if buy.adet == 0:
                buy.delete()

    for i in shop:
        toplamfiyat += i.fiyat
        
    context = {
        "shop": shop,
        "toplamfiyat": toplamfiyat,
    }
    return render(request, 'shoping.html', context)


def deleteshop(request,id):
    buy=Shop.objects.get(id=id)
    buy.delete()
    return redirect('shoping')

def about(request):

    return render(request,'about.html')

def userLogin(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password=password)
        
        if user is not None:
            login(request,user)
            
            return redirect('index')
        # {'email':value, 'password':value}
        print(username)
        print(password)
    
    return render(request,'users/login.html')

def userLogout(request):
    logout(request)
    
    return redirect('index')

def userRegister(request):
    
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request,'users/register.html',{
                    "hata":"Aynı ada sahip kullanıcı adı var"
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'users/register.html', {
                        "hata": "Email daha önce kullanılmış!"
                    })
                else:
                    print("evet")
                    usersave = UserSave(user=username, password=password1)
                    usersave.save()
                    user = User.objects.create_user(first_name=name,
                                                    last_name=surname,
                                                    email=email,
                                                    username=username,
                                                    password=password1)
                    user.save()
                    return redirect('index')
        else:
            return render(request, 'users/register.html', {
                        "hata": "password aynı değil!!"
                    })    
                
    return render(request,'users/register.html')
    

def userChangePassword(request):
    user = User.objects.get(username=request.user)
    if UserSave.objects.filter(user=request.user).exists():
        usersave = UserSave.objects.get(user=request.user)

        if request.method == "POST":
            password_old = request.POST['password_old']
            password_new = request.POST['password_new']
            password_renew = request.POST['password_renew']
            if password_old == usersave.password:
                if password_new == password_renew:
                    user.set_password(password_new)
                    user.save()
                    usersave.password = password_new
                    usersave.save()
                    return redirect('userlogin')
                else:
                    return render(request, 'users/changepassword.html', {"hata": "Şifreler aynı değğil!!"})
            else:
                return render(request, 'users/changepassword.html', {"hata": "Eski şifre yanlış!!"})
    return render(request, 'users/changepassword.html')
