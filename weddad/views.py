from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Post,Profile,Plan,Plan_member3,Adress
from .forms import *
from .models import Post
import folium 
import geocoder
from django.core.mail import send_mail
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Subquery, OuterRef

# Create your views here.
def first(request):
    all=Post.objects.all().order_by('-published_time')
    form2=New_p(request.POST or None ,request.FILES or None)
    if form2.is_valid():
        pst=form2.save(commit=False)
        pst.author2=request.user
        pst.save() 
        return redirect('home')
    return render(request,"sif.html",{'post':all,'form':form2,})

def Likeview(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))
def jrview(request,mypk):
    #my_plan=get_object_or_404(Plan,id=mypk)
    my_plan=Plan.objects.get(pk=mypk)
    pln_mem=Plan_member3(member=request.user,plan=my_plan)
    pln_mem.save()
    return HttpResponseRedirect(reverse('plans'))
def Delete_post_view(request,post_id):
    mypost=Post.objects.get(pk=post_id)
    mypost.delete()
    return HttpResponseRedirect(reverse('home'))
def Delete_plan_view(request,plan_id):
    myplan=Plan.objects.get(pk=plan_id)
    myplan.delete()
    return HttpResponseRedirect(reverse('plans'))
def trip_planner(request,plan_id):
    theplan=Plan.objects.get(pk=plan_id)
    form4=Day_planner_form(request.POST or None ,request.FILES or None)
    if form4.is_valid():
        lp=form4.save(commit=False)
        lp.plan=theplan
        if Day_Planner.objects.filter(plan=theplan).exists():
            lp.num=Day_Planner.objects.filter(plan=theplan).count()+1
            lp.n=Day_Planner.objects.filter(plan=theplan).count()
        else:
            lp.n=0
            lp.num=1
        lp.save()
        return redirect('tripplanner',plan_id=plan_id)    
    return render(request,'spec_plan.html',{'form':form4,'plan':theplan})
def plview(request,memberchip_id):
    my_memberchip=get_object_or_404(Plan_member3,pk=memberchip_id)
    my_memberchip.status="oui"
    my_memberchip.save()
    return HttpResponseRedirect(reverse('plans'))
def newp(request):
    form2=New_p(request.POST or None ,request.FILES or None)
    if form2.is_valid():
        pst=form2.save(commit=False)
        pst.author2=request.user
        pst.save() 
        return redirect('home')
    return render(request,'new_p.html',{'form':form2})

def planview(request):
    userk = Plan.objects.exclude(id__in=Subquery(Plan_member3.objects.filter(plan=OuterRef('pk'), member=request.user).values('plan')))
    all=Plan.objects.all().filter
    myplans=Plan.objects.filter(Creatur=request.user)
    #userk=Plan_member3.objects.filter(~Q(member=request.user))
    form3=New_plan(request.POST or None ,request.FILES or None)
    if form3.is_valid():
        pst2=form3.save(commit=False)
        pst2.Creatur=request.user
        pst2.save() 
        return redirect('tripplanner',plan_id=pst2.id)
    return render(request,"plans.html",{'plans':all,'form':form3,'myplans':myplans,'dif':userk,})




def sign(request):
    form=UserCreationForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('home')
    return render(request,'auth_sign.html',{'form':form})


def profilepage(request,user_id):
    user_p=User.objects.get(pk=user_id)
    if Profile.objects.filter( user=user_p).exists():
        reponse=True
    else:
        reponse=False

    return render(request,'profile.html',{'my_user':user_p,'reponse':False})
def cantactview(request):
    form12=CantactForm(request.POST or None,request.FILES or None)
    email=''
    if request.method == 'POST':
        form12=CantactForm(request.POST or None,request.FILES or None)
        if form12.is_valid():
            sub=form12.cleaned_data['subject']
            email=form12.cleaned_data['email']
            message=form12.cleaned_data['message']
            send_mail(sub,
                      message,
                      email,
                      ['sifeddine.addar@gmail.com'],
                      )

    return render(request,'cantacts.html',{'form':form12,'mail':email})

def updatedef(request,post_id):
    lpost=Post.objects.get(pk=post_id)
    up_form=New_p(request.POST or None ,request.FILES or None,instance=lpost)
    if up_form.is_valid():
        up_form.save()
        return redirect('home')
    return render(request,'post.update_page.html',{'up_form':up_form})
def postpagedef(request,post_id):
    main_post=Post.objects.get(pk=post_id)
    comment_form=New_com(request.POST or None ,request.FILES or None)
    if comment_form.is_valid():
        comy=comment_form.save(commit=False)
        comy.author=request.user
        comy.post_id=main_post
        comy.save()
    return render(request,'post_page.html',{'post':main_post,'comment_form':comment_form})

import requests
def my_map(request):
    form=Location_search_form(request.POST or None ,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('mapping')
    
    adress=Adress.objects.all().last()
    location=geocoder.osm(adress)
    lat=location.lat
    lng=location.lng
    country=location.country
    if lng==None or lat==None:
        adress.delete()
        return HttpResponse("adress invalid")
    map=folium.Map(tiles="OpenStreetMap", zoom_start=8,location=[lat,lng])
    #folium.Marker([5.222,-0.210],tooltip="click for more",popup="Gana").add_to(map)
    map.add_child(folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"))
    map.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=False))
    folium.Marker([lat,lng],tooltip="click for more",popup=f"{country}").add_to(map)
    map=map._repr_html_()
    return render(request,'mapping.html',{'map':map,'form':form})
def my_weather(request):
    url="http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    my_city="blida"
    complet=url+my_city
    response=requests.get(complet)
    content=response.json()
    my_info={
        'City':my_city,
        'temperateur' :content['main']['temp'],
        'description' :content['weather'][0]['description'],
        'icon' :content['weather'][0]['icon'],

    }
    return render(request,'mapping.html',{'content':my_info,'con':content})
def my_accountdef(request):
    reponse=False
    if Profile.objects.filter( user=request.user).exists():
        reponse=True
        lprofile=request.user.profile
        up_profile=New_profile(request.POST or None ,request.FILES or None,instance=lprofile)
        if up_profile.is_valid():
            up_profile.save()
            #return redirect('profile'id=request.user.id)
    else:
        up_profile=New_profile(request.POST or None ,request.FILES or None)
        if up_profile.is_valid():
             comy=up_profile.save(commit=False)
             comy.user=request.user
             comy.save()

    return render(request,'my_account.html',{'up_profile':up_profile,'reponse':reponse})

