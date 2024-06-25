# Case referral agg

### Environment
Quickstart docker container

### Features
- All friends total purchase count

### Accuracy
SNAPSHOT

### Data
Data is in data/case_referral_agg.md

### Purpose
It is tricky because purchase event happen after the referral event.

### Scripts
```
# Copy files into quickstart container
docker cp group_bys b28b04fe2716:/srv/chronon
docker cp joins b28b04fe2716:/srv/chronon
docker cp teams.json b28b04fe2716:/srv/chronon

# Make it to use latest Chronon version
unset CHRONON_DRIVER_JAR

# Compile and run backfill
rm -rf production
compile.py --conf=joins/case_referral_agg/observation.py
run.py --conf=production/joins/case_referral_agg/observation.v1
```

Sample result
```agsl
-RECORD 0--------------------------------------------------------------------------
 user_id                                                           | userA         
 ts                                                                | 1701172800000 
 case_referral_agg_referral_agg_v1_friend_agg_payment_id_count_sum | null           <--- expected is 2 
 ds                                                                | 2023-11-28
```
