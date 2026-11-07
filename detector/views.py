from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import URLPrediction
from .ml_utils import predict
def home(request): return render(request,'detector/home.html')
def register_view(request):
    if request.method=='POST':
        u=request.POST.get('username','').strip(); p=request.POST.get('password','')
        if u and p and not User.objects.filter(username=u).exists():
            user=User.objects.create_user(u,password=p); login(request,user); return redirect('dashboard')
    return render(request,'detector/register.html')
def login_view(request):
    if request.method=='POST':
        user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user: login(request,user); return redirect('dashboard')
    return render(request,'detector/login.html')
def logout_view(request): logout(request); return redirect('home')
@login_required
def detect_view(request):
    if request.method=='POST':
        url=request.POST.get('url','').strip()
        if url:
            label,conf,risk=predict(url)
            obj=URLPrediction.objects.create(user=request.user,url=url,prediction=label,confidence=conf,risk_level=risk)
            return redirect('result',pk=obj.pk)
    return render(request,'detector/detect.html')
@login_required
def result_view(request,pk): return render(request,'detector/result.html',{'item':get_object_or_404(URLPrediction,pk=pk,user=request.user)})
@login_required
def dashboard(request):
    qs=URLPrediction.objects.filter(user=request.user)
    return render(request,'detector/dashboard.html',{'total':qs.count(),'malicious':qs.filter(prediction='MALICIOUS').count(),'benign':qs.filter(prediction='BENIGN').count(),'recent':qs[:6]})
@login_required
def history(request): return render(request,'detector/history.html',{'items':URLPrediction.objects.filter(user=request.user)})
