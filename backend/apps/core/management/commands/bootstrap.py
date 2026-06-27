import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command

User = get_user_model()


class Command(BaseCommand):
    help = "Bootstrap the application"

    def add_arguments(self, parser):
        parser.add_argument(
            "--migrate-only",
            action="store_true",
            help="Only apply migrations.",
        )

        parser.add_argument(
            "--admin-only",
            action="store_true",
            help="Only create/update the admin user.",
        )

    def handle(self, *args, **options):
        migrate_only = options["migrate_only"]
        admin_only = options["admin_only"]

        if migrate_only and admin_only:
            self.stderr.write(
                self.style.ERROR(
                    "Cannot use --migrate-only and --admin-only together."
                )
            )
            return

        if not admin_only:
            self.stdout.write("Applying migrations...")
            call_command("migrate", interactive=False)

        if not migrate_only:
            self.create_superuser()

        self.stdout.write(self.style.SUCCESS("Bootstrap completed."))

    def create_superuser(self):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not all([username, email, password]):
            self.stdout.write(
                self.style.WARNING(
                    "Superuser environment variables not found. Skipping."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
            },
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created superuser '{username}'.")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f"Updated superuser '{username}'.")
            )