from django.shortcuts import render
from .models import MyModel

def my_model_list(request):
    
    MyModel.objects.create(name="Objet de test")
    
    objects = MyModel.objects.all()
    
    return render(request, 'myapp/my_model_list.html', {'objects': objects})