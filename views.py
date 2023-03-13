from django.shortcuts import render
from django.http import  HttpResponse

def Midterm_A(request):
    jobroles = ['Reporting Executives',
    'Business Analyst',
    'Data Analyst',
    'Statistician',
    'Data Scientist',
    'Data Engineer/Data Architect',
    'Machine Learning Engineer',
    'Big Data Engineer']
context = {'jobroles':jobroles}
return render(request,'Midterm_A/midterma.html',context)