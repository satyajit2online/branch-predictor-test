import streamlit as st
import os
import csv

# File where student records will be saved
DATA_FILE = "student_leads.csv"

def save_lead(name, mobile, result):
    """Saves student details and their test result to a CSV file."""
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Mobile Number", "Recommended Branch"])
        writer.writerow([name, mobile, result])

# Set up page configuration
st.set_page_config(page_title="Engineering Fitment Test", page_icon="🧠", layout="centered")

if "user_registered" not in st.session_state:
    st.session_state.user_registered = False
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

st.title("🧠 Engineering Branch & Psychometric Predictor")
st.write("This test combines your practical interests with psychometric profiling to find your ideal engineering field.")
st.markdown("---")

# STEP 1: Registration Form
if not st.session_state.user_registered:
    st.subheader("📝 Enter your details to unlock the assessment")
    
    with st.form("registration_form"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        mobile = st.text_input("Mobile Number", max_chars=10, placeholder="Enter 10-digit mobile number")
        
        submit_btn = st.form_submit_button("Start Assessment")
        
        if submit_btn:
            if not name.strip():
                st.error("Please enter your name.")
            elif not mobile.isdigit() or len(mobile) != 10:
                st.error("Please enter a valid 10-digit mobile number.")
            else:
                st.session_state.user_data = {"name": name, "mobile": mobile}
                st.session_state.user_registered = True
                st.rerun()

# STEP 2: The Combined Test
else:
    st.sidebar.success(f"📋 Candidate: {st.session_state.user_data['name']}")
    
    with st.form("quiz_form"):
        st.subheader("Section 1: Work Style & Cognitive Traits")
        
        # Defining exact text options (completely hidden mappings)
        p1_options = [
            "Break it down into logical, step-by-step sequences or rules.",
            "Visualize how the physical pieces fit together or interact spatially.",
            "Look for the underlying pattern, data flow, or invisible connections.",
            "Try to physically manipulate it, open it up, or see it in action."
        ]
        p1 = st.radio("1. When facing a complex puzzle or breakdown, what is your first instinct?", p1_options)

        p2_options = [
            "Abstract thinking: Working with concepts, logic, codes, and data structures.",
            "Spatial thinking: Visualizing 3D objects, layouts, landscapes, and scales.",
            "Kinesthetic thinking: Understanding forces, mechanics, speeds, and physical motion.",
            "System thinking: Understanding loops, signal flows, and energy distribution."
        ]
        p2 = st.radio("2. Which type of thinking do you find most satisfying?", p2_options)

        p3_options = [
            "Writing the operating system, apps, and making the interface smooth.",
            "Designing the physical sleekness, structural durability, and drop-resistance.",
            "Designing the internal cooling vents, battery thermal limits, and assembly.",
            "Optimizing the motherboard circuits, microchips, and 5G signal reception."
        ]
        p3 = st.radio("3. Imagine you are building a new smartphone. What part of the process excites you most?", p3_options)

        p4_options = [
            "Virtually: A perfectly running program, app, or website on a screen.",
            "Monumentally: A real-life physical structure standing tall in the real world.",
            "Dynamically: A machine, vehicle, or engine moving and operating smoothly.",
            "Functionally: Seamless power distribution, automation, or active connectivity."
        ]
        p4 = st.radio("4. How do you prefer to see the results of your hard work?", p4_options)

        st.markdown("---")
        st.subheader("Section 2: Engineering & Technology Interests")

        q1_options = [
            "An AI research lab or a massive cloud data data center.",
            "A mega-structure construction site, tunnel project, or smart city development.",
            "An automated automotive manufacturing plant or robotics assembly line.",
            "A semiconductor fabrication facility (chip plant) or satellite ground station."
        ]
        q1 = st.radio("5. If you could visit a cutting-edge facility tomorrow, where would you go?", q1_options)

        q2_options = [
            "Generative AI, Cyber Security, and Web3 frameworks.",
            "Sustainable green infrastructure, earthquake-proof designs, and smart highways.",
            "Hypercars, supersonic aerospace designs, and defense robotics.",
            "Quantum computing chips, IoT smart grids, and wireless networks."
        ]
        q2 = st.radio("6. Which tech trend catches your attention the most in the news?", q2_options)

        submit_test = st.form_submit_button("Calculate My Fitment Profile")

    # STEP 3: Hidden Backend Scoring Matrix
    if submit_test:
        scores = {
            "Computer Engineering / IT": 0,
            "Civil Engineering": 0,
            "Mechanical Engineering": 0,
            "Electronics & Telecommunication": 0
        }
        
        # Question 1 logic mapping
        if p1 == p1_options[0]: scores["Computer Engineering / IT"] += 2
        elif p1 == p1_options[1]: 
            scores["Civil Engineering"] += 1.5
            scores["Mechanical Engineering"] += 1.5
        elif p1 == p1_options[2]:
            scores["Electronics & Telecommunication"] += 1.5
            scores["Computer Engineering / IT"] += 1.5
        elif p1 == p1_options[3]:
            scores["Mechanical Engineering"] += 1.5
            scores["Civil Engineering"] += 1.5

        # Question 2 logic mapping
        if p2 == p2_options[0]: scores["Computer Engineering / IT"] += 2
        elif p2 == p2_options[1]: scores["Civil Engineering"] += 2
        elif p2 == p2_options[2]: scores["Mechanical Engineering"] += 2
        elif p2 == p2_options[3]: scores["Electronics & Telecommunication"] += 2

        # Question 3 logic mapping
        if p3 == p3_options[0]: scores["Computer Engineering / IT"] += 2
        elif p3 == p3_options[1]: scores["Civil Engineering"] += 2
        elif p3 == p3_options[2]: scores["Mechanical Engineering"] += 2
        elif p3 == p3_options[3]: scores["Electronics & Telecommunication"] += 2

        # Question 4 logic mapping
        if p4 == p4_options[0]: scores["Computer Engineering / IT"] += 2
        elif p4 == p4_options[1]: scores["Civil Engineering"] += 2
        elif p4 == p4_options[2]: scores["Mechanical Engineering"] += 2
        elif p4 == p4_options[3]: scores["Electronics & Telecommunication"] += 2

        # Question 5 logic mapping
        if q1 == q1_options[0]: scores["Computer Engineering / IT"] += 2
        elif q1 == q1_options[1]: scores["Civil Engineering"] += 2
        elif q1 == q1_options[2]: scores["Mechanical Engineering"] += 2
        elif q1 == q1_options[3]: scores["Electronics & Telecommunication"] += 2

        # Question 6 logic mapping
        if q2 == q2_options[0]: scores["Computer Engineering / IT"] += 2
        elif q2 == q2_options[1]: scores["Civil Engineering"] += 2
        elif q2 == q2_options[2]: scores["Mechanical Engineering"] += 2
        elif q2 == q2_options[3]: scores["Electronics & Telecommunication"] += 2

        recommended_branch = max(scores, key=scores.get)
        total_score_pool = sum(scores.values())

        # Save data
        save_lead(st.session_state.user_data['name'], st.session_state.user_data['mobile'], recommended_branch)

        st.markdown("---")
        st.balloons()
        st.subheader(f"🎉 Fitment Analysis for {st.session_state.user_data['name']}!")
        st.success(f"### **{recommended_branch}**")
        
        descriptions = {
            "Computer Engineering / IT": "**Psychometric Profile:** High logical-abstract reasoning, strong preference for rule-based systems, and symbolic problem-solving.",
            "Civil Engineering": "**Psychometric Profile:** Strong spatial-visual orientation, macro-system thinking, and a preference for tangible, long-lasting real-world infrastructure.",
            "Mechanical Engineering": "**Psychometric Profile:** High kinesthetic and physical mechanics curiosity. You are naturally drawn to how dynamic forces and machinery operate.",
            "Electronics & Telecommunication": "**Psychometric Profile:** Strong microscopic and flow-based analytical thinking. You bridge the gap between invisible signals and physical hardware."
        }
        st.write(descriptions[recommended_branch])
        
        st.markdown("### **Your Match Profile Breakdown:**")
        for branch, score in scores.items():
            percentage = min(int((score / total_score_pool) * 100), 100)
            st.progress(percentage / 100, text=f"**{branch}**: {percentage}% Match")
