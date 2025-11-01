from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'description', 'price', 'material', 'image', 'stock',
            'raw_material_source', 'transportation_method', 'manufacturing_process',
            'certifications', 'environmental_benefits', 'usage_advantages',
            'conventional_impact', 'carbon_footprint', 'water_usage', 'recyclability'
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'raw_material_source': forms.Textarea(attrs={'rows': 3}),
            'transportation_method': forms.Textarea(attrs={'rows': 3}),
            'manufacturing_process': forms.Textarea(attrs={'rows': 4}),
            'environmental_benefits': forms.Textarea(attrs={'rows': 3}),
            'usage_advantages': forms.Textarea(attrs={'rows': 3}),
            'conventional_impact': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control-file'
            
            if field_name in ['name', 'price', 'material', 'stock', 'certifications', 
                             'carbon_footprint', 'water_usage', 'recyclability']:
                field.widget.attrs['placeholder'] = field.label
