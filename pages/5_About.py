import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="About | Iron Hide",
    page_icon="ℹ️",
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
        max-width: 1050px;
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

        max-width: 760px;

        margin: 15px 0 0 0;
    }


    /* =====================================================
       SECTION HEADINGS
    ===================================================== */

    .section-heading {
        display: flex;
        align-items: center;
        gap: 13px;

        margin: 0;
    }

    .section-icon {
        width: 40px;
        height: 40px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 11px;

        background: #E7EEF4;

        border: 1px solid var(--border-light);

        color: var(--blue-dark);

        font-size: 15px;
        font-weight: 700;

        flex-shrink: 0;
    }

    .section-title {
        color: var(--text);

        font-size: 23px;
        font-weight: 750;

        margin: 0;
    }

    .section-description {
        color: var(--text-muted);

        font-size: 13px;

        margin-top: 3px;
    }


    /* =====================================================
       CONTENT CARDS
    ===================================================== */

    .about-card {
        background:
            linear-gradient(
                145deg,
                #F7F9FC,
                #EAF0F5
            );

        border: 1px solid var(--border);

        border-radius: 18px;

        padding: 28px 30px;

        margin-bottom: 22px;

        box-shadow:
            0 8px 22px var(--shadow);
    }

    .about-icon {
        width: 50px;
        height: 50px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 14px;

        background: rgba(82, 123, 157, 0.10);

        border: 1px solid rgba(82, 123, 157, 0.24);

        color: var(--blue-dark);

        font-size: 16px;
        font-weight: 700;

        margin-bottom: 17px;
    }

    .about-title {
        color: var(--text);

        font-size: 22px;
        font-weight: 750;

        margin-bottom: 10px;
    }

    .about-text {
        color: var(--text-secondary);

        font-size: 15px;
        line-height: 1.75;

        margin: 0;
    }


    /* =====================================================
       PREDICTION MODULES OUTER BOX
    ===================================================== */

    .modules-wrapper {
        background:
            linear-gradient(
                145deg,
                #F7F9FC,
                #E8EEF4
            );

        border: 1px solid var(--border);

        border-radius: 20px;

        padding: 28px;

        margin-top: 30px;
        margin-bottom: 22px;

        box-shadow:
            0 10px 26px var(--shadow);
    }


    /* =====================================================
       MODULE GRID
    ===================================================== */

    .module-grid {
        display: grid;

        grid-template-columns:
            repeat(3, 1fr);

        gap: 22px;

        margin-top: 22px;
    }


    /* =====================================================
       MODULE CARDS
    ===================================================== */

    .module-card {
        background:
            linear-gradient(
                145deg,
                #F7F9FC,
                #E7EDF3
            );

        border: 1px solid var(--border);

        border-radius: 16px;

        padding: 24px;

        min-height: 200px;

        box-shadow:
            0 6px 18px rgba(15, 23, 42, 0.07);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .module-card:hover {
        transform: translateY(-3px);

        border-color: var(--border-light);

        box-shadow:
            0 12px 26px rgba(15, 23, 42, 0.11);
    }

    .module-badge {
        width: 34px;
        height: 34px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 9px;

        background: rgba(82, 123, 157, 0.10);

        border: 1px solid rgba(82, 123, 157, 0.22);

        color: var(--blue-dark);

        font-size: 12px;
        font-weight: 800;

        margin-bottom: 15px;
    }

    .module-title {
        color: var(--text);

        font-size: 18px;
        font-weight: 700;

        margin-bottom: 8px;
    }

    .module-text {
        color: var(--text-secondary);

        font-size: 13px;
        line-height: 1.65;

        margin: 0;
    }


    /* =====================================================
       TECHNOLOGY TAGS
    ===================================================== */

    .tech {
        display: inline-block;

        background: #E2E9F0;

        border: 1px solid var(--border-light);

        color: var(--blue-dark);

        padding: 7px 11px;

        border-radius: 8px;

        font-size: 12px;
        font-weight: 600;

        margin: 4px 5px 4px 0;
    }


    /* =====================================================
       DISCLAIMER
    ===================================================== */

    .note {
        background: #E4EBF1;

        border: 1px solid var(--border);

        border-left: 3px solid var(--blue);

        border-radius: 10px;

        padding: 15px 18px;

        color: var(--text-secondary);

        font-size: 13px;

        line-height: 1.65;

        margin-top: 24px;
    }

</style>
""")


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="header-badge">
        ABOUT THE PROJECT
    </div>

    <div class="header-title">
        Iron Hide
        <span class="header-accent">AI</span>
    </div>

    <p class="header-description">
        A machine-learning based decision support platform
        designed to demonstrate how real-estate data can be
        used to support pricing, customer analysis, and
        residential scheme evaluation.
    </p>

</div>
""")


