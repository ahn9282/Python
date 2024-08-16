from django.shortcuts import render
from app import models
from django.shortcuts import render, redirect
from app.models import Contact

# Create your views here.
def thanks_view(request):
    data = Contact.objects.all()
    username = data[len(data) - 1].name
    return render(request, 'thanks.html',{'name':username})

def main_view(request):
    return render(request, 'main.html')

def test_view(request):
    return render(request, 'test.html')
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('thanks')

    return render(request, 'contact.html')