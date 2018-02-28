import datetime
from django.db import models

class Patient(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    registration_date = models.DateTimeField('date registered')

    #def __str__(self):
    #    return self.surname
		
class Occurrence(models.Model):
    occurrence = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stage = models.IntegerField(default=0, help_text="Enter cancer stage number")
    description = models.CharField(max_length=200)
    age_occurrence = models.IntegerField(default=0)

class Investigation(models.Model):
    investigation = models.ForeignKey(Occurrence, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    investigation_date = models.DateTimeField('date investigated')
		
class Gene(models.Model):
    gene = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=50)

class Refseq(models.Model):
    refseq = models.ForeignKey(Gene, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)

# class Variant(models.Model):
    # variant = models.ForeignKey(Refseq, on_delete=models.CASCADE)
    # cDNA = models.CharField(max_length=200)
    # protein = models.CharField(max_length=200)
    # genome = models.CharField(default=0, max_length=200)
	