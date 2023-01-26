from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'pages/contact_us.html')

def send(request):
    subject = request.GET['subject']
    message = request.GET['message']
    send_mail(subject=subject, message=message, from_email='setting.EMAIL_HOST_USER', recipient_list=['lucasmurrayh@gmail.com'], fail_silently=False)
    return render(request, 'pages/contact_us.html')