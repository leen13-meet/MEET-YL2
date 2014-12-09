from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Answer
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request

def wazap(request):
	return render(request, 'polls/detail.html',{})
	

