from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Flan, ContactForm
from .forms import ContactFormForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        flans = Flan.objects.all().values()
        for f in flans:
            f["new_price"] = round(f["price"] * 0.9, 2)
    else:
        flans = Flan.objects.filter(is_private=False).values()
    return render(request, "index.html", {"flans": flans})

def about(request):
    return render(request, "about.html", {})
    
def success(request):
    return render(request, "success.html", {})

def contact(request):
    if request.method == "POST":
        print(request.POST)
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/success")
        else:
            print("HUBO UN ERROR CON LOS DATOS DEL FORMULARIO")
    else:
        form = ContactFormForm
    return render(request, "contact.html", {"form": form})

def flan_recipe(request, slug):
    flan = Flan.objects.filter(slug=slug).values()[0]
    return render(request, "flan_recipe.html", {"flan": flan})

@login_required
def welcome(request):
    return render(request, "welcome.html", {})