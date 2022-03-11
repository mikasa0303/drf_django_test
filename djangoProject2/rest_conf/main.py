from datetime import timedelta

from django.conf import settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permission.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    )
}

SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
    'ROTATE_REFRESH_TOKENS': True,
}