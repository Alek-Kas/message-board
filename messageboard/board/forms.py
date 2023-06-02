from django import forms

from .models import Category, Announce


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Announce
        # fields = '__all__'  # Для всех полей модели
        fields = ['author', 'title', 'slug', 'content', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
        # TODO: self.fields['author'].empty_label = '' переделать под автора

