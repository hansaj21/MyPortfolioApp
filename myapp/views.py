from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	Contact.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		subject=request.POST['subject'],
		message=request.POST['message'],
		)
	msg="Message Saved Successfully.Will reach you very soon."
	return render(request,'index.html',{'msg':msg})

