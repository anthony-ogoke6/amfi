from django import forms

from .models import *






class EnrollForm(forms.ModelForm):

    class Meta:
        model = Enroll
        fields = (
        	'full_name',
        	'email',
        	'phone_number',
        	'address',
        	'training',
        	'your_parish',
        )


# class CommentForm(forms.ModelForm):
#     content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Comment here!!!', 'rows': '4', 'cols':'50'}))
#     class Meta:
#         model = Comment
#         fields = ('content',)