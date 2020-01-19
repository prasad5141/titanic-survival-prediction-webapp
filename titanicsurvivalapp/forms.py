from django import forms


class InputForm(forms.Form):
    P_class = (
        ('1', '1st Class'),
        ('2', '2nd Class'),
        ('3', '3rd Class')
    )
    gender = (
        ('0', 'Female'),
        ('1', 'Male')
    )
    name = forms.CharField(required=True)
    passenger_class = forms.ChoiceField(choices=P_class, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=gender)