from django import forms
from store.models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [f.name for f in Store._meta.fields]
       