from django.shortcuts import render

# Create your views here.
def index(request):
    APP_NAME = 'myapp'
    msg = 'My Message'
    return render(request, APP_NAME+'/index.html', {'message': msg})