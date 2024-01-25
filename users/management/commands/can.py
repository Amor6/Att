from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание пользователя"""

    def handle(self, *args, **options):
        # User_1
        user = User.objects.create(
            email='lok7854981sa@gmail.com',
            first_name='Pavel',
            last_name='Pavlov',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('31testpass5513')
        user.save()