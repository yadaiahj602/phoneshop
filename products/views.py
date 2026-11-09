from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Phone

# Create your views here.
def base(request):
  return render(request,'base.html')

def index(request):
  total = Phone.objects.all()
  tot = total.count()
  context = {
    'total':total,
    'tot':tot,
  }
  return render(request,'index.html',context)

def details(request,pk):
  tota = get_object_or_404(Phone,pk=pk)
  context = {
    'tota':tota,
  }
  return render(request,'product-details.html',context)
  
def list(request):
  tos = Phone.objects.all()
  context = {
    'tos':tos,
  }
  return render(request,'list.html',context)

def add(request):
  if request.method == "POST":
    phone_name = request.POST['phone_name']
    brand = request.POST['brand']
    price = request.POST['price']
    image = request.FILES.get('image')
    quantity = request.POST['quantity']
    description = request.POST['description']
    
    Phone.objects.create(
      phone_name=phone_name,
      brand=brand,
      price=price,
      image=image,
      quantity =quantity ,
      description=description,
    )
    return redirect('home')
  return render(request,'add.html')

def edit(request,pk):
  edi=get_object_or_404(Phone,pk=pk)
  if request.method == "POST":
    edi.phone_name = request.POST['phone_name']
    edi.brand = request.POST['brand']
    edi.price = request.POST['price']
    edi.image = request.FILES.get('image')
    edi.quantity = request.POST['quantity']
    edi.description = request.POST['description']
    edi.save()
    return redirect('home')
  context = {
    'edi':edi,
    }
  return render(request,'edit.html',context)
    

def delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)

    if request.method == "POST":
        phone.delete()
        return redirect('home')

    return render(request, 'delete.html', {'phone': phone})