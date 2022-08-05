from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

from expr.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ('fname', 'lname', 'email', 'phone', 'password')

    def clean(self):
        super(UsersForm, self).clean()
        fname = self.cleaned_data.get('fname')
        lname = self.cleaned_data.get('lname')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')

        if len(fname) < 5:
            self._errors['fname'] = self.error_class([
                'Minimum 5 characters required'])
        if len(lname) < 5:
            self._errors['lname'] = self.error_class([
        'Minimum 5 characters required'])
        if len(phone) < 10:
            self._errors['phone'] = self.error_class([
                'Minimum 10 digits required'])
        if len(password) < 6:
            self._errors['password'] = self.error_class(['Minimum password length should be 6'])

        return self.cleaned_data