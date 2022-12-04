from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class UserCustom(AbstractUser, PermissionsMixin):
    """
    Người dùng (tùy chỉnh)
    """

    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    email_verified = models.BooleanField(default=False)
    account_verified = models.BooleanField(default=False)
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="Địa chỉ")
    MALE, FEMALE, OTHER = range(3)
    GENDER = [
        (MALE, 'Nam'),
        (FEMALE, 'Nữ'),
        (OTHER, 'Khác')
    ]
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=MALE,verbose_name="Giới tính")
    introduce = models.CharField(max_length=300, blank=True, null=True, verbose_name="Giới thiệu")

    phone = models.CharField(max_length=15, blank=True, null=True)
    birth = models.DateField(
        blank=True, null=True
    )

    previous_permission = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    is_active = models.BooleanField(default=True, verbose_name='Hoạt động',
                                    help_text='Chỉ định xem người dùng này phải được coi là đang hoạt động. Bạn nên bỏ chọn này thay vì xóa tài khoản.')
    is_staff = models.BooleanField(default=False, verbose_name='Nhân viên',
                                   help_text='Chỉ định người dùng nào được phép truy cập vào trang admin.')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser',
                                       help_text='Chỉ định rằng người dùng này có tất cả các quyền mà không gán cho họ một cách cụ thể.')

    USERNAME_FIELD = 'username'

    # REQUIRED_FIELDS = ['phone', 'user_role']

    # def __str__(self):
    #     return self.username
    def __unicode__(self):
        return u'{0}'.format(self.get_full_name())

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    # Metadata
    class Meta:
        ordering = ['id']
        db_table = 'auth_user'
        verbose_name = 'Người dùng'
        verbose_name_plural = 'Tất cả người dùng'