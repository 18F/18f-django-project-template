# Dependencies included with the template
In the interest of full transparency, this is the full list of dependencies from the Pipfile
and why we include them:


| Name            | Usage                                                 |
|-----------------|-------------------------------------------------------|
| Django          | Well... yeah, of course                               |
| cfenv           | Simplifies interactions with Cloud.gov env variables  |
| cg-django-uaa   | Cloud.gov UAA authentication                          |
| dj-database-url | Easier and more secure DB handling                    |
| docutils        | To enable Django built-in documentation               |
| psycopg2-binary | For Postgresql                                        |
| typogrify       | Nice typographical utilitiies                         |
| whitenoise      | Simple static file serving                            |


## In Dev environments
The follow are also added in development environments

| Name                 | Usage                                            |
|----------------------|--------------------------------------------------|
| coverage             | For code coverage                                |
| django-debug-toolbar | General development debugging                    |
| factory-boy          | Testing                                          |
| flake8               | Linting                                          |
