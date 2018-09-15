from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from LoginScreen.models import *

from datetime import datetime
import LoginTest.settings as settings

# Create your views here.


class Join(View):

    def post(self, request, *args, **kwargs):
        # post로 보낸 값을 받는다.
        # formMsg = [request.POST['username'], request.POST['email'], request.POST['psw']]

        condition = False

        create_id = request.POST['username']
        create_psw = request.POST['psw']
        create_email = request.POST['email']

        try:
            User.objects.get(username=create_id)
        except ObjectDoesNotExist:
            condition = True

        if not condition:
            context = {"id": create_id}
            response = render(request, "join.html", context=context)
        else:
            user = User.objects.create_user(create_id, create_email, create_psw)
            user.save()
            # template을 입력해야 다음화면으로 진행이 됨.
            response = render(request, "home.html")

        return response


class MainView(View):

    def get(self, request):
        post_list = Post.objects.all()
        context = {"post": post_list}
        response = render(request, "board/boardExe.html", context=context)

        return response


class Detail(View):

    def get(self, request,  *args, **kwargs):
        detail = Post.objects.get(id=kwargs["post_id"])

        content = {"contents": detail}
        # if you send return values,
        # you must to send dict type
        response = render(request, "board/detail.html", context=content)
        return response


class Modify(View):
    def get(self, request,  *args, **kwargs):
        detail = Post.objects.get(id=kwargs["post_id"])

        content = {"contents": detail}
        # if you send return values,
        # you must to send dict type
        response = render(request, "board/modify.html", context=content)
        return response


class SendModify(View):
    def post(self, request, *args, **kwargs):

        board = Post.objects.get(pk=request.POST['id'])

        title = request.POST['title']
        contents = request.POST['contents']
        update_time = datetime.now()

        board.title = title
        board.content = contents
        board.update_at = update_time

        board.save()

        post_list = Post.objects.all()
        context = {"post": post_list}
        context['rs'] = True

        # response = render(request, "board/boardExe.html", context=context)

        # http://127.0.0.1:8000/accounts/admin
        response = HttpResponseRedirect(reverse('board'))
        return response
