from django import forms
from .models import Article



class NewArticleForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Текст статті.'}
        ),
        max_length=1500,
        help_text='Максимальна довжина тексту - 1500 знаків.'
        )

    image = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = ['name', 'price', 'description', 'text', 'image']


class EditArticleForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Текст статті.'}
        ),
        max_length=1500,
        help_text='Максимальна довжина тексту - 1500 знаків.'
        )

    image = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = ['name', 'price', 'description', 'text', 'image']