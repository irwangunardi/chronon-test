from ai.chronon.join import Join, JoinPart
from ai.chronon.api.ttypes import Source, EventSource
from ai.chronon.query import Query, select
from ai.chronon.group_by import (
    GroupBy,
    Aggregation,
    Accuracy,
    Operation,
)

referral_source = Source(
    events=EventSource(
        table="case_referral_agg.referral",
        query=Query(
            selects=select("referrer_user_id", "friend_user_id"),
            time_column="ts",
        )
    )
)

payment_source = Source(
    events=EventSource(
        table="case_referral_agg.payment",
        query=Query(
            selects=select("payment_id", "user_id"),
            time_column="ts")
    )
)

v1 = Join(
    left=referral_source,
    right_parts=[
        JoinPart(
            group_by=GroupBy(
               name="friend_agg",
               sources=[payment_source],
               keys=["user_id"],
               online=True,
               aggregations=[
                   Aggregation(
                       input_column="payment_id",
                       operation=Operation.COUNT,
                   ),
               ],
               output_namespace="case_referral_agg",
               accuracy=Accuracy.SNAPSHOT
           ),
           key_mapping={'friend_user_id': 'user_id'}
       )],
    output_namespace="case_referral_agg"
)