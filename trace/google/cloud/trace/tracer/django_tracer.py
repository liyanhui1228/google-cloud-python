# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    import flask
except ImportError:  # pragma: NO COVER
    flask = None

from google.cloud.trace.tracer.middleware.request import (
    _get_django_request)

from google.cloud.trace.trace_context import generate_context_from_header
from google.cloud.trace.tracer.context_tracer import ContextTracer

_DJANGO_TRACE_HEADER = 'HTTP_X_CLOUD_TRACE_CONTEXT'


class DjangoTracer(ContextTracer):
    """The django implementation of the ContextTracer Interface.

    :type client: :class:`~google.cloud.trace.client.Client`
    :param client: The client that owns this API object.
    """

    def __init__(self, client, trace_context=None):
        if trace_context is None:
            header = get_django_header()
            trace_context = generate_context_from_header(header)

        super(DjangoTracer, self).__init__(
            client=client,
            trace_context=trace_context)


def get_django_header():
    """Get trace context header from django request headers.

    :rtype: str
    :returns: Trace context header in HTTP request headers.
    """
    request = _get_django_request()

    if request is None:
        return None

    header = request.META.get(_DJANGO_TRACE_HEADER)
    if header is None:
        return None

    return header
