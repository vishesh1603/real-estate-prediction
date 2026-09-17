import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Insights | Iron Hide",
    page_icon="📈",
    layout="wide"
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"


# =========================================================
# THEME
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

        padding: 42px 46px;

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

        font-size: 42px;
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

        max-width: 780px;

        margin: 15px 0 0 0;
    }


    /* =====================================================
       SECTION HEADINGS
    ===================================================== */

    .section-title {
        color: var(--text);

        font-size: 23px;
        font-weight: 750;

        margin-top: 30px;
        margin-bottom: 5px;
    }

    .section-description {
        color: var(--text-muted);

        font-size: 13px;

        margin-bottom: 18px;
    }


    /* =====================================================
       CARDS
    ===================================================== */

    .card {
        background:
            linear-gradient(
                145deg,
                #F7F9FC,
                #E8EEF4
            );

        border: 1px solid var(--border);

        border-radius: 18px;

        padding: 24px;

        box-shadow:
            0 8px 22px var(--shadow);
    }

    .card-title {
        color: var(--text);

        font-size: 19px;
        font-weight: 750;

        margin-bottom: 9px;
    }

    .card-text {
        color: var(--text-secondary);

        font-size: 13px;
        line-height: 1.7;

        margin: 0;
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

        border-radius: 16px;

        padding: 20px;

        text-align: center;

        min-height: 105px;

        box-shadow:
            0 7px 18px rgba(15, 23, 42, 0.06);
    }

    .metric-label {
        color: var(--text-muted);

        font-size: 10px;
        font-weight: 750;

        letter-spacing: 0.6px;
    }

    .metric-value {
        color: var(--blue-dark);

        font-size: 26px;
        font-weight: 800;

        margin-top: 7px;
    }


    /* =====================================================
       INSIGHT CARDS
    ===================================================== */

    .insight-card {
        background:
            linear-gradient(
                145deg,
                #F7F9FC,
                #E8EEF4
            );

        border: 1px solid var(--border);

        border-radius: 18px;

        padding: 24px;

        min-height: 175px;

        box-shadow:
            0 8px 22px var(--shadow);
    }

    .insight-number {
        color: var(--blue);

        font-size: 10px;
        font-weight: 800;

        letter-spacing: 0.9px;

        margin-bottom: 10px;
    }

    .insight-title {
        color: var(--text);

        font-size: 19px;
        font-weight: 750;

        margin-bottom: 8px;
    }

    .insight-text {
        color: var(--text-secondary);

        font-size: 13px;
        line-height: 1.7;

        margin: 0;
    }


    /* =====================================================
       TAKEAWAY
    ===================================================== */

    .takeaway {
        background: #E4EBF1;

        border: 1px solid var(--border);

        border-left: 3px solid var(--blue);

        border-radius: 10px;

        padding: 14px 17px;

        color: var(--text-secondary);

        font-size: 13px;

        line-height: 1.7;

        margin-top: 15px;
    }


    /* =====================================================
       NOTE
    ===================================================== */

    .note {
        background: #E7EDF3;

        border: 1px solid var(--border);

        border-radius: 10px;

        padding: 14px 17px;

        color: var(--text-muted);

        font-size: 12px;

        line-height: 1.65;
    }


    /* =====================================================
       MATPLOTLIB AREA
    ===================================================== */

    [data-testid="stImage"],
    [data-testid="stPyplot"] {
        background: transparent !important;
    }

</style>
""")


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="header-badge">
        DATA INSIGHTS
    </div>

    <div class="header-title">
        Iron Hide
        <span class="header-accent">Insights</span>
    </div>

    <p class="header-description">
        Key findings from the project's machine-learning models
        and real-estate data.
    </p>

</div>
""")


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.html("""
<div class="section-title">
    Model Performance
</div>

<div class="section-description">
    Reported evaluation results from the project's models.
</div>
""")


m1, m2, m3, m4 = st.columns(4, gap="medium")


with m1:
    st.html("""
    <div class="metric-card">

        <div class="metric-label">
            PURCHASE ACCURACY
        </div>

        <div class="metric-value">
            ~80%
        </div>

    </div>
    """)


with m2:
    st.html("""
    <div class="metric-card">

        <div class="metric-label">
            PURCHASE AUC
        </div>

        <div class="metric-value">
            0.85
        </div>

    </div>
    """)


with m3:
    st.html("""
    <div class="metric-card">

        <div class="metric-label">
            PRICE R²
        </div>

        <div class="metric-value">
            0.84
        </div>

    </div>
    """)


with m4:
    st.html("""
    <div class="metric-card">

        <div class="metric-label">
            SCHEME R²
        </div>

        <div class="metric-value">
            0.756
        </div>

    </div>
    """)


# =========================================================
# KEY INSIGHTS
# =========================================================

st.html("""
<div class="section-title">
    Key Insights
</div>

<div class="section-description">
    The most important findings identified during the project.
</div>
""")


