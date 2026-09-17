import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Purchase Intent | Iron Hide",
    page_icon="👤",
    layout="wide"
)


# =========================================================
# GREY-BLUE + BLACK THEME
# =========================================================

st.html("""
<style>

    /* =====================================================
       GLOBAL
    ===================================================== */

    :root {
        --bg: #DFE8F2;

        --surface: #F7F9FC;
        --surface-2: #E8EEF4;
        --surface-hover: #D4DFEA;

        --border: #C3D0DC;
        --border-light: #AEBECC;

        --blue: #527B9D;
        --blue-light: #6D92AF;
        --blue-dark: #3F627E;

        --text: #151A20;
        --text-secondary: #4F5964;
        --text-muted: #687582;

        --input-bg: #F8FAFC;

        --shadow: rgba(15, 23, 42, 0.10);
    }


    /* =====================================================
       APP
    ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 0%,
                rgba(82, 123, 157, 0.10),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(82, 123, 157, 0.07),
                transparent 22%
            ),
            #DFE8F2;

        color: var(--text);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 38px;
        padding-bottom: 55px;
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    [data-testid="stSidebar"] {
        background: #D6E0EA;
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] * {
        color: var(--text-secondary);
    }


    /* =====================================================
       HEADER
    ===================================================== */

    .page-header {
        background:
            linear-gradient(
                145deg,
                #EAF0F5,
                #DDE6EE
            );

        border: 1px solid var(--border);
        border-radius: 22px;

        padding: 38px 42px;

        margin-bottom: 34px;

        box-shadow:
            0 12px 32px var(--shadow);
    }

    .header-badge {
        display: inline-block;

        padding: 7px 13px;

        border-radius: 999px;

        background: rgba(82, 123, 157, 0.10);

        border: 1px solid rgba(82, 123, 157, 0.24);

        color: var(--blue-dark);

        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.8px;

        margin-bottom: 16px;
    }

    .header-title {
        color: var(--text);

        font-size: 40px;
        font-weight: 800;

        line-height: 1.08;

        margin: 0;
    }

    .header-accent {
        color: var(--blue);
    }

    .header-description {
        color: var(--text-secondary);

        font-size: 15px;
        line-height: 1.7;

        max-width: 760px;

        margin: 15px 0 0 0;
    }


    /* =====================================================
       SECTION HEADERS
    ===================================================== */

    .section-title {
        color: var(--text);

        font-size: 22px;
        font-weight: 750;

        margin-top: 10px;
        margin-bottom: 5px;
    }

    .section-description {
        color: var(--text-muted);

        font-size: 13px;

        margin-bottom: 20px;
    }


    /* =====================================================
       PANELS
    ===================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(247, 249, 252, 0.78) !important;

        border: 1px solid var(--border) !important;

        border-radius: 18px !important;

        box-shadow:
            0 8px 22px rgba(15, 23, 42, 0.05);
    }


    /* =====================================================
       WIDGET LABELS
    ===================================================== */

    [data-testid="stWidgetLabel"] p {
        color: var(--text-secondary) !important;

        font-size: 13px !important;
        font-weight: 600 !important;
    }

    [data-testid="stWidgetLabel"] small {
        color: var(--text-muted) !important;
    }


    /* =====================================================
       SELECTBOX
    ===================================================== */

    [data-baseweb="select"] > div {

        background: var(--input-bg) !important;

        border: 1px solid var(--border-light) !important;

        border-radius: 10px !important;
    }

    [data-baseweb="select"] span {
        color: var(--text) !important;
    }

    [data-baseweb="select"] svg {
        fill: var(--blue-dark) !important;
    }

    [data-baseweb="popover"] {
        background: #F7F9FC !important;

        border: 1px solid var(--border) !important;
    }

    [role="listbox"] {
        background: #F7F9FC !important;
    }

    [role="option"] {
        color: var(--text-secondary) !important;

        background: #F7F9FC !important;
    }

    [role="option"]:hover {
        background: #E7EDF3 !important;

        color: var(--text) !important;
    }

    [aria-selected="true"] {
        background: #DCE7F0 !important;

        color: var(--blue-dark) !important;
    }


    /* =====================================================
       NUMBER INPUT
    ===================================================== */

    [data-testid="stNumberInput"] > div {

        background: var(--input-bg) !important;

        border: 1px solid var(--border-light) !important;

        border-radius: 10px !important;
    }

    [data-testid="stNumberInput"] input {

        background: transparent !important;

        color: var(--text) !important;

        -webkit-text-fill-color: var(--text) !important;

        caret-color: var(--blue) !important;
    }

    [data-testid="stNumberInput"] > div:focus-within {

        border-color: var(--blue) !important;

        box-shadow:
            0 0 0 1px var(--blue) !important;
    }

    [data-testid="stNumberInput"] button {

        background: #E4EAF0 !important;

        color: var(--blue-dark) !important;

        border-color: var(--border-light) !important;
    }

    [data-testid="stNumberInput"] button:hover {

        background: #D7E1E9 !important;

        color: #2F526C !important;
    }


    /* =====================================================
       RADIO
    ===================================================== */

    [data-testid="stRadio"] label {
        color: var(--text-secondary) !important;
    }

    [data-testid="stRadio"] label p {
        color: var(--text-secondary) !important;
    }


    /* =====================================================
       CHECKBOX
    ===================================================== */

    [data-testid="stCheckbox"] label {
        color: var(--text-secondary) !important;
    }

    [data-testid="stCheckbox"] label p {
        color: var(--text-secondary) !important;
    }


    /* =====================================================
       SLIDER
    ===================================================== */

    [data-testid="stSlider"] [role="slider"] {

        background: var(--blue) !important;

        border-color: var(--blue) !important;

        box-shadow:
            0 0 0 1px var(--blue) !important;
    }

    [data-testid="stSlider"] [data-baseweb="slider"] > div {

        background: #C4D0DB !important;
    }

    [data-testid="stSlider"]
    [data-baseweb="slider"]
    > div
    > div:first-child {

        background: var(--blue) !important;
    }

    [data-testid="stSlider"] [data-testid="stThumbValue"] {

        color: var(--blue-dark) !important;
    }


    /* =====================================================
       PREDICT BUTTON
    ===================================================== */

    .predict-button {
        margin-top: 8px;
    }

    .predict-button > div > button {

        width: 100% !important;

        min-height: 48px !important;

        background: var(--blue) !important;

        border: 1px solid var(--blue-dark) !important;

        border-radius: 11px !important;

        color: #FFFFFF !important;

        font-size: 15px !important;

        font-weight: 700 !important;

        box-shadow:
            0 7px 18px rgba(63, 98, 126, 0.22) !important;

        transition:
            background 0.2s ease,
            transform 0.2s ease !important;
    }

    .predict-button > div > button:hover {

        background: var(--blue-dark) !important;

        border-color: #34536B !important;

        transform: translateY(-2px);
    }


    /* =====================================================
       INTENT RESULT
    ===================================================== */

    .intent-result {

        background:
            linear-gradient(
                145deg,
                #E8EFF5,
                #DCE6EF
            );

        border: 1px solid var(--border-light);

        border-radius: 20px;

        padding: 30px;

        margin-top: 28px;
        margin-bottom: 20px;

        text-align: center;

        box-shadow:
            0 12px 30px var(--shadow);
    }

    .intent-label {

        color: var(--text-muted);

        font-size: 12px;
        font-weight: 700;

        letter-spacing: 0.8px;

        margin-bottom: 8px;
    }

    .intent-value {

        color: var(--blue-dark);

        font-size: 40px;
        font-weight: 800;

        line-height: 1.1;
    }


    /* =====================================================
       METRICS
    ===================================================== */

    .metric-card {

        background:
            linear-gradient(
                145deg,
                #F7F9FC,
                #E9EFF4
            );

        border: 1px solid var(--border);

        border-radius: 17px;

        padding: 22px;

        text-align: center;

        min-height: 110px;

        box-shadow:
            0 8px 20px rgba(15, 23, 42, 0.06);
    }

    .metric-label {

        color: var(--text-muted);

        font-size: 12px;
        font-weight: 700;

        letter-spacing: 0.5px;
    }

    .metric-value {

        color: var(--blue-dark);

        font-size: 25px;
        font-weight: 750;

        margin-top: 8px;
    }


    /* =====================================================
       MODEL NOTE
    ===================================================== */

    .model-note {

        background: #E5EBF1;

        border: 1px solid var(--border);

        border-left: 3px solid var(--blue);

        border-radius: 10px;

        padding: 14px 17px;

        margin-top: 22px;

        color: var(--text-secondary);

        font-size: 13px;

        line-height: 1.6;
    }


    /* =====================================================
       STREAMLIT ALERTS
    ===================================================== */

    [data-testid="stAlert"] {
        border-radius: 10px;
    }


    /* =====================================================
       DIVIDER
    ===================================================== */

    hr {
        border-color: var(--border) !important;
    }

</style>
""")


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="header-badge">
        CUSTOMER ANALYSIS
    </div>

    <div class="header-title">
        Customer Purchase
        <span class="header-accent">Intent</span>
    </div>

    <p class="header-description">
        Estimate how likely a customer is to purchase a property
        using demographic, financial, preference, and behavioural data.
    </p>

