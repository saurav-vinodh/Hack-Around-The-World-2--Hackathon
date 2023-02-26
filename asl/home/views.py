from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
import requests
from home.models import Task




def home(request):
    return render(request, 'index.html')

def upload(request):

    global context
    context={}
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)
        context={'url':fs.url(name)}
        title=request.POST['story']
        ins=Task(taskTitle=title)
        ins.save()
    return render(request, 'upload.html',context)

def translate(request):
    
    if request.method=='POST':
        title=request.POST['transtext']
        url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"

        querystring = {"langpair":"fr|en","q":"","mt":"1","onlyprivate":"0","de":"a@b.c"}
        querystring['q']=title

        headers = {
            "X-RapidAPI-Key": "6199b53bf7msh2e016ae3e5e685ep19513fjsne90f296150e2",
            "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        context['translated']=response.json()['responseData']['translatedText']

        return render(request,'video.html',context)


    return render(request,'translate.html',context)


