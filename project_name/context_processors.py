import datetime
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def site_processor(request):
    # convenience method to avoid DB hit of request.user
    authenticated_request = request.user.is_authenticated

    return {
        'site': get_current_site(request),
        'project_name': getattr(settings, 'PROJECT_NAME', None),
        'current_path': request.get_full_path(),
        'authenticated_request': authenticated_request,
        'agency': getattr(settings, 'AGENCY', None),
    }