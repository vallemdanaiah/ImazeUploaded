from django.shortcuts import render
from .models import Imaze
from .forms import ImazeForms
# Create your views here.
def index(request): 
    if request.method == "POST":
        form = ImazeForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        form=ImazeForms()
        img = Imaze.objects.all()
    return render(request,'myapp/home.html',{'img':img,'form':form})