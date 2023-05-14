from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)