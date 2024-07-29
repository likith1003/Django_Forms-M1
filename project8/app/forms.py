from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    pno = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=False)
    un = forms.CharField(max_length=50, required=True)
    pw = forms.CharField(max_length=50, required=True)
