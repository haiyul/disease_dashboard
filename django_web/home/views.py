from django.shortcuts import render, redirect
from .forms import *
from .models import *
from dis_dashboard.models import *
from django.contrib.auth import authenticate, login


def index(request):
    # ret = AggTb.objects.all().values('id', 'case_num', 'month__month_cn')
    # for item in ret:
    #     print(item['id'], item['case_num'], item['month__month_cn'])
    return render(request, 'home/index.html')


def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            #设定对应的对象
            invite_code_input = form.cleaned_data["invite_code_input"]
            form.cleaned_data["inviteCode"] = InviteCode.objects.filter(invite_code=invite_code_input)

            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 然后登陆这个东西
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'home/index.html', context={'form': form})
