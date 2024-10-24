from django.shortcuts import render,get_object_or_404, redirect
from .models import Cause
from .forms import causeForm
from BimsCharity.userApp.models import Profile
from django.contrib import messages


# Create your views here.
def addcauseView(request):
    if request.method == 'POST':
        form = causeForm(request.POST,  request.FILES)
        if form.is_valid():
            cause_form = form.save(commit=False)
            created_by = Profile.objects.get(user_id = request.user.id)
            cause_form.created_by = created_by
            cause_form.save()

            messages.success(request, 'cause created')
            return redirect('home')
        else:
            messages.error(request, 'Error creating a cause')
            return render(request, template_name='causesApp/create_cause.html', context={'causeForm':form})
    else:
        form = causeForm()
        return render(request, template_name='causesApp/create_cause.html', context={'causeForm':form}) 
 
    
def deletecauseView(request, id):
    deletecause = Cause.objects.get(cause_id = id)
    deletecause.delete()
    return redirect('all-cause')

def editcauseView(request, id):
    causeObject = get_object_or_404(Cause, cause_id = id)

    if request.method == 'POST':
        form = causeForm(request.POST, request.FILES, instance=causeObject)
        if form.is_valid():
            form.save()

            messages.success(request, 'cause edited')
            return redirect('all-cause')
        else:
            messages.error(request, 'Error editing a cause')
            return render(request, template_name='causesApp/edit_cause.html', context={'editCauseForm':form})   

    else:
        form = causeForm(instance=causeObject)
        return render(request, template_name='causesApp/edit_cause.html', context={'editCauseForm':form})
    

def allcauseView(request):
    allcause = Cause.objects.all()
    print(allcause)
    return render(request, template_name='index.html', context={'allcause': allcause})

def allcauses(request):
    allcause = Cause.objects.all()
    # print(allcause)
    return render(request, template_name='causesApp/all_cause.html', context={'allcause': allcause})





















# ef allPostView(request):
    # allPost = BlogInfo.objects.all()
    # return render(request, template_name='index.html', context={'allpost':allPost}) 