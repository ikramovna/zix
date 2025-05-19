import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

MY_APPS = [
    'app',
]

THIRD_PARTY_APPS = [
    'drf_yasg',
    'rest_framework',
    'import_export',
    'corsheaders',
    'django_filters',
    'rest_framework_simplejwt',
    'mptt',
    'ckeditor',
    'parler',
    'rosetta',
]

INSTALLED_APPS = [
                     'jazzmin',
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                 ] + MY_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}


# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR / 'static')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR / 'staticfiles')


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Swagger Config

SWAGGER_SETTINGS = {
    'VALIDATOR_URL': 'http://localhost:8189',
    'DEFAULT_INFO': 'import.path.to.urls.api_info',
    'USE_SESSION_AUTH': True,
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Type in the *\'Value\'* input box below: **\'Bearer &lt;JWT&gt;\'**, '
                           'where JWT is the JSON web token you get back when logging in.'
        }
    }

}

# CORS Config
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

# AUTH_USER_MODEL = 'users.User'

# Email Config

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'auto',
    },
}

LANGUAGE_CODE = 'uz'  # Default language set to Uzbek
LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
    ('uz', 'Uzbek'),
]
PARLER_LANGUAGES = {
    None: (
        {'code': 'en', 'name': 'English'},
        {'code': 'ru', 'name': 'Russian'},
        {'code': 'uz', 'name': 'Uzbek'},
    ),
    'default': {
        'fallbacks': ['en'],  # defaults to English if translation is missing
        'hide_untranslated': False,  # show empty translations
    }
}

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


JAZZMIN_SETTINGS = {
    # Title of the window (browser tab)
    "site_title": "ZIXX",

    # Title on the login screen
    "site_header": "ZIXX",

    # Title on the brand (top-left corner)
    "site_brand": "ZIXX",

    # Logo to use for your site (must be available in static files)
    "site_logo": "zix.png",

    # Favicon (use a hammer icon or related graphic)
    "site_icon": "zix.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to ZIXX Admin Panel",

    # Copyright text for the footer
    "copyright": "© 2025 ZIXX. All rights reserved.",

    # Search bar configuration
    "search_model": ["auth.User", "auction.Auction"],

    # Avatar field on user model
    "user_avatar": "profile_picture",

    # Top Menu
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://fothebys.com/support", "new_window": True},
        {"model": "auth.User"},
        {"app": "auction"},
    ],

    # Side Menu
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "auction"],

    # Icons for apps and models
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "auction": "fas fa-gavel",
        "auction.Auction": "fas fa-hammer",
    },

    # Related Modal
    "related_modal_active": True,

    # UI Tweaks
    "custom_css": "/static/css/fothebys_custom.css",  # Path to your custom CSS file
    "custom_js": "/static/js/fothebys_custom.js",  # Path to your custom JS file
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    # Change View
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible"},
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "navbar": "navbar-dark bg-black",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-dark bg-black",
    "accent": "accent-danger",
    "dark_mode_theme": "slate",
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "button_classes": {
        "primary": "btn btn-danger",
        "secondary": "btn btn-light",
    },

    # Include custom CSS snippet for enhanced design
    "custom_css_snippet": """
        /* Center the language tabs */
        .parler-language-tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        /* Style the tabs */
        .parler-language-tabs li {
            margin: 0 10px;
        }

        .parler-language-tabs a {
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #343a40;
            color: #ffffff;
            font-weight: bold;
            text-decoration: none;
        }

        .parler-language-tabs a.active {
            background-color: #007bff;
            color: #ffffff;
        }

        .parler-language-tabs a:hover {
            background-color: #0056b3;
        }

        /* Adjust the form container */
        .form-container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #212529;
            padding: 20px;
            border-radius: 10px;
        }

        /* Form field styling */
        .form-row input, .form-row select, .form-row textarea {
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 5px;
            width: 100%;
            background-color: #343a40;
            color: #ffffff;
        }

        /* Button alignment and styling */
        .submit-row {
            display: flex;
            justify-content: center;
            gap: 15px;
        }

        .submit-row button {
            padding: 10px 15px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 5px;
        }

        .submit-row button:hover {
            opacity: 0.9;
        }

        /* Spacing below language tabs */
        .parler-language-tabs + .inline-group {
            margin-top: 20px;
        }
    """,
}

