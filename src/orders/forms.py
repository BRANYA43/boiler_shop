import re

from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('created', 'updated')

    def clean_phone(self):
        data = self.cleaned_data['phone']
        data = ''.join(re.findall(r'\d+', data))
        if data.startswith('38'):
            return f'38({data[2:5]}) {data[5:8]} {data[8:10]}-{data[10:12]}'
        return f'38({data[:3]}) {data[3:6]} {data[6:8]}-{data[8:10]}'

    def save(self, commit=True):
        if qs := Customer.objects.filter(phone=self.cleaned_data['phone']):
            return qs[0]
        return super().save(commit=commit)
