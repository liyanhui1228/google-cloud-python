# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""py.test shared testing configuration.

This defines fixtures (expected to be) shared across different test
modules.
"""

from google.cloud.ndb import model

import pytest


@pytest.fixture(autouse=True)
def reset_state():
    """Reset module and class level runtime state.

    To make sure that each test has the same starting conditions, we reset
    module or class level datastructures that maintain runtime state.

    This resets:

    - ``model.Property._FIND_METHODS_CACHE``
    - ``model.Model._kind_map``
    """
    assert model.Property._FIND_METHODS_CACHE == {}
    assert model.Model._kind_map == {}
    yield
    model.Property._FIND_METHODS_CACHE.clear()
    model.Model._kind_map.clear()
