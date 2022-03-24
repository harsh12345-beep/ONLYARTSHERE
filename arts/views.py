from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Image, photo
# Create your views here.
def index(request):
    image =  Image.objects.all()
    context = {'image':image}
    return render(request,"arts/index.html" ,context)

def addyour(request):
    if request.method == "POST":
        Heading= request.POST.get('heading')
        Typee= request.POST.get('type')
        Imagee = request.POST.get('image')
        ab = Image(heading=Heading,maintext=Typee,image=Imagee)
        ab.save()
        return redirect("/")
    return render(request,"arts/addyour.html")