"""
Real Estate Prediction Dashboard
Three tabs - Purchase Intent, Price Prediction, Scheme Success.
Run with: streamlit run app/app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Real Estate Prediction", page_icon="🏠", layout="centered")

# ---------------------------------------------------------------------------
# Model loading - each tab uses whichever version (original or _v2) won
# ---------------------------------------------------------------------------
@st.cache_resource
def load_price_models():
    pipe = joblib.load("models/price_model_pipeline_v2.pkl")
    log_min, log_max = joblib.load("models/price_log_clip_range_v2.pkl")
    quantile_models = joblib.load("models/price_quantile_models_v2.pkl")
    return pipe, log_min, log_max, quantile_models

@st.cache_resource
def load_purchase_intent_models():
    reg_model = joblib.load("models/purchase_multi_output_model_v2.pkl")
    reg_scaler = joblib.load("models/purchase_reg_scaler.pkl")
    reg_cols = joblib.load("models/purchase_reg_columns.pkl")
    reg_targets = joblib.load("models/purchase_reg_targets.pkl")
    clf_model = joblib.load("models/purchase_intent_classifier.pkl")
    clf_scaler = joblib.load("models/purchase_intent_clf_scaler.pkl")
    clf_cols = joblib.load("models/purchase_intent_clf_columns.pkl")
    return reg_model, reg_scaler, reg_cols, reg_targets, clf_model, clf_scaler, clf_cols

@st.cache_resource
def load_scheme_models():
    reg_model = joblib.load("models/scheme_multi_output_model.pkl")
    reg_scaler = joblib.load("models/scheme_reg_scaler.pkl")
    reg_cols = joblib.load("models/scheme_reg_columns.pkl")
    reg_targets = joblib.load("models/scheme_reg_targets.pkl")
    clf_model = joblib.load("models/scheme_demand_classifier.pkl")
    clf_scaler = joblib.load("models/scheme_demand_scaler.pkl")
    clf_cols = joblib.load("models/scheme_demand_columns.pkl")
    return reg_model, reg_scaler, reg_cols, reg_targets, clf_model, clf_scaler, clf_cols

tab1, tab2, tab3 = st.tabs(["Purchase Intent", "Price Prediction", "Scheme Success"])

# ---------------------------------------------------------------------------
# TAB 1 - purchase intent
# ---------------------------------------------------------------------------
with tab1:
    st.header("Will this customer buy?")

    reg_model, reg_scaler, reg_cols, reg_targets, clf_model, clf_scaler, clf_cols = load_purchase_intent_models()
    num_cols_used = list(reg_scaler.feature_names_in_)

    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age", 18, 90, 35)
        gender = st.selectbox("Gender", ["Male", "Female"])
        occupation = st.selectbox("Occupation", [
            "IT & Software", "Business Owner", "Government & PSU", "Healthcare",
            "Education", "Real Estate & Construction", "Retail & Commerce",
            "Manufacturing & Engineering", "Retired", "Unknown"
        ])
        city = st.selectbox("City", ["Mumbai", "Delhi", "Bengaluru", "Hyderabad",
                                       "Pune", "Chennai", "Kolkata", "Noida", "Gurugram"])
        monthly_income = st.number_input("Monthly Income (INR)", 10000, 1000000, 80000, step=5000)
        family_size = st.slider("Family Size", 1, 7, 4)
        housing_status = st.selectbox("Current Housing Status", ["Owned Flat/House", "Rented", "Living with Parents"])

    with c2:
        budget = st.number_input("Plot Budget (INR)", 500000, 50000000, 5000000, step=100000)
        plot_size = st.number_input("Preferred Plot Size (sqft)", 300, 5000, 1200, step=50)
        distance = st.slider("Distance to City Center (km)", 0, 60, 20)
        preferred_location = st.selectbox("Preferred Location", [
            "City Centre", "Suburbs", "Within City Limits", "Periphery / Growth Corridor"
        ])
        purpose = st.radio("Purpose", ["Self-use", "Investment"], horizontal=True)
        loan_required = st.radio("Loan Required", ["Yes", "No"], horizontal=True)
        timeline = st.selectbox("Expected Purchase Timeline", ["0-6 months", "6-12 months", "1-3 years", ">3 years"])
        lead_source = st.selectbox("Lead Source", [
            "Google & Social Media Ads", "Magicbricks / Real Estate Portal",
            "Channel Partner / Broker", "Print / Newspaper Ad", "Direct Walk-in / Exhibition"
        ])

    st.subheader("Behaviour so far")
    b1, b2, b3 = st.columns(3)
    with b1:
        previous_enquiry = st.checkbox("Previous Enquiry")
    with b2:
        site_visit = st.checkbox("Site Visit Done")
    with b3:
        negotiation = st.checkbox("Negotiation Done")

    if st.button("Predict Purchase Intent", type="primary"):
        row = {c: 0 for c in reg_cols}
        row["Age"] = age
        row["Monthly_Income"] = monthly_income
        row["Annual_Income"] = monthly_income * 12
        row["Family_Size"] = family_size
        row["Plot_Budget"] = budget
        row["Preferred_Plot_Size_SqFt"] = plot_size
        row["Distance_to_City_Center_km"] = distance

        for key, val in [
            (f"Gender_{gender}", 1),
            (f"Occupation_{occupation}", 1),
            (f"City_{city}", 1),
            (f"Current_Housing_Status_{housing_status}", 1),
            (f"Preferred_Location_{preferred_location}", 1),
            (f"Purpose_{purpose}", 1),
            (f"Loan_Required_{loan_required}", 1 if loan_required == "Yes" else 0),
            (f"Expected_Purchase_Timeline_{timeline}", 1),
            (f"Lead_Source_{lead_source}", 1),
            ("Previous_Enquiry_Yes", 1 if previous_enquiry else 0),
            ("Site_Visit_Yes", 1 if site_visit else 0),
            ("Negotiation_Done_Yes", 1 if negotiation else 0),
        ]:
            if key in row:
                row[key] = val

        reg_input_df = pd.DataFrame([[row[c] for c in reg_cols]], columns=reg_cols)
        reg_input_df[num_cols_used] = reg_scaler.transform(reg_input_df[num_cols_used])
        reg_pred = reg_model.predict(reg_input_df)[0]
        pred_dict = dict(zip(reg_targets, reg_pred))

        clf_input_df = pd.DataFrame([[row[c] for c in clf_cols]], columns=clf_cols)
        clf_num_cols = list(clf_scaler.feature_names_in_)
        clf_input_df[clf_num_cols] = clf_scaler.transform(clf_input_df[clf_num_cols])
        intent_pred = clf_model.predict(clf_input_df)[0]

        badge = {"High": st.success, "Medium": st.warning, "Low": st.error}.get(intent_pred, st.info)
        badge(f"Purchase Intent: {intent_pred}")

        m1, m2 = st.columns(2)
        m1.metric("Purchase Probability", f"{pred_dict['Purchase_Probability']:.0%}")
        m2.metric("Expected Purchase Value", f"Rs {max(pred_dict['Purchase_Value'], 0):,.0f}")

        st.caption("Expected Purchase Value is the less reliable of these two numbers - "
                   "treat it as a rough guide rather than a precise figure.")

# ---------------------------------------------------------------------------
# TAB 2 - price prediction
# ---------------------------------------------------------------------------
with tab2:
    st.header("What should this property cost?")

    pipe, log_min, log_max, quantile_models = load_price_models()

    c1, c2 = st.columns(2)
    with c1:
        city2 = st.selectbox("City", ["Chandigarh", "Ghaziabad", "Lucknow", "Pune"], key="price_city")
        property_type = st.selectbox("Property Type", ["Builderfloor", "Plot", "Villa"])
        location = st.text_input("Locality / Location", "Wagholi")
        area = st.number_input("Area (sq.ft.)", 200, 20000, 1200, step=50)
        facing = st.selectbox("Facing Direction", ["Unknown", "North", "Northeast", "East", "Southeast",
                                                     "South", "Southwest", "West", "Northwest"])
        age_of_property = st.number_input("Age of Property (years)", 0, 50, 2)

    with c2:
        security_deposit = st.number_input("Security Deposit (Rs)", 0, 5000000, 0, step=5000)
        locality_score = st.slider("Locality Score (1-10)", 1.0, 10.0, 6.0, step=0.5)
        new_resale = st.radio("New or Resale", ["New", "Resale"], horizontal=True)
        price_negotiable = st.radio("Price Negotiable?", ["Yes", "No"], horizontal=True)
        furnished = st.radio("Furnished?", ["Yes", "No"], horizontal=True)

    st.subheader("Amenities")
    amenity_labels = ["Lift(s)", "Full Power Backup", "24 X 7 Security", "Children's play area",
                       "Club House", "Gymnasium", "Swimming Pool", "Sports Facility",
                       "Jogging Track", "Landscaped Gardens", "Car Parking"]
    a_cols = st.columns(3)
    amenities = {}
    for i, label in enumerate(amenity_labels):
        with a_cols[i % 3]:
            amenities[label] = st.checkbox(label, key=f"price_amenity_{label}")

    description = st.text_area("Listing Description (optional)", "",
                                help="Keywords like metro, luxury, premium, gated, corner plot, spacious are picked up automatically.")

    if st.button("Predict Price", type="primary", use_container_width=True):
        amenity_count = sum(1 for k, v in amenities.items() if v and k != "Car Parking")
        desc_lower = description.lower()

        row = {
            "city": city2, "property_type": property_type, "facing": facing, "status": "Unknown",
            "location": location,
            "area": area, "security_deposit": security_deposit, "age of property": age_of_property,
            "locality_score": locality_score, "amenity_count": amenity_count,
            "new/resale": 1 if new_resale == "New" else 0,
            "price_negotiable": 1 if price_negotiable == "Yes" else 0,
            "furnished": 1 if furnished == "Yes" else 0,
        }
        for label in amenity_labels:
            row[label] = 1 if amenities[label] else 0
        for name, kw in {"desc_has_metro": "metro", "desc_has_luxury": "luxury", "desc_has_premium": "premium",
                          "desc_has_gated": "gated", "desc_has_corner_plot": "corner plot", "desc_has_spacious": "spacious"}.items():
            row[name] = 1 if kw in desc_lower else 0

        input_df = pd.DataFrame([row])
        point_pred = float(np.expm1(np.clip(pipe.predict(input_df), log_min, log_max))[0])
        p10 = float(np.expm1(np.clip(quantile_models[0.1].predict(input_df), log_min, log_max))[0])
        p90 = float(np.expm1(np.clip(quantile_models[0.9].predict(input_df), log_min, log_max))[0])

        st.success(f"### Estimated Price: Rs {point_pred:,.0f}")
        st.caption(f"Likely range: Rs {p10:,.0f} - Rs {p90:,.0f} (P10-P90)  |  ~Rs {point_pred/area:,.0f} per sq.ft.")

# ---------------------------------------------------------------------------
# TAB 3 - scheme success
# ---------------------------------------------------------------------------
with tab3:
    st.header("Will this scheme succeed?")
    st.caption("Enter a proposed scheme's details - only what you'd know before launch.")

    reg_model, reg_scaler, reg_cols, reg_targets, clf_model, clf_scaler, clf_cols = load_scheme_models()
    reg_num_cols = list(reg_scaler.feature_names_in_)

    locations = ["Delhi (Outer/Bawana)", "Gurugram (SPR/Sohna)", "Greater Noida",
                 "Kolkata (New Town/Rajarhat)", "Bengaluru (North)", "Bengaluru (East)",
                 "Chennai (OMR/Guduvanchery)", "Faridabad (Neharpar)",
                 "Hyderabad (Tellapur/Kollur)", "Pune (Hinjewadi/Wakad)",
                 "Pune (Wagholi/Kharadi)", "Ahmedabad (SG Highway)"]

    c1, c2 = st.columns(2)
    with c1:
        scheme_location = st.selectbox("Location", locations)
        plot_size = st.number_input("Plot Size (sqft)", 400, 4000, 1200, step=50, key="scheme_plot_size")
        price = st.number_input("Price (INR)", 500000, 20000000, 5000000, step=100000, key="scheme_price")
        emi = st.number_input("Monthly EMI (INR)", 3000, 200000, 35000, step=1000)

    with c2:
        distance = st.slider("Distance from Metro (km)", 0.0, 40.0, 10.0, step=0.5, key="scheme_distance")
        ad_budget = st.number_input("Advertising Budget (INR)", 100000, 5000000, 1000000, step=50000)
        park = st.radio("Park", ["Yes", "No"], horizontal=True, key="scheme_park")
        clubhouse = st.radio("Clubhouse", ["Yes", "No"], horizontal=True, key="scheme_clubhouse")

    if st.button("Predict Scheme Outcome", type="primary"):
        emi_to_price = emi / price if price else 0
        ad_per_sqft = ad_budget / plot_size if plot_size else 0

        row = {c: 0 for c in reg_cols}
        row["Plot_Size_SqFt"] = plot_size
        row["Price_INR"] = price
        row["Monthly_EMI_INR"] = emi
        row["Distance_from_Metro_km"] = distance
        row["Advertising_Budget_INR"] = ad_budget
        if "EMI_to_Price_Ratio" in row:
            row["EMI_to_Price_Ratio"] = emi_to_price
        if "AdBudget_per_Sqft" in row:
            row["AdBudget_per_Sqft"] = ad_per_sqft

        loc_key = f"Location_{scheme_location}"
        if loc_key in row:
            row[loc_key] = 1
        if park == "Yes" and "Park_Yes" in row:
            row["Park_Yes"] = 1
        if clubhouse == "Yes" and "Clubhouse_Yes" in row:
            row["Clubhouse_Yes"] = 1

        input_df = pd.DataFrame([[row[c] for c in reg_cols]], columns=reg_cols)
        input_df[reg_num_cols] = reg_scaler.transform(input_df[reg_num_cols])
        pred = reg_model.predict(input_df)[0]
        pred_dict = dict(zip(reg_targets, pred))

        clf_input_df = pd.DataFrame([[row[c] for c in clf_cols]], columns=clf_cols)
        clf_num_cols = list(clf_scaler.feature_names_in_)
        clf_input_df[clf_num_cols] = clf_scaler.transform(clf_input_df[clf_num_cols])
        demand_pred = clf_model.predict(clf_input_df)[0]

        badge = {"HIGH": st.success, "MEDIUM": st.warning, "LOW": st.error}.get(demand_pred, st.info)
        badge(f"Predicted Demand Level: {demand_pred}")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Expected Leads", f"{pred_dict['Expected_Leads']:.0f}")
        m2.metric("Expected Bookings", f"{pred_dict['Expected_Bookings']:.0f}")
        m3.metric("Est. Conversion", f"{pred_dict['Estimated_Conversion_Pct']:.1f}%")
        m4.metric("Success Score", f"{pred_dict['Scheme_Success_Score']:.0f}/100")

        st.caption("Estimated Conversion is the hardest of these to predict accurately - "
                   "treat it as a rough guide rather than a precise number.")