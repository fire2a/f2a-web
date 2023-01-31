from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'pages/contact_us.html')

def send(request):
    message = request.GET['message']
    sender = request.GET['name']
    subject = sender + ": " + request.GET['subject']
    address = request.GET['email']
    send_mail(subject=subject, message=message, from_email='setting.EMAIL_HOST_USER', recipient_list=['lucasmurrayh@gmail.com', address], fail_silently=False)
    return render(request, 'pages/contact_us.html')