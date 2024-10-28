from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Collec

# Create your views here.
def about(request):
	return HttpResponse("about page.")