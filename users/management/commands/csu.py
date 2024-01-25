from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание админки"""

    def handle(self, *args, **options):
        # Staff_1
        user = User.objects.create(
            email='test695783t@gmail.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('31testpass55')
        user.save()

