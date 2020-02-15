from django import forms

from .models import News


class NewsCreationForm(forms.ModelForm):
    title = forms.TextInput()
    description = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'image'
        ]
