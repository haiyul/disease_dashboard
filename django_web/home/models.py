from django.db import models
from django.contrib.auth.models import AbstractUser

# 继承注册类


class InviteCode(models.Model):
    # user = models.ForeignKey(User, on_delete="CASCADE")
    # invite_code = models.ForeignKey(User.invite_code, null=False, primary_key=True, on_delete="CASCADE")
    invite_code = models.CharField(max_length=20, null=True, unique=True)
    # invite_code_val = models.ForeignKey(to="User", to_field="invite_code", on_delete="")
    group_name = models.CharField(max_length=20, null=True)


class User(AbstractUser):
    # invite_code = models.CharField(max_length=20, blank=True)
    #需要对应的对象
    inviteCode = models.ForeignKey(InviteCode,  on_delete="CASCADE")
    #输入的内容
    invite_code_input = models.CharField(max_length=20, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

