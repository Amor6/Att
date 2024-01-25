from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, phone, password=None, role='Администратор'):
        '''Создание админки'''

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )

        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, phone, password_hid=None, role='Пользователь'):
        """Создание пользевотеля, JWT Token создаст скрытый пароль."""

        if not email:
            raise ValueError('Необходим адрес электронной почты')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password_hid)
        user.save(using=self._db)

        return user