i1, i2, i3 = st.columns(3, gap="large")


with i1:
    st.html("""
    <div class="insight-card">

        <div class="insight-number">
            01 • CUSTOMER
        </div>

        <div class="insight-title">
            Customer engagement matters
        </div>

        <p class="insight-text">
            Previous enquiry and site visit were identified
            as strong predictors of purchase intent.
        </p>

    </div>
    """)


with i2:
    st.html("""
    <div class="insight-card">

        <div class="insight-number">
            02 • PRICING
        </div>

        <div class="insight-title">
            Area and city drive pricing
        </div>

        <p class="insight-text">
            Property area and city were identified as the
            main drivers in the price prediction model.
        </p>

    </div>
    """)


with i3:
    st.html("""
    <div class="insight-card">

        <div class="insight-number">
            03 • SCHEME
        </div>

        <div class="insight-title">
            Access and marketing matter
        </div>

        <p class="insight-text">
            Distance from metro and advertising budget were
            identified as important predictors of scheme performance.
        </p>

    </div>
    """)


# =========================================================
# CUSTOMER PURCHASE INTENT
# =========================================================

st.html("""
<div class="section-title">
    Customer Purchase Intent
</div>

<div class="section-description">
    Documented customer-engagement factors from the project.
</div>
""")


customer_chart, customer_text = st.columns(
    [1.65, 1],
    gap="large"
)


