# A Django settings module to support the tests

SECRET_KEY = 'dummy'
TEST_RUNNER = 'django_nose.runner.NoseTestSuiteRunner'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
)

# The default database should point to the master.
DATABASES = {
    'default': {
        'NAME': 'master.sqlite',
        'ENGINE': 'django.db.backends.sqlite3',
    },
    'slave': {
        'NAME': 'slave.sqlite',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

# Put the aliases for slave databases in this list.
SLAVE_DATABASES = ['slave']

# If you use PinningMasterSlaveRouter and its associated middleware, you can
# customize the cookie name and its lifetime like so:
# MULTIDB_PINNING_COOKIE = "multidb_pin_writes"
# MULTIDB_PINNING_SECONDS = 15
