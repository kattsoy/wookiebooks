from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager)
from django.conf import settings

class UserManager(BaseUserManager):

    def create_user(self, email, author_pseudonym, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, author_pseudonym=author_pseudonym, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, author_pseudonym, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError ('Superuser must have is_staff=True.')

        return self.create_user(email, author_pseudonym, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email               = models.EmailField(max_length=254, unique=True)
    name                = models.CharField(max_length=254)
    author_pseudonym    = models.CharField(max_length=254)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)

    objects             = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['author_pseudonym',]

    def __str__(self):
        return self.name


class Book(models.Model):

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'
        ordering = ["title"]

    title           = models.CharField(max_length=255, unique=True)
    description     = models.TextField(max_length=1000)
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_image     = models.ImageField(blank=True, null=True, upload_to="books_covers", default='images/tg.svg')
    price           = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title