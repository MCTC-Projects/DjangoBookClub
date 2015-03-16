from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers

from base64 import urlsafe_b64decode
from json import loads,dumps

from bookit.BookForms import BookClubRegistration
from django.http import HttpResponseRedirect,HttpResponse
from bookit.models import BookClub, BookClubMembers

class MainLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm
        return render(request, 'main.html', {'form':form})

    def post(self,request, *args, **kwargs):
        username = request.POST['username']
        user_password = request.POST['password']
        user = authenticate(username=username, password = user_password)
        if user is not None:
            if user.is_active:
                login(request,user)
                bookclub = serializers.serialize('json', BookClubMembers.objects.filter(user = user).all(),use_natural_foreign_keys=True,fields=('bookclub',))
                return render(request,'bookclub.html',{'bookclub':bookclub})

        else:
            form = AuthenticationForm
            return render(request, 'main.html', {'form':form, 'message':"Try again."})



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
        user = authenticate(data_dict['email'],data_dict['password'])
        if user is not None and len(BookClub.objects.filter(user=user).all())>0:
            result = {'login' : 'true'}
        else:
            result = {'login' : 'false'}

        return HttpResponse(dumps(result))

