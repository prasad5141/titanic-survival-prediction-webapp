from django import forms


class InputForm(forms.Form):
    P_class = (
        ('Class 1', '1st Class'),
        ('Class 2', '2nd Class'),
        ('Class 3', '3rd Class')
    )
    gender = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    name = forms.CharField(required=True)
    passenger_class = forms.ChoiceField(choices=P_class, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=gender)