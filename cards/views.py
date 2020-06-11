from django.shortcuts import render,redirect
from .models import Profile,Subjects,cards
from .forms import SubjectForm
# Create your views here.
def index(request):
    
    subjects=Subjects.objects.all()    
    
    return render(request,'index.html',{'subjects':subjects})

def newsubject(request):
    current_user =request.user

    if request.method=='POST':
        subjectform=SubjectForm(request.POST)
        
        
        if subjectform.is_valid() :
            subject=subjectform.cleaned_data['subject']
            existsubject=Subjects.objects.filter(subjects=subject,user_id=current_user)
            if len(existsubject)<1:
                newsubject=Subjects(subjects=subject,user=current_user)
                newsubject.save()
                return redirect ('index')
            else:
                message=f'{subject} flash card already exist!'
                return render(request,'newsubject.html',{'subjectform':subjectform , 'message':message})
    else:
        subjectform=SubjectForm()
        
    return render(request,'newsubject.html',{'subjectform':subjectform ,})

def subject(request,subject):
    current_user =request.user
    subjects=Subjects.objects.all() 
    searched_subject = Subjects.objects.filter(subjects=subject ,user_id=current_user).first()
    print(searched_subject)
       
    message = f"{subject}"

    return render(request, 'index.html',{"message":message,'searched_subject':searched_subject, 'subjects':subjects})