</div>
""")


# =========================================================
# LOAD MODELS
# =========================================================

@st.cache_resource
def load_purchase_intent_models():

    # NEW V2 REGRESSION MODEL
    reg_model = joblib.load(
        "models/purchase_multi_output_model_v2.pkl"
    )

    reg_scaler = joblib.load(
        "models/purchase_reg_scaler.pkl"
    )

    reg_cols = joblib.load(
        "models/purchase_reg_columns.pkl"
    )

    reg_targets = joblib.load(
        "models/purchase_reg_targets.pkl"
    )

    # CLASSIFIER REMAINS THE SAME
    clf_model = joblib.load(
        "models/purchase_intent_classifier.pkl"
    )

    clf_scaler = joblib.load(
        "models/purchase_intent_clf_scaler.pkl"
    )

    clf_cols = joblib.load(
        "models/purchase_intent_clf_columns.pkl"
    )

    return (
        reg_model,
        reg_scaler,
        reg_cols,
        reg_targets,
        clf_model,
        clf_scaler,
        clf_cols
    )


(
    reg_model,
    reg_scaler,
    reg_cols,
    reg_targets,
    clf_model,
    clf_scaler,
    clf_cols
) = load_purchase_intent_models()

num_cols_used = list(
    reg_scaler.feature_names_in_
)


# =========================================================
# CUSTOMER PROFILE + PROPERTY PREFERENCE
# SIDE BY SIDE
# =========================================================

left_col, right_col = st.columns(2, gap="large")


# =========================================================
# CUSTOMER PROFILE
# =========================================================

with left_col:

    st.html("""
    <div class="section-title">
        Customer Profile
    </div>

    <div class="section-description">
        Demographic and financial information.
    </div>
    """)

    with st.container(border=True):

        age = st.number_input(
            "Age",
            18,
            90,
            35
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        occupation = st.selectbox(
            "Occupation",
            [
                "IT & Software",
                "Business Owner",
                "Government & PSU",
                "Healthcare",
                "Education",
                "Real Estate & Construction",
                "Retail & Commerce",
                "Manufacturing & Engineering",
                "Retired",
                "Unknown"
            ]
        )

        city = st.selectbox(
            "City",
            [
                "Mumbai",
                "Delhi",
                "Bengaluru",
                "Hyderabad",
                "Pune",
                "Chennai",
                "Kolkata",
                "Noida",
                "Gurugram"
            ]
        )

        monthly_income = st.number_input(
            "Monthly Income (INR)",
            10000,
            1000000,
            80000,
            step=5000
        )

        family_size = st.slider(
            "Family Size",
            1,
            7,
            4
        )

        housing_status = st.selectbox(
            "Current Housing Status",
            [
                "Owned Flat/House",
                "Rented",
                "Living with Parents"
            ]
        )


# =========================================================
# PROPERTY PREFERENCE
# =========================================================

with right_col:

    st.html("""
    <div class="section-title">
        Property Preference
    </div>

    <div class="section-description">
        Customer's property requirements and purchase preferences.
    </div>
    """)

    with st.container(border=True):

        budget = st.number_input(
            "Plot Budget (INR)",
            500000,
            50000000,
            5000000,
            step=100000
        )

        plot_size = st.number_input(
            "Preferred Plot Size (sqft)",
            300,
            5000,
            1200,
            step=50
        )

        distance = st.slider(
            "Distance to City Center (km)",
            0,
            60,
            20
        )

        preferred_location = st.selectbox(
            "Preferred Location",
            [
                "City Centre",
                "Suburbs",
                "Within City Limits",
                "Periphery / Growth Corridor"
            ]
        )

        purpose = st.radio(
            "Purpose",
            ["Self-use", "Investment"],
            horizontal=True
        )

        loan_required = st.radio(
            "Loan Required",
            ["Yes", "No"],
            horizontal=True
        )

        timeline = st.selectbox(
            "Expected Purchase Timeline",
            [
                "0-6 months",
                "6-12 months",
                "1-3 years",
                ">3 years"
            ]
        )

        lead_source = st.selectbox(
            "Lead Source",
            [
                "Google & Social Media Ads",
                "Magicbricks / Real Estate Portal",
                "Channel Partner / Broker",
                "Print / Newspaper Ad",
                "Direct Walk-in / Exhibition"
            ]
        )


# =========================================================
# CUSTOMER BEHAVIOUR
# =========================================================

st.html("""
<div class="section-title">
    Customer Behaviour
