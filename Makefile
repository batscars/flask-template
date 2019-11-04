install:
    virtualenv env
    env/bin/pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
run:
    env/bin/supervisord -c supervisor/echo_supervisord.conf
update:
    env/bin/supervisorctl -c supervisor/supervisord.conf restart all
test:
    env/bin/python tests/test_webapp.py
