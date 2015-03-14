from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext

from base64 import urlsafe_b64decode
from json import loads,dumps

from bookit.BookForms import BookClubRegistration, UserLogin
from django.http import HttpResponseRedirect,HttpResponse
from bookit.models import BookClub,User

class MainLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UserLogin()
        return render(request,'main.html',{'form':form})

    def post(self,request, *args, **kwargs):
        form = UserLogin(request.POST)
        if form.is_valid():
            user = User.objects.filter(email_address=form.data['email_address']).filter(password=form.data['password'])
            if len(user)>0:
                return HttpResponse("You won.")
            else:
                return render(request,'main.html', {'form':form})
        else:
            return render(request, 'main.html',{'form':form})





class Registration(TemplateView):
    def get(self,request, *args,**kwargs):
        form = BookClubRegistration()
        return render(request,"registration.html",{'form':form},context_instance=RequestContext(request))

    def post(self,request, *args,**kwargs):
        form = BookClubRegistration(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/instructions/")


class Instructions(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,"instructions.html")


class AppLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        data = request.GET.get('data',b'224dfasdf')
        data = str.encode(str(data))
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)
        if len(BookClub.objects.filter(owners_email_address=data_dict['email']))==0:
            result = {'login':'false'}
        else:
            if len(BookClub.objects.filter(owners_email_address=data_dict['email']).filter(owners_password=data_dict['password']))>0:
                result = {'login':'true'}
            else:
                result = {'login':'false'}
        return HttpResponse(dumps(result))