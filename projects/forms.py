from django.forms import ModelForm
from django import forms
from .models import Project



class Projectform(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_code', 'tags']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(Projectform, self).__init__(*args, **kwargs)

        for k, v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'add title'})
