from django.http import QueryDict
import json
from rest_framework import parsers


class MultipartJsonParser(parsers.MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        qdict = QueryDict('', mutable=True)
        if "data" in result.data:
            # find the data field and parse it
            data = json.loads(result.data["data"])
            qdict.update(data)
        else:
            data = None

        return parsers.DataAndFiles(qdict, result.files)
