from ai.chronon.join import Join, JoinPart
from ai.chronon.api.ttypes import Source, EventSource
from ai.chronon.query import Query, select
from ai.chronon.api import ttypes
from ai.chronon.group_by import (
    GroupBy,
    Aggregation,
    Accuracy,
    Operation,
)

from group_bys.case_referral_agg.referral_agg import v1 as referral_agg

source = Source(
    events=EventSource(
        table="case_referral_agg.observation",
        query=Query(
            selects=select("user_id"),
            time_column="ts",
        )
    )
)

v1 = Join(
    left=source,
    right_parts=[JoinPart(
        group_by=referral_agg,
        key_mapping={'user_id': 'referrer_user_id'}
    )],
    output_namespace="case_referral_agg"
)


