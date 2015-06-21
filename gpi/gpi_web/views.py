from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError

import json

from gpi.gpi_web.models import Release, Project, Email
from gpi.gpi_web.serializer import PackageSerializer

def project_details(request, name=None):
    project = get_object_or_404(Project, package_name=name)

    serializer = PackageSerializer()

    data = json.loads(
        serializer.serialize(
            [project],
            use_natural_foreign_keys=True
        )[1:-1]
    )

    return JsonResponse(data)

def index(request):
    return render(request, 'index.html', {})


@require_POST
def email(request):
    try:
        print request.GET.get('email')
        validate_email(request.GET.get('email'))
        email = Email.objects.create(email=request.GET.get('email'))
    except IntegrityError:
        return JsonResponse(
            {'status': False, 'errortext': "You've already signed up!"})
    except ValidationError:
        return JsonResponse(
            {'status': False, 'errortext': 'Invalid email address!'})
    else:
        return JsonResponse({'status': True})
