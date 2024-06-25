DROP DATABASE `case_referral_agg` CASCADE;
CREATE DATABASE `case_referral_agg`;

CREATE TABLE `case_referral_agg`.`referral` (
                                             `ts` BIGINT,
                                             `referrer_user_id` STRING,
                                             `friend_user_id` STRING,
                                             `ds` STRING)
    USING parquet
PARTITIONED BY (ds);
INSERT INTO `case_referral_agg`.`referral` values ( unix_timestamp('2023-11-25 11:00:00') * 1000 , 'userA', 'userB', '2023-11-25');
INSERT INTO `case_referral_agg`.`referral` values ( unix_timestamp('2023-11-26 11:00:00') * 1000 , 'userA', 'otherUser', '2023-11-26');

CREATE TABLE `case_referral_agg`.`payment` (
                                                  `ts` BIGINT,
                                                  `user_id` STRING,
                                                  `payment_id` STRING,
                                                  `ds` STRING)
    USING parquet
PARTITIONED BY (ds);
INSERT INTO `case_referral_agg`.`payment` values ( unix_timestamp('2023-11-26 11:00:00') * 1000 , 'userB', 'payment1', '2023-11-26');
INSERT INTO `case_referral_agg`.`payment` values ( unix_timestamp('2023-11-27 11:00:00') * 1000 , 'userB', 'payment2', '2023-11-27');

CREATE TABLE `case_referral_agg`.`observation` (
                                                 `ts` BIGINT,
                                                 `user_id` STRING,
                                                 `ds` STRING)
    USING parquet
PARTITIONED BY (ds);
INSERT INTO `case_referral_agg`.`observation` values ( unix_timestamp('2023-11-28 12:00:00') * 1000, 'userA', '2023-11-28');
-- at this point we expect have 2 total payments from all his friends