import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Iron Hide",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
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
        --bg: #D6E0EA;
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
            #D6E0EA;

        color: var(--text);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 42px;
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
       HERO
    ===================================================== */

    .hero {
        position: relative;
        overflow: hidden;

        background:
            linear-gradient(
                145deg,
                #EAF0F5 0%,
                #E2EAF1 58%,
                #D7E1EA 100%
            );

        border: 1px solid var(--border);
        border-radius: 24px;

        padding: 50px 54px;

        margin-bottom: 44px;

        box-shadow:
            0 18px 45px var(--shadow);
    }

    .hero::after {
        content: "";
        position: absolute;

        width: 220px;
        height: 220px;

        right: -70px;
        top: -70px;

        border-radius: 50%;

        background: rgba(82, 123, 157, 0.09);
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;

        background: rgba(82, 123, 157, 0.10);

        border: 1px solid rgba(82, 123, 157, 0.28);

        color: var(--blue-dark);

        padding: 8px 14px;

        border-radius: 999px;

        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.8px;

        margin-bottom: 22px;
    }

    .hero-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--blue);
    }

    .hero-title {
        color: var(--text);

        font-size: 56px;
        font-weight: 800;

        letter-spacing: -1.6px;
        line-height: 1.02;

        margin: 0;
    }

    .hero-accent {
        color: var(--blue);
    }

    .hero-description {
        color: var(--text-secondary);

        font-size: 17px;
        line-height: 1.75;

        max-width: 740px;

        margin-top: 20px;
        margin-bottom: 0;
    }


    /* =====================================================
       SECTION HEADER
    ===================================================== */

    .section-title {
        color: var(--text);

        font-size: 28px;
        font-weight: 750;

        letter-spacing: -0.4px;

        margin-bottom: 5px;
    }

    .section-description {
        color: var(--text-muted);

        font-size: 14px;

        margin-bottom: 26px;
    }


    /* =====================================================
       CARDS
    ===================================================== */

    .card {
        min-height: 325px;

        padding: 32px;

        box-sizing: border-box;

        background:
            linear-gradient(
                160deg,
                #F7F9FC,
                #EAF0F5
            );

        border: 1px solid var(--border);

        border-radius: 22px;

        box-shadow:
            0 12px 30px var(--shadow);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .card:hover {
        transform: translateY(-4px);

        border-color: var(--border-light);

        box-shadow:
            0 18px 38px rgba(15, 23, 42, 0.15);
    }

    .card-icon {
        width: 68px;
        height: 68px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 18px;

        background: rgba(82, 123, 157, 0.11);

        border: 1px solid rgba(82, 123, 157, 0.24);

        color: var(--blue-dark);

        font-size: 32px;

        margin-bottom: 28px;

        box-shadow:
            inset 0 0 20px rgba(82, 123, 157, 0.04);
    }

    .card-title {
        color: var(--text);

        font-size: 25px;
        font-weight: 750;

        letter-spacing: -0.3px;

        margin-bottom: 13px;
    }

    .card-text {
        color: var(--text-secondary);

        font-size: 15px;

        line-height: 1.75;

        max-width: 320px;

        margin: 0;
    }

    .card-category {
        color: var(--blue-dark);

        font-size: 11px;
        font-weight: 700;

        letter-spacing: 0.9px;

        margin-top: 26px;
    }


    /* =====================================================
       NAVIGATION BUTTONS
    ===================================================== */

    .nav-button {
        margin-top: 14px;
    }

    .nav-button > div > button {
        width: 100% !important;

        min-height: 44px !important;

        background: #E7EDF3 !important;

        border: 1px solid var(--border-light) !important;

        border-radius: 11px !important;

        color: var(--blue-dark) !important;

        font-weight: 650 !important;

        transition:
            background 0.2s ease,
            border-color 0.2s ease,
            transform 0.2s ease !important;
    }

    .nav-button > div > button:hover {
        background: #D9E3EC !important;

        border-color: var(--blue) !important;

        color: #263B4D !important;

        transform: translateY(-1px);
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer {
        margin-top: 58px;

        padding-top: 22px;

        border-top: 1px solid var(--border);

        text-align: center;

        color: var(--text-muted);

        font-size: 12px;

        line-height: 1.8;
    }

    .footer-brand {
        color: var(--text);
        font-weight: 650;
    }

</style>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-badge">
        <span class="hero-dot"></span>
        IRON HIDE ANALYTICS
    </div>

    <div class="hero-title">
        Iron Hide
        <br>
        <span class="hero-accent">
            Intelligence.
        </span>
    </div>

    <p class="hero-description">
        A machine-learning based decision support platform
        for property pricing, customer purchase intent,
        and residential scheme analysis.
    </p>

</div>
""")


# =========================================================
# SECTION HEADER
# =========================================================

st.html("""
<div class="section-title">
    Prediction Tools
</div>

<div class="section-description">
    Select a module to begin your analysis.
</div>
""")


# =========================================================
# CARDS
# =========================================================

col1, col2, col3 = st.columns(3, gap="large")


# =========================================================
# PROPERTY PRICE
# =========================================================

with col1:

    st.html("""
    <div class="card">

        <div class="card-icon">
            ₹
        </div>

        <div class="card-title">
            Property Price
        </div>

        <p class="card-text">
            Estimate the expected price of a property using
            location, area, property characteristics,
            furnishing, and amenities.
        </p>

        <div class="card-category">
            PRICE ANALYSIS
        </div>

    </div>
    """)

    st.markdown(
        '<div class="nav-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "Open Price Prediction  →",
        key="price_button",
        use_container_width=True
    ):
        st.switch_page("pages/1_Price_Prediction.py")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# PURCHASE INTENT
# =========================================================

with col2:

    st.html("""
    <div class="card">

        <div class="card-icon">
            ◉
        </div>

        <div class="card-title">
            Purchase Intent
        </div>

        <p class="card-text">
            Estimate customer purchase intent using
            demographic, financial, preference,
            and behavioural information.
        </p>

        <div class="card-category">
            CUSTOMER ANALYSIS
        </div>

    </div>
    """)

    st.markdown(
        '<div class="nav-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "Open Purchase Intent  →",
        key="purchase_button",
        use_container_width=True
    ):
        st.switch_page("pages/2_Purchase_Intent.py")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# SCHEME SUCCESS
# =========================================================

with col3:

    st.html("""
    <div class="card">

        <div class="card-icon">
            📊
        </div>

        <div class="card-title">
            Scheme Success
        </div>

        <p class="card-text">
            Analyze a proposed residential scheme using
            location, pricing, accessibility, amenities,
            and advertising investment.
        </p>

        <div class="card-category">
            SCHEME ANALYSIS
        </div>

    </div>
    """)

    st.markdown(
        '<div class="nav-button">',
        unsafe_allow_html=True
    )

    if st.button(
        "Open Scheme Success  →",
        key="scheme_button",
        use_container_width=True
    ):
        st.switch_page("pages/3_Scheme_Success.py")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    <span class="footer-brand">
        Iron Hide AI
    </span>

    <br>

    Machine Learning Decision Support Platform

    <br>

    Predictions are estimates and intended for
    decision-support purposes.

</div>
""")