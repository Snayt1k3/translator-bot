import os


def test_required_env_variables_exist():
    assert 'DEEPL_KEY' in os.environ
    assert 'MONGO_URI_DEV' in os.environ
    assert 'MONGO_DOCKER_URI' in os.environ
    assert 'TOKEN' in os.environ


def test_api_key_is_not_empty():
    api_key = os.environ.get('DEEPL_KEY')
    assert api_key is not None
    assert api_key != 'YOUR_AUTH_KEY'


def test_token_is_not_empty():
    token = os.environ.get('TOKEN')
    assert token is not None
    assert token != 'YOUR_TELEGRAM_BOT_TOKEN'
