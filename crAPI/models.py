from django.db import models

class RequestForm(models.Model):
	countrystatus_CHOICES = (
		('OECD', 'OECD'),
		('DAC-UMICT', 'DAC-UMICT'),
		('Non-OECD / Non-DAC','Non-OECD / Non-DAC'),
		('DAC-LMICT','DAC-LMICT'),
		('DAC-LDC','DAC-LDC'),
		('DAC-OLIC','DAC-OLIC'),
	)

	featurereport_CHOICES = (
		('No', 'No'),
		('nan', 'nan'),
		('Yes', 'Yes'),

	)

	goldcommunity_CHOICES = (
		('No', 'No'),
		('nan', 'nan'),
		('Yes', 'Yes'),

	)
	companylisted_CHOICES = (
		('Listed', 'Listed'),
		('Non-listed', 'Non-listed'),
		('nan', 'nan'),
		('Not applicable', 'Not applicable'),
	)

	organisationtype_CHOICES = (
		('Private company', 'Private company'),
		('Subsidiary', 'Subsidiary'),
		('nan', 'nan'),
		('State-owned company', 'State-owned company'),
		('Cooperative', 'Cooperative'),
		('Non-profit organization', 'Non-profit organization'),
		('Public institution', 'Public institution'),
		('Partnership', 'Partnership'),

	)
	sector_CHOICES = (
		('No', 'Energy Utilities'),
		('nan', 'Healthcare Products'),
		('Yes', 'Aviation'),
		('No', 'Consumer Durables'),
		('Construction Materials', 'Construction Materials'),
		('Automotive', 'Automotive'),
		('Household and Personal Products', 'Household and Personal Products'),
		('Energy', 'Energy'),
		('Forest and Paper Products', 'Forest and Paper Products'),
		('Conglomerates', 'Conglomerates'),
		('Financial Services', 'Financial Services'),
		('Waste Management', 'Waste Management'),
		('Construction', 'Construction'),
		('Mining', 'Mining'),
		('Technology Hardware', 'Technology Hardware'),
		('Other', 'Other'),
		('Equipment', 'Equipment'),
		('Metals Products', 'Metals Products'),
		('Food and Beverage Products', 'Food and Beverage Products'),
		('Telecommunications', 'Telecommunications'),
		('Media', 'Media'),
		('Tourism/Leisure', 'Tourism/Leisure'),
		('Real Estate', 'Real Estate'),
		('Tobacco', 'Tobacco'),
		('Water Utilities', 'Water Utilities'),
		('Healthcare Services', 'Healthcare Services'),
		('Retailers', 'Retailers'),
		('Non-Profit / Services', 'Non-Profit / Services'),
		('Railroad', 'Railroad'),
		('Commercial Services', 'Commercial Services'),
		('Textiles and Apparel', 'Textiles and Apparel'),
		('Universities', 'Universities'),
		('Computers', 'Computers'),
		('Logistics', 'Logistics'),
		('Agriculture', 'Agriculture'),
		('Public Agency', 'Public Agency'),
		('Toys', 'Toys'),
		('=', '='),

	)
	companysize_CHOICES = (
		('Large', 'Large'),
		('MNE', 'MNE'),
		('SME', 'SME'),
		('nan','nan')

	)




	coyname = models.CharField(max_length=30)
	countryname=models.CharField(max_length=30)
	countrystatus=models.IntegerField(choices = countrystatus_CHOICES)
	featurereport=models.IntegerField(choices = featurereport_CHOICES)
	goldcommunity=models.IntegerField(choices = goldcommunity_CHOICES)
	companylisted=models.IntegerField(choices = companylisted_CHOICES)
	organisationtype=models.IntegerField(choices = organisationtype_CHOICES)
	sector=models.IntegerField(choices = sector_CHOICES)
	companysize=models.IntegerField(choices=companysize_CHOICES)

	def __str__(self):
		return self.coyname