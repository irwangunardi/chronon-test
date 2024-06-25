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

from joins.case_referral_agg.friend_agg import v1 as friend_agg

v1 = GroupBy(
    sources=ttypes.Source(joinSource=ttypes.JoinSource(
        join=friend_agg,
        query=Query(
            selects=select(
                referrer_user_id="referrer_user_id",
                friend_user_id="friend_user_id",
                amount="friend_agg_payment_id_count"
            ),
            time_column="ts")
    )),
    keys=["referrer_user_id"],
    aggregations=[
        Aggregation(input_column="friend_agg_payment_id_count", operation=Operation.SUM)
    ],
    online=True,
    output_namespace="case_referral_agg",
    accuracy=Accuracy.SNAPSHOT
)