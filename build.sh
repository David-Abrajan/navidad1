#!/usr/bin/env bash

set -o errexit

pip install --upgrade
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
