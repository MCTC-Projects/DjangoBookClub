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
                bookclub=BookClubMembers.objects.filter(user = user).all()
                bookclub_json = serializers.serialize('json',bookclub ,use_natural_foreign_keys=True,fields=('bookclub',))
                books=''
                for bc in bookclub:
                    books += serializers.serialize('json',Book.objects.filter(bookclub=bc).all(),fields=('title','author','description','bookclub'),use_natural_foreign_keys=True)
                return render(request,'bookclub.html',{'bookclub':bookclub_json,'books':books})

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
            form.save(commit=True)
            return HttpResponseRedirect("/instructions/")
        else:
            return render(request,"registration.html",{'form':form}, context_instance=RequestContext(request))

class Instructions(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,"instructions.html")


class AppLogin(TemplateView):
    def get(self, request, *args, **kwargs):
        data = str(request.GET.get('data','eyJlbWFpbCI6Iml'))
        data = data.encode('utf-8')
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)

        user = authenticate(username=str(data_dict['email']),password=str(data_dict['password']))
        if user is not None and len(BookClub.objects.filter(owner=user).all())>0:
            result = {"login":True}
        else:
            result = {"login":False}
        return HttpResponse(dumps(result))


class BookDump(TemplateView):
    def get(self, request, *args, **kwargs):
        data = request.GET.get('data',b'224dfasdf')
        data = data.encode('utf-8')
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)
        user = authenticate(username=str(data_dict['email']),password=str(data_dict['password']))
        if user is not None:
            bookclub = BookClub.objects.filter(owner=user).first()
            books = Book.objects.filter(bookclub = bookclub)
            books = serializers.serialize('python',books)
            results = books
        else:
            results = []
        return HttpResponse(dumps(results))


    def post(self, request, *args, **kwargs):
        data = request.POST.get('data','eyJlbWFpbCI6Iml')
        data = data.encode('utf-8')
        data_decoded = urlsafe_b64decode(data).decode('utf-8')
        data_dict = loads(data_decoded)
        user = authenticate(username=str(data_dict['email']),password=str(data_dict['password']))
        if user is not None:
            bookclub = BookClub.objects.filter(owner=user).first()
            books = request.POST.get('books')
            book_data = loads(books)
            for book in book_data:
                b = Book(title = book['title'],author = book['author'],isbn = book['isbn'],bookclub = bookclub)
                b.save()
            results = {'login':True}
        else:
            results = {'login':False}
        return HttpResponse(dumps(results))