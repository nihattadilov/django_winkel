from django import forms



from user.models import BaseUser



class BaseUserForm(forms.ModelForm):

    

        confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'email-bt', 'placeholder':"Confirm Password"}))



        class Meta:

            model = BaseUser

            fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

            widgets = {

                'username': forms.TextInput(attrs={'class': 'email-bt', 'placeholder':"Username"}),

                'first_name': forms.TextInput(attrs={'class': 'email-bt', 'placeholder':"First Name"}),

                'last_name': forms.TextInput(attrs={'class': 'email-bt', 'placeholder':"Last Name"}),

                'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder':"Email"}),

               #  'bio': forms.Textarea(attrs={'class': 'email-bt', 'rows': 2, 'placeholder':"Bio"}),

               #  'birth_date': forms.DateInput(attrs={'class': 'email-bt', 'placeholder':"Birth Date"}),

                # 'picture': forms.FileInput(attrs={'class': 'email-bt', 'placeholder':"Picture"}),

                'password': forms.PasswordInput(attrs={'class': 'email-bt', 'placeholder':"Password"}),

                

            }



        def clean(self):

            cleaned_data = super(BaseUserForm, self).clean()

            password = cleaned_data.get("password")

            confirm_password = cleaned_data.get("confirm_password")


            if password != confirm_password:

                raise forms.ValidationError(

                    "password and confirm_password does not match"

                )

            


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder':"Username"}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'email-bt', 'placeholder':"Password"}) )