from rest_framework.response import Response
from rest_framework.views import APIView

from app_account.models import UserCustom
from app_account.process import is_valid_account, change_password


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username == '' or username is None:
            return Response({
                "type": "3",
                "message": "Không được bỏ trống tên tài khoản!",
                "accept": 0
            }, status=200)
        if password == '' or password is None:
            return Response({
                "type": "3",
                "message": "Không được bỏ trống mật khẩu!",
                "accept": 0
            }, status=200)
        tmp_check_username_exist = UserCustom.objects.filter(username=username.lower())
        if tmp_check_username_exist.count() == 0:
            return Response({
                "type": "3",
                "message": "Tài khoản không tồn tại trên hệ thống",
                "accept": 0
            }, status=200)
        tmp_check_user = UserCustom.objects.get(username=username.lower())
        if not tmp_check_user.check_password(password):
            return Response({
                "type": "2",
                "message": "Mật khẩu không chính xác",
                "accept": 0
            }, status=200)
        return Response({
            "type": "1",
            "message": "",
            "accept": 1,
            "user_id": str(tmp_check_user.id)
        }, status=200)


class Signup(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        re_password = request.data.get('re_password')

        try:
            is_valid_account(username, pass1=password, pass2=re_password)
        except Exception as ex:
            return Response({
                "type": "2",
                "message": str(ex),
                "accept": 0
            })
        new_user = UserCustom.objects.create_user(username=username, password=password)
        return Response({
            "type": "1",
            "message": "Đã đăng ký tài khoản thành công!",
            "accept": 1,
            "new_user": str(new_user.id)
        })


class UpdatePassword(APIView):
    def post(self, request):
        user_id = request.data.get('user')
        username = UserCustom.objects.get(id=int(user_id)).username
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        re_new_password = request.data.get('re_new_password')

        try:
            change_password(username, old_pass=password, new_pass=new_password, re_pass=re_new_password)
        except Exception as ex:
            return Response({
                "type": "2",
                "message": str(ex),
                "accept": 0
            })

        return Response({
            "type": "1",
            "message": "Đã thay đổi mật khẩu thành công!",
            "accept": 1,
        })


class ForgetPassword(APIView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or username is None:
            return Response({
                "type": "3",
                "message": "Không được bỏ trống tên tài khoản!",
                "accept": 0
            }, status=200)
        if password == '' or username is None:
            return Response({
                "type": "3",
                "message": "Không được bỏ trống mật khẩu!",
                "accept": 0
            }, status=200)
        tmp_check_username = UserCustom.objects.filter(username=username)
        if tmp_check_username.count() > 0:
            return Response({
                "type": "2",
                "message": "Tên tài khoản đã được sử dụng!",
                "accept": 0
            }, status=200)
        UserCustom.objects.create_user(username=username, password=password)
        return Response({
            "type": "1",
            "message": "Đã đăng ký tài khoản thành công!",
            "accept": 1
        })


