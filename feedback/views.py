from django.shortcuts import render
from . forms import feedbackForm
from . forms import studentForm
from . models import Students
from . models import Feedback
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    feedbacks = Feedback.objects.filter(owner=request.user.id)
    context={'feedbacks':feedbacks}
    return render(request,'feedback/index.html', context)

@login_required
def create_feedback(request):
    form = feedbackForm(request.POST or None)
    context = {'form': form}
    

    if request.method=="POST":

        
        feedback= request.POST.get('feedback')
        feedback_reply= request.POST.get('feedback_reply')
        #department_id=request.POST.get('department_id')
        unit_name=request.POST.get('unit_name')
        



        feedback=Feedback()

        
        feedback.feedback= feedback
        feedback.feedback_reply = feedback_reply
        #feedback.department_id=department_id
        feedback.unit_name=unit_name
        feedback.owner = request.user
       
        

        feedback.save()

        messages.add_message(request, messages.SUCCESS, "feedback created successfully ")

        return HttpResponseRedirect(reverse('history', kwargs={'id':feedback.pk}))

    return render(request, 'feedback/create_feedback.html',context)
@login_required
def feedback_history(request,id):
    history = get_object_or_404(Feedback, pk=id)
    context={'history':history}
    return render(request, 'feedback/feedback-history.html', context)

@login_required
def delete_history(request,id):
    history = get_object_or_404(Feedback, pk=id)
    context={'history':history}

    if request.method=='POST':
        if history.owner== request.user:
             history.delete()
             return HttpResponseRedirect(reverse('home'))
        return render(request, 'feedback/delete_history.html', context)

    return render(request, 'feedback/delete_history.html', context)

@login_required
def edit_history(request,id):
    history = get_object_or_404(Feedback, pk=id)
   
    form=feedbackForm(instance=history)
    context={'history':history, 'form':form}

    if request.method=="POST":
        
        feedback= request.POST.get('feedback')
        feedback_reply= request.POST.get('feedback_reply')
        #department_id=request.POST.get('department_id')
        unit_name=request.POST.get('unit_name')
        


        feedback=Feedback()


        feedback.feedback= feedback
        feedback.feedback_reply = feedback_reply
        #feedback.department_id=department_id
        feedback.unit_name=unit_name
        

        
        feedback.save()
        
        messages.add_message(request, messages.SUCCESS, "feedback updated successfully "
        )

        return HttpResponseRedirect(reverse('history', kwargs={'id':feedback.pk}))


    return render(request, 'feedback/edit_history.html',context)


    




def student_profile(request):
    return render(request, 'feedback/student_profile.html')


def handle_error(request,exception):
    return render(request, 'error_page.html')


def handle_server_error(request):
    return render(request, 'server_error_page.html')
@login_required
def updateProfile(request):
    form=studentForm
    context = {'form': form}

    if request.method=="POST":

        student_id = request.POST.get('student_id')
        gender= request.POST.get('gender')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        reg_No=request.POST.get('reg_No')
        profile_pic= request.POST.get('profile_pic')
        session_year=request.POST.get('session_year')
        address=request.POST.get('address')


        profile=Students()

        profile.student_id= student_id
        profile.gender= gender
        profile.first_name=first_name
        profile.last_name=last_name
        profile.reg_No=reg_No
        profile.profile_pic = profile_pic
        profile.session_year=session_year
        profile.address=address
        
        profile.save()

        messages.add_message(request, messages.SUCCESS, "profile updated successfully "
        )

    return render(request, 'feedback/update_profile.html',context)

def search(request):
    if request.method=="POST":
        searcher=request.POST['searcher']
        feedback=Feedback.objects.filter(feedback__contains=searcher)
        return render(request, 'feedback/search.html',{'searcher':searcher},{'feedback':feedback})
    else:
        return render(request, 'feedback/search.html')



