from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Batch 
from .forms import BatchForm 

def batch_index(request):
    my_batches = Batch.objects.all().values()
    template = loader.get_template('./batch/batch_index.html')
    context = {
        'my_batches' : my_batches,
    }
    return HttpResponse(template.render(context,request))



def add_batch(request):
    '''
    to add a batch
    '''
    if request.method == 'POST': 
        batch_data = request.POST.copy()
        # pop the 'csrfmiddlewaretoken'
        batch_data.pop('csrfmiddlewaretoken')
        # convert it to a dictionary to create a Model object
        batch_data_dict = batch_data.dict()
        print(batch_data_dict)
        
        # ** are required to unpack the dictionary

        batch = Batch(**batch_data_dict)

        print("saving to batch database")
        batch.save()
        print("saving to student database")
        return HttpResponseRedirect(reverse(batch_index))

    else:
        form = BatchForm() 
        return render(request,'./batch/add_batch.html',{'form':form})

def update_batch(request,batch_id):
    '''
    To update the name of a batch
    '''
    batch = Batch.objects.get(id = batch_id)
    if (request.method == 'POST'):

        form = BatchForm(request.POST, instance = batch)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(batch_index))

    elif (request.method == 'GET'):
        form = BatchForm(instance = batch)
        template = loader.get_template('./batch/update_batch.html') 
        context = {}
        context['form'] = form
        context['batch'] = batch 
        # if view is called by a get method then call with values from database

        return HttpResponse(template.render(context,request))


def delete_batch (request,batch_id):
    '''
    Usage: To delete a student from the table
    '''
    batch = Batch.objects.get(id = batch_id)
    batch.delete()
    return HttpResponseRedirect(reverse(batch_index))
