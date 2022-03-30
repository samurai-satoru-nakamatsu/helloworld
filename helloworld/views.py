from django.http import HttpRequest, HttpResponse


from django.http import HttpResponse

def helloworld(request):
    return HttpResponse('Hello world.')