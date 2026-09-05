# E-commerce Growth Analytics

## Project Overview

This project analyzes transactional and behavioral data from an e-commerce company operating in the cosmetics sector in Russia. The company has experienced a relatively flat evolution in overall business performance during recent months and commissioned a data analytics project to identify potential growth opportunities across the customer journey.

The analysis focuses on understanding how users interact with the platform, how sessions convert into purchases, how customer value evolves over time and which products and product categories contribute most to revenue.

The project also implements advanced analytical assets, including **RFM customer segmentation** and an **item-item product recommendation system**, with the objective of supporting personalized CRO actions and improving the main commercial drivers of the business.

The analysis follows a **progressive approach**, moving from transactional and session-level behavior to customer analytics, product performance and ultimately business recommendations.

## Business Context

E-commerce growth depends on the interaction between traffic, conversion and customer value. A business may increase revenue by attracting more users, improving purchase rate (PR) per session, increasing average order value or encouraging existing customers to buy again.

For this reason, the analysis evaluates the customer journey at different levels:

* **Session level:** understanding visits, product interactions and conversion.
* **Customer level:** analyzing recurrence, retention, customer value and lifecycle.
* **Product level:** identifying products with strong revenue, engagement or conversion potential.
* **Category level:** identifying product categories with different commercial behaviors.

The objective is therefore not only to describe historical performance, but to identify where the company could concentrate its efforts to generate additional revenue.

## Project Objectives

The main objectives of this project are:

* Analyze transactional and behavioral data to understand session activity, conversion and purchasing patterns over time.
* Evaluate customer recurrence, retention and customer value, including high-value customer segmentation through RFM analysis.
* Assess product and category performance across engagement, conversion and revenue, including the impact of major commercial events.
* Build an item-item product recommendation system based on Euclidean distance.
* Translate analytical findings into CRO and commercial opportunities.
* Identify potential actions to improve key business drivers, including conversion, customer value and overall revenue.


## Dataset Description

### Database

The project uses the following database:

* `ecommerce.db`

The database contains event-level records from the e-commerce platform, including product views, cart interactions and purchases.

### Coverage Period

* Start date: **01/10/2019**
* End date: **28/02/2020**
* Total duration: **5 months**
* Expected data granularity: **individual product interactions**


## Repository Structure

```text
data/
├── raw/
├── processed/
notebooks/
reports/
├── graphics/
src/
README.md
requirements.txt
```

## Methodology

The analysis follows a progressive workflow, moving from event-level behavior to customer analytics and finally to product-level analysis.

1. Dataset Validation
2. Temporal and Market Context
3. Exploratory Data Analysis (EDA), divided into 4 main areas:
   3.1. Customer Session Analysis
   3.2. Product Interaction Event Analysis
   3.3. Customer Analysis
   3.4. Product Analysis
4. Product recommendation system (euclidean item-item based)
5. Business Interpretation and Recommendations

## Assumptions & Limitations

The analysis is based on approximately five months of transactional and behavioral data, with limited information about the company's commercial context.

Key business information such as marketing campaigns, advertising spend, acquisition channels, inventory, margins and customer acquisition costs was not available. Therefore, the identified opportunities should be interpreted as **data-driven hypotheses rather than confirmed causal relationships**.

Product and category identifiers are also not accompanied by detailed product information, so recommendations are based on observed behavioral and commercial metrics rather than full merchandising analysis.

## Dataset Validation

Given the event-based nature of the dataset, unusual behavioral patterns were generally retained to avoid removing potentially valid customer activity.

The only explicit data-quality rule applied was the removal of events with a product price **≤ 0**, which accounted for approximately **0.98% of the original dataset**.

<br>

# Key Findings

The following findings summarize the main results identified across session behavior, customer economics, retention, segmentation, product performance and product categories.

## Session & Conversion

### Insight 1: Overall Session Conversion Rate is 3.35%

The overall analytical session conversion rate observed is **3.35%**.
However, among analytical sessions containing at least **one product view**:

* **23.35%** progressed to at least one cart interaction.
* **3.58%** resulted in at least one purchase.

The analytical session definition splits sessions when periods of inactivity exceed **60 minutes**, reducing distortion from unusually long sessions while preserving the underlying events and purchases.

![Session Based Conversion Funnel](../reports/graphics/session_based_conversion_funnel.png)
*Session-based conversion funnel from product interaction to purchase.*

