from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

from expr.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ('fname', 'lname', 'email', 'phone', 'password')