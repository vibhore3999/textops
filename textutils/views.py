# Views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    #return HttpResponse("home")
def ex1(request):
    sites = ['''<h1>For my poems blog</h1><a href="http://poemlyf.blogspot.com/">my poems</a>''',
             ]
    return HttpResponse((sites))


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("please select operations")
    return render(request, 'analyze.html', params)
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
