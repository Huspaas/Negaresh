from django.shortcuts import render, HttpResponseRedirect
from .models import contract
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import Count    
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate
# Create your views here.


def contractForm(request):
    return render(request, 'contractForm.html')


def contractSave(request):
    clientName = request.POST['clientName']
    dealer = request.POST['dealer']
    clientNumber = request.POST['clientNumber']
    print(request.user.id)
    tempContract = contract(clientName=clientName,
                            dealer=dealer, clientNumber=clientNumber , publisher=request.user)
    tempContract.save()
    return HttpResponseRedirect(reverse('contractForm'))


def manageContract(request):
    context = {
        'contracts': reversed(contract.objects.all())
    }
    return render(request, 'ManageContract.html', context)


def deleteContract(request, id):
    tempContract = contract.objects.get(id=id)
    tempContract.delete()
    return HttpResponseRedirect(reverse('manageContract'))


def editContract(request, id):
        context = {'contract': contract.objects.get(id=id)}
        return render(request, 'editContract.html', context)


def submitEditContract(request , id):
    tempContract = contract.objects.get(id =id)
    tempContract.clientName = request.POST['clientName']
    tempContract.dealer = request.POST['dealer']
    tempContract.clientNumber = request.POST['clientNumber']
    tempContract.save()
    return HttpResponseRedirect(reverse('manageContract'))



def empolyes(request):
    context = {
        'employes':get_user_model().objects.all(),
        'totalContracts':User.objects.annotate(total = Count('contract'))
    }
    return render(request , 'employes.html' , context)


def employe(request):
    context={}
    return render(request , 'employe.html' , context)


def signupEmploy(request):
    if request.method == 'POST':
        user = request.POST['username']
        name = request.POST['name']
        family = request.POST['family']
        password = request.POST['password']
        form = User.objects.create_user(username=user,first_name=name,last_name=family,password=password)
        form.save()
        return HttpResponseRedirect(reverse('home'))
    else: return render(request , 'signupEmploy.html')


def loginEmploy(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect(reverse('home'))