### Insight 2: December Shows a Declining Purchasing Trend, While Sales Concentrate Around Major Commercial Events

December shows a clear declining purchasing trend starting abruptly on **December 1st**, followed by a relatively flat and declining pattern during the second half of the month.

At the same time, purchasing activity is strongly concentrated around specific commercial periods.

The most relevant periods identified are:

* ***Black Friday week (22–29 November)** and Black Friday itself.
* ***Russian Cyber Monday (27–29 January)**.
* *The days immediately preceding **Singles' Day (11 November)**.

![Purchases and Views During High Sales Periods](../reports/graphics/purchases_views_on_high_sales_period.png)
*Purchase and view events during the main high-sales periods.*

This indicates that commercial events have a meaningful relationship with purchasing activity and should be considered when allocating marketing effort.


## Primary Customer Analysis

### Insight 3.1: Repeat Customers Generate a Disproportionate Share of Revenue

Only **21.74% of customers make repeat purchases**, but this group generates **48.44% of total sales** and spends approximately **3.4 times more** than customers who purchase only once.

At the same time, customers who purchase only once represent **78.26% of the customer base** while still generating **51.55% of historical revenue**.

This highlights customer recurrence as one of the strongest potential growth levers identified in the analysis.

### Insight 3.2: Revenue is Highly Concentrated Among High-Value Customers

The **top 10% of customers generate 42.44% of total sales**, while the top 20% generate **58.93%**.

High-value customers also combine higher purchasing frequency with higher revenue per session:

| Metric                    | Top 10% |  Rest |
| ------------------------- | ------: | ----: |
| Average purchase sessions |    3.22 |  1.21 |
| Revenue per session       |  107.70 | 30.53 |

This indicates that high-value customers are valuable through both purchasing frequency and spending intensity.

### Insight 3.3: Single-Purchase Customers Represent the Majority of the Customer Base

Customers who have purchased only once represent **78.26% of the customer base**. Despite their low recurrence, this group still generates **51.55% of historical revenue**.

### Insight 3.4: A Large Share of Customers is Currently Inactive

**54.28% of customers have not made a purchase during the last 60 days**, while this group represents **43.33% of historical revenue**.

Customer activity also declines rapidly after purchase:

* **75.34%** of customers have not purchased for more than 30 days.
* **87.47%** have not purchased for more than 15 days.

## Insight 3.5: The Repurchase Window is Relatively Short

Among repeat customers, the median period between the first and last purchase is **43 days**. This behaviour underlines the importance of encouraging repeat purchases during the first two months in order to increase customer retention and lifetime value.

## Cohort analysis

### Insight 3.6: Customer Retention Declines Across Subsequent Cohort Months

Cohort analysis shows that retention remains around **10% in the second month** and approximately **8% in the third month**. The results indicate that improving early retention and increasing second-purchase probability represent significant opportunities for increasing customer value.
The analysis also shows that 21.74% of customers are repeat customers overall, generating 48.44% of total revenue, highlighting the economic relevance of returning customers.

## Customer Lifetime Value

### Insight 3.7: LTV Increases 33.08% During the First Three Months

Average customer Lifetime Value reaches **59.11 after three months**, increasing **33.08%** from an initial value of **44.42**.
Comparable cohorts also show relatively consistent growth of approximately **10–12% during the first month**. This reinforces the importance of the early customer lifecycle for maximizing the economic return from acquired customers.

## RFM Customer Segmentation

An RFM segmentation was implemented using recency, purchase frequency and customer monetary value. The segmentation reveals substantial differences in customer value and purchasing behavior.

### Insight 3.8: Promising and Hibernating Segments Represent a Large Share of potential Value Customers

**Promising (29.1%) and Hibernating (17.1%) represent 46.2% of customers and generate 36.4% of historical revenue.**

These segments represent a substantial proportion of the customer base and therefore provide significant opportunities for customer development and reactivation.

![RFM Customer vs Revenue Share](../reports/graphics/rfm_customer_vs_revenue_share.png)

*Customer distribution and historical revenue contribution by RFM segment.*

### Insight 3.9: At Risk Customers Have Disproportionately High Economic Value

The **At Risk segment represents only 1.1% of customers but generates 5.3% of revenue**, corresponding to a **4.68× value index**.

![RFM Value Index](../reports/graphics/rfm_value_index.png)

*Relative economic value of each RFM customer segment.*

