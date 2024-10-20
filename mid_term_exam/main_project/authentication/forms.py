from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


########### User Registration Form ##########
class userRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


########### User Update Form ##########
class userUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']