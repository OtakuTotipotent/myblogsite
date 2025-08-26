from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class PostSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label="Search by Title",
    )
    start_date = forms.DateField(
        required=False,
        label="From Date",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = forms.DateField(
        required=False,
        label="To Date",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
