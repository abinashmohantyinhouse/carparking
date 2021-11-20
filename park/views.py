from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from .models import SlotStatus
# Create your views here.
def home(request,pk):
    parking = SlotStatus.objects.get(device_id=pk)
    return JsonResponse({'slot_1':str(parking.slot_1),
    'slot_2':str(parking.slot_2)})

def update_slot_1(request,pk,status):
    slot1 = SlotStatus.objects.get(device_id=pk)
    slot1.slot_1 = status
    slot1.save()
    return redirect('park_home',pk)

def update_slot_2(request,pk,status):
    slot2 = SlotStatus.objects.get(device_id=pk)
    slot2.slot_2 = status
    slot2.save()
    return redirect('park_home',pk)

