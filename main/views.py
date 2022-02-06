from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Inputt
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

# Create your views here.
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>")

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")
# def index(response,id):
#     ls=ToDoList.objects.get(id=id)
#     # return render(response,"main/base.html",{"name":ls.name})
#     return render(response,"main/base.html",{})

def out(response):
    # return HttpResponse("<h1>tech with tim!</h1>")
    if response.method =="POST":
        form=Inputt(response.POST)
        
        if form.is_valid():
            # form.save()
            itl=50
            text=form.cleaned_data["txt"]
            l=[]
            sentences = nltk.sent_tokenize(text)
            for sentence in sentences:
                words = nltk.word_tokenize(sentence)
                words = [word for word in words if word not in set(stopwords.words('english'))]
                tagged = nltk.pos_tag(words)
                for (word, tag) in tagged:
                    if tag == 'NNP': # If the word is a proper noun
                        l.append(word)


            text=text.upper()
            lis=l
            return render(response,"main/out.html",{"text":text,'itll':itl,'lis':l})
    return render(response,"main/out.html",{"text":"hiiii",'itll':500,'lis':[]})

def home(response):
    if response.method =="POST":
        form=Inputt(response.POST)
        if form.is_valid():
            form.save()
            itl=50
            text=form
            return render(response,"main/out.html",{"text":text,'itll':itl})
        # return render(response,"main/out.html",{"text":text})
    form=Inputt()
    return render(response,"main/home.html",{"form":form})
    # return render(response,"main/home.html",{})
    # return HttpResponse("<h1>view 1!</h1>")



# def create(response):
#     if response.method =="POST":
#         form=CreateNewList(response.POST)
#         n=form.cleaned_data["name"]
#         t=ToDoList(name=n)
#         t.save()
#         return HttpResponseRedirect("/%i" %t.id)
#     else:
#         form=CreateNewList()
#     return render(response,"main/create.html",{"form":form})
