# Power-BI-and-Profit-Prediction

# Data cleaning 
https://www.datacamp.com/blog/infographic-data-cleaning-checklist?utm_cid=19589720821&utm_aid=152984011334&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1006886-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~emea-en~dsa~tofu~blog~data-science&gad_source=1&gad_campaignid=19589720821&gbraid=0AAAAADQ9WsG6QLdUGnhkM3nohq3bZFgtO&gclid=Cj0KCQiAp-zLBhDkARIsABcYc6vt71dWX5gMtOC5DzinjBvuSu41Az5D9MZBGTSnevVzcX3ZzzgkpnwaAodsEALw_wcB

After using df.info() we can see that there are missing values in the "Discount Band" column. Lets see the column "Discount" depending on that we will give a value to the "Discount Band".

## Cardinality check 
https://www.datacamp.com/tutorial/cardinality?utm_cid=19589720821&utm_aid=157156374671&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1006886-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~emea-en~dsa~tofu~tutorial~data-science&gad_source=1&gad_campaignid=19589720821&gbraid=0AAAAADQ9WsG6QLdUGnhkM3nohq3bZFgtO&gclid=Cj0KCQiAp-zLBhDkARIsABcYc6tCszWLijHc3NM2ywCmQGCKeBpDVE18u1gRqB1CRLEENJxWDHh_3DUaApxmEALw_wcB

Cardinality refers to the number of unique values in a dataset column. A column with high cardinality contains a vast number of unique values, while columns with low cardinality contain fewer unique entries.
