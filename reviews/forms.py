from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'review']
        widgets = {'rating': forms.NumberInput(attrs={'min': 1, 'max': 10})}

    # name = forms.CharField(max_length=25)
    # email = forms.EmailField()
    # rating = forms.IntegerField(min_value=1, max_value=10)
    # review = forms.CharField(widget=forms.Textarea)
