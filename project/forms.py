from django import forms
from project.models import User, Reservation, MenuItem, Feedback


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last name'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email Adress'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'picture', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'picture', 'bio',
                  'phone_number', 'email', 'website']


class ReservationForm(forms.ModelForm):
    time = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-group'}))
    date_reserved = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': 'yyyy-mm-dd',
               'id': 'datepicker'}), required=True,)
    resto_type=forms.RadioSelect()
    class Meta:
        model = Reservation
        fields = ['first_name', 'resto_type',
                  'email', 'people', 'time',
                  'phone', 'date_reserved', 'status']

class ReservationUpdateForm(forms.ModelForm):
    time = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'timepicker',
                                      'class': 'input-group'}))
    date_reserved = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': 'yyyy-mm-dd',
               'id': 'datepicker'}), required=True,)
    resto_type=forms.RadioSelect()
    class Meta:
        model = Reservation
        fields = ['first_name',
                  'email', 'people', 'time',
                  'phone', 'date_reserved', 'status']


class MenuForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))

    class Meta:
        model = MenuItem
        fields = ['name', 'cost', 'Menu_type',
                  'description', 'image', 'status', 'category', 'dutch_description']

class FeedbackForm(forms.ModelForm):
    

    class Meta:
        model = Feedback
        fields = ['rate','name', 'email', 'message']
        widgets = {
        'rate' : forms.RadioSelect(attrs={'label': 'Food'}),
        'rate_2' : forms.RadioSelect(attrs={'label': 'Delivery'}),
        }
