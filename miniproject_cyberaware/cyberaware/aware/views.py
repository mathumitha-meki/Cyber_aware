from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from . models.ques import Questionaries
from .models import *
from .forms import *











# Create your views here.


def layout(request):
    return render(request,'index.html')

def html(request):
    return HttpResponse('working')

def aware(request):
    return render(request,'awareof.html')  


def ques(request):
    if request.method == "GET":
        return render(request,'questionaries.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender=request.POST.get('Gender')
        qualification=request.POST.get('Qualification')
        phising=request.POST.get('phising')
        hack=request.POST.get('hack')
        firewall=request.POST.get('firewall')
        laws=request.POST.get('laws')
        publish=request.POST.get('publish')
        cyberbulied=request.POST.get('cyberbulied')
        stalking=request.POST.get('stalking')
        report=request.POST.get('report')
        dna=request.POST.get('DNA')
        happen=request.POST.get('happen')
        idea=request.POST.get('idea')

        data = Questionaries(name=name,email=email,gender=gender,school=qualification,ques_five=phising,ques_six=hack,ques_seven=firewall,ques_eight=laws,ques_nine=publish,ques_ten=cyberbulied,ques_eleven=stalking,description=report,ques_twelve=dna,ques_thirteen=happen,ques_fourteen=idea)
        data.save()
        return HttpResponse(f'<h1>Thanks for your response,{name}! </h1>  ') 

        



def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/login') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/layout')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

