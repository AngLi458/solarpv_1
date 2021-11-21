from django import forms

class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

    user_id = forms.CharField(max_length=20)
    client = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    middle_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    job_title = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    office_phone = forms.CharField(max_length=15)
    cell_phone = forms.CharField(max_length=15)
    prefix = forms.CharField(max_length=10)
    is_staff = forms.CharField(max_length=1)
