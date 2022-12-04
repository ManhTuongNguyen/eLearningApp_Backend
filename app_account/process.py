from app_account.models import UserCustom
from app_email.process import is_valid_email


def is_valid_account(username: str, pass1: str, pass2: str) -> bool:
    is_valid_username(username)
    is_valid_password(pass1, pass2)
    return True


def is_valid_username(username):
    if not username.strip():
        raise Exception("Không được bỏ trống tên tài khoản!")
    if username.__len__() < 4:
        raise Exception("Độ dài tên tài khoản không hợp lệ!")
    if UserCustom.objects.filter(username=username).exists():
        raise Exception("Tên tài khoản đã được sử dụng!")
    return True


def is_valid_password(pass1, pass2):
    if not pass1.strip():
        raise Exception("Không được bỏ trống mật khẩu!")
    if pass1.__len__() < 3:
        raise Exception("Độ dài mật khẩu không hợp lệ!")
    if pass1 != pass2:
        raise Exception("Mật khẩu nhập lại không khớp!")
    return True


def is_match_password_account(username, old_pass) -> bool:
    u = UserCustom.objects.get(username=username)
    if u.check_password(old_pass):
        return True
    raise Exception("Mật khẩu cũ không đúng!")


def update_password(username, new_pass):
    user = UserCustom.objects.get(username=username)
    user.set_password(new_pass)
    user.save()


def change_password(username: str, old_pass: str, new_pass: str, re_pass: str) -> bool:
    is_match_password_account(username, old_pass)
    if not new_pass.strip():
        raise Exception("Không được bỏ trống mật khẩu mới!")
    if new_pass.__len__() < 3:
        raise Exception("Độ dài mật khẩu mới không hợp lệ!")
    if new_pass != re_pass:
        raise Exception("Mật khẩu mới nhập lại không khớp!")
    update_password(username, new_pass)
    return True