from django.shortcuts import render
from app import models
import random
import string
from django.shortcuts import render, redirect
from app.models import Contact
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def thanks_view(request):
    data = Contact.objects.all()
    username = data[len(data)-1].name
    image = data[len(data)-1].image
    print(image)
    if image:
        print('o ing')
        return render(request, 'thanks.html',{'name':username, 'image':image})
    else:
        print('no ing')
        return render(request, 'thanks.html', {'name': username})


def main_view(request):
    return render(request, 'main.html')

def test_view(request):
    return render(request, 'test.html')
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        image = request.FILES.get('photo')
        print(name, email, message)

        if image:
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            imgname = f'photo_{random_string}.jpg'
            media_path = os.path.join(settings.BASE_DIR, 'app/static/images')
            fs = FileSystemStorage(location=media_path)
            file_name = fs.save(imgname, image)
            file_url = fs.url(file_name)

            print('Uploaded IMG:', imgname)
            print('File URL:', file_url)
            print('path : ', fs.path(imgname))
        else:
            print('no img in views')
            imgname = None

        Contact.objects.create(name=name, email=email, message=message, image=imgname)
        return redirect('thanks')

    return render(request, 'contact.html')
