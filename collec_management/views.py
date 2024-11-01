from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Collec
from .forms import CollectionForm

# Create your views here.
def index(request):
	return render(request, "index.html")

def about(request):
	return HttpResponse("about page.")

def collection(request, id):
	c = get_object_or_404(Collec, id=id)

	return render(request, "collection.html", {"c": c})

def collections(request):
	collects = Collec.objects.all()

	return render(request, "all.html", {"collects": collects})

def new(request):
	if request.method == 'POST':
		form = CollectionForm(request.POST)
		if form.is_valid():
			c = Collec(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
			c.save()
			return redirect("all")
	else:
		form = CollectionForm()
		return render(request, "new.html", {"form": form})

def change(request, id):
	c = get_object_or_404(Collec, id=id)
	if request.method == 'POST':
		form = CollectionForm(request.POST)
		if form.is_valid():
			c.title = form.cleaned_data['title']
			c.description = form.cleaned_data['description']
			c.save()
			return redirect("all")
	else:
		form = CollectionForm(instance=c)
		return render(request, "change.html", {"form": form, "c":c})

def delete(request, id):
	c = get_object_or_404(Collec, id=id)
	if request.method == 'POST':
		if request.POST['delete'] == "1":
			c.delete()
			return redirect("all")
	else:
		return render(request, "delete.html", {"c": c})