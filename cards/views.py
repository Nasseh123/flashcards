from django.shortcuts import render,redirect
from .models import Profile,Subjects,cards
from .forms import SubjectForm, CardForm
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

def new_card(request):
    current_user = request.user
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = current_user
            card.save()
        return redirect('index')
    else:
        form = CardForm()
    return render(request, 'new_card.html', {'form': form})