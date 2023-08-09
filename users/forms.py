from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1',  'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(customUserCreationForm, self).__init__(*args, **kwargs)

        for k, v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})
