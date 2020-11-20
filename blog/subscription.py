from django import forms
from blog.models import Subscribers

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'