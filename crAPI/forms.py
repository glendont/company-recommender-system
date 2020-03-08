from django import forms

class SubmissionForm(forms.Form):
	

	countryname=forms.CharField(max_length=30)
	# # countrystatus=forms.CharField(max_length=30)
	# featurereport=forms.CharField(max_length=30)
	# goldcommunity=forms.CharField(max_length=30)
	# companylisted=forms.CharField(max_length=30)
	
	# organisationtype=forms.CharField(max_length=30)
	# countryregion=forms.CharField()
	# sector=forms.CharField(max_length=30)
	# companysize=forms.CharField(max_length=30)

	countrystatus=forms.ChoiceField(choices=(('OECD', 'OECD'),
		('DAC-UMICT', 'DAC-UMICT'),
		('Non-OECD / Non-DAC','Non-OECD / Non-DAC'),
		('DAC-LMICT','DAC-LMICT'),
		('DAC-LDC','DAC-LDC'),
		('DAC-OLIC','DAC-OLIC'))
)

	featurereport=forms.ChoiceField(choices=(('No', 'No'),
		('Yes', 'Yes')))

	goldcommunity=forms.ChoiceField(choices=(('No', 'No'),
		('Yes', 'Yes')))

	companylisted=forms.ChoiceField(choices=(('Listed', 'Listed'),
		('Non-listed', 'Non-listed'),
		('Not applicable', 'Not applicable')))

	coyname = forms.CharField(max_length=30)

	organisationtype=forms.ChoiceField(choices=(('Private company', 'Private company'),
	('Subsidiary', 'Subsidiary'),
	('nan', 'nan'),
	('State-owned company', 'State-owned company'),
	('Cooperative', 'Cooperative'),
	('Non-profit organization', 'Non-profit organization'),
	('Public institution', 'Public institution'),
	('Partnership', 'Partnership')))

	countryregion=forms.ChoiceField(choices=(('Europe', 'Europe'),
		('Northern America', 'Northern America'),
		('Asia', 'Asia'),
		('Latin America & the Caribbean', 'Latin America & the Caribbean'),
		('Africa', 'Africa'),
		('Oceania', 'Oceania')))

	sector=forms.ChoiceField(choices=(('No', 'Energy Utilities'),
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
		('Toys', 'Toys')))

	companysize=forms.ChoiceField(choices=(('Large', 'Large'),
		('MNE', 'MNE'),
		('SME', 'SME')))


	
