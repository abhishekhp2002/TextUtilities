#I HAVE CREATED THIS FILE IS NOT FROM SERVER
from string import punctuation

from cytoolz import remove
from django.http import HttpResponse
from django.shortcuts import render
from joblib.testing import param
from sympy.physics.vector.printing import params


def index(request):
    #return HttpResponse("HOME")
    #params={'name':'Abhishek','Place':'Bnegaluru'}
    return render(request,'index.html')
def analyze(request):
    #print(request.GET.get('text','default'))
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    #print(removepunc)
    #analyzed = djtext
    if removepunc =="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzed =""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed
    if(newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed
    if (extraspaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed
    if (removepunc != "on" and newlineremove != "on" and extraspaceremove != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return  render(request,'analyze.html',params)

    """else:
        return HttpResponse("ERROR")"""

"""def index(request):
    return HttpResponse('''<h1>HELLO BHAI</h1> <a href="https://www.youtube.com/@hpdrivinggames336"> HP DRIVING GAMES </a> ''')
def about(request):
    return HttpResponse("Hello Abhishek")
def ex1(request):
    s=''' Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s) """

"""def capfirst(request):
    return HttpResponse("CAPITALIZE FIRST")
def newlineremove(request):
    return HttpResponse("NEWLINE REMOVE")
def spaceremove(request):
    return  HttpResponse("SPACE REMOVE <a href='/'>BACK</a>")
def charcount(request):
    return HttpResponse("CHAR COUNT")"""

