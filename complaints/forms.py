from django import forms

from complaints.models import Category, Complaint


class ComplaintForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea({'rows': 3}))
    
    class Meta:
        model = Complaint
        fields = ('title', 'description', 'category', 'already_raised', 'old_ticket_id')

class ComplaintEditForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea({'rows': 3}))
    
    class Meta:
        model = Complaint
        fields = ('title', 'description', 'category', 'already_raised', 'old_ticket_id', 'status')