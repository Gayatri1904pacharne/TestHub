from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db import connection
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from loginapp.models import Question
from loginapp.models import Result



def addquestion(request):
    if request.method == "POST":
        qno = request.POST.get('qno')
        qtext = request.POST.get('qtext')
        answer = request.POST.get('answer')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        subject = request.POST.get('subject')
        if qno and qtext and answer and op1 and op2 and op3 and op4 and subject:
            question = Question(qno=qno,qtext=qtext,answer=answer,op1=op1,op2=op2,op3=op3,op4=op4,subject=subject)
            question.save()
        questions = Question.objects.all()
        return render(request, "adminapp/addquestion.html", {"questions": questions})
    questions = Question.objects.all()
    return render(request, "adminapp/addquestion.html", {"questions": questions})



def updatequestion(request):
    if request.method == "POST":
        qno = request.POST['qno']
        subject = request.POST['subject']
    
        question = Question.objects.filter(qno=qno, subject=subject) # type: ignore
        qtextfromuser = request.POST['qtext']
        answerfromuser = request.POST['answer']
        op1fromuser = request.POST['op1']
        op2fromuser = request.POST['op2']
        op3fromuser = request.POST['op3']
        op4fromuser = request.POST['op4']

        question.update(qtext=qtextfromuser,answer=answerfromuser,op1=op1fromuser,op2=op2fromuser,op3=op3fromuser,op4=op4fromuser)

        return render(request, 'adminapp/updatequestion.html', {'message': 'Question updated successfully!'})

    return render(request, 'adminapp/updatequestion.html')




def getquestion(request):
    if request.method == "POST":
        qno = request.POST.get('qno')
        subject = request.POST.get('subject')
        
        question = Question.objects.get(qno=qno, subject=subject) 
    
        questions = Question.objects.all()

        return render(request, 'adminapp/updatequestion.html', {
            'question': question,  
            'questions': questions  
        })



def deletequestion(request):
    if request.method =='POST':
        qno = request.POST['qno']
        subject = request.POST['subject']
        Question.objects.get(qno=qno,subject=subject).delete()
        return render(request,'adminapp/deletequestion.html',{"message":"quetions deleted..."})
    return render(request,'adminapp/deletequestion.html')


def marks_analysis(request):
    results = Result.objects.all()
    return render(request, 'adminapp/markanalysis.html', {'results': results})



