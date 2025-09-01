from django import forms

class PostForm(forms.Form):
    text = forms.CharField(
        max_length=140,
        required=True,
        widget=forms.Textarea(attrs={'rows':4, 'cols':40})
    )
    image = forms.ImageField(required=False)  # Only for images
    file = forms.FileField(required=False)    # For PDFs or other files
