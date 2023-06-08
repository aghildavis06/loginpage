from django.shortcuts import render,redirect
from . models import crud
from .forms import items_form
from django.views.generic import ListView

# # Create your views here.
# def home(request):
#     items=crud.objects.all()
#     if request.method=='POST':
#         sl=request.POST['sl']
#         name=request.POST['name']
#         description=request.POST['description']
#         obj=crud(name=name,description=description)
#         obj.save()
#     print('items saved ')
    
#     return render (request,'index.html',{'items':items})

# def delete(request, id):
#     item = crud.objects.get(id=id)
#     if request.method == 'POST':
        
#         item.delete()
#         return redirect('/')
#     print('item deleted')
#     return redirect('/')

# # def update(request, id):
# #     items = crud.objects.get(id=id)
# #     item_form = items_form(request.POST or None, instance=items)
# #     if item_form.is_valid():
# #         item_form.save()
# #         return redirect('/')
# #     return render(request, 'update.html', {'items': items, 'item_form': item_form})


# def update(request,id):
    
#     task1=crud.objects.get(id=id)
#     if request.method=="POST":
#         slnumber=request.POST.get('slnumber','')
#         itemname=request.POST.get('itemname','')
#         description=request.POST.get('description','')
#         task1.slnumber=slnumber
#         task1.itemname=itemname
#         task1.description=description
#         task1.save()
#         return redirect('/')
#     return render(request,'updates.html',{"task1":task1})




class MyModelListView(ListView):
    model = crud 
    template_name = 'classList.html' 
    
