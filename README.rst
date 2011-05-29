==============
Django AllAuth
==============

Integrated set of Django applications addressing authentication,
registration, account management as well as 3rd party (social) account
authentication.

Installation
============

Django
------

settings.py::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        "allauth.context_processors.allauth",
        "allauth.account.context_processors.account"
    )

    AUTHENTICATION_BACKENDS = (
        ...
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    INSTALLED_APPS = (
        ...
        'emailconfirmation',
	'uni_form',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.twitter',
        'allauth.openid',
        'allauth.facebook',

urls.py::

    urlpatterns = patterns('',
        ...
        (r'^accounts/', include('allauth.urls')))


Configuration
=============

Available settings:

ACCOUNT_EMAIL_REQUIRED (=False)
  The user is required to hand over an e-mail address when signing up

ACCOUNT_EMAIL_VERIFICATION (=False)
  After signing up, keep the user account inactive until the e-mail
  address is verified

ACCOUNT_EMAIL_AUTHENTICATION (=False)
  Login by e-mail address, not username

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION (=True)
  When signing up, let the user type in his password twice to avoid typ-o's.

ACCOUNT_UNIQUE_EMAIL (=True)
  Enforce uniqueness of e-mail addresses

ACCOUNT_USERNAME_REQUIRED (=True)
  If false, generates a random username rather than prompting for one
  at signup

SOCIALACCOUNT_QUERY_EMAIL (=ACCOUNT_EMAIL_REQUIRED)
  Request e-mail address from 3rd party account provider? E.g. using
  OpenID AX, or the Facebook "email" permission

SOCIALACCOUNT_AUTO_SIGNUP (=True) 
  Attempt to bypass the signup form by using fields (e.g. username,
  email) retrieved from the social account provider. If a conflict
  arises due to a duplicate e-mail address the signup form will still
  kick in.

SOCIALACCOUNT_AVATAR_SUPPORT (= 'avatar' in settings.INSTALLED_APPS)
  Enable support for django-avatar. When enabled, the profile image of
  the user is copied locally into django-avatar at signup.

EMAIL_CONFIRMATION_DAYS (=# of days, no default)
  Determines the expiration date of email confirmation mails sent by
  django-email-confirmation.

Facebook & Twitter
------------------

The required keys and secrets for interacting with Facebook and
Twitter are to be configured in the database via the Django admin
using the TwitterApp and FacebookApp models. 
