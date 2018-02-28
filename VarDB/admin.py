from django.contrib import admin

from .models import Patient, Occurrence, Investigation, Gene, Refseq, Variant

admin.site.register(Patient)
admin.site.register(Occurrence)
admin.site.register(Investigation)
admin.site.register(Gene)
admin.site.register(Refseq)
admin.site.register(Variant)