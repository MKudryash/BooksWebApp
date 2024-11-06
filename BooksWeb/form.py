from .models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],  # Рейтинг от 1 до 5
        widget=forms.RadioSelect,
        label='Рейтинг (из 5)'
    )
        fields = ['nameUser', 'email', 'title', 'feedback', 'rating']
        labels={
            'nameUser': 'User name',
            'title': 'Title book',
            'email': 'User email'
        }

        widgets = {  # Добавление атрибута disabled для поля 'title'
            'title': forms.TextInput(attrs={'readonly': 'readonly'}) 
        }