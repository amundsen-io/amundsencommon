# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

import attr
from marshmallow3_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class TableQualityCheckRun:
    run_id: str = attr.ib()
    execution_status: str = attr.ib()
    execution_timestamp: int = attr.ib()


class TableQualityCheckRunSchema(AttrsSchema):
    class Meta:
        target = TableQualityCheckRun
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class TableQualityCheck:
    check_id: str = attr.ib()
    runs: Optional[List[TableQualityCheckRun]] = []


class TableQualityCheckSchema(AttrsSchema):
    class Meta:
        target = TableQualityCheck
        register_as_scheme = True
