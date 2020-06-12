from django.shortcuts import render,redirect
from .models import Profile,Subjects,cards
from .forms import SubjectForm, CardForm,Profileform
# Create your views here.
def index(request):
    all_cards = cards.objects.all()
    
    
    subjects=Subjects.objects.all()    
    
    return render(request,'index.html',{'subjects':subjects,"all_cards": all_cards})

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
    subjects=Subjects.objects.all() 
    searched_subject = Subjects.objects.filter(subjects=subject ,user_id=current_user).first()
    print(searched_subject)
       
    message = f"{subject}"
    
    return render(request, 'index.html',{"message":message,'searched_subject':searched_subject, 'subjects':subjects})

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

def delete(request, id):
    card = cards.objects.filter(title=id).delete()
    
    return redirect("index")

    # return render(request, "delete.html")
