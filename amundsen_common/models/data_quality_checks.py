# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import attr
from marshmallow3_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class TableQualityChecksSummary:
    num_passing_checks: int = attr.ib()
    num_total_checks: int = attr.ib()
    last_run_timestamp: int = attr.ib()


class TableQualityChecksSummarySchema(AttrsSchema):
    class Meta:
        target = TableQualityChecksSummary
        register_as_scheme = True
