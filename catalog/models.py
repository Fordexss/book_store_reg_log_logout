from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     description = models.TextField(null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     published_date = models.DateTimeField(auto_now_add=True, editable=True, null=True)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='books', null=True)
#
#     def __str__(self):
#         return self.title