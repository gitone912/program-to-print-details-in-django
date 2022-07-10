from django.shortcuts import render
from .models import user
# Create your views here.
def user_func(request):
    data=user.objects.all()
    context={'data':data}
    return render(request,'index.html',context)