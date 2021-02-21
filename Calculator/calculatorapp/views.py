from django.shortcuts import render
from django.http import HttpResponse
import smtplib #for email
from calculatorapp.models import UserFeedback
# from calculatorapp.models import UserFeedback
def connectTOMail():
    con = smtplib.SMTP("smtp.gmail.com",587)
    con.ehlo()
    print("hello sucessfull")
    con.starttls()
    con.login("arpit456jain@gmail.com","#vanshika jain#")
    print("login succesfull")
    return con
# Create your views here.
def index(request):
    # return HttpResponse('hello this is calc page')
    return render(request,'index.html')

def calculate(request):
    if request.method == 'POST':
        print("post method")
        equation = request.POST['equation']
        print(equation)
        # Exception Handling
        try:
            ans = eval(equation)
            print(ans)
            params = {'ans':ans,'log':True,'eq':equation}
        except:
            params = {'error':True}
    # return HttpResponse('ans')
    return render(request,'index.html',params)

def feedback(request):
    if request.method == 'POST':
       
        feedback = request.POST['feedback']
        name = request.POST['name']
        email = request.POST['email']

        print(name,email,feedback)
        
        con = connectTOMail()
        obj = UserFeedback(name=name,email=email,msg=feedback)
        obj.save()
        con.sendmail("arpit456jain@gmail.com",email,"Subject:Feed Back of Calculator app \n\n"+"Thank You for the feed back")
        params = {'msg':True}
    else:
        params = {}
    
    # return HttpResponse('feedback page')
    return render(request,'feedback.html',params)