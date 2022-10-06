from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class Finch:
#     def __init__(self, name, image, description):
#         self.name = name
#         self.image = image
#         self.description = description
    
finches = [
    Finch("House Finch","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/306327341/1800","The house finch is native to western North America and has been introduced to the eastern half of the continent and Hawaii."),
    Finch("American Goldfinch","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/306710541/1800","This finch is yellow and looks like the combination of a bumblebee and a finch."),
    Finch("Eurasian", "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/257629601/1800","Got a bit of orange, grey and black. Looks really dope"),
    Finch("Purple Finch","https://upload.wikimedia.org/wikipedia/commons/4/42/Carpodacus_purpureus_CT3.jpg","The purple finch yo. Sometimes it don't even look purple. It kinda looks red in some pics. Maybe they should call it the red finch.")
]

class FinchesList(TemplateView):
    template_name = "finches_list.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["finches"] = finches
    #     context["finches"] = Finch.objects.all()
    #     return context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["finches"] = Finch.objects.all()
            context["header"] = f"Searching for {name}"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'description', 'verified_finch']
    template_name = "finch_create.html"
    # success_url = "/finches/"
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'description', 'verified_finch']
    template_name = "finch_update.html"
    # success_url = "/finches/"
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finches/"