from django.urls import include, path

from . import views

urlpatterns = [
    path('BRCA1/NM_007294.3/<int:variant_id>/', views.variant_details, name='variant_details'),
	path('BRCA1/NM_007294.3/', views.variant_index, name='variant_index'),
    path('BRCA1/', views.refseq_index, name='refseq_index'),
	path('all/', views.index, name='index'),
    path('', views.gene_index, name='gene_index'),
	path('list/', views.list, name='list'),
]
