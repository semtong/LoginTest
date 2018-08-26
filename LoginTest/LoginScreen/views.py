from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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