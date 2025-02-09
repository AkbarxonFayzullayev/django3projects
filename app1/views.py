from django.http import HttpResponse
def func1_1(request):
    return HttpResponse("Salom Django,bu 1-Appdagi 1-funksiyam")
def func1_2(request):
    return HttpResponse("Salom,Bu 1-Appdagi ikkinchi funksiyam")
def func1_3(request):
    return HttpResponse("Salom,Bu 1- Appdagi 3-funksiyam")