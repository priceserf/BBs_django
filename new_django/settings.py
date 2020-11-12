"""
Django settings for new_django project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q25^wcz&(dm=8f)qe%3q^=grij96e)p&_dwndm$af$^##w50j&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'app01.apps.App01Config',
    'app01'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'new_django.urls'
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'new_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bbs',
        "USER":'root',
        'PASSWORD':'831015',
        'HOST':'localhost',
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  #用于存储会话数据的模块 ，默认放在数据库中

# SESSION_ENGINE = 'django.contrib.sessions.backends.file'    将session存在文件中，配合PATH使用
SESSION_COOKIE_PATH = '/'           #会话cookie的路径。

# SESSION_ENGINE = 'django.contrib.sessions.backends.db‘    放在缓存中
SESSION_CACHE_ALIAS = 'default'     #如果使用缓存会话后端，则缓存以存储会话数据。

SESSION_COOKIE_NAME = 'sessionid'   #cookie名称，自定义cookie名字

SESSION_COOKIE_AGE = 60 * 50 * 3600         #cookie过期时间，以秒为单位（默认值：2周）。 现在是5分钟

SESSION_COOKIE_DOMAIN = None

SESSION_COOKIE_SECURE = False       #会话cookie是否应该是安全的（仅限https：//）。

SESSION_COOKIE_HTTPONLY = True      #是否使用非RFC标准的httpOnly标志（IE，FF3 +，其他）

SESSION_SAVE_EVERY_REQUEST = False   #是否在每个请求上保存会话数据。

SESSION_EXPIRE_AT_BROWSER_CLOSE = True  #Web浏览器关闭时用户的会话cookie是否过期。

SESSION_FILE_PATH = None

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'   #用于序列化会话数据的类
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL =os.path.join(BASE_DIR,'/static/')

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),
    # os.path.join(BASE_DIR,"media")
)


AUTH_USER_MODEL = "app01.UserInfo"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

LOGIN_URL ="/login/"

