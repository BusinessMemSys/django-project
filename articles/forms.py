
from django.forms import ModelForm
from .models import CommentPost


class CommentForm(ModelForm):

    class Meta:
        model = CommentPost
        fields = ("author", "comment",)