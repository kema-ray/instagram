from django.shortcuts import render

# Create your views here.
def home(request):
    # title = 'Instagram'

    return render(request,'home.html')