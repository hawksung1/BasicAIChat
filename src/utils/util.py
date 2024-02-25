def load_secrets():
    from src.constants import secrets
    import os
    secrets_dict = {key: value for key, value in secrets.__dict__.items() if not key.startswith("__")}
    os.environ.update(secrets_dict)
