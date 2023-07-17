from django import forms
 
from bank_app.models import Member, Branch
 
class MemberCreationForm(forms.ModelForm):
    account_type = forms.ChoiceField(choices=[
        ('savings', 'Savings'),
        ('current', 'Current'),
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    materials_required = forms.MultipleChoiceField(choices=[
        ('debit', 'Debit Card'),
        ('credit', 'Credit Card'),
        ('cheque', 'Chequebook'),
    ], widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}))

    class Meta:
        model = Member
        fields = '__all__'
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'account_type': forms.Select(attrs={'class': 'form-select'}),
            'materials_required': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        }

   
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()
 
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty branch queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')