</div>

<div class="section-description">
    Record the customer's previous interactions and engagement.
</div>
""")


with st.container(border=True):

    b1, b2, b3 = st.columns(3)

    with b1:

        previous_enquiry = st.checkbox(
            "Previous Enquiry"
        )

    with b2:

        site_visit = st.checkbox(
            "Site Visit Done"
        )

    with b3:

        negotiation = st.checkbox(
            "Negotiation Done"
        )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict_col, _ = st.columns([1.5, 3])

with predict_col:

    st.markdown(
        '<div class="predict-button">',
        unsafe_allow_html=True
    )

    predict_clicked = st.button(
        "🔮  Predict Purchase Intent",
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# PREDICTION LOGIC
# =========================================================

if predict_clicked:

    row = {
        c: 0
        for c in reg_cols
    }

    row["Age"] = age
    row["Monthly_Income"] = monthly_income
    row["Annual_Income"] = monthly_income * 12
    row["Family_Size"] = family_size
    row["Plot_Budget"] = budget
    row["Preferred_Plot_Size_SqFt"] = plot_size
    row["Distance_to_City_Center_km"] = distance


    # =====================================================
    # CATEGORICAL VARIABLES
    # =====================================================

    for key, val in [

        (f"Gender_{gender}", 1),

        (f"Occupation_{occupation}", 1),

        (f"City_{city}", 1),

        (f"Current_Housing_Status_{housing_status}", 1),

        (f"Preferred_Location_{preferred_location}", 1),

        (f"Purpose_{purpose}", 1),

        (
            f"Loan_Required_{loan_required}",
            1 if loan_required == "Yes" else 0
        ),

        (f"Expected_Purchase_Timeline_{timeline}", 1),

        (f"Lead_Source_{lead_source}", 1),

        (
            "Previous_Enquiry_Yes",
            1 if previous_enquiry else 0
        ),

        (
            "Site_Visit_Yes",
            1 if site_visit else 0
        ),

        (
            "Negotiation_Done_Yes",
            1 if negotiation else 0
        ),

    ]:

        if key in row:
            row[key] = val


    # =====================================================
    # REGRESSION
    # =====================================================

    reg_input_df = pd.DataFrame(
        [
            [
                row[c]
                for c in reg_cols
            ]
        ],
        columns=reg_cols
    )

    reg_input_df[num_cols_used] = (
        reg_scaler.transform(
            reg_input_df[num_cols_used]
        )
    )

    reg_pred = reg_model.predict(
        reg_input_df
    )[0]

    pred_dict = dict(
        zip(
            reg_targets,
            reg_pred
        )
    )


    # =====================================================
    # CLASSIFICATION
    # =====================================================

    clf_input_df = pd.DataFrame(
        [
            [
                row[c]
                for c in clf_cols
            ]
        ],
        columns=clf_cols
    )

    clf_num_cols = list(
        clf_scaler.feature_names_in_
    )

    clf_input_df[clf_num_cols] = (
        clf_scaler.transform(
            clf_input_df[clf_num_cols]
        )
    )

    intent_pred = clf_model.predict(
        clf_input_df
    )[0]


    # =====================================================
    # RESULTS
    # =====================================================

    st.divider()

    st.html("""
    <div class="section-title">
        Prediction Results
    </div>

    <div class="section-description">
        Model-generated estimates based on the information provided.
    </div>
    """)


    st.html(
        f"""
        <div class="intent-result">

            <div class="intent-label">
                PREDICTED PURCHASE INTENT
            </div>

            <div class="intent-value">
                {intent_pred}
            </div>

        </div>
        """
    )


    if intent_pred == "High":

        st.success(
            "High purchase intent — this customer appears "
            "more likely to purchase."
        )

    elif intent_pred == "Medium":

        st.warning(
            "Medium purchase intent — this customer may "
            "require further engagement."
        )

    else:

        st.error(
            "Low purchase intent — this customer appears "
            "less likely to purchase."
        )


    # =====================================================
    # METRICS
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2 = st.columns(2, gap="large")


    with m1:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    PURCHASE PROBABILITY
                </div>

                <div class="metric-value">
                    {pred_dict['Purchase_Probability']:.0%}
                </div>

            </div>
            """
        )


    with m2:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    EXPECTED PURCHASE VALUE
                </div>

                <div class="metric-value">
                    ₹ {max(
                        pred_dict['Purchase_Value'],
                        0
                    ):,.0f}
                </div>

            </div>
            """
        )


    # =====================================================
    # NOTE
    # =====================================================

    st.html("""
    <div class="model-note">

        Expected Purchase Value is the least reliable of
        these two outputs. Treat it as a rough guide rather
        than a precise figure.

    </div>
    """)