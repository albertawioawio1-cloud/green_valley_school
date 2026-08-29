MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Added for production static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... keep the rest unchanged
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
