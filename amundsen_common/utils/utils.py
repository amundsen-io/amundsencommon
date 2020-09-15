# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional, TypeVar

X = TypeVar('X')


def check_not_none(x: Optional[X], *, message: str = 'is None') -> X:
    if x is None:
        raise RuntimeError(message)
    return x
