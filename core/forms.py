from django import forms
from .models import User, Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': '4',
                'placeholder': 'Type your message here...'
            }
        )
    )

    class Meta:
        model = Message
        fields = ['content']

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'country', 'flag', 'password']