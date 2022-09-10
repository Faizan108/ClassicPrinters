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
    if User.isauthenticated:
        return redirect(home)
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=fname+lname
        email=request.POST['email']
        pass1=request.POST['pass']
        pass2=request.POST['pass2']
        if pass1==pass2:
            newUser=User.objects.create_user(uname, email, pass1)
            newUser.first_name=fname
            newUser.last_name=lname
            newUser.save()
        else:
            pass
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
            return render(request,'home.html',{'error':"Wrong Credentials"})
    return redirect('home')



def contactus(request):
    if request.method=='POST':
        name=request.POST['cname']
        mail=request.POST['cmail']
        phone=request.POST['cphone']
        msg=request.POST['cmsg']
        newcontact=Contactus(c_name=name, c_phone=phone, c_mail=mail, msg=msg)
        newcontact.save()
        # messages.success("Data Success Fully Sent")
        return redirect('home')
    # messages.error("Data Not Sent")
    return redirect('home') 

def logout(request):
    userlogout(request)
    return redirect('home')