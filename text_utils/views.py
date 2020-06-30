# I have created this file - Deepak
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def analyze(request):
    #get the text
    djtext=request.POST.get('text' , 'off')
    print(djtext)

    removepunc=request.POST.get('removepunc' , 'off')
    print(removepunc)

    fullcaps=request.POST.get('fullcaps' , 'off')
    print(fullcaps)

    newlineremover=request.POST.get('newlineremover' , 'off')
    print(newlineremover)

    extraspaceremover=request.POST.get('extraspaceremover' , 'off')
    print(extraspaceremover)
                                                            #remove punctuatioons
    if removepunc=='on':
        punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''

        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed
        params={'purpose':'removed punctuations','analyzed_text':analyzed}

        #analyze the text
        #return render(request,'analyze.html',params)

                                                           #convert lower case into upper case
    if fullcaps =='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext=analyzed
        params={ 'purpose' : 'convert into upper case' , 'analyzed_text' : analyzed }
        # return render(request,'analyze.html',params)

                                                                            #new line remove from the text
    if newlineremover == 'on':
        analyzed=''
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        djtext=analyzed
        params={ 'purpose' : 'new line remove' , 'analyzed_text' : analyzed }
        # return render(request,'analyze.html',params)

                                                                         # extra space remove from the text
    if extraspaceremover == 'on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        djtext=analyzed
        params={ 'purpose' : 'remove extra space' , 'analyzed_text' : analyzed }

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
        return HttpResponse('please select the any operations')

    return render(request,'analyze.html',params)



# def capitalizefirst(request):
#     return HttpResponse("capitalize first <a href='/'>back</a>")
#
# def newlineremove(request):
#     return HttpResponse("new line remove <a href='/'>back</a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character count <a href='/'>back</a>")