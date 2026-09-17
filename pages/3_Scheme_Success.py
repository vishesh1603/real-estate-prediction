import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Scheme Success | Iron Hide",
    page_icon="📊",
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
       PAGE HEADER
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
       INPUT PANELS
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

    [data-testid="stSelectbox"] [data-baseweb="select"] {
        background: var(--input-bg) !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: var(--input-bg) !important;

        border: 1px solid var(--border-light) !important;

        border-radius: 10px !important;

        min-height: 42px !important;

        box-shadow: none !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div:hover {
        border-color: var(--blue) !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] span {
        color: var(--text) !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] svg {
        fill: var(--blue-dark) !important;
        color: var(--blue-dark) !important;
    }


    /* =====================================================
       SELECTBOX POPUP
    ===================================================== */

    [data-baseweb="popover"] {
        background: #F7F9FC !important;

        border: 1px solid var(--border) !important;
    }

    [data-baseweb="menu"] {
        background: #F7F9FC !important;
    }

    [role="listbox"] {
        background: #F7F9FC !important;
    }

    [role="option"] {
        background: #F7F9FC !important;

        color: var(--text-secondary) !important;
    }

    [role="option"]:hover {
        background: #E7EDF3 !important;

        color: var(--text) !important;
    }

    [role="option"][aria-selected="true"] {
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
       RADIO BUTTONS
    ===================================================== */

    [data-testid="stRadio"] label {
        color: var(--text-secondary) !important;
    }

    [data-testid="stRadio"] label p {
        color: var(--text-secondary) !important;
    }

    [data-testid="stRadio"] [role="radiogroup"] {
        gap: 14px !important;
    }

    [data-testid="stRadio"] [role="radio"] {
        background: #F7F9FC !important;

        border-color: var(--border-light) !important;
    }

    [data-testid="stRadio"] [role="radio"][aria-checked="true"] {
        background: var(--blue) !important;

        border-color: var(--blue-dark) !important;
    }

    [data-testid="stRadio"] [role="radio"]::after {
        background: #FFFFFF !important;
    }


    /* =====================================================
       SLIDER
    ===================================================== */

    [data-testid="stSlider"] {
        padding-top: 5px !important;
    }

    [data-testid="stSlider"] [data-baseweb="slider"] {
        background: transparent !important;
    }

    [data-testid="stSlider"] [data-baseweb="slider"] > div {
        background: #C4D0DB !important;
    }

    [data-testid="stSlider"] [role="slider"] {
        background: var(--blue) !important;

        border: 3px solid #F7F9FC !important;

        box-shadow:
            0 0 0 1px var(--blue) !important;
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
       DEMAND RESULT
    ===================================================== */

    .demand-result {
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

    .demand-label {
        color: var(--text-muted);

        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.8px;

        margin-bottom: 8px;
    }

    .demand-value {
        color: var(--blue-dark);

        font-size: 40px;
        font-weight: 800;

        line-height: 1.1;
    }


    /* =====================================================
       METRIC CARDS
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

        min-height: 115px;

        box-shadow:
            0 8px 20px rgba(15, 23, 42, 0.06);
    }

    .metric-label {
        color: var(--text-muted);

        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.6px;
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
# PAGE HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="header-badge">
        SCHEME ANALYSIS
    </div>

    <div class="header-title">
        Residential Scheme
        <span class="header-accent">Success</span>
    </div>

    <p class="header-description">
        Evaluate the potential performance of a proposed residential
        scheme using pricing, location, accessibility, amenities,
        and advertising investment.
    </p>

</div>
""")


# =========================================================
# LOAD MODELS
# =========================================================

@st.cache_resource
def load_scheme_models():

    reg_model = joblib.load(
        "models/scheme_multi_output_model.pkl"
    )

    reg_scaler = joblib.load(
        "models/scheme_reg_scaler.pkl"
    )

    reg_cols = joblib.load(
        "models/scheme_reg_columns.pkl"
    )

    reg_targets = joblib.load(
        "models/scheme_reg_targets.pkl"
    )

    clf_model = joblib.load(
        "models/scheme_demand_classifier.pkl"
    )

    clf_scaler = joblib.load(
        "models/scheme_demand_scaler.pkl"
    )

    clf_cols = joblib.load(
        "models/scheme_demand_columns.pkl"
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
) = load_scheme_models()

reg_num_cols = list(
    reg_scaler.feature_names_in_
)


# =========================================================
# SCHEME DETAILS
# =========================================================

st.html("""
<div class="section-title">
    Scheme Details
</div>

<div class="section-description">
    Enter the information available before the scheme launch.
</div>
""")


locations = [
    "Delhi (Outer/Bawana)",
    "Gurugram (SPR/Sohna)",
    "Greater Noida",
    "Kolkata (New Town/Rajarhat)",
    "Bengaluru (North)",
    "Bengaluru (East)",
    "Chennai (OMR/Guduvanchery)",
    "Faridabad (Neharpar)",
    "Hyderabad (Tellapur/Kollur)",
    "Pune (Hinjewadi/Wakad)",
    "Pune (Wagholi/Kharadi)",
    "Ahmedabad (SG Highway)"
]


# =========================================================
# INPUTS
# =========================================================

c1, c2 = st.columns(2, gap="large")


# =========================================================
# LEFT COLUMN
# =========================================================

with c1:

    with st.container(border=True):

        scheme_location = st.selectbox(
            "Location",
            locations
        )

        plot_size = st.number_input(
            "Plot Size (sqft)",
            400,
            4000,
            1200,
            step=50,
            key="scheme_plot_size"
        )

        price = st.number_input(
            "Price (INR)",
            500000,
            20000000,
            5000000,
            step=100000,
            key="scheme_price"
        )

        emi = st.number_input(
            "Monthly EMI (INR)",
            3000,
            200000,
            35000,
            step=1000
        )


# =========================================================
# RIGHT COLUMN
# =========================================================

with c2:

    with st.container(border=True):

        distance = st.slider(
            "Distance from Metro (km)",
            0.0,
            40.0,
            10.0,
            step=0.5,
            key="scheme_distance"
        )

        ad_budget = st.number_input(
            "Advertising Budget (INR)",
            100000,
            5000000,
            1000000,
            step=50000
        )

        park = st.radio(
            "Park",
            ["Yes", "No"],
            horizontal=True,
            key="scheme_park"
        )

        clubhouse = st.radio(
            "Clubhouse",
            ["Yes", "No"],
            horizontal=True,
            key="scheme_clubhouse"
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
        "📊  Predict Scheme Outcome",
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

    # -----------------------------------------------------
    # NEW ENGINEERED FEATURES FROM UPDATED ML CODE
    # -----------------------------------------------------

    emi_to_price = (
        emi / price
        if price
        else 0
    )

    ad_per_sqft = (
        ad_budget / plot_size
        if plot_size
        else 0
    )


    # -----------------------------------------------------
    # BUILD MODEL INPUT
    # -----------------------------------------------------

    row = {
        c: 0
        for c in reg_cols
    }

    row["Plot_Size_SqFt"] = plot_size
    row["Price_INR"] = price
    row["Monthly_EMI_INR"] = emi
    row["Distance_from_Metro_km"] = distance
    row["Advertising_Budget_INR"] = ad_budget


    # -----------------------------------------------------
    # NEW ENGINEERED FEATURES
    # -----------------------------------------------------

    if "EMI_to_Price_Ratio" in row:
        row["EMI_to_Price_Ratio"] = emi_to_price

    if "AdBudget_per_Sqft" in row:
        row["AdBudget_per_Sqft"] = ad_per_sqft


    # -----------------------------------------------------
    # LOCATION
    # -----------------------------------------------------

    loc_key = f"Location_{scheme_location}"

    if loc_key in row:
        row[loc_key] = 1


    # -----------------------------------------------------
    # AMENITIES
    # -----------------------------------------------------

    if park == "Yes" and "Park_Yes" in row:
        row["Park_Yes"] = 1

    if clubhouse == "Yes" and "Clubhouse_Yes" in row:
        row["Clubhouse_Yes"] = 1


    # =====================================================
    # REGRESSION
    # =====================================================

    input_df = pd.DataFrame(
        [
            [
                row[c]
                for c in reg_cols
            ]
        ],
        columns=reg_cols
    )

    input_df[reg_num_cols] = (
        reg_scaler.transform(
            input_df[reg_num_cols]
        )
    )

    pred = reg_model.predict(
        input_df
    )[0]

    pred_dict = dict(
        zip(
            reg_targets,
            pred
        )
    )


    # =====================================================
    # DEMAND CLASSIFICATION
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

    demand_pred = clf_model.predict(
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
        Model-generated estimates based on the proposed scheme.
    </div>
    """)


    st.html(
        f"""
        <div class="demand-result">

            <div class="demand-label">
                PREDICTED DEMAND LEVEL
            </div>

            <div class="demand-value">
                {demand_pred}
            </div>

        </div>
        """
    )


    # Updated ML app uses uppercase labels:
    # HIGH / MEDIUM / LOW

    demand_upper = str(
        demand_pred
    ).upper()

    if demand_upper == "HIGH":

        st.success(
            "High demand — the proposed scheme shows strong "
            "predicted demand."
        )

    elif demand_upper == "MEDIUM":

        st.warning(
            "Medium demand — the scheme may require stronger "
            "positioning or marketing."
        )

    else:

        st.error(
            "Low demand — the scheme has relatively weaker "
            "predicted demand."
        )


    # =====================================================
    # METRICS
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4, gap="medium")


    with m1:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    EXPECTED LEADS
                </div>

                <div class="metric-value">
                    {pred_dict['Expected_Leads']:.0f}
                </div>

            </div>
            """
        )


    with m2:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    EXPECTED BOOKINGS
                </div>

                <div class="metric-value">
                    {pred_dict['Expected_Bookings']:.0f}
                </div>

            </div>
            """
        )


    with m3:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    EST. CONVERSION
                </div>

                <div class="metric-value">
                    {pred_dict['Estimated_Conversion_Pct']:.1f}%
                </div>

            </div>
            """
        )


    with m4:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    SUCCESS SCORE
                </div>

                <div class="metric-value">
                    {pred_dict['Scheme_Success_Score']:.0f}/100
                </div>

            </div>
            """
        )


    # =====================================================
    # MODEL NOTE
    # =====================================================

    st.html("""
    <div class="model-note">

        Estimated Conversion is the hardest of these metrics
        to predict accurately. Treat it as a rough guide
        rather than a precise number.

    </div>
    """)