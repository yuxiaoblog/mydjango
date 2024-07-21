from django.shortcuts import render,HttpResponse
from django.http import HttpResponseForbidden
# Create your views here.

def index_view(request):
    return render(request,'index/index.html')
    # return HttpResponseForbidden()