### Insight 3.10: Champions Represent a Small but Extremely Valuable Customer Group

**Champions generate 9.6% of revenue while representing only 1.2% of customers**, resulting in a **7.75× value index**.

Champions also generate approximately **15.62 products per session** and **70.45 revenue per session**, considerably above Loyal Customers. This unusual purchasing volume suggests that Champions may display substantially different purchasing behavior from the broader customer base.

## Product Performance

### Insight 4.1: Revenue is Highly Concentrated in a Small Number of Products

* The **top 20% of products generate approximately 86.6% of total revenue**, while the top 1% account for approximately **33.4%**.
* Product **5809910** stands out as the most popular product by a considerable margin and ranks **second in total revenue**.

This indicates strong dependence on a relatively small group of commercial leaders combined with a long tail of lower-revenue products.

### Insight 4.2: Products Show Distinct Commercial Profiles

Product-level analysis identifies several relevant profiles:

* Products **89343, 5560756 and 5560754** generate substantial revenue while showing relatively low PR of approximately **1–5%**.
* Products including **5809858, 5867091, 5622678, 5809860, 5798928, 5867090 and 5787965** reach PR between approximately **39% and 50%** despite relatively low engagement.
* Products **5792800, 5810480, 5528035, 5751422, 5849033, 5751383 and 5809910** combine relatively high revenue with PR between approximately **9% and 30%**.
* Products **5729864** and **5843836** reach exceptionally high PR of **57% and 55%** respectively.

### Insight 4.3: Product 5809910 Shows Exceptional Engagement

Product **5809910** has a significantly higher engagement rate than the rest of the analyzed catalog while also ranking highly in revenue and popularity.

![Product Engagement vs Purchase Rate](../reports/graphics/product_engagement_vs_purchase_rate.png)

*Relationship between product engagement and PR.*

This makes it a particularly relevant product for investigating the drivers of unusually high customer interaction.

### Insight 4.4: Major Commercial Events Amplify Specific Products

Product performance changes significantly around major commercial events.

* During **Black Friday**, products **89343, 5560754 and 5560756** show the strongest combination of revenue and lift.
* During **Cyber Monday**, the leading products differ, with **5877506, 5906217, 89343, 5588154 and 5768981** showing the strongest performance.

![Black Friday vs Cyber Monday](../reports/graphics/black_friday_vs_cyber_monday_dumbbell.png)
*Comparison of product performance during Black Friday and Cyber Monday.*

The analysis also identifies products with relatively stable revenue throughout the observation period, providing a more consistent revenue base outside major promotional events.

![Top 50 Product Revenue Stability](../reports/graphics/top_50_product_revenue_stability_heatmap.png)
*Revenue stability across the observation period for the top 50 products.*

Several products also display strong performance concentrated in specific periods, including:

* **5850281:** approximately 2.82× the global average sales in December.
* **89343:** strong performance during major commercial events.
* **5877453:** approximately 2.41× average sales in February.
* **5877454:** approximately 1.82× and 1.90× in October and November.
* **5560756:** approximately 2.15× average sales in October.

These results indicate that product performance should be evaluated in its temporal and commercial context rather than assuming stable demand across all periods.

## Product Category Analysis

### Insight 5: Product Categories Display Different Commercial Profiles

Category-level analysis reveals substantial differences in engagement, revenue and PR.

![Category Engagement vs Purchase Rate](../reports/graphics/category_engagement_vs_purchase_rate.png)
*Engagement and PR across product categories.*

* Category **1487580005092295511** is the most engaged category, with approximately **24,592 engaged sessions**, and generates the highest total revenue at **40,547.66**.

Two categories stand out when considering **both revenue and PR**:

| Category            |   Revenue | Purchase Rate |
| ------------------- | --------: | ------------: |
| 1487580005268456287 | 25,962.73 |           17% |
| 1487580006317032337 | 17,397.78 |           15% |

Several categories show high PR despite lower total revenue, suggesting potential opportunities to increase exposure.


Conversely:

* **1487580006300255120:** 32,576.40 revenue and approximately 2% PR.
* **1487580013950664926:** 14,374.37 revenue and approximately 3% PR.

