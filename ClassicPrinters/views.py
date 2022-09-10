import imp
from posixpath import isabs
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as dj_login,logout as dj_logout,authenticate
from django.contrib import messages
from products.models import visiting_card, brochure, letter_head, envelope, Contactus
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def search(request):
    query=request.GET('query')
    if (len(query)==0 or len(query)>30):
        card=visiting_card.objects.none()
        lh=letter_head.objects.none()
        bro=brochure.objects.none()
        env=envelope.objects.none()
    else:
        card=visiting_card.objects.filter(card_name=query)
        card=card.union(visiting_card.objects.filter(card_size=query))
        card=card.union(visiting_card.objects.filter(card_cat=query))
        card=card.union(visiting_card.objects.filter(card_qual=query))
        lh=letter_head.objects.filter(lh_name=query)
        lh=lh.union(letter_head.objects.filter(lh_qual=query))
        lh=lh.union(letter_head.objects.filter(lh_size=query))
        bro=brochure.objects.filter(bro_name=query)
        bro=bro.union(brochure.objects.filter(bro_size=query))
        env=envelope.objects.filter(env_name=query)
        env=env.union(brochure.objects.filter(env_size=query))
        env=env.union(brochure.objects.filter(env_cat=query))
    params={'cards':card, 'letter':lh, 'brochure':bro, 'envelope':env, 'query':query}
    print(params)
    return render(request, 'home.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method=='POST':
        fname=request.POST['f_name']
        lname=request.POST['l_name']
        uname=fname+lname
        email=request.POST['e_mail']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(pass1)<8:
            err="Password must be of length 8"
            return HttpResponse(err)
        elif pass1!=pass2:
            err="Password and Confirm Password not same"
            return HttpResponse(err)
        else:
            newUser=User.objects.create_user(uname, email, pass1)
            newUser.first_name=fname
            newUser.last_name=lname
            newUser.save()
    return redirect(home)


def hanlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method=='POST'):
        uname=request.POST['username']
        pass1=request.POST['password']
        myuser=authenticate(username=uname, password=pass1)
        if myuser is not None:
            userlogin(request, myuser)
            return redirect('home')
        else:
<<<<<<< HEAD
            return render(request,'home.html',{'error':"Wrong Credentials"})
    return redirect('home')
=======
            return HttpResponse('Incorrect Username or Password')
>>>>>>> b8858cb2c51143aa29de7ac923d3e782d4e7d2c7



def contactus(request):
    if request.method=='POST':
        name=request.POST['cname']
        mail=request.POST['cmail']
        phone=request.POST['cphone']
        msg=request.POST['cmsg']
        err=""
        if(len(phone)!=10):
            err="phone number should be of 10 digit"
            return HttpResponse(err)
        for i in range(len(phone)):
            if(phone[i]<'0' or phone[i]>'9'):
                err="phone must not contain characters other than digit"
                return HttpResponse(err)
        if(len(err)==0):
            newcontact=Contactus(c_name=name, c_phone=phone, c_mail=mail, msg=msg)
            newcontact.save()
    return HttpResponse("")

def logout(request):
    userlogout(request)
    return redirect('home')