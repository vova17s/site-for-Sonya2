from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-oe_gb=p9(u7p4+p0i)fz7ted-toqunxt(nzwqsi!cvdg%v=u*c"

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', "backend.localhost", "62.109.15.31"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'whitenoise',
    'allauth',
    'allauth.account',

    'accounts',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # cors headers
    'django.middleware.common.CommonMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # whitenoise
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'settings.urls'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    STATIC_ROOT / "pages",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Settings allauth
AUTH_USER_MODEL = "accounts.CustomUser"

SITE_ID = 1

LOGIN_REDIRECT_URL = "homepage"

ACCOUNT_LOGOUT_REDIRECT_URL = "homepage"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_FORMS = {
    "login": "allauth.account.forms.LoginForm",
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",

    "signup": "accounts.forms.CustomUserCreationForm",
}

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'