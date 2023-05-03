from django import forms
from .models import Shops

class bookform (forms.ModelForm):
    class Meta :
        model= Shops
        fields= [
            "cus_name",
            "order",
            "p_img",
        ]