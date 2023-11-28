from .palm_model import test


def chat(msg, *args, **kwargs):
    user_id = kwargs.get('user_id')
    response, accuracy = test(msg, user_id=user_id)

    return response
