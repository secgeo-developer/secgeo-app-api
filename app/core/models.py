"""
Veritabanı Modelleri.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
class UserManager(BaseUserManager):
    """Kullanıcılar için Yönetici"""

    def create_user(self, email, password=None, **extra_fields):
        """Bir kullanıcı oluştur,kaydet ve geri döndür."""
        if not email:
            raise ValueError("Email gerekli")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Bir Süper kullanıcı oluştur,kaydet ve geri döndür."""

        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Sistem içerisinde yer alan kullanıcılar."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, verbose_name="Adı Soyadı")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    is_staff = models.BooleanField(default=False, verbose_name="Yönetici")

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"
