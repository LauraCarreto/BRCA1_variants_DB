# from django.http import HttpResponse


# def index(request):
    # return HttpResponse("Hello, world. You have a variant db.")

from django.http import HttpResponse
from django.template import loader
from .models import Patient

# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

# from .models import Patient
# from .forms import UploadForm


def index(request):
    patient_list = Patient.objects.order_by('-registration_date')[:5]
    template = loader.get_template('VarDB/index.html')
    context = {
        'patient_list': patient_list,
    }
    return HttpResponse(template.render(context, request))

