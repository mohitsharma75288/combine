from django import forms
class contactform(forms.Form):
	name=forms.CharField(max_length=200)
	email=forms.EmailField(max_length=200)
	message=forms.CharField(
		max_length=2000,
		widget=forms.Textarea(),
		help_text='please write something'
     )
	source=forms.CharField(
		max_length=200,
		widget=forms.HiddenInput(),
		required=False
	 )
	def clean(self):
		cleaned_data = super(contactform, self).clean()
		name = cleaned_data.get('name')
		email = cleaned_data.get('email')
		message = cleaned_data.get('message')
		if not name and not email and not message:
			raise form.validationerror('you have write something')  
