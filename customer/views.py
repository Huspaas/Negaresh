from django.shortcuts import render, HttpResponseRedirect
from .models import contract
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your views here.


def contractForm(request):
    return render(request, 'contractForm.html')


def contractSave(request):
    clientName = request.POST['clientName']
    dealer = request.POST['dealer']
    clientNumber = request.POST['clientNumber']
    tempContract = contract(clientName=clientName,
                            dealer=dealer, clientNumber=clientNumber)
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


# def counter(request):
#     count = contract.objects.filter(get_user_model)