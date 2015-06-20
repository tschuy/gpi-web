from django.shortcuts import render
from django.http import JsonResponse
import json

from gpi.gpi_web.models import Release, Project
from gpi.gpi_web.serializer import PackageSerializer

def project_details(request, name=None):
    project = Project.objects.get(package_name=name)

    serializer = PackageSerializer()

    data = json.loads(
        serializer.serialize(
            [project],
            use_natural_foreign_keys=True
        )[1:-1]
    )

    return JsonResponse(data)
