from django import forms
from models import UserModel, PostModel, LikeModel, CommentModel, CategoryModel

CATEGORY = (
    ('LAP', 'laptop'),
    ('CAR', 'cars'),
    ('MOB', 'Mobile'),
    ('BIKE', 'Bike'),
)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','username','name','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY, required=True)
    class Meta:
        model = PostModel
        fields=['image', 'caption', 'price']


class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']

class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields=['category']