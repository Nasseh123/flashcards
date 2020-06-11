from django.shortcuts import render
from .models import Profile,Subjects,cards
from .forms import SubjectForm
# Create your views here.
def index(request):

    return render(request,'index.html')

def newsubject(request):
    current_user =request.user

    if request.method=='POST':
        subjectform=SubjectForm(request.POST)
        
        if subjectform.is_valid():
            subject=subjectform.save(commit=False)
            subject.user=current_user
            subject.save()

        return redirect ('index')
    else:
        subjectform=SubjectForm()
    
    return render(request,'newsubject.html',{'subjectform':subjectform})