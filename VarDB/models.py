import datetime
from django.db import models

class Patient(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    registration_date = models.DateTimeField('date registered')

    def __str__(self):
        return '%s %s' %(self.forename, self.surname)
		
class Occurrence(models.Model):
    occurrence = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stage = models.IntegerField(default=0, help_text="Enter cancer stage number")
    description = models.CharField(max_length=200)
    age_occurrence = models.IntegerField(default=0)
	
    def __str__(self):
        return 'Stage %s; %s; %sy' %(self.stage, self.description, self.age_occurrence)

class Investigation(models.Model):
    investigation = models.ForeignKey(Occurrence, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    investigation_date = models.DateTimeField(help_text='date investigated')

    def __str__(self):
        return '%s %s' %(self.platform, self.investigation_date)
		
class Gene(models.Model):
    gene = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=50)
	
    def __str__(self):
        return '%s' %(self.symbol)

class Refseq(models.Model):
    refseq = models.ForeignKey(Gene, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)

    def __str__(self):
        return '%s' %(self.reference)

class Variant(models.Model):
    variant = models.ForeignKey(Refseq, on_delete=models.CASCADE)
    cDNA = models.CharField(max_length=200)
    protein = models.CharField(null = True, max_length=200)
    genome = models.CharField(null = True, max_length=200)
    pathogenicity = models.IntegerField(null = True, help_text= '1-5 Classification')
    date_classified = models.DateTimeField(null = True, help_text= 'Date classified')

    def __str__(self):
        if self.pathogenicity:
            return '%s, %s --- Class %s (%s)' %(self.cDNA, self.protein, self.pathogenicity, self.date_classified)
        else:
            return '%s, %s --- VUS' %(self.cDNA, self.protein)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')