from django import views
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from flask_login import login_url
from computerApp.models import Machine
from computerApp.forms import AddMachineForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required(login_url='/account/login/')
def my_view(request):
	if not request.user.is_authenticated:
		return redirect('/accounts/login/')

def login (request) :
	context = {}
	return render (request, 'registration/login.html', context)

def index (request) :
	machines = Machine.objects.all()
	context = {'machines': machines}
	return render (request, 'index.html', context)

def machine_list_view (request) :
	machines = Machine.objects.all()
	context = {'machines': machines}
	return render(request, 'computerapp/machine_list.html',context)	

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request, 'computerapp/machine_detail.html', context)

def machine_add_form(request):
	if request.method == 'POST':
		form = AddMachineForm(request.POST or None)
		if form.is_valid():
			new_machine = Machine(nom=form.cleaned_data['nom'])
			new_machine.save()
			return redirect('machines')
	else :
		form = AddMachineForm()
		context = {'form' : form}
		return render(request,
	 	 'computerapp/machine_add.html',context)