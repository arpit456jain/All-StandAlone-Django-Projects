from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
global count_freq
count_freq = dict()
languages = ['Java','Python','C++','C','PHP']
def index(request):
    params = {'languages':languages}
    return render(request, 'index.html',params)

def getQuery(request):
    q = request.GET['languages']
    #using hashing we count freq of voting 
    if q in languages:    
        if q in count_freq.keys():
            count_freq[q] +=1
        else:
            count_freq[q] = 1
        print(count_freq)
        params = {'languages':languages,'count_freq':count_freq,"error":False}
    else:
        params = {'languages':languages,'count_freq':count_freq,"error":True}
    return render(request, 'index.html',params)