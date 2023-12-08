
from django import forms

class Application(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    Id = forms.IntegerField()  #required=False
    Firstname = forms.CharField()     # widget=forms.Textarea,
    Lastname = forms.CharField()
    Mobile_No=forms.IntegerField()
    Email = forms.CharField()
    Gender = forms.CharField(widget=forms.Select(choices=GENDER))
    # Password = forms.CharField(widget=forms.PasswordInput)

    def clean_Firstname(self):
        inputfirstname = self.cleaned_data['Firstname']
        if len(inputfirstname)>10:
            raise forms.ValidationError('The max firstname of the 10 letters')
        return inputfirstname

    def clean_Lastname(self):
        inputLastname = self.cleaned_data['Lastname']
        if len(inputLastname) > 20:
            raise forms.ValidationError('THe len of the last name is 20 characters')
        return inputLastname

    def clean_Email(self):
        userEmail = self.cleaned_data['Email']
        if userEmail.find('@')==-1:
            raise forms.ValidationError('Email should contains @ sym')
        return userEmail
