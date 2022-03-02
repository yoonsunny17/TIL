from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')
    # return render(A, B, C) 
    #=> A: request(고정), B: template file(어떤 file을 rendering해서 줄건지), C(optional): view와 template이 자료를 주고 받는 창구 자리
    # return HttpResponse("<h1>Hello!</h1>") 