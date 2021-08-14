from django import forms
from photo.models import Photo
from account.models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        img = forms.FileField()
        widgets = {
            'sharing_end_date' : DateInput(),
            'shared_users': forms.CheckboxSelectMultiple
        }
       # shared_users = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
        shared_users = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
        fields = [
            'img', 
            'description', 
            'shared_users', 
            'sharing_end_date'
        ]


