from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from bookit.BookForms import BookClubRegistration, UserLogin
from django.http import HttpResponseRedirect

class MainLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UserLogin()
        return render()







class Registration(TemplateView):
    def get(self,request, *args,**kwargs):
        form = BookClubRegistration()
        return render(request,"registration.html",{'form':form},context_instance=RequestContext(request))

    def post(self,request, *args,**kwargs):
        form = BookClubRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/instructions/")


class Instructions(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,"instructions.html")