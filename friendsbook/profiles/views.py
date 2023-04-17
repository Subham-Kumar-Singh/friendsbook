from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm

# Create your views here.


def my_profile_view(request):
    confirm=False
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        fm = ProfileModelForm(request.POST, instance=profile)
        if fm.is_valid():
            fm.save()
            confirm=True
    else:
        fm = ProfileModelForm(instance=profile)
    return render(request, 'profiles/myprofile.html', {"form":fm,"confirm":confirm})
