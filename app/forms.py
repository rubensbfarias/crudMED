from django import forms


class UserMaskAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserMaskAdmin, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'mask-phone'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

