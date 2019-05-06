from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from .forms import SignupForm
class Home(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Form submitted successfully")

class SignUp(View):
    form = SignupForm()

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            print(user.username)
            #return HttpResponse('submitted successfully')
            return redirect('home')
            #return render(request, 'poll/index.html', {'form': form})
    def get(self, request, *args, **kwargs):
        form = SignupForm()
                #return HttpResponse("submitted successfully")
        return render(request, 'poll/index.html', {'form': form})
    #     if request.user.is_authenticated:
    #         #return HttpResponse("submitted successfully")
    #         return render(request,'poll/index.html',{'form':form})
    #     else:
    #         form = SignupForm()
    #         #return HttpResponse("submitted successfully")
    #         return render(request, 'poll/index.html', {'form': form})




# Create your views here.