# =========================================================
# PROJECT OVERVIEW
# =========================================================

st.html("""
<div class="about-card">

    <div class="about-icon">
        AI
    </div>

    <div class="about-title">
        Project Overview
    </div>

    <p class="about-text">
        Iron Hide demonstrates how historical customer,
        lead, pricing, and scheme information can be used
        with machine learning to generate useful predictions
        for real-estate decision support.
    </p>

</div>
""")


# =========================================================
# PREDICTION MODULES
# =========================================================

st.html("""
<div class="modules-wrapper">

    <div class="section-heading">

        <div class="section-icon">
            ML
        </div>

        <div>
            <div class="section-title">
                Prediction Modules
            </div>

            <div class="section-description">
                Three machine-learning modules included in the platform
            </div>
        </div>

    </div>


    <div class="module-grid">


        <!-- MODULE 01 -->

        <div class="module-card">

            <div class="module-badge">
                01
            </div>

            <div class="module-title">
                Property Price
            </div>

            <p class="module-text">
                Estimates property price using characteristics
                such as area, location, furnishing, and amenities.
            </p>

        </div>


        <!-- MODULE 02 -->

        <div class="module-card">

            <div class="module-badge">
                02
            </div>

            <div class="module-title">
                Purchase Intent
            </div>

            <p class="module-text">
                Estimates customer purchase intent from
                demographic, financial, preference, and
                behavioural information.
            </p>

        </div>


        <!-- MODULE 03 -->

        <div class="module-card">

            <div class="module-badge">
                03
            </div>

            <div class="module-title">
                Scheme Success
            </div>

            <p class="module-text">
                Estimates demand, leads, bookings, conversion,
                and success score for a proposed residential scheme.
            </p>

        </div>


    </div>

</div>
""")


# =========================================================
# TECHNOLOGY
# =========================================================

st.html("""
<div class="about-card" style="margin-top: 30px;">

    <div class="about-icon">
        PY
    </div>

    <div class="about-title">
        Technology Stack
    </div>

    <p class="about-text">
        Built using:
    </p>

    <div style="margin-top: 12px;">

        <span class="tech">Python</span>
        <span class="tech">Pandas</span>
        <span class="tech">NumPy</span>
        <span class="tech">Scikit-learn</span>
        <span class="tech">Joblib</span>
        <span class="tech">Streamlit</span>

    </div>

</div>
""")


# =========================================================
# PROJECT PURPOSE
# =========================================================

st.html("""
<div class="about-card">

    <div class="about-icon">
        ✓
    </div>

    <div class="about-title">
        Project Purpose
    </div>

    <p class="about-text">
        The project connects a real business problem with
        the complete machine-learning workflow — from data
        preparation and analysis to model building,
        evaluation, prediction, and deployment through
        a Streamlit dashboard.
    </p>

</div>
""")


# =========================================================
# DISCLAIMER
# =========================================================

st.html("""
<div class="note">

    <strong>Important:</strong>
    The predictions generated by this application are estimates
    from trained machine-learning models and are intended for
    academic demonstration and decision-support purposes.
    They should not be treated as guaranteed real-world outcomes.

</div>
""")