# Copyright 2019 Zuru Tech HK Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Callback definition
"""

from ashpy.contexts import BaseContext


class Callback:
    r"""
    Callback definition.
    Every callback must extend from this class.
    This class defines the basic events.
    Every event takes as input the context in order to use the objects defined.

    Order:

    .. code-block::

        --on_train_start

        ----on_epoch_start

        ------on_batch_start

        ------on_batch_end

        ----on_epoch_end

        --on_train_end

        on_exception – if an Exception was raised

    """
    def on_train_start(self, context: BaseContext) -> None:
        """
        Method called at the beginning of the training loop

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """

    def on_train_end(self, context: BaseContext) -> None:
        """
        Method called at the end of the training loop

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """

    def on_epoch_start(self, context: BaseContext) -> None:
        """
        Method called at the beginning of an epoch

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """

    def on_epoch_end(self, context: BaseContext) -> None:
        """
        Method called at the end of an epoch

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """

    def on_batch_start(self, context: BaseContext) -> None:
        """
        Method called at the beginning of a batch

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """

    def on_batch_end(self, context: BaseContext) -> None:
        """
        Method called at the end of a batch

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """

    def on_exception(self, context: BaseContext) -> None:
        """
        Method called when an exception is raised

        Args:
            context (:py:class:`ashpy.contexts.base_context.BaseContext`): training context

        """
