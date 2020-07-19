from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group','text']
        help_texts = {
            'group': 'Выберите группу для поста',
            'text': 'Введите текст поста'
        }

