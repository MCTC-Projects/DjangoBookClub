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
from bookit.models import BookClub, BookClubMembers, Book

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
        else:
            return render(request,"registration.html",{'form':form}, context_instance=RequestContext(request))

class Instructions(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,"instructions.html")


class AppLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        data = request.GET.get('data','eyJlbWFpbCI6Iml')
        data = bytes(data,'utf-8')
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)

        user = authenticate(username=str(data_dict['email']),password=str(data_dict['password']))
        if user is not None and len(BookClub.objects.filter(owner=user).all())>0:
            result = {"login" : "true"}
        else:
            result = {"login" : "false"}

        return HttpResponse(dumps(result))


class BookDump(TemplateView):
    def get(self, request, *args, **kwargs):
        data = request.GET.get('data',b'224dfasdf')
        data = str.encode(str(data))
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)
        user = authenticate(data_dict['email'],data_dict['password'])
        if user is not None:
            bookclub = BookClub.objects.filter(user=user).first()
            books = Book.objects.filter(bookclub = bookclub)
            books = serializers.serialize('json',books)
            result = {'books':books}

        else:
            result = {'books':'404'}
        return HttpResponse(dumps(result))


    def post(self, request, *args, **kwargs):
        data = request.POST.get('data',b'224dfasdf')
        data = str.encode(str(data))
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)
        user = authenticate(data_dict['email'],data_dict['password'])
        if user is not None:
            books = request.POST.get('books')
            books = loads(books)
            for book in books:
                b=  Book(author=book['author'],title=book['title'])
                b.save()
            return HttpResponse(dumps({'login':'true'}))
        else:
            return HttpResponse(dumps({'login':'false'}))