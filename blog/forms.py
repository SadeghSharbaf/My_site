from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name":"Your Name",
            "user_email":"Your Email",
            "text":"Your Comment"
        }
        erorrs_massage = {
            "user_name":{
            "required":"Please enter a Name and that mustn't be empty",
            "max_length":"This is too long"
        }}