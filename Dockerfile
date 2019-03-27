# Select the Python image we want to base our container on
# We use an official Python runtime as a parent image
FROM python:3.6

# We're taking a NAME argument, so this is just a default
ARG NAME=myproject

# The enviroment variable ensures that the python output 
# is set straight to the terminal without buffering it first.
ENV PYTHONUNBUFFERED 1

# Install node, so we can use `npm` later.
RUN apt-get update && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs

# Your pip version *should* be up-to-date, but just in case
# we'll be sure, and we'll go ahead and install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Now, we'll create a clean, empty working directory,
# so we're not working at /
WORKDIR /wd

# Install standard dependencies. Every project should have these
# These flags are important. Don't mess with them lightly.
RUN pipenv install --dev --system --skip-lock

# Now we'll install USWDS, too.
# After installation, it should be available at 
# code/node_modules/uswds/dist or
# code/node_modules/uswds/src
RUN npm install --save uswds

# Now let's attempt to create a new django project
# From our standard project template
RUN django-admin startproject --template=project_name ${NAME}

# Your /code working directory should now contain:
# Pipfile  node_modules  package-lock.json  project2

# MOVE into your new project
WORKDIR ${NAME}
