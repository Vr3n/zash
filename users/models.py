from django.db import models
from PIL import Image
from django.core.validators import RegexValidator
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

# Custom User Manager model (Overrides the default Django User Manager model)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have an Email ID')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username, email, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Custom User model (Overrides the default Django User model)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=15,
                                validators=[
                                    RegexValidator(regex=USERNAME_REGEX,
                                                   message="Username must be less than 15 characters",
                                                   code='Invalid Username'
                                                   )],
                                unique=True
                                )

    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name='email address'
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        "Does the user have a permission"
        # Simplest possible answer: yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have a permission to view the app 'app_label'? "
        # Simplest possible answer: yes, always
        return True


# Model to Create Profile of User.


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return (f'{self.user.username} Profile')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)
