""" from django.shortcuts import render,redirect
from .forms import LoginForm,authenticationForm,qusetionForm
from .models import User,Chapter
import PyPDF2

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .Models import models
import random
import json




def index(request):
    return render(request,'pages/index.html')

def authentications(request):
    login_form = LoginForm(request.POST or None)
    signup_form = authenticationForm(request.POST or None)
    if request.method == 'POST':
       if 'login_submit' in request.POST and login_form.is_valid():
            email = login_form.cleaned_data['email']
            request.session['email'] = email
            if User.objects.filter(email=email).exists():
                return redirect('profile')
            else:
                return redirect('signup')
         
       elif 'signup_submit' in request.POST and signup_form.is_valid():
            signup_form.save()
            return redirect('signup')
 

    context = {
        'form1': login_form,
        'form2': signup_form
    }
    return render(request, 'authentication/signUp.html', context)

def convert_pdf_text(pdf_file):
    try:
        pdffileobj = open(pdf_file, 'rb')
        pdfreader = PyPDF2.PdfReader(pdffileobj)
        x = len(pdfreader.pages)
        pageobj = pdfreader.pages[x - 1]
        text = pageobj.extract_text()
        file1 = open(r"myfile", "w")
        file1.writelines(text)
        file1.close()
        print("Text extracted and saved successfully!")
        return file1

    except Exception as e:
         print(f"An error occurred: {e}")
         return None

def CreateQuestion(request):
    if request.method=='POST':
        form=qusetionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form=qusetionForm() 
    return render(request,'pages/question.html',{'form':form})




@csrf_exempt
def process(request):
    if request.method == 'POST':
        data_json = json.loads(request.body.decode('utf-8'))
        input_text = data_json['input_text']
        max_answers = int(data_json['max_answers'])
        input_text = ' '.join(input_text.split())
        generate_distractor = bool(int(data_json['generate_distractor']))

        questions_t5, _answers_t5 = models.generate_from_T5(input_text, n=max_answers)
        answers_t5 = []
        for a in _answers_t5:
            if not generate_distractor:
                ans = [(a, True)]
            else:
                dis = models.generate_distractor(a, 4)
                ans = [(a, True)] + dis
            random.shuffle(ans)
            answers_t5.append(ans)

        return JsonResponse({'questions': questions_t5, 'answers': answers_t5})

    return JsonResponse({'error': 'Invalid request method'}, status=400) """