from django import forms

class HeightForm(forms.Form):
    feet = forms.IntegerField(min_value=0)
    inches = forms.IntegerField(min_value=0, max_value=11)
    lbs = forms.IntegerField(min_value=0)