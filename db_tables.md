


Member |
------ |
member_id |
email |
password |


Profile |
------- |
profile_id |
member_id |
first_name |
last_name |


Band |
---- |
band_id |
owner_id |
member_set |


Engineer |
-------- |
engineer_id |
member_id |


Competition Type |
---------------- |
competion_type_id |
title |
description |
price |


Competition |
-----------	|
competition_id |
band_id |
competion_type_id |


Competition Profile |
------------------- |
competition_profile_id |
competition_id |
cometition_field_set |
zip_file |


Transaction |
----------- |
transation_id |
transaction_key |
transaction_data |


Competition Payment |
------------------- |
competition_payment_id |
competition_id |
member_id |
transation_id |
amount |


Competition Funding |
------------------- |
competition_funding_id |
competition_id |






