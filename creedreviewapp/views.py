from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def hollywood(request):
    return render(request,'Hollywood.html')
def nollywood(request):
    return render(request,'category.html')
def bollywood(request):
    return render(request,'Bollywood.html')
def korean(request):
    return render(request,'Korean.html')
def movie1(request):
    return render(request,'movie 1.html')
def movie2(request):
    return render(request,'nollymovie2.html')
def movie3(request):
    return render(request,'nollymovie3.html')
def movie4(request):
    return render(request,'nollymovie4.html')
def hollymovie1(request):
    return render(request,'hollymovie1.html')
def hollymovie2(request):
    return render(request,'hollymovie2.html')
def hollymovie3(request):
    return render(request,'hollymovie3.html')
def hollymovie4(request):
    return render(request,'hollymovie4.html')
def bollymovie1(request):
    return render(request,'bollymovie1.html')
def bollymovie2(request):
    return render(request,'bollymovie2.html')
def bollymovie3(request):
    return render(request,'bollymovie3.html')
def bollymovie4(request):
    return render(request,'bollymovie4.html')
def korea1(request):
    return render(request,'korea1.html')
def korea2(request):
    return render(request,'korea2.html')
def korea3(request):
    return render(request,'korea3.html')
def korea4(request):
    return render(request,'korea4.html')


