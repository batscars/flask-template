install:
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    deactivate
run:
    if [ `which python` = '/usr/bin/python'];then source env/bin/activate;fi
    supervisord -c supervisor/echo_supervisord.conf
    if [ `which python` != '/usr/bin/python'];then deactivate;fi
update:
    if [ `which python` = '/usr/bin/python'];then source env/bin/activate;fi
    supervisorctl -c supervisor/supervisord.conf restart all
    if [ `which python` != '/usr/bin/python'];then deactivate;fi
test:
    if [ `which python` = '/usr/bin/python'];then source env/bin/activate;fi
    python tests/test_webapp.py
    if [ `which python` != '/usr/bin/python'];then deactivate;fi