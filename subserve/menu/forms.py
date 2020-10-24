from django import forms
from menu.models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [f.name for f in Menu._meta.fields]
  