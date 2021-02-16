from django import forms
from post.models import Post

from django.forms import ClearableFileInput

class NewPostForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input form-control'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input form-control'}), required=True)

	class Meta:
		model = Post
		fields = ('content', 'caption', 'tags')