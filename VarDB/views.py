# from django.http import HttpResponse


# def index(request):
    # return HttpResponse("Hello, world. You have a variant db.")

from django.http import HttpResponse
from django.template import loader
from .models import *

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document
from .forms import DocumentForm
from django.db.models import Count

# def index(request):
    # patient_list = Patient.objects.order_by('-registration_date')[:5]
    # template = loader.get_template('VarDB/index.html')
    # context = {
        # 'patient_list': patient_list,
    # }
    # return HttpResponse(template.render(context, request))
	
def gene_index(request):
    gene_list = Gene.objects.values('symbol').annotate(Count('id')).order_by()
    template = loader.get_template('VarDB/gene_index.html')
    context = {
        'gene_list': gene_list
    }
    return HttpResponse(template.render(context, request))

def refseq_index(request):
    refseq_list = Refseq.objects.values('reference').annotate(Count('id')).order_by()
    template = loader.get_template('VarDB/refseq_index.html')
    context = {
        'refseq_list': refseq_list
    }
    return HttpResponse(template.render(context, request))
	
def variant_index(request):
    variant_list = Variant.objects.order_by('cDNA')
    template = loader.get_template('VarDB/variant_index.html')
    context = {
        'variant_list': variant_list
    }
    return HttpResponse(template.render(context, request))
	
def variant_details(request, variant_id):
    variant_details = Variant.objects.get(id=variant_id)
    template = loader.get_template('VarDB/variant_details.html')
    context = {
        'variant_details': variant_details
    }
    return HttpResponse(template.render(context, request))
	
def index(request):
    number = Patient.objects.count()
    variants = Variant.objects.all()	
    context = {
        'variants' : variants,
        'number' : number,
    }
	
    return render(request, 'VarDB/patients.html', context)
	
# def index(request):
	# data = Patient.objects.all()
	# return render(request, 'VarDB/patients.html', locals())
	
###############################not working from here##################

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('VarDB.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render('VarDB/list.html',
        {'documents': documents, 'form': form},
    )