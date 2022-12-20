from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users

def index(request):
    my_users = Users.objects.all().values()
    template = loader.get_template('users_index.html')
    context = {
        'my_users' : my_users,
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
