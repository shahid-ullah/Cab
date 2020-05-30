from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

from .models import Snippet, Language



class AddSnippetForm(forms.Form):
    def __init__(self, author, *args, **kwargs):
        super(AddSnippetForm, self).__init__(*args, **kwargs)
        self.author = author
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    code = forms.CharField(widget=forms.Textarea())
    tags = forms.CharField(max_length=255)
    language = forms.ModelChoiceField(queryset=Language.objects.all())

    def save(self):
        return Snippet.objects.create(
                                 title=self.cleaned_data['title'],
                                 description=self.cleaned_data['description'],
                                 tags=self.cleaned_data['tags'],
                                 code=self.cleaned_data['code'],
                                 author=self.author,
                                 language=self.cleaned_data['language'])


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author', ]


STATES = (
        ('', 'Choose...'),
        ('MG', 'Minas Gerais'),
        ('SP', 'Sao Paulo'),
        ('RJ', 'Rio de Janeiro')
)


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )
