from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):

    name = forms.CharField(label='Назва')
    description = forms.CharField(label='Опис')

    text = forms.CharField(label='Текст',
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Текст статті.'}
        ),
        max_length=1500,
        help_text='Максимальна довжина тексту - 1500 знаків.'
        )

    image = forms.ImageField(required=False, label='Основне зображення', help_text='Натисніть тут, щоб завантажити.')
    gallery_image = forms.ImageField(required=False, label='Зображення для галереї', help_text='Натисніть тут, щоб завантажити.')

    class Meta:
        model = Article
        fields = ['name', 'price', 'description', 'text', 'image', 'gallery_image']
