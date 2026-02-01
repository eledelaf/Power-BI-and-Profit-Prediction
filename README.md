# Power-BI-and-Profit-Prediction

# Data cleaning 

'Segment'=  
'Country'= Which country are those sales from  
'Product'= Which product are they buying
'Discount Band'=  Wich type of discount, None, low, medium, high
'Units Sold'= How many units have been sold that month 
'Manufacturing Price' = The price of creating one unit 
'Sale Price' = Price of the unit to the public
'Gross Sales' = 
'Discounts' = How much discounted was the unit
' Sales' =
'COGS' = Cost of Goods Sold represents the direct costs attributable to the production or purchase of goods sold by a business, including raw materials, direct labor, and manufacturing overhead
'Profit' = How much money they made with out the costs 
'Date' = Date of the pursache 

https://www.datacamp.com/blog/infographic-data-cleaning-checklist?utm_cid=19589720821&utm_aid=152984011334&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1006886-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~emea-en~dsa~tofu~blog~data-science&gad_source=1&gad_campaignid=19589720821&gbraid=0AAAAADQ9WsG6QLdUGnhkM3nohq3bZFgtO&gclid=Cj0KCQiAp-zLBhDkARIsABcYc6vt71dWX5gMtOC5DzinjBvuSu41Az5D9MZBGTSnevVzcX3ZzzgkpnwaAodsEALw_wcB

After using df.info() we can see that there are missing values in the "Discount Band" column. Lets see the column "Discount" depending on that we will give a value to the "Discount Band".

## Cardinality check 
https://www.datacamp.com/tutorial/cardinality?utm_cid=19589720821&utm_aid=157156374671&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1006886-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~emea-en~dsa~tofu~tutorial~data-science&gad_source=1&gad_campaignid=19589720821&gbraid=0AAAAADQ9WsG6QLdUGnhkM3nohq3bZFgtO&gclid=Cj0KCQiAp-zLBhDkARIsABcYc6tCszWLijHc3NM2ywCmQGCKeBpDVE18u1gRqB1CRLEENJxWDHh_3DUaApxmEALw_wcB

Cardinality refers to the number of unique values in a dataset column. A column with high cardinality contains a vast number of unique values, while columns with low cardinality contain fewer unique entries.

# Sales Performance Analysis
https://www.ibm.com/products/planning-analytics/sales-planning?utm_content=SRCWW&p1=Search&p4=41756381&p5=b&p9=169118374741&gclsrc=aw.ds&gad_source=1&gad_campaignid=22027252986&gbraid=0AAAAA-h2TOFSpa4pRPkK_g-hmshODEudN&gclid=Cj0KCQiAp-zLBhDkARIsABcYc6tiE6e5KQcpsIMyF_9Gqlu6F-6sutmYay59U-5f2dqJMc8ca2k9jcoaAonuEALw_wcB

## What do we want to answer
1. How much are we selling?
2. Is performance improving or declinign over time?
3. Which products drive results?
4. Are sales profitable?

## KPIs Key Performance Indicator 
KPIs are the most important quantifiable measures of progress toward your intended outcome.
1. Leading Indicators
2. Lagging indicators 

Caracteristics of KPIs:
1. Provide objective evidence that we are working towards the desired outcome.
2. Measure the right things to inform better decision making
3. Link to strategic Imperatives, create KPIs that mirrors our organisation priorities
4. Track how performance cahnges over time 
5. Track things that matter to us
6. Significant, measurable, achivable, relevant, trackable, ethical and time bound

How do I create good KPIs?

## Net Sales (Revenue)
The money that we actually earned selling pro

