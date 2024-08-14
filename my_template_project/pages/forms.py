from django import forms
from .models import Page, Placeholder

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'template_name']

    def __init__(self, *args, **kwargs):
        self.template = kwargs.pop('template', None)
        super().__init__(*args, **kwargs)
        
        if self.template:
            # Add fields based on template placeholders
            self._add_placeholder_fields()

    def _add_placeholder_fields(self):
        # Define a mapping of field types
        placeholder_types = {
            'text': forms.CharField,
            'icon': forms.FileField,
            'image': forms.FileField,
        }
        
        # Extract placeholder keys from the template
        placeholders = self.template.get('placeholders', {})
        for key, value in placeholders.items():
            field_type = self._get_placeholder_type(key)
            if field_type:
                self.fields[key] = field_type(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}) if 'image' in key else forms.Textarea(attrs={'placeholder': value.get('label', '')}))

    def _get_placeholder_type(self, key):
        if '_text' in key:
            return forms.CharField
        elif '_icon' in key or '_image' in key:
            return forms.FileField
        return None

    def save(self, commit=True):
        page = super().save(commit=False)
        if commit:
            page.save()
        # Save placeholders
        placeholders = {key: value for key, value in self.cleaned_data.items() if key.startswith('placeholder_')}
        page.placeholders = placeholders
        if commit:
            page.save()
        return page