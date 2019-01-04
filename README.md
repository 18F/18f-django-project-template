# 18F Django project template

Django project templates are a [little-known option](https://docs.djangoproject.com/en/2.0/ref/django-admin/#cmdoption-startproject-template) that allows you to create new Django projects based on your own preferences and boilerplate. This means you can pre-install apps, templates and dependencies and have them already in place, predictably and consistently, when you start a new project.

This (currently WIP) project template is designed to make starting a new USWDS-based Django project as simple as possible, while including additional government-related boilerplate such as federated analytics tags. 

## Starting a new project

1. Follow the [instructions to install Django](https://docs.djangoproject.com/en/2.1/topics/install/)
2. In development, the project template will create a simple sqlite db. When you prep your staging and prod environments, you'll want to be sure postgresql is ready for you.
3. Make sure pipenv is installed: `pip install pipenv`
4. Create or navigate to your Git repository.
5. `pipenv install django`
6. Now you'll start your project pulling from this repo for the template: `django-admin.py startproject --template=https://github.com/tBaxter/tango-starter-kit/archive/master.zip project_name`. Be sure to replace `project_name` with whatever your project should be named.
7. And move the example.env file to `.env` to set up your development environment variables: `mv example.env .env`
8. Run `python manage.py runserver` and go take a look at your new project.


## What's next
Remember to go into your admin and set the site variables, so you don't show up as `example.com`

By default your AGENCY setting (used for analytics) is set to the project name. Since that's probably not what you want, you'll want to change that.


## What's included with the project template

- Django 2.0+ support
- `base.html` based on HTML5 Boilerplate, optimized for USWDS, accessibility and best practices.
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- Some additional context processors for useful items.


## Upcoming
- USWDS integration (NPM? Submodule? Preferences?)
- Cloud.gov readiness


## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

(Coming) It is possible to deploy to Cloud.gov or to your own server.

## License

TBD

# Notes
- [Checklist of Requirements for Federal Websites and Digital Services](https://digital.gov/resources/checklist-of-requirements-for-federal-digital-services/)
- 
