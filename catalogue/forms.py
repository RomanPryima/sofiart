from django import forms

from .models import Article, Review


class NewArticleForm(forms.ModelForm):
    name = forms.CharField(label='Назва')
    description = forms.CharField(label='Опис')

    text = forms.CharField(label='Текст',
                           widget=forms.Textarea(
                               attrs={'rows': 2, 'placeholder': 'Текст статті.'}
                           ),
                           max_length=1500,
                           help_text='Максимальна довжина тексту - 2500 знаків.'
                           )
    gallery_images = forms.ImageField(required=False, label='Зображення для галереї',
                                      help_text='Натисніть тут, щоб завантажити.',
                                      widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Article
        fields = ['name', 'price', 'description', 'text', 'gallery_images']

class ReviewForm(forms.ModelForm):
    creator = forms.CharField(label='Автор')
    email = forms.CharField(required=False, label='Електронна пошта')

    text = forms.CharField(label='Текст',
                           widget=forms.Textarea(
                               attrs={'rows': 3, 'placeholder': 'Ваш відгук'}
                           ),
                           max_length= 1000,
                           help_text='Максимальна довжина тексту - 1000 знаків.'
                           )

    class Meta:
        model = Review
        fields = ['creator', 'email', 'text']