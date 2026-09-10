# Data Dictionary

## customer purchase intent dataset (real_estate_raw_messy.csv)

Synthetic data made to look like a real plot-buyer survey (deliberately messy - mixed
units, inconsistent Yes/No formatting, casing issues etc.) so cleaning has real work to do.

**The dataset is synthetically generated for academic demonstration and does not represent
actual customers of any real-estate company.**

| Column | Notes |
|---|---|
| Customer_ID | unique id |
| Age | 18-90 |
| Gender | Male/Female (messy in raw file) |
| Occupation | messy - grouped into broader categories during cleaning |
| City | 8 Indian cities, some abbreviations in raw file (BLR etc) |
| Monthly_Income | mixed formats in raw file (₹ symbol, "X Lakh/pm") |
| Annual_Income | mostly clean, used as fallback when monthly income missing |
| Family_Size | 1-7 |
| Current_Housing_Status | Owned / Rented / Living with Parents |
| Plot_Budget | mixed formats ("INR X", "X Lakh", "Not Disclosed") |
| Preferred_Plot_Size_SqFt | some rows in sq.yd instead of sq.ft |
| Preferred_Location | City Centre / Suburbs / Within City Limits / Periphery / Any |
| Distance_to_City_Center_km | a few negative values (data entry errors) |
| Purpose | Self-use / Investment |
| Loan_Required | Yes/No (messy) |
| Expected_Purchase_Timeline | 0-6 months / 6-12 months / 1-3 years / >3 years |
| Lead_Source | how the lead came in |
| Enquiry_Date | too messy to parse reliably, dropped during cleaning |
| Previous_Enquiry | Yes/No (messy) |
| Site_Visit | Yes/No (messy) |
| Negotiation_Done | Yes/No (messy) |
| Booking_Done | Yes/No - **not used as a model feature**, this happens after/alongside the purchase decision |
| Purchase_Probability | pre-computed probability - **not used as feature**, would leak the answer |
| Purchase_Intent | Low/Medium/High - descriptive label, not used as feature (redundant with target) |
| Purchased | **target column** for the classification model |
| Purchase_Value | amount if purchased - not used as feature (only exists after purchase) |

## listings dataset (real_estate_master.csv)

Real property listings merged from 12 source files - 4 cities (Chandigarh, Ghaziabad,
Lucknow, Pune) x 3 property types (Plot, Villa, Builder Floor). ~14k rows after cleaning.

Key columns: location, area, price, status, facing, furnished, security_deposit,
amenity flags (Club House, Gymnasium, Swimming Pool etc), city, property_type.

About 15 columns (project_score, builder_experience, Golf Course, Cafeteria etc.) were
dropped during cleaning - over 75% missing, not usable.

## scheme dataset (historical_scheme_data.csv)

800 historical residential plot schemes across 12 locations (Delhi, Gurugram, Greater
Noida, Pune, Ahmedabad, Kolkata, Bengaluru, Chennai, Faridabad, Hyderabad).

**Real inputs** (used as model features - known before launching a scheme):
Location, Plot_Size_SqFt, Price_INR, Monthly_EMI_INR, Park, Clubhouse,
Distance_from_Metro_km, Advertising_Budget_INR

**Target:** Scheme_Success_Score (0-100)

**Excluded from features (leakage):** Expected_Leads, Expected_Bookings,
Estimated_Conversion_Pct, Demand_Level, Target_Age_Group, Most_Likely_Buyers - these
are all outcomes of the same prediction problem (0.65-0.76 correlation with the target),
not information a manager would have in advance.
