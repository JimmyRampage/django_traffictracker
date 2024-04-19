from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Flan
from .forms import ContactFormForm

# Create your views here.
def index(request):
    flanes = Flan.objects.all()
    flanes_pub = Flan.objects.filter(is_private=False)
    flanes_priv = Flan.objects.filter(is_private=True)
    return render(request, "index.html", {"flanes_pub": flanes_pub})

def about(request):
    return render(request, "about.html", {})
    
def welcome(request):
    return render(request, "welcome.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = ContactFormForm
    return render(request, "contact.html", {"form": form})