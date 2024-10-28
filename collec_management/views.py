from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Collec

# Create your views here.
def about(request):
	return HttpResponse("about page.")

def collection(request, id):
	c = get_object_or_404(Collec, id=id)

	return render(request, "collection.html", {"c": c})

def collections(request):
	collects = Collec.objects.all()

	return render(request, "all.html", {"collects": collects})