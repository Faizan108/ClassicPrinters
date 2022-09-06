from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as dj_login,logout as dj_logout,authenticate
from django.contrib import messages
from products.models import visiting_card, brochure, letter_head, envelope


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