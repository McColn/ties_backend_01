# forms.py
from django import forms
from .models import *

class InvestmentsForm(forms.ModelForm):
    class Meta:
        model = Investments
        fields = ['projectName', 'owner', 'resources',
                  'resourcesSummary','areaCovered','licenceType','licenceNumber',
                  'physicalLocation','mapLocation','image','modeOfInvestment',
                  'attachments', 'projectStatus','levelInvestment','studiesDone'
                  ]


class InvestmentComplianceForm(forms.ModelForm):
    class Meta:
        model = InvestmentCompliance
        fields = [
            'title', 'pdf_file',
            'paragraph1', 'paragraph2', 'paragraph3', 'paragraph4',
            'paragraph5', 'paragraph6', 'paragraph7', 'paragraph8',
            'paragraph9', 'paragraph10', 'paragraph11', 'paragraph12',
            'paragraph13', 'paragraph14', 'paragraph15', 'paragraph16',
            'paragraph17', 'paragraph18', 'paragraph19', 'paragraph20'
        ]
        widgets = {
            'paragraph1': forms.Textarea(attrs={'required': False}),
            'paragraph2': forms.Textarea(attrs={'required': False}),
            'paragraph3': forms.Textarea(attrs={'required': False}),
            'paragraph4': forms.Textarea(attrs={'required': False}),
            'paragraph5': forms.Textarea(attrs={'required': False}),
            'paragraph6': forms.Textarea(attrs={'required': False}),
            'paragraph7': forms.Textarea(attrs={'required': False}),
            'paragraph8': forms.Textarea(attrs={'required': False}),
            'paragraph9': forms.Textarea(attrs={'required': False}),
            'paragraph10': forms.Textarea(attrs={'required': False}),
            'paragraph11': forms.Textarea(attrs={'required': False}),
            'paragraph12': forms.Textarea(attrs={'required': False}),
            'paragraph13': forms.Textarea(attrs={'required': False}),
            'paragraph14': forms.Textarea(attrs={'required': False}),
            'paragraph15': forms.Textarea(attrs={'required': False}),
            'paragraph16': forms.Textarea(attrs={'required': False}),
            'paragraph17': forms.Textarea(attrs={'required': False}),
            'paragraph18': forms.Textarea(attrs={'required': False}),
            'paragraph19': forms.Textarea(attrs={'required': False}),
            'paragraph20': forms.Textarea(attrs={'required': False}),
        }


class ConsultancyTiesCategoryForm(forms.ModelForm):
    class Meta:
        model = ConsultancyTiesCategory
        fields = ['title', 'image']

class ConsultationComplianceForm(forms.ModelForm):
    class Meta:
        model = ConsultancyTiesDetails
        fields = ['title','image','category','description']


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['category', 'title', 'price', 'discount_price', 'description', 'image',
                  'location', 'quality', 'sellOrRent', 'quantity', 'manufacturer',
                  'technicalDetails', 'dimension', 'weight', 'capacity', 'horsepower',
                  'groundedArea', 'physicalProperties', 'grade', 'qualityAssurance']
        
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        optional_fields = [
            'discount_price', 'description', 'image', 'location', 'quality', 'sellOrRent', 
            'quantity', 'manufacturer', 'technicalDetails', 'dimension', 'weight', 'capacity', 
            'horsepower', 'groundedArea', 'physicalProperties', 'grade', 'qualityAssurance'
        ]
        for field in optional_fields:
            self.fields[field].required = False  # Make fields optional


class MiningTrendsForm(forms.ModelForm):
    class Meta:
        model = MiningTrends
        fields = ['mine_name', 'local_cost', 'international_cost']

