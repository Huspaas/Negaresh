from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    verbose_name='قرارداد'
    verbose_name_plural = 'قرارداد ها'