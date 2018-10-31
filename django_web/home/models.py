from django.db import models
from django.contrib.auth.models import AbstractUser

# 继承注册类
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    # invite_code = models.CharField(max_length=20, blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class InviteCode(models.Model):
    # user = models.ForeignKey(User, on_delete="CASCADE")
    # invite_code = models.CharField(max_length=20, null=False, primary_key=True)
    # invite_code_val = models.ForeignKey(to="User", to_field="invite_code", on_delete="")
    group_name = models.CharField(max_length=20, null=True)