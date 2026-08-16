import streamlit as st
import joblib


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="wide"
)


# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("model/student_score_model.pkl")


# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

/* ---------- BACKGROUND ---------- */

.stApp {
    background: #f4f8ff;
}

.block-container {
    max-width: 1350px;
    padding-top: 10px;
    padding-bottom: 8px;
}


/* ---------- REMOVE EXTRA TOP SPACE ---------- */

header[data-testid="stHeader"] {
    background: transparent;
}


/* ---------- TITLE ---------- */

.main-title {
    background: linear-gradient(135deg, #eef5ff, #dbe9ff);
    border: 1px solid #d3e2f8;
    border-radius: 16px;
    padding: 14px 28px;
    box-shadow: 0 5px 18px rgba(50, 90, 170, 0.08);
    margin-bottom: 8px;
    position: relative;
    overflow: hidden;
}

.title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.title-left {
    display: flex;
    align-items: center;
}

.title-icon {
    width: 54px;
    height: 54px;
    background: #c9dcff;
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    margin-right: 16px;
}

.title-text {
    color: #102a5c;
    font-size: 26px;
    font-weight: 800;
    line-height: 1.1;
}

.subtitle {
    color: #2860c7;
    font-size: 13px;
    margin-top: 3px;
}

/* ---------- HEADER DECORATION (right side) ---------- */

.title-decor {
    display: flex;
    align-items: center;
    gap: 14px;
}

.dot-grid {
    display: grid;
    grid-template-columns: repeat(4, 6px);
    grid-gap: 4px;
    opacity: 0.35;
}

.dot-grid span {
    width: 6px;
    height: 6px;
    border-radius: 2px;
    background: #7fa4e8;
    display: block;
}

.chart-card {
    background: white;
    border-radius: 12px;
    padding: 8px 12px;
    box-shadow: 0 8px 20px rgba(50, 90, 170, 0.18);
    font-size: 20px;
}

.pie-icon {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: conic-gradient(#2059dc 0deg 260deg, #dbe9ff 260deg 360deg);
    box-shadow: 0 4px 10px rgba(50, 90, 170, 0.2);
}


/* ---------- SECTION TITLE ---------- */

.section {
    background: white;
    border: 1px solid #d6e3f7;
    border-radius: 14px;
    padding: 10px 20px;
    margin-bottom: 8px;
    box-shadow: 0 3px 10px rgba(50, 90, 170, 0.05);
}

.section-title {
    color: #2059dc;
    font-size: 18px;
    font-weight: 800;
}

.section-text {
    color: #526d97;
    font-size: 12px;
    margin-top: 2px;
}


/* ---------- INPUT CARD ---------- */

.card {
    background: white;
    border: 1px solid #d5e2f5;
    border-radius: 14px;
    padding: 10px 14px;
    min-height: 90px;
    box-shadow: 0 3px 10px rgba(50, 90, 170, 0.05);
}

.card-icon {
    background: #edf4ff;
    border: 1px solid #d8e5fa;
    border-radius: 10px;
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

.card-title {
    color: #142e60;
    font-size: 14px;
    font-weight: 750;
    margin-top: 6px;
}

.card-description {
    color: #55709b;
    font-size: 11px;
    margin-top: 1px;
}


/* ---------- GLOBAL THEME OVERRIDE (kills default red/dark accents) ---------- */

:root {
    --primary-color: #2059dc !important;
}


/* ---------- NUMBER INPUT ---------- */

div[data-testid="stNumberInput"] {
    margin-top: 4px;
}

div[data-testid="stNumberInput"] > div,
div[data-testid="stNumberInput"] div[data-baseweb="input"],
div[data-testid="stNumberInput"] div[data-baseweb="input"] > div {
    border: 1px solid #cbdcf6 !important;
    border-radius: 8px !important;
    background: white !important;
    box-shadow: none !important;
}

div[data-testid="stNumberInput"] input {
    background: white !important;
    color: #173566 !important;
    font-size: 14px !important;
    font-weight: 650 !important;
    padding-top: 6px !important;
    padding-bottom: 6px !important;
    -webkit-text-fill-color: #173566 !important;
}

div[data-testid="stNumberInputStepDown"],
div[data-testid="stNumberInputStepUp"] {
    background: white !important;
}

div[data-testid="stNumberInputStepDown"] svg,
div[data-testid="stNumberInputStepUp"] svg {
    fill: #2059dc !important;
    color: #2059dc !important;
}


/* ---------- SLIDER ---------- */

div[data-testid="stSlider"] {
    margin-top: -12px;
}

div[data-testid="stSlider"] label {
    display: none;
}

/* track (unfilled) */
div[data-testid="stSlider"] div[data-baseweb="slider"] > div:first-child {
    background: #dbe6fb !important;
}

/* filled range */
div[data-testid="stSlider"] div[data-baseweb="slider"] div[data-testid="stSliderTrackHighlight"],
div[data-testid="stSlider"] div[data-baseweb="slider"] > div > div {
    background: #3474ee !important;
}

/* thumb (draggable dot) */
div[data-testid="stSlider"] div[role="slider"] {
    background-color: #2059dc !important;
    border-color: #2059dc !important;
    box-shadow: 0 0 0 4px rgba(32, 89, 220, 0.15) !important;
}

/* floating value bubble above thumb */
div[data-testid="stSlider"] div[data-testid="stThumbValue"] {
    color: #2059dc !important;
    font-weight: 700 !important;
}

/* min/max range labels below slider */
div[data-testid="stSlider"] div[data-testid="stTickBar"] {
    color: #7a94bd !important;
}


/* ---------- BUTTON ---------- */

div.stButton > button {
    height: 38px !important;
    border-radius: 9px !important;
    border: none !important;
    background: linear-gradient(135deg, #3474ee, #1e50d2) !important;
    color: white !important;
    font-size: 15px !important;
    font-weight: 750 !important;
    box-shadow: 0 5px 13px rgba(35, 90, 215, 0.25);
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #2866e5, #1949c7) !important;
}


/* ---------- RESULT ---------- */

.result-box {
    background: white;
    border: 1px solid #d5e2f5;
    border-radius: 14px;
    padding: 10px 14px;
    margin-top: 6px;
    box-shadow: 0 3px 10px rgba(50, 90, 170, 0.05);
}

.result-title {
    color: #2059dc;
    font-size: 16px;
    font-weight: 800;
}

.result-description {
    color: #526d97;
    font-size: 11px;
    margin-top: 3px;
}

.score-box {
    background: linear-gradient(135deg, #edf4ff, #dce9ff);
    border: 1px solid #cbdcff;
    border-radius: 12px;
    text-align: center;
    padding: 6px;
    margin-top: 4px;
}

.score-label {
    color: #2860c7;
    font-size: 13px;
    font-weight: 700;
}

.score {
    color: #2059dc;
    font-size: 30px;
    font-weight: 850;
    line-height: 1.05;
}


/* ---------- NOTE ---------- */

.note {
    background: #edf4ff;
    border: 1px solid #d5e2f5;
    border-radius: 10px;
    padding: 6px 12px;
    margin-top: 6px;
    color: #526d97;
    font-size: 11px;
}

.note strong {
    color: #2059dc;
}


/* ---------- STREAMLIT GAP ---------- */

div[data-testid="stVerticalBlock"] {
    gap: 0.2rem;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    gap: 0.2rem;
}

.stApp [data-testid="stAppViewBlockContainer"] {
    padding-top: 0.6rem;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE DEFAULTS (needed to sync number_input <-> slider)
# =====================================================
# IMPORTANT: once a widget's `key` exists in session_state, Streamlit
# ignores any `value=` argument passed to it on future reruns. So we
# must NOT pass value= at all once initialized -- instead each
# widget's callback directly writes into the *other* widget's key.

for field, default in [
    ("study", 10.0),
    ("attendance", 85.0),
    ("participation", 5.0),
]:
    if f"{field}_num" not in st.session_state:
        st.session_state[f"{field}_num"] = default
    if f"{field}_slider" not in st.session_state:
        st.session_state[f"{field}_slider"] = default


def sync_from_number(field):
    st.session_state[f"{field}_slider"] = st.session_state[f"{field}_num"]


def sync_from_slider(field):
    st.session_state[f"{field}_num"] = st.session_state[f"{field}_slider"]


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '''
    <div class="main-title">
        <div class="title-row">
            <div class="title-left">
                <div class="title-icon">🎓</div>
                <div>
                    <div class="title-text">Student Score Predictor</div>
                    <div class="subtitle">Machine Learning Powered Prediction</div>
                </div>
            </div>
            <div class="title-decor">
                <div class="dot-grid">
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                </div>
                <div class="chart-card">📈</div>
                <div class="pie-icon"></div>
            </div>
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)


# =====================================================
# DETAILS
# =====================================================

st.markdown(
    '''
    <div class="section">
        <div class="section-title">👨‍🎓 Enter Student Details</div>
        <div class="section-text">Fill in the information below to predict the student's total score.</div>
    </div>
    ''',
    unsafe_allow_html=True
)


# =====================================================
# INPUT COLUMNS
# =====================================================

col1, col2, col3 = st.columns(3)


# =====================================================
# STUDY HOURS
# =====================================================

with col1:

    st.markdown(
        '''
        <div class="card">
            <div class="card-icon">📖</div>
            <div class="card-title">Weekly Self Study Hours</div>
            <div class="card-description">Hours spent studying per week</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=40.0,
        step=0.5,
        key="study_num",
        on_change=sync_from_number,
        args=("study",),
        label_visibility="collapsed"
    )

    st.slider(
        "Study Slider",
        min_value=0.0,
        max_value=40.0,
        step=0.5,
        key="study_slider",
        on_change=sync_from_slider,
        args=("study",),
        label_visibility="collapsed"
    )

    study = st.session_state.study_num


# =====================================================
# ATTENDANCE
# =====================================================

with col2:

    st.markdown(
        '''
        <div class="card">
            <div class="card-icon">🗓️</div>
            <div class="card-title">Attendance Percentage</div>
            <div class="card-description">Overall attendance percentage</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.number_input(
        "Attendance",
        min_value=50.0,
        max_value=100.0,
        step=1.0,
        key="attendance_num",
        on_change=sync_from_number,
        args=("attendance",),
        label_visibility="collapsed"
    )

    st.slider(
        "Attendance Slider",
        min_value=50.0,
        max_value=100.0,
        step=1.0,
        key="attendance_slider",
        on_change=sync_from_slider,
        args=("attendance",),
        label_visibility="collapsed"
    )

    attendance = st.session_state.attendance_num


# =====================================================
# PARTICIPATION
# =====================================================

with col3:

    st.markdown(
        '''
        <div class="card">
            <div class="card-icon">🎯</div>
            <div class="card-title">Class Participation</div>
            <div class="card-description">Participation level in class</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.number_input(
        "Participation",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        key="participation_num",
        on_change=sync_from_number,
        args=("participation",),
        label_visibility="collapsed"
    )

    st.slider(
        "Participation Slider",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        key="participation_slider",
        on_change=sync_from_slider,
        args=("participation",),
        label_visibility="collapsed"
    )

    participation = st.session_state.participation_num


# =====================================================
# PREDICT BUTTON
# =====================================================

st.write("")

button_left, button_middle, button_right = st.columns([1, 1, 1])

with button_middle:
    predict = st.button("🚀  Predict Score", use_container_width=True)


# =====================================================
# PREDICTION
# =====================================================

if predict:
    input_data = [[study, attendance, participation]]
    prediction = model.predict(input_data)
    score = float(prediction[0])
    st.session_state["prediction"] = score


# =====================================================
# RESULT
# =====================================================

if "prediction" in st.session_state:

    score = st.session_state["prediction"]

    result_left, result_right = st.columns([1, 1.5])

    with result_left:
        st.markdown(
            '''
            <div class="result-box">
                <div class="result-title">🏆 Prediction Result</div>
                <div class="result-description">The predicted total score based on the provided student details.</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with result_right:
        st.markdown(
            f'''
            <div class="result-box">
                <div class="score-box">
                    <div class="score-label">Predicted Total Score</div>
                    <div class="score">{score:.2f}</div>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )


# =====================================================
# NOTE
# =====================================================

st.markdown(
    '''
    <div class="note">
        <strong>ⓘ Note:</strong> This prediction is based on the provided student inputs and the trained machine learning model.
    </div>
    ''',
    unsafe_allow_html=True
)