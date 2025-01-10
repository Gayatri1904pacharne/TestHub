from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db import connection
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from loginapp.models import Question
from loginapp.models import Result




import pymysql

# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method=='POST':
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        un=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            if User.objects.filter(username=un).exists():
                messages.error(request,'user name already exists')
                return redirect('/signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'already have email')
                    return redirect('/signup')
                else:
                    
                    user=User.objects.create_user(username=un,password=pass1,first_name=fn,last_name=ln,email=email)
                    user.save()
                    print(connection.queries)
                    messages.info(request,'sign up successfully')
                    return redirect('/login')
        else:
            messages.error(request,'Password not match')
            return redirect('/signup')
    return render(request,'signup.html')    
        


def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_superuser==1:
                return render(request,"dashboard.html")
            request.session['questionindex']=0   # add questionindex in session dictionary
            # [questionindex=0] session dictionary
            messages.success(request,"login successfully")
            request.session['answers']={}
            request.session['score']=0
            request.session['username']=username
            
        
            return render(request,'indexfortest.html')
            #return render(request,'subject.html')
        else:
            messages.error(request,'Invalid credential')
            return redirect('/login')
    return render(request,'login.html')



@login_required(login_url="/login")
def dashboard(request):
    return render(request,'dashboard.html')



def question(request):
     print(request.GET["subject"])
     subjectname=request.GET["subject"]
     request.session['subject']=subjectname
     firstquestion=Question.objects.filter(subject=subjectname)[0]
     return render(request,"question.html",{'question':firstquestion})


def logout(request):
    auth.logout(request)
    return redirect("/")


def search(request):
    searchString=request.GET["searchString"]
    return redirect(f"https:www.google.co.in/search?q={searchString}")


def indexfortest(request):
    return render(request,"indexfortest.html")


def nextQuestion(request):
    if 'op' in request.GET:
        allanswers=request.session['answers']           #{}
        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]             # allanswers  {'1':[1,'what','a','c'],'2':[2,'why','d','d']}
        print(allanswers)
    #allquestions=Question.objects.all()

        queryset=Question.objects.filter(subject= request.session['subject'])
        allquestions=list(queryset)

        print(f"allquestions in nextquestion is {allquestions}")
    
        if request.session['questionindex']<len(allquestions)-1:
            request.session['questionindex']=request.session['questionindex']+1
        question=allquestions[request.session['questionindex']]
        print(f"question is {question} and it's type is {type(question)}")
        if question.qno==10:
            isdisabled=True
        else:
            isdisabled=False

        return render(request,'question.html',{'question':question,'isdisabled':isdisabled})
    else:
        return render(request,'question.html',{'question':allquestions[len(allquestions)-1]})
    

    
def previousQuestion(request):
    queryset=Question.objects.filter(subject= request.session['subject'])
    allquestions=list(queryset)
    if request.session['questionindex']>0:
        request.session['questionindex']=request.session['questionindex']-1
        question=allquestions[request.session['questionindex']]
        qno=question.qno
        submitteddetails=request.session['answers']
        print(f"submited answers are {submitteddetails}")
        if str(qno) in submitteddetails:
            questiondetails=submitteddetails[str(qno)]
            previousanswer=questiondetails[3]
            print(f"previousanswer is {previousanswer}")
        else:
            previousanswer=''
        return render(request,'question.html',{'question':question,'previousanswer':previousanswer})
    else:
        return render(request,'question.html',{'question':allquestions[0]})
    
    
    
def endexam(request):
    if 'answers' in request.session:
        if 'op' in request.GET:
            allanswers=request.session['answers']           #{}
            allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]          # allanswers  {'1':[1,'what','a','c'],'2':[2,'why','d','d']}
            print(allanswers)
        dictionary=request.session['answers']     #{1:[1,'what',2,2],2:[2,'why',4,6]}
        listoflist=dictionary.values()           #[[1,'what',2,2],[2,'why',4,6]]
        print(listoflist)
        for list in listoflist:
            if list[2]==list[3]:
                request.session['score']= request.session['score']+1
        finalscore=request.session['score']
        username=request.session['username']
        result=Result.objects.create(username=username,subject=request.session['subject'],score=finalscore)
        print("record is added in database")
        print(connection.queries)
       # auth.logout(request)
        return render(request,'score.html',{'username':username,'score':finalscore,'listoflist':listoflist})
    else:
        messages.info(request,'login again..')
        return render(request,'login.html')

    
    
def viewscore(request):
        
        
        dictionary=request.session['answers']     #{1:[1,'what',2,2],2:[2,'why',4,6]}
        listoflist=dictionary.values()           #[[1,'what',2,2],[2,'why',4,6]]
        

        print("type of list of list is " , type(listoflist)) 

        print(listoflist)
        
        auth.logout(request)

        return render(request,'viewscore.html',{'listoflist':listoflist})
    

   
                 



