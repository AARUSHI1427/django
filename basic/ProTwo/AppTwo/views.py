from django.shortcuts import render
from AppTwo.models import user

# Create your views here.
def index(response):
    return render(response,'AppTwo/index.html')

def users(response):
    user_list= user.objects.order_by('first_name')
    user_dict= {'user':user_list}
    return render(response,'AppTwo/users.html',context=user_dict)
