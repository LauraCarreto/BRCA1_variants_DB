
import csv
import os, sys
#import datetime
from django.utils import timezone

# Full path to your django project directory
VarDB_home="/Users/User/Desktop/ITModule/VarDB/"

# name to your csv file
csv_file="BRCA1_Django_test_data.csv"

# Full path to your django project directory
VarDB_home="/Users/User/Desktop/ITModule/VarDB/"

os.chdir(VarDB_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

from django.db import models

from VarDB.models import * # imports the models
with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Patient()
		
        p.forename = row['Name'].split()[0]
        p.surname = row['Name'].split()[1]
        p.registration_date = timezone.now()
        p.save()

        o = Occurrence()
        o.occurrence = p
        o.stage = row['Stage']
        o.description = row['Description']
        o.age_occurrence = row['Age']
        o.save()
		
        i = Investigation()
        i.investigation = o
        i.platform = row['Sequencer']
        i.investigation_date = timezone.now()
        i.save()

        g = Gene()
        g.gene = i
        g.symbol = row['Gene']
        g.save()

        r = Refseq()
        r.refseq = g
        r.reference = row['Transcript']
        r.save()
		
        v = Variant()
        v.variant = r
        v.cDNA = row['Variant cDNA']
        v.protein = row['Variant Protein']
        v.genome = row['Variant Genome']
        v.patogenicity = row['Pathogenicity']
        v.date_classified = timezone.now()
        v.save()