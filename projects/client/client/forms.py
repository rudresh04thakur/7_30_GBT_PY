from django import forms  
from .models import Services,Products

class ServicesForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False
            self.fields[key].widget.attrs['class'] = 'form-control'

    class Meta:  
        model = Services  
        fields = ['name','description']

class ProductsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductsForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False
            self.fields[key].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Products
        fields = ['title','discription','price','quantity','image']