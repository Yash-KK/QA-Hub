from django_registration.forms import RegistrationForm

from users.models import CustomUser


class MyCustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        