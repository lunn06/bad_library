
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None

    context_object_name = 'user'

    class Meta:
        db_table = 'user'
