from django import forms
from .models import Project, ContactMessage

class CreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ()
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Example: Validate email format
        if not email.endswith('@example.com'):
            raise forms.ValidationError("This email domain is not supported.")
        return email
