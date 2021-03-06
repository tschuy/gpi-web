from django.core.serializers import json
from gpi.gpi_web.models import Project, Release


class PackageSerializer(json.Serializer):

    def get_dump_object(self, obj):
        self._current['id'] = obj.id

        if isinstance(obj, Project):
            self._current['releases'] = [
                {
                    'file': release.file.url,
                    'version': str(release.version)
                }
                for release in sorted(
                    obj.release_set.all(),
                    key=lambda o: o.version,
                    reverse=True) 
            ]
            self._current['owner'] = obj.owner.username;

        return self._current
