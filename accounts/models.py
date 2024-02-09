from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=30)
    country_code = models.CharField(
        verbose_name="Country Code", max_length=5, blank=True, null=True
    )
    contact_no = models.CharField(
        verbose_name="Contact No.", max_length=10, blank=True, null=True
    )
    password = models.CharField(verbose_name="Password", max_length=255)
    email_verified = models.BooleanField(verbose_name="Email Verified", default=False)
    contact_no_verified = models.BooleanField(
        verbose_name="Email Verified", default=False
    )
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Users"
