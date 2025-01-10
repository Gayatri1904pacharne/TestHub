from django.db import models

# Create your models here.


class Question(models.Model):
    qno=models.IntegerField(primary_key=True)
    qtext=models.CharField(max_length=70)
    answer=models.CharField(max_length=70)
    op1=models.CharField(max_length=70)
    op2=models.CharField(max_length=70)
    op3=models.CharField(max_length=70)
    op4=models.CharField(max_length=70)
    subject=models.CharField(max_length=70)

    def __str__(self)->str:
        return f"{self.qno,self.qtext,self.answer,self.op1,self.op2,self.op3,self.op4,self.subject}"

    class Meta:
        db_table="question"
     




class Result(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    subject=models.CharField(max_length=20)
    score=models.IntegerField()

    class Meta:
        db_table="result"


