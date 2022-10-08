from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
	def create_user(self, email, full_name, password=None):
		if not email:
			raise ValueError("Email is required")
		if not full_name:
			raise ValueError("Name  is required")

		user = self.model(
			email = self.normalize_email(email),
			full_name = full_name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password=None):
		user = self.create_user(
			email = self.normalize_email(email),
			full_name = full_name,
		)
		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True
		user.set_password(password)
		user.save(using=self._db)
		return user

class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, verbose_name="Name(FirstName LastName)")
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = MyUserManager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
