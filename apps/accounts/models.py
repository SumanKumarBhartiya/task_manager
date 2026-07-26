from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN = "ADMIN"
MANAGER = "MANAGER"
EMPLOYEE = "EMPLOYEE"

ROLE_CHOICES = (
    (ADMIN, "Admin"),
    (MANAGER, "Manager"),
    (EMPLOYEE, "Employee"),
)

class User(AbstractUser):


    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=EMPLOYEE
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username