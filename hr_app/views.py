from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Register


def Register_fun(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            register = form.save()
            # Generate QR code for the registered user
            register.generate_qr_code()
            return redirect('Registration_sucess')
    else:
        form = RegisterForm()
    return render(request, 'hr_app/register.html', {'form': form})

def Register_form_sucess(request):
    registers = Register.objects.all()
    return render(request, 'hr_app/Registration_success.html', {'registers': registers})


def qr_code(request, id):
    register = Register.objects.get(id=id)
    qr_image = register.qr_code
    return HttpResponse(qr_image.read(), content_type="image/png")




def details(request, id):
    registers = Register.objects.get(id=id)
    return render(request, 'hr_app/card.html', {'registers': registers})