from django.shortcuts import render,redirect
from .models import Profile,Subjects,cards
from .forms import SubjectForm, CardForm,Profileform,UpdateForm
# Create your views here.
def index(request):
    current_user=request.user
    all_cards = cards.objects.filter(user=current_user)
    
    updateformd=UpdateForm()
   
    subjects=Subjects.objects.filter(user=current_user)    
    
    return render(request,'index.html',{'subjects':subjects,"all_cards": all_cards,'updateformd':updateformd})

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
        
    return render(request,'newsubject.html',{'subjectform':subjectform ,})

def subject(request,subject):
    current_user =request.user
    subjects=Subjects.objects.filter(user=current_user)
    subjectid=Subjects.objects.get(subjects=subject)
    all_cards = cards.objects.filter(subject=subjectid.id ,user_id=current_user)
    print(all_cards)
       
    message = f"{subject}"
    updateformd=UpdateForm()
    return render(request, 'index.html',{"message":message,'all_cards':all_cards, 'subjects':subjects,'updateformd':updateformd})

def profile(request,id):
    profile=Profile.objects.get(user_id=id)
    print(profile.user.id)
    if request.method=='POST':
        profiledform=Profileform(request.POST,request.FILES,instance=profile)

        if profiledform.is_valid():
            profiledform.save()
            return redirect('profile' ,id=id)
    else:
        profiledform=Profileform()

    return render(request,'profile.html',{'profile':profile,'profiledform':profiledform})

def update(request,id):
    cardinstance=cards.objects.get(id=id)
    if request.method == 'POST':
        updateformd = UpdateForm(request.POST, request.FILES,instance=cardinstance)
        if updateformd.is_valid():
            updateformd.save()
        
        return redirect('index')
        
