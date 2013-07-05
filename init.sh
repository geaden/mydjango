export SECRET_KEY=$( cat secret.txt )
export DJANGO_SETTINGS_MODULE=mydjango.settings.local
export PYTHONPATH=$PYTHONPATH:./mydjango/mydjango/
