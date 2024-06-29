from django.db import migrations


def create_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    user = User.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='123'
    )
    user.is_staff = True
    user.is_superuser = True
    user.save()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(create_user),
    ]
