import streamlit as st
import json

with open("companies.json") as f:
    COMPANIES = json.load(f)["companies"]


from resume_checker import (
    analyze_resume_base,
    match_resume_to_company
)

from placement import evaluate_company

with open("curriculum.json") as f:
    curriculum = json.load(f)


st.set_page_config(
    page_title="Placement Guidance System",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 5px;'>
        Placement Guidance System
    </h1>
    <p style='text-align: center; color: gray; margin-top: 0;'>
        Curriculum-aware career guidance for students
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- TOP NAVIGATION ----------------
tabs = st.tabs(
    ["🏠 Home", "📄 Resume Checker", "🏢 Companies",
        "🎯 Placement", "📘 Study", "📘HR Round"]
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("Student Profile")

year = st.sidebar.selectbox(
    "Academic Year",
    ["Select", "1st Year", "2nd Year", "3rd Year", "4th Year"]
)

cgpa = st.sidebar.number_input("CGPA", 0.0, 10.0, step=0.1)
skills = st.sidebar.text_input("Skills (comma separated)")
experience = st.sidebar.number_input("Experience (months)", 0, 60)

# ======================================================
# HOME
# ======================================================
with tabs[0]:
    st.subheader("Welcome")

    if year == "Select":
        st.info(
            "Select your academic year from the sidebar to activate personalization.")
    else:
        st.success(f"Personalized mode active for **{year}** students.")

    st.write(
        """
        This platform helps students understand:
        - where they stand today
        - what companies expect
        - what to study next (without violating curriculum flow)
        """
    )

# ======================================================
# RESUME CHECKER
# ======================================================
with tabs[1]:
    st.subheader("Resume Checker")

    uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    KNOWN_SKILLS = [
        "c", "python", "java", "sql", "dbms",
        "data structures", "algorithms",
        "html", "css", "javascript"
    ]

    REQUIRED_SKILLS = ["python", "sql"]  # example role/company

    if uploaded:
        st.success("Resume uploaded successfully.")

        KNOWN_SKILLS = [
            "c", "python", "java", "sql", "dbms",
            "data structures", "algorithms",
            "html", "css", "javascript"
        ]

        resume_data = analyze_resume_base(uploaded, KNOWN_SKILLS)

        st.subheader("Resume Skills Detected")
        st.write(list(resume_data["found_skills"]))

        st.subheader("Company-wise Match")

        for company in COMPANIES:
            result = match_resume_to_company(
                resume_data,
                company["skills"]
            )

            st.markdown(f"### {company['company']}")
            st.metric("Skill Match", f"{result['match_percent']}%")
            st.write("Missing Skills:", result["missing_skills"])
            st.divider()

    else:
        st.warning("Upload a resume to begin analysis.")

# ======================================================
# COMPANIES
# ======================================================
with tabs[2]:
    st.subheader("Companies on Campus")

    st.write("Explore company eligibility, packages, and hiring process.")

    st.table({
        "Company": [
            "Juspay",
            "Paytm",
            "Coforge Limited",
            "Bharti Airtel Ltd.",
            "TATA Consultancy Services (TCS)",
            "Sopra Steria India Limited",
            "LTIMindtree Limited",
            "HCL Technologies Ltd.",
            "OneBanc Technologies Pvt. Ltd.",
            "Samsung India Electronics Pvt. Ltd.",
            "Polycab India Limited",
            "Planify Capital Limited",
            "Freecharge Payment Technologies Pvt. Ltd.",
            "Comviva Technologies Limited",
            "Capgemini Technology Services India Limited",
            "TalentServe",
            "Tech Mahindra",
            "Airtel India",
            "Crowe Horwath IT Services LLP",
            "CG Infinity (Cyber Group India Pvt. Ltd.)",
            "i2V Systems Pvt. Ltd.",
            "Eazy ERP Technologies Pvt. Ltd.",
            "DCM Infotech Ltd.",
            "BrightRays",
            "FutureSoft India Pvt. Ltd.",
            "Uneecops Technologies Limited",
            "Octa Byte AI Private Limited",
            "One97 Communications Limited (Paytm)",
            "Cache Digitech Pvt. Ltd.",
            "Keywords Studios India Private Limited",
            "American EPAY Services Pvt. Ltd.",
            "Rupeek Capital Private Limited",
            "ArdorIT Solutions INC",
            "Urban Company",
            "Planetspark | Winspark Innovations Learning Private Limited",
            "Prudentia Group LLC",
            "Dhani Stocks Limited",
            "Mahindra & Mahindra (Minda Corp)",
            "Shimadzu Analytical India Pvt. Ltd.",
            "Gamix Labs"
        ],

        "Min CGPA": [
            7.0, 6.5, 6.5, 6.0, 6.0, 6.0, 6.5, 6.0, 6.5, 7.0,
            6.0, 6.0, 6.5, 6.5, 6.0, 6.5, 6.0, 6.0, 6.0, 6.0,
            6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.5, 6.0, 6.0,
            6.0, 6.0, 6.0, 6.0, 6.0, 6.5, 6.0, 6.0, 6.0, 6.0
        ],

        "Package (LPA / Stipend)": [
            "21 – 27 LPA",                 # Juspay
            "3.0 LPA",                     # Paytm
            "4.25 LPA",                    # Coforge
            "5.5 – 5.57 LPA",              # Bharti Airtel
            "3.36 LPA",                    # TCS
            "4 – 6 LPA",                   # Sopra Steria
            "4.05 LPA",                    # LTIMindtree
            "3 – 4.25 LPA",                # HCL
            "10 LPA",                      # OneBanc
            "7.65 LPA",                    # Samsung
            "3.0 LPA",                     # Polycab
            "4.25 – 6.26 LPA",             # Planify
            "5.5 – 7 LPA",                 # Freecharge
            "5.5 LPA",                     # Comviva
            "4 LPA",                       # Capgemini
            "5.5-12 LPA",                  # talentserve
            "2.37 – 3.25 LPA",             # Tech Mahindra
            "5.5 – 5.57 LPA",              # Airtel India
            "6.0 LPA",                     # Crowe Horwath
            "7.0 LPA",                     # CG Infinity
            "3 – 4.8 LPA",                 # i2V Systems
            "3.0 – 4.2 LPA",               # Eazy ERP
            "3 – 4.25 LPA",                # DCM Infotech
            "4.80 LPA",                    # BrightRays
            "4.50 LPA",                    # FutureSoft
            "5 LPA",                       # Uneecops
            "5 LPA",                       # Octa Byte AI
            "3.0 LPA",                     # One97 Communications
            "6 LPA",                       # Cache Digitech
            "4.41 LPA",                    # Keywords Studios
            "6.25 LPA",                    # American EPAY
            "3.50 LPA",                    # Rupeek Capital
            "5.80 LPA",                    # ArdorIT
            "3.49 – 3.63 LPA",             # Urban Company
            "6.50 LPA",               # Planetspark
            "6.5 – 7 LPA",                 # Prudentia Group
            "4.6 LPA",                     # Dhani Stocks
            "3 LPA",                       # Mahindra & Mahindra
            "3.5-4.8 LPA",               # Shimadzu
            "2.5 – 4 LPA"                  # Gamix Labs
        ]
    })


# ======================================================
# PLACEMENT
# ======================================================
with tabs[3]:
    st.subheader("Placement Readiness")

    if year == "Select" or not skills:
        st.warning("Please select academic year and enter skills.")
    else:
        # ---------------- STUDENT OBJECT ----------------
        student = {
            "year": year,
            "cgpa": cgpa,
            "skills": [s.strip().lower() for s in skills.split(",") if s.strip()],
            "experience_months": experience,
            "projects": 0
        }

        results = []

        for company in COMPANIES:
            result = evaluate_company(student, company, curriculum)
            results.append({
                "company": company["company"],
                **result
            })

        eligible_results = [r for r in results if r["eligible"]]
        eligible_results.sort(key=lambda x: x["fit_score"], reverse=True)

        col1, col2, col3 = st.columns(3)

        if eligible_results:
            best = eligible_results[0]
            col1.metric("Best Fit Score", f"{best['fit_score']}%")
            col2.metric("Eligible Companies", len(eligible_results))
            col3.metric("Top Company", best["company"])
        else:
            col1.metric("Fit Score", "0%")
            col2.metric("Eligible Companies", 0)
            col3.metric("Status", "Not Eligible")

        st.divider()
        st.subheader("Company-wise Placement Evaluation")

        for r in eligible_results:
            st.markdown(f"### {r['company']}")
            st.write(f"Fit Score: {r['fit_score']}%")
            st.write("Missing Skills:", r["missing_skills"])
            for reason in r["reasons"]:
                st.info(reason)
            st.divider()


# ======================================================
# STUDY
# ======================================================
with tabs[4]:
    st.subheader("Study Guidance")

    if year == "Select":
        st.warning("Select your academic year to view roadmap.")
    else:
        st.write(f"Recommended focus areas for **{year}**:")

        if year == "1st Year":
            st.write("- Programming fundamentals\n- Math & logic\n- Exploration")
        elif year == "2nd Year":
            st.write("- DSA\n- OOPS\n- Mini projects")
        elif year == "3rd Year":
            st.write("- OS, CN\n- Internships\n- Resume building")
        elif year == "4th Year":
            st.write("- SQL & system design\n- Interview prep\n- Company targeting")


# ======================================================
# INTERVIEW QUIZ
# ======================================================
with tabs[5]:
    st.subheader("Interview Quiz")

    st.write("Test your knowledge with a quick quiz!")

    q1 = st.selectbox(
        "What is the time complexity of binary search?",
        ["Select", "O(n)", "O(log n)", "O(n log n)", "O(1)"]
    )

    q2 = st.selectbox(
        "Which data structure uses FIFO order?",
        ["Select", "Stack", "Queue", "Linked List", "Tree"]
    )

    if q1 != "Select" and q2 != "Select":
        score = 0
        if q1 == "O(log n)":
            score += 50
        if q2 == "Queue":
            score += 50

        st.success(f"Your quiz score: {score}%")
