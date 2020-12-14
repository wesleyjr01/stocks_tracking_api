#!/bin/bash
FIRST_TIME=".first-time"

if [ ! -f $FIRST_TIME ]; then
    if [ -f "manage.py" ]; then

        echo ":: Running migrations"
        python manage.py migrate --no-input

        echo ":: Importing fixtures"
        find . -iname "init*.json" \
            -exec echo "Applying {}" \; \
            -exec python manage.py loaddata {} \;

        echo ":: Creating super user"
        python manage.py createsuperuser \
            --username ${DJANGO_SUPERUSER_USERNAME} \
            --email ${DJANGO_SUPERUSER_EMAIL} \
            --noinput
    fi
    touch $FIRST_TIME;
fi

exec "$@"