Both categories present really low PR given their high total revenue. When compared with other product categories with similar revenue, such as *1487580006300255120 and 1487580013950664926* (11% and 13% resp.), the only notable difference observed lies in the price of the products (categories with low PR have a much higher median product price than the medians of categories with higher PR and the overall median). This may suggest that investing more in advertising for these categories may not necessarily increase their conversion rate, as their nature may be completely different (as no information is available on the categories beyond their identification numbers, it has not been possible to compare their nature).

<br>

# Advanced Analytical Assets

## Product Recommendation System

An **item-item recommendation system based on Euclidean distances** was implemented as an additional analytical asset.

The system identifies products that are behaviorally similar and provides recommendations that could support:

* Cross-selling
* Product discovery
* Personalized product pages
* Post-purchase recommendations
* Retention campaigns
* Increasing the number of products purchased per session

The recommendation system should be considered an analytical prototype rather than a fully productionized recommendation engine. Before deployment, its effectiveness should be validated using appropriate recommendation metrics and, ideally, online experimentation.

<br>

# Recommendations
Based on the complete analysis, the main opportunities identified can be grouped into five strategic areas.

## 1. Prioritize Retention Before Relying Exclusively on Acquisition
Customer **recurrence and retention** represent one of the strongest opportunities identified. The business should establish a structured customer lifecycle focused on increasing the probability of a **second purchase** and retaining high-value customers.

## 2. Develop Segment-Specific CRM Strategies
The RFM segmentation shows that customers have substantially different economic value and purchasing behavior.

Priority groups include:

* **Champions:** protect and expand their value.
* **At Risk:** prevent the loss of high-value customers.
* **Promising:** increase recurrence and move customers toward higher-value segments.
* **Hibernating:** reactivate before customer value deteriorates further.
* **New Customers:** maximize the probability of a second purchase.

## 3. Concentrate Marketing Around High-Impact Commercial Events
Purchasing activity is particularly concentrated around major commercial periods, especially **Black Friday, Cyber Monday and the period preceding Singles' Day**. Therefore, marketing resources and product assortments should be adapted to the historical response observed during each event.

## 4. Protect Best Sellers While Developing the Long Tail
Revenue is highly concentrated in a relatively small number of products. The business should protect availability and visibility of key revenue drivers while identifying high-conversion products with low engagement that could benefit from increased exposure.

## 5. Use Personalization to Increase Conversion and Customer Value
The combination of RFM segmentation and the product recommendation system provides the foundations for a more personalized CRO strategy. Potential applications include personalized product recommendations, cross-selling, post-purchase recommendations and segment-specific retention campaigns.

<br>

# Future Work
Possible extensions of this project include:

### Marketing & Acquisition Analysis
Integrate **marketing campaign data, advertising spend, acquisition channels, customer acquisition cost and campaign attribution** to distinguish changes in customer behavior from changes driven by marketing activity.

### CRO Experimentation
Validate the identified opportunities through controlled A/B tests covering **product-page improvements, second-purchase incentives, personalized recommendations, segment-specific offers, promotional messaging and product merchandising**.

### Recommendation System Evaluation
Evaluate and improve the recommendation system using metrics such as **Precision@K, Recall@K, Hit Rate, NDCG, conversion uplift and revenue per session**. Online experimentation would be required before considering production deployment.

### Predictive Customer Modeling
Extend the customer analysis with models estimating **repeat-purchase probability, churn probability, expected customer value and purchase propensity**, potentially combining these predictions with the existing RFM segmentation.

### Product Demand Forecasting
Use the identified temporal patterns to support **product demand forecasting, event-specific demand estimation, inventory planning and seasonal product identification**.

### Product & Category Enrichment
Integrate additional product metadata such as **product name, type, brand, price, margin, target customer, characteristics, inventory and launch date** to move from behavioral analysis toward more complete merchandising analytics.

<br>

# Conclusion
This project demonstrates how transactional and behavioral e-commerce data can be transformed into actionable insights across the customer journey.

The analysis identifies **customer retention, customer segmentation, product concentration and event-driven purchasing behavior** as the main growth opportunities.

Repeat customers generate a disproportionate share of revenue, while RFM segmentation reveals high-value customer groups requiring differentiated strategies. Product analysis also highlights opportunities to improve visibility of high-conversion products while protecting key revenue drivers.

Overall, the strongest growth opportunity lies in combining **retention, behavioral segmentation, personalization and targeted CRO experimentation**.

The RFM segmentation and recommendation system provide analytical foundations for implementing and testing these strategies, while future experimentation should be used to validate which actions generate measurable incremental revenue.
