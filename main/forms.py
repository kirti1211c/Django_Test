from django import forms
class Inputt(forms.Form):
    txt=forms.CharField(label="Enter Text",max_length=1000)