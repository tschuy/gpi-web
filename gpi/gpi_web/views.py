from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

from gpi.gpi_web.models import Release, Project
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
