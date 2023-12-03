from .palm_model import test


def chat(msg, *args, **kwargs):
    user_id = kwargs.get('user_id')
    final_response, actual_response, confidence = test(msg, user_id=user_id)

    return final_response, actual_response, confidence
