from django.shortcuts import render, HttpResponse

# Create your views here.
def covid(request):
    return render(request, "covid/dashboard.html")