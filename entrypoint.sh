set -e

echo "Waiting for database..."
while ! nc -z db 5432; do
  echo "Database is not ready yet. Waiting..."
  sleep 2
done
echo "Database is ready!"

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Creating migrations for core app..."
python manage.py makemigrations core --noinput

echo "Applying core migrations..."
python manage.py migrate --noinput

echo "Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
exec gunicorn myproject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --worker-class sync \
    --timeout 120 \
    --keep-alive 2 \
    --max-requests 1000 \
    --max-requests-jitter 100