with customer_chart:

    features = [
        "Previous Enquiry",
        "Site Visit"
    ]

    values = [1, 1]

    fig, ax = plt.subplots(
        figsize=(7, 3.8)
    )

    ax.barh(
        features,
        values,
        color="#527B9D",
        height=0.45
    )

    ax.set_xlim(0, 1.18)

    ax.set_xticks([])

    ax.set_title(
        "Documented Engagement Signals",
        fontsize=13
    )

    for i, value in enumerate(values):

        ax.text(
            value + 0.02,
            i,
            "Strong predictor",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


with customer_text:

    st.html("""
    <div class="card">

        <div class="card-title">
            Customer Finding
        </div>

        <p class="card-text">
            Previous enquiries and completed site visits
            provide useful behavioural information for
            purchase-intent prediction.
        </p>

        <div class="takeaway">
            <strong>Takeaway:</strong>
            Earlier customer engagement can provide
            valuable information to the model.
        </div>

    </div>
    """)


# =========================================================
# PROPERTY PRICE INSIGHTS
# =========================================================

st.html("""
<div class="section-title">
    Property Price Insights
</div>

<div class="section-description">
    Explore pricing patterns in the processed property listings.
</div>
""")


listings_path = DATA_DIR / "cleaned_listings.csv"


if listings_path.exists():

    try:

        df = pd.read_csv(
            listings_path
        )


        # -------------------------------------------------
        # FIND COLUMN
        # -------------------------------------------------

        def find_column(candidates):

            lower_map = {
                str(col).lower(): col
                for col in df.columns
            }

            for candidate in candidates:

                if candidate.lower() in lower_map:
                    return lower_map[
                        candidate.lower()
                    ]

            for col in df.columns:

                col_lower = str(col).lower()

                for candidate in candidates:

                    if candidate.lower() in col_lower:
                        return col

            return None


        price_col = find_column([
            "price",
            "price_inr",
            "Price_INR",
            "price_in"
        ])

        area_col = find_column([
            "area",
            "area_sqft",
            "Area",
            "Area_sqft",
            "Area_SqFt",
            "property_area"
        ])

        city_col = find_column([
            "city",
            "City",
            "location_city"
        ])


        p1, p2 = st.columns(
            2,
            gap="large"
        )


        # =================================================
        # MEDIAN PRICE BY CITY
        # =================================================

        with p1:

            if (
                price_col is not None
                and city_col is not None
            ):

                temp = df[
                    [city_col, price_col]
                ].copy()

                temp[price_col] = pd.to_numeric(
                    temp[price_col],
                    errors="coerce"
                )

                temp = temp.dropna()

                grouped = (
                    temp
                    .groupby(city_col)[price_col]
                    .median()
                    .sort_values(ascending=True)
                    .tail(8)
                )

                if not grouped.empty:

                    fig, ax = plt.subplots(
                        figsize=(7, 4)
                    )

                    ax.barh(
                        grouped.index.astype(str),
                        grouped.values,
                        color="#527B9D"
                    )

                    ax.set_title(
                        "Median Listing Price by City",
                        fontsize=13
                    )

                    ax.set_xlabel(
                        "Median Price"
                    )

                    ax.grid(
                        axis="x",
                        alpha=0.15
                    )

                    ax.spines["top"].set_visible(False)
                    ax.spines["right"].set_visible(False)

                    plt.tight_layout()

                    st.pyplot(
                        fig,
                        use_container_width=True
                    )

                    plt.close(fig)

                else:

                    st.info(
                        "Not enough valid city/price data."
                    )

            else:

                st.info(
                    "City or price column was not found "
                    "in cleaned_listings.csv."
                )


        # =================================================
        # AREA VS PRICE
        # =================================================

        with p2:

            if (
                price_col is not None
                and area_col is not None
            ):

                temp = df[
                    [area_col, price_col]
                ].copy()

                temp[area_col] = pd.to_numeric(
                    temp[area_col],
                    errors="coerce"
                )

                temp[price_col] = pd.to_numeric(
                    temp[price_col],
                    errors="coerce"
                )

                temp = temp.dropna()

                temp = temp[
                    (temp[area_col] > 0) &
                    (temp[price_col] > 0)
                ]

                temp = temp.head(2500)

                if not temp.empty:

                    fig, ax = plt.subplots(
                        figsize=(7, 4)
                    )

                    ax.scatter(
                        temp[area_col],
                        temp[price_col],
                        alpha=0.35,
                        color="#527B9D",
                        s=18
                    )

                    ax.set_title(
                        "Property Area vs Listing Price",
                        fontsize=13
                    )

                    ax.set_xlabel(
                        "Area"
                    )

                    ax.set_ylabel(
                        "Price"
                    )

                    ax.grid(
                        alpha=0.15
                    )

                    ax.spines["top"].set_visible(False)
                    ax.spines["right"].set_visible(False)

                    plt.tight_layout()

                    st.pyplot(
                        fig,
                        use_container_width=True
                    )

                    plt.close(fig)

                else:

                    st.info(
                        "Not enough valid area/price data."
                    )

            else:

                st.info(
                    "Area or price column was not found "
                    "in cleaned_listings.csv."
                )


    except Exception as e:

        st.info(
            "The processed listings dataset could not be read."
        )

else:

    st.html("""
    <div class="note">

        <strong>Dataset not available yet:</strong>
        Run the listing-cleaning notebook to generate
        <code>cleaned_listings.csv</code>. The pricing charts
        will appear automatically after that.

    </div>
    """)


# =========================================================
# SCHEME SUCCESS
# =========================================================

st.html("""
<div class="section-title">
    Residential Scheme Insights
</div>

<div class="section-description">
    Documented factors identified as important for scheme performance.
</div>
""")


scheme_chart, scheme_text = st.columns(
    [1.65, 1],
    gap="large"
)


with scheme_chart:

    features = [
        "Advertising Budget",
        "Distance from Metro"
    ]

    values = [1, 1]

    fig, ax = plt.subplots(
        figsize=(7, 3.8)
    )

    ax.barh(
        features,
        values,
        color="#527B9D",
        height=0.45
    )

    ax.set_xlim(
        0,
        1.18
    )

    ax.set_xticks([])

    ax.set_title(
        "Key Scheme Performance Drivers",
        fontsize=13
    )

    for i, value in enumerate(values):

        ax.text(
            value + 0.02,
            i,
            "Important predictor",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


with scheme_text:

    st.html("""
    <div class="card">

        <div class="card-title">
            Scheme Finding
        </div>

        <p class="card-text">
            Metro accessibility and advertising budget
            are important factors considered by the
            scheme-success model.
        </p>

        <div class="takeaway">
            <strong>Takeaway:</strong>
            Both physical accessibility and marketing
            investment should be considered when evaluating
            a proposed residential scheme.
        </div>

    </div>
    """)


# =========================================================
# PROJECT TAKEAWAYS
# =========================================================

st.html("""
<div class="section-title">
    Project Takeaways
</div>

<div class="section-description">
    Main conclusions from the complete machine-learning workflow.
</div>
""")


t1, t2, t3 = st.columns(
    3,
    gap="large"
)


with t1:

    st.html("""
    <div class="insight-card">

        <div class="insight-number">
            CUSTOMER
        </div>

        <div class="insight-title">
            Behaviour adds signal
        </div>

        <p class="insight-text">
            Previous interactions and site visits provide
            useful behavioural information for purchase-intent
            prediction.
        </p>

    </div>
    """)


with t2:

    st.html("""
    <div class="insight-card">

        <div class="insight-number">
            PROPERTY
        </div>

        <div class="insight-title">
            Pricing is multi-factor
        </div>

        <p class="insight-text">
            Property size and location both matter, so
            area alone does not fully describe price differences.
        </p>

    </div>
    """)


with t3:

    st.html("""
    <div class="insight-card">

        <div class="insight-number">
            SCHEME
        </div>

        <div class="insight-title">
            Location + promotion
        </div>

        <p class="insight-text">
            Accessibility and advertising investment are
            important considerations in scheme evaluation.
        </p>

    </div>
    """)


# =========================================================
# FINAL NOTE
# =========================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

st.html("""
<div class="note">

    <strong>Note:</strong>
    The customer and scheme driver visuals are qualitative
    summaries of documented project findings. The pricing
    charts are generated from the processed listings dataset
    available locally.

</div>
""")