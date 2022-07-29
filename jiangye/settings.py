"""
Django settings for jiangye project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR =os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#by2!sfq&54f0xa&cbcgmvk7$(^uf0)e^9n0nq)ga71!(3p#5r'

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
    'jiangyeapp.apps.JiangyeappConfig',
    'jiangyebook',
    'moviesList',
    "bootstrap5",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jiangye.urls'
#AUTH_USER_MODEL = 'user.User'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'moviesList/templates'),
                BASE_DIR / 'templates',
                BASE_DIR / 'jiangyeapp/templates',
                BASE_DIR / 'moviesList/templates',
                
                ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'jiangye.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
#------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zxyy',  # 数据库名字
        'USER': 'root',
        'PASSWORD': 'zxy013',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
        'TEST': {
            'CHARSET' : 'utf8',
            'COLLATION':'utf8_general_ci'
        }
    }
}
#=======================================================

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 设置根目录的静态资源文件夹static
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#print(os.path.join(BASE_DIR, 'jiangyeapp/static'),111) 

# 设置根目录的静态资源文件夹static
STATICFILES_DIRS = [BASE_DIR / 'static',
# 设置App(index)的静态资源文件夹Mystatic
BASE_DIR / 'jiangyeapp/static/',]


# 设置媒体路由地址信息
MEDIA_URL = '/media/'
# 获取media文件夹的完整路径信息
#MEDIA_ROOT = BASE_DIR / 'media'


MEDIA_ROOT = os.path.join(BASE_DIR, "jiangyeapp/media/")#此代码可以计算出文件夹的相对路径，配合print进行调试

MEDIA_ROOT = os.path.join(BASE_DIR, "/media/")

print(MEDIA_ROOT)
    


#email

EMAIL_HOST='smtp.163.com'
EMAIL_PORT='25'
EMAIL_HOST_USER='15225107379@163.com'
EMAIL_HOST_PASSWORD='CYKXOMJWJICDEOV'
EMAIL_USER_TLS=True


YOUTUBE_DATA_API_KEY ='AIzaSyD_rx9dvz2vXgFMXzwWey2CDweIotkaKmA'

# AIzaSyD_rx9dvz2vXgFMXzwWey2CDweIotkaKmA
# AIzaSyC7AzByBAZCy_ElGo08hsR7oKz9hmeFzQs