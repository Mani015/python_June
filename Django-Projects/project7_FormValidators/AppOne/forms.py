
from django import  forms
from django.core import validators
class Customer(forms.Form):
    gender = [('male','MALE'),('female','FEMALE')]
    Firstname = forms.CharField()
    Lastname = forms.CharField()
    Email = forms.CharField()
    Age = forms.IntegerField()
    Gender = forms.CharField(widget=forms.Select(choices=gender))
    Password = forms.CharField(widget=forms.PasswordInput)

    def clean_Firstname(self):
        userinputfirstname = self.cleaned_data['Firstname']
        if len(userinputfirstname)>10:
            raise forms.ValidationError('The max lenght of firstname is 10 characters')
        return userinputfirstname
    #
    #
    #
    def clean_Lastname(self):
        userinputlastname = self.cleaned_data['Lastname']
        if len(userinputlastname)>10:
            raise forms.ValidationError('The last name is upto 10 characters')
        return userinputlastname

    def clean_Email(self):
        inputemail = self.cleaned_data['Email']
        if inputemail.find('@')==-1:
            raise forms.ValidationError('User enter your email with give @ symbol')
        return inputemail
