from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from audit.middleware import RequestMiddleware


@receiver(post_save)
def audit_log(sender, instance, created, raw, update_fields, **kwargs):
    # Lista de los modelos que se requienran que escuche
    list_of_models = ['MyModel', ]
    if sender.__name__ not in list_of_models:
        return
    user = get_user()
    if created:
        instance.save_addition(user)
    elif not raw:
        instance.save_edition(user)


@receiver(post_delete)
def audit_delete_log(sender, instance, **kwargs):
    # Lista de los modelos que se requienran que escuche
    list_of_models = ['MyModel', ]
    if sender.__name__ not in list_of_models:
        return
    user = get_user()
    instance.save_deletion(user)


def get_user():
    thread_local = RequestMiddleware.thread_local
    if hasattr(thread_local, ‘user’):
        user = thread_local.user
    else:
        user = None
    return user
