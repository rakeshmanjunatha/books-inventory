from django import forms
from models import Books, Author, BookCategory

class AddBooksForm(forms.ModelForm):
	"""docstring for AddBooksForm"""
	class Meta:
		model = Books
		fields = '__all__'
		widgets = {
            'publish_date': forms.DateInput(attrs={'class':'datepicker form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            # 'is_most_popular': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class AddCategoryForm(forms.ModelForm):
    """docstring for AddCategoryForm"""
    class Meta:
        model = BookCategory
        fields = '__all__'
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.Textarea(attrs={'class':'form-control'}),
        }

class AddAuthorDetailsForm(forms.ModelForm):
    """docstring for AddAuthorDetailsForm"""
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'address' : forms.Textarea(attrs={'class':'form-control'}),
        }
        