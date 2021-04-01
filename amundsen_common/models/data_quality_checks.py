# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import attr
from marshmallow3_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class TableQualityCheck:
    check_id: str = attr.ib()
    last_execution_status: str = attr.ib()
    last_execution_timestamp: int = attr.ib()


class TableQualityCheckSchema(AttrsSchema):
    class Meta:
        target = TableQualityCheck
        register_as_scheme = True
