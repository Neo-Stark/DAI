from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {'usuario':'Ivan',
    }
    return render(request,'test.html', context)
