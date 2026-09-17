import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Property Price | Iron Hide",
    page_icon="💰",
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

        font-size: 21px;
        font-weight: 750;

        margin-top: 10px;
        margin-bottom: 4px;
    }

    .section-description {
        color: var(--text-muted);

        font-size: 13px;

        margin-bottom: 18px;
    }


    /* =====================================================
       WIDGET LABELS
    ===================================================== */

    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label {
        color: var(--text-secondary) !important;

        font-size: 13px !important;
        font-weight: 600 !important;
    }

    [data-testid="stWidgetLabel"] small {
        color: var(--text-muted) !important;
    }


    /* =====================================================
       NUMBER + TEXT INPUT
    ===================================================== */

    [data-testid="stNumberInput"] > div,
    [data-testid="stTextInput"] > div {

        background: var(--input-bg) !important;

        border: 1px solid var(--border-light) !important;

        border-radius: 10px !important;

        box-shadow: none !important;
    }

    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input {

        background: transparent !important;

        color: var(--text) !important;

        -webkit-text-fill-color: var(--text) !important;

        caret-color: var(--blue) !important;
    }

    [data-testid="stNumberInput"] > div:focus-within,
    [data-testid="stTextInput"] > div:focus-within {

        border-color: var(--blue) !important;

        box-shadow:
            0 0 0 1px var(--blue) !important;
    }


    /* =====================================================
       TEXT AREA
    ===================================================== */

    [data-testid="stTextArea"] textarea {

        background: var(--input-bg) !important;

        color: var(--text) !important;

        -webkit-text-fill-color: var(--text) !important;

        border: 1px solid var(--border-light) !important;

        border-radius: 10px !important;
    }

    [data-testid="stTextArea"] textarea:focus {

        border-color: var(--blue) !important;

        box-shadow:
            0 0 0 1px var(--blue) !important;
    }


    /* =====================================================
       NUMBER INPUT +/- BUTTONS
    ===================================================== */

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
       SELECTBOX
    ===================================================== */

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
    }


    /* =====================================================
       DROPDOWN MENU
    ===================================================== */

    [data-baseweb="popover"] {

        background: #F7F9FC !important;

        border: 1px solid var(--border) !important;
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

    [aria-selected="true"] {

        background: #DCE7F0 !important;

        color: var(--blue-dark) !important;
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

    [data-testid="stRadio"] input + div {

        background: #F7F9FC !important;

        border-color: var(--border-light) !important;
    }

    [data-testid="stRadio"] input:checked + div {

        background: var(--blue) !important;

        border-color: var(--blue) !important;
    }


    /* =====================================================
       CHECKBOXES
    ===================================================== */

    [data-testid="stCheckbox"] label {

        color: var(--text-secondary) !important;
    }

    [data-testid="stCheckbox"] label p {

        color: var(--text-secondary) !important;
    }

    [data-testid="stCheckbox"] input + div {

        background: #F7F9FC !important;

        border: 1px solid var(--border-light) !important;
    }

    [data-testid="stCheckbox"] input:checked + div {

        background: var(--blue) !important;

        border-color: var(--blue-dark) !important;
    }


    /* =====================================================
       SLIDER
    ===================================================== */

    [data-testid="stSlider"] [data-baseweb="slider"] {

        padding-top: 8px;
        padding-bottom: 8px;
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

    [data-testid="stSlider"] [role="slider"] {

        background: var(--blue) !important;

        border: 3px solid #EAF0F5 !important;

        box-shadow:
            0 0 0 1px var(--blue) !important;
    }

    [data-testid="stSlider"] [data-testid="stThumbValue"] {

        color: var(--blue-dark) !important;
    }


    /* =====================================================
       INPUT PANELS
    ===================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {

        background: rgba(247, 249, 252, 0.72) !important;

        border: 1px solid var(--border) !important;

        border-radius: 18px !important;
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
       RESULT CARD
    ===================================================== */

    .result-card {

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

        text-align: center;

        box-shadow:
            0 12px 30px var(--shadow);
    }

    .result-label {

        color: var(--text-muted);

        font-size: 12px;
        font-weight: 700;

        letter-spacing: 0.8px;

        margin-bottom: 8px;
    }

    .result-price {

        color: var(--blue-dark);

        font-size: 42px;
        font-weight: 800;

        line-height: 1.1;

        margin-bottom: 8px;
    }

    .result-range {

        color: var(--text-secondary);

        font-size: 15px;

        margin-bottom: 6px;
    }

    .result-sqft {

        color: var(--text-secondary);

        font-size: 14px;
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
        PROPERTY ANALYSIS
    </div>

    <div class="header-title">
        Property Price
        <span class="header-accent">Prediction</span>
    </div>

    <p class="header-description">
        Estimate the expected market price of a property using
        its location, characteristics, furnishing, amenities,
        and listing information.
    </p>

</div>
""")


# =========================================================
# LOAD NEW V2 MODEL
# =========================================================

@st.cache_resource
def load_price_models():

    pipe = joblib.load(
        "models/price_model_pipeline_v2.pkl"
    )

    log_min, log_max = joblib.load(
        "models/price_log_clip_range_v2.pkl"
    )

    quantile_models = joblib.load(
        "models/price_quantile_models_v2.pkl"
    )

    return (
        pipe,
        log_min,
        log_max,
        quantile_models
    )


pipe, log_min, log_max, quantile_models = load_price_models()


# =========================================================
# PROPERTY DETAILS
# =========================================================

st.html("""
<div class="section-title">
    Property Details
</div>

<div class="section-description">
    Enter the basic characteristics of the property.
</div>
""")


c1, c2 = st.columns(2, gap="large")


# =========================================================
# LEFT COLUMN
# =========================================================

with c1:

    with st.container(border=True):

        city2 = st.selectbox(
            "City",
            [
                "Chandigarh",
                "Ghaziabad",
                "Lucknow",
                "Pune"
            ],
            key="price_city"
        )

        property_type = st.selectbox(
            "Property Type",
            [
                "Builderfloor",
                "Plot",
                "Villa"
            ]
        )

        location = st.text_input(
            "Locality / Location",
            "Wagholi"
        )

        area = st.number_input(
            "Area (sq.ft.)",
            200,
            20000,
            1200,
            step=50
        )

        facing = st.selectbox(
            "Facing Direction",
            [
                "Unknown",
                "North",
                "Northeast",
                "East",
                "Southeast",
                "South",
                "Southwest",
                "West",
                "Northwest"
            ]
        )

        age_of_property = st.number_input(
            "Age of Property (years)",
            0,
            50,
            2
        )


# =========================================================
# RIGHT COLUMN
# =========================================================

with c2:

    with st.container(border=True):

        security_deposit = st.number_input(
            "Security Deposit (Rs)",
            0,
            5000000,
            0,
            step=5000
        )

        locality_score = st.slider(
            "Locality Score (1-10)",
            1.0,
            10.0,
            6.0,
            step=0.5
        )

        new_resale = st.radio(
            "New or Resale",
            ["New", "Resale"],
            horizontal=True
        )

        price_negotiable = st.radio(
            "Price Negotiable?",
            ["Yes", "No"],
            horizontal=True
        )

        furnished = st.radio(
            "Furnished?",
            ["Yes", "No"],
            horizontal=True
        )


# =========================================================
# AMENITIES
# =========================================================

st.html("""
<div style="margin-top:28px;">

    <div class="section-title">
        Amenities
    </div>

    <div class="section-description">
        Select the facilities available with the property.
    </div>

</div>
""")


with st.container(border=True):

    amenity_labels = [
        "Lift(s)",
        "Full Power Backup",
        "24 X 7 Security",
        "Children's play area",
        "Club House",
        "Gymnasium",
        "Swimming Pool",
        "Sports Facility",
        "Jogging Track",
        "Landscaped Gardens",
        "Car Parking"
    ]

    a_cols = st.columns(3)

    amenities = {}

    for i, label in enumerate(amenity_labels):

        with a_cols[i % 3]:

            amenities[label] = st.checkbox(
                label,
                key=f"price_amenity_{label}"
            )


# =========================================================
# LISTING DESCRIPTION
# =========================================================

st.html("""
<div style="margin-top:28px;">

    <div class="section-title">
        Listing Description
    </div>

    <div class="section-description">
        Optional — relevant keywords are automatically extracted by the model.
    </div>

</div>
""")


description = st.text_area(
    "Listing Description (optional)",
    "",
    help=(
        "Keywords such as metro, luxury, premium, gated, "
        "corner plot, and spacious are picked up automatically."
    )
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
        "💰  Predict Property Price",
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
    # AMENITY COUNT
    # -----------------------------------------------------

    amenity_count = sum(
        1
        for key, value in amenities.items()
        if value and key != "Car Parking"
    )


    # -----------------------------------------------------
    # DESCRIPTION KEYWORDS
    # -----------------------------------------------------

    desc_lower = description.lower()

    description_features = {
        "desc_has_metro":
            1 if "metro" in desc_lower else 0,

        "desc_has_luxury":
            1 if "luxury" in desc_lower else 0,

        "desc_has_premium":
            1 if "premium" in desc_lower else 0,

        "desc_has_gated":
            1 if "gated" in desc_lower else 0,

        "desc_has_corner_plot":
            1 if "corner plot" in desc_lower else 0,

        "desc_has_spacious":
            1 if "spacious" in desc_lower else 0
    }


    # -----------------------------------------------------
    # BUILD MODEL INPUT
    # -----------------------------------------------------

    row = {
        "city": city2,
        "property_type": property_type,
        "facing": facing,
        "status": "Unknown",

        "location": location,

        "area": area,

        "security_deposit": security_deposit,

        "age of property": age_of_property,

        "locality_score": locality_score,

        "amenity_count": amenity_count,

        "new/resale":
            1 if new_resale == "New" else 0,

        "price_negotiable":
            1 if price_negotiable == "Yes" else 0,

        "furnished":
            1 if furnished == "Yes" else 0
    }


    # -----------------------------------------------------
    # INDIVIDUAL AMENITIES
    # -----------------------------------------------------

    for label in amenity_labels:

        row[label] = (
            1
            if amenities[label]
            else 0
        )


    # -----------------------------------------------------
    # DESCRIPTION FEATURES
    # -----------------------------------------------------

    row.update(
        description_features
    )


    # -----------------------------------------------------
    # CREATE DATAFRAME
    # -----------------------------------------------------

    input_df = pd.DataFrame(
        [row]
    )


    # =====================================================
    # PREDICTION
    # =====================================================

    point_pred = float(
        np.expm1(
            np.clip(
                pipe.predict(input_df),
                log_min,
                log_max
            )
        )[0]
    )


    p10 = float(
        np.expm1(
            np.clip(
                quantile_models[0.1].predict(input_df),
                log_min,
                log_max
            )
        )[0]
    )


    p90 = float(
        np.expm1(
            np.clip(
                quantile_models[0.9].predict(input_df),
                log_min,
                log_max
            )
        )[0]
    )


    price_per_sqft = (
        point_pred / area
        if area > 0
        else 0
    )


    # =====================================================
    # RESULT
    # =====================================================

    st.html(
        f"""
        <div class="result-card">

            <div class="result-label">
                ESTIMATED PROPERTY PRICE
            </div>

            <div class="result-price">
                ₹ {point_pred:,.0f}
            </div>

            <div class="result-range">
                Likely range: ₹ {p10:,.0f}
                — ₹ {p90:,.0f}
            </div>

            <div class="result-sqft">
                Approximately ₹ {price_per_sqft:,.0f}
                per sq.ft.
            </div>

        </div>
        """
    )