from django.shortcuts import render_to_response,HttpResponse
from django.views.generic import TemplateView
from BookForms import LoginForm, RegistrationForm, NewBooClubForm


class MainLogin(TemplateView):
    def get(self, request, *args, **kwargs):



    def post(self,request, *args, **kwargs):
