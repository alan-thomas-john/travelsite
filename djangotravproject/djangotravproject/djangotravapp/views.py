from django.shortcuts import render
from.models import Place
from.models import Photo
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objj = Photo.objects.all()
    return render(request, "index.html",{'result':obj,'result2':objj})
#def demo1(request):
    #objj=Photo.objects.all()
   # return render(request, "index.html",{'result2':objj})