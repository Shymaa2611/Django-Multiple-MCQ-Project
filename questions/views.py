from django.shortcuts import render,redirect
from .forms import authenticationForm,qusetionForm,LoginForm
from .models import User,Chapter
import fitz
import random
from .Models import models

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question')
        else:
            return redirect('question')
    else:
        form =LoginForm()
    return render(request,'authentication/login.html',{'form':form})

def index(request):
    return render(request,'pages/index.html')


def signUp(request):
    if request.method=='POST':
     form=authenticationForm(request.POST)
     if form.is_valid():
         form.save()
         return redirect('login')
    else:
        form=authenticationForm()
    return render(request, 'authentication/signUp.html',{'form':form})


def extract_pdf_content(file):
    pdf_document = fitz.open(file)
    text = ""
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text += page.get_text()
    return str(text)

def CreateQuestion(request):
    ques = None
    ans = None
    qa_pairs = None
    if request.method == 'POST':
        form = qusetionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = form.cleaned_data['chapter']
            context = extract_pdf_content("media/chapters/" + str(data))
            ques, ans = models.generateMCQQA(context)
            qa_pairs = list(zip(ques, ans))

    else:
        form = qusetionForm()

    return render(request, 'pages/question.html', {'form': form, 'qa_pairs': qa_pairs})
 


