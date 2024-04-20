from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from .models import Flan, ContactForm
from .forms import ContactFormForm

# Create your views here.
def index(request):
    flanes = Flan.objects.all()
    flanes_pub = Flan.objects.filter(is_private=False)
    flanes_priv = Flan.objects.filter(is_private=True)
    return render(request, "index.html", {"flanes_pub": flanes_pub})

def about(request):
    return render(request, "about.html", {})
    
def success(request):
    return render(request, "success.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/success")
    else:
        form = ContactFormForm
    return render(request, "contact.html", {"form": form})

class LoginRequiredMixin(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class Welcome(LoginRequiredMixin, TemplateView):
    template_name = "welcome.html"