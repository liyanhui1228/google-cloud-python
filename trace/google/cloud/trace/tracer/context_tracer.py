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

from google.cloud.trace.trace import Trace
from google.cloud.trace.trace_context import TraceContext
from google.cloud.trace.trace_span import TraceSpan

from google.cloud.trace.samplers.always_on import AlwaysOnSampler


class ContextTracer(object):
    """The interface for tracing a request context.

    :type client: :class:`~google.cloud.trace.client.Client`
    :param client: The client that owns this API object.
    
    :rtype: :class:`~google.cloud.trace.trace_context.TraceContext`
    :returns: A TraceContext object.
    """
    _span_stack = []

    def __init__(self, client, trace_context=None, sampler=None):
        self.client = client

        if trace_context is None:
            trace_context = TraceContext()

        if sampler is None:
            sampler = AlwaysOnSampler()

        self.trace_context = trace_context
        self.sampler = sampler
        self.trace_id = trace_context.trace_id
        self.enabled = self.set_enabled()
        self.cur_trace = self.trace()

    def set_enabled(self):
        """Determine whether to sample this request or not.
        If the context forces not tracing, just set enabled to False.
        Else follow the sampler.

        :rtype: bool
        :returns: Whether to trace the request or not.
        """
        if self.trace_context.enabled is False:
            return False
        elif self.sampler.should_sample is True:
            return True
        else:
            return False

    def trace(self):
        """Create a trace using the context information.

        :rtype: :class:`~google.cloud.trace.trace.Trace`
        :returns: The Trace object.
        """
        if self.enabled is True:
            return Trace(client=self.client, trace_id=self.trace_id)
        else:
            return NullObject()

    def start_trace(self):
        """Start a trace."""
        if self.enabled is False:
            return

        self.cur_trace.start()

    def end_trace(self):
        """End a trace."""
        if self.enabled is False:
            return

        self.cur_trace.finish()

    def span(self, name='span'):
        """Create a new span with the trace using the context information.
        
        :type name: str
        :param name: The name of the span.
        
        :rtype: :class:`~google.cloud.trace.trace_span.TraceSpan`
        :returns: The TraceSpan object.
        """
        if self.enabled is True:
            parent_span_id = self.trace_context.span_id
            span = TraceSpan(name, parent_span_id=parent_span_id)
            self.cur_trace.spans.append(span)
            self._span_stack.append(span)
            self.trace_context.span_id = span.span_id
            return span
        else:
            return NullObject()

    def start_span(self, name='span'):
        """Start a span."""
        if self.enabled is False:
            return

        span = self.span(name=name)
        span.start()

    def end_span(self):
        """End a span. Remove the span from the span stack, and update the
        span_id in TraceContext as the current span_id which is the peek
        element in the span stack.
        """
        if self.enabled is False:
            return

        try:
            cur_span = self._span_stack.pop()
        except IndexError:
            raise

        cur_span.finish()

        if not self._span_stack:
            self.trace_context.span_id = None
        else:
            self.trace_context.span_id = self._span_stack[-1]


class NullObject(object):
    """Empty object as a helper for faking Trace and TraceSpan when tracing is
    disabled.
    """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass
