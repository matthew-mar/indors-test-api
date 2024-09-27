from django.contrib.auth.models import BaseUserManager


class BreederManager(BaseUserManager):
    def create_user(
        self,
        username: str,
        password: str|None = None,
        **extra_fields
    ):
        if not username:
            raise ValueError('The Username field is required')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(
        self, 
        username: str, 
        password: str|None = None,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_superuser(username, password, **extra_fields)
