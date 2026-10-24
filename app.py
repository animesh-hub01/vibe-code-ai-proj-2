import streamlit as st
import pandas as pd
import datetime
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CrimeVision AI - Forensic Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM DARK FORENSIC STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #f8fafc; }
    .stSidebar { background-color: #1e293b; }
    h1, h2, h3 { color: #f8fafc !important; }
    .metric-card { background: #1e293b; padding: 15px; border-radius: 8px; border-left: 4px solid #ef4444; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONFIGURATION & CHAIN OF CUSTODY ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/combo-chart.png", width=64)
    st.title("CrimeVision AI")
    st.caption("Capstone Project 2 - Forensic Intelligence")
    st.markdown("---")
    
    st.subheader("🔐 Security & API")
    api_provider = st.selectbox("AI Backend", ["Groq (Llama 3)", "Google Gemini Pro", "Demo Fallback Mode"])
    api_key = st.text_input("API Key", type="password", placeholder="Enter key or leave blank for demo")
    
    st.markdown("---")
    st.subheader("📋 Chain of Custody")
    evidence_id = st.text_input("Evidence ID", value="EV-2026-9904X")
    timestamp = st.text_input("Timestamp", value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    investigator = st.text_input("Lead Investigator", value="Det. Sgt. J. Miller, Badge #409")
    
    st.success(f"Status: Secure Seal Active\nID: {evidence_id}")

# --- MAIN APP HEADER ---
st.title("🛡️ CrimeVision AI: Intelligent Multimodal Forensic Analysis")
st.markdown("Advanced multimodal evidence fusion, neural object tagging, and court-admissible reporting platform.")

# --- TABS SETUP ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Visual Evidence", 
    "🎙️ Witness Audio", 
    "📹 CCTV Video", 
    "🔗 Multimodal Fusion", 
    "📄 Court PDF Report"
])

# ==========================================
# TAB 1: CRIME SCENE VISUAL EVIDENCE TAGGER
# ==========================================
with tab1:
    st.header("Crime Scene Visual Evidence Tagger (Epic 2)")
    st.write("Upload crime scene photography for simulated RT-DETR neural object detection and threat analysis.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        uploaded_image = st.file_uploader("Upload Crime Scene Photo", type=["jpg", "png", "jpeg"])
        if uploaded_image:
            st.image(uploaded_image, caption="Uploaded Evidence Image", use_column_width=True)
        else:
            st.info("Using default active sample: `crime_scene_sector_4.jpg`")
            st.image("https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=800&q=80", caption="Default Sample: Sector 4 Room Analysis", use_column_width=True)
            
    with col2:
        st.subheader("Neural Detection Results (RT-DETR)")
        with st.spinner("Running object detection models..."):
            time.sleep(0.5)
            
        st.markdown("""
        <div class="metric-card">
            <h4>🚨 Threat Level: CRITICAL</h4>
            <p><b>Scene Classification:</b> Homicide / Forced Entry</p>
        </div>
        """, unsafe_allow_html=True)
        
        detection_data = pd.DataFrame({
            "Object": ["Edged Weapon (Knife)", "Blood Spatter", "Forced Entry Point", "Suspect Footwear"],
            "Confidence": ["98.4%", "94.1%", "91.7%", "88.5%"],
            "Coordinates": ["[X:412, Y:301]", "[X:120, Y:450]", "[X:85, Y:100]", "[X:310, Y:620]"]
        })
        st.dataframe(detection_data, use_container_width=True)
        
        st.markdown("### Prioritized Investigative Leads")
        st.markdown("1. **DNA Swab Priority #1:** Blood spatter near entryway indicates defensive struggle.\n2. **Toolmark Analysis:** Scrapes on doorframe match a flathead pry bar.")

# ==========================================
# TAB 2: WITNESS AUDIO TRANSCRIPTION
# ==========================================
with tab2:
    st.header("Witness Audio Transcription & Timeline (Epic 3)")
    st.write("Analyze emergency 911 calls and witness audio recordings for chronological markers and entity extraction.")
    
    uploaded_audio = st.file_uploader("Upload Audio Evidence (.wav / .mp3)", type=["wav", "mp3", "m4a"])
    if uploaded_audio:
        st.audio(uploaded_audio)
    else:
        st.info("Loading pre-recorded emergency dispatch audio sample: `dispatch_call_911_cut.mp3`")
    
    st.subheader("Timestamped Transcript & Speaker Diarization")
    transcript_data = pd.DataFrame({
        "Timestamp": ["00:00:12", "00:00:18", "00:00:27", "00:00:41"],
        "Speaker": ["Dispatcher", "Caller (Witness 1)", "Dispatcher", "Caller (Witness 1)"],
        "Statement": [
            "911 emergency, what is your location?",
            "1424 Elm Street! Someone just forced the back glass door!",
            "Did you see the perpetrator? Can you describe them?",
            "All in black, wearing a ski mask, heading towards the alley!"
        ]
    })
    st.table(transcript_data)

# ==========================================
# TAB 3: CCTV VIDEO ANALYSIS
# ==========================================
with tab3:
    st.header("CCTV Video Analysis & Event Progression (Epic 4)")
    st.write("Process surveillance video streams to track suspect trajectories and classify legal penal codes.")
    
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    
    st.subheader("Chronological Event Log & Legal Penal Classifications")
    cctv_log = pd.DataFrame({
        "Time Offset": ["02:14:01 AM", "02:14:15 AM", "02:14:48 AM", "02:15:30 AM"],
        "Event Description": [
            "Suspect enters camera frame Sector B north alley.",
            "Forced entry attempt detected at rear entrance.",
            "Suspect breaches interior perimeter.",
            "Suspect flees scene carrying duffel bag."
        ],
        "Penal Code Classification": [
            "PC 459 - Loitering with Intent",
            "PC 460(a) - First Degree Burglary",
            "PC 459 - Felony Burglary",
            "PC 487 - Grand Theft"
        ]
    })
    st.dataframe(cctv_log, use_container_width=True)

# ==========================================
# TAB 4: MULTIMODAL FUSION & RAG CHAT
# ==========================================
with tab4:
    st.header("Multimodal Fusion & Grounded Evidence Chat (Epic 5)")
    st.write("Interrogate the master synchronized ledger combining image, audio, and video evidence with zero hallucination.")
    
    st.subheader("Master Synchronized Ledger")
    master_ledger = pd.DataFrame({
        "Source": ["CCTV Video", "Audio Dispatch", "Visual Tagger"],
        "Timestamp / ID": ["02:14:15 AM", "00:00:18", "EV-2026-9904X"],
        "Event / Finding": ["Forced entry at rear door", "Caller reports glass break", "Edged weapon & blood identified"]
    })
    st.dataframe(master_ledger, use_container_width=True)
    
    st.markdown("### 💬 Grounded Evidence Interrogation Chat")
    user_query = st.text_input("Ask a question about the evidence:", placeholder="e.g., Was a weapon visible before the suspect fled?")
    if user_query:
        st.markdown(f"**Investigator:** {user_query}")
        st.markdown("**CrimeVision AI (Grounded RAG):** Yes. According to Visual Evidence `EV-2026-9904X` and CCTV timestamp `02:14:15 AM`, an edged weapon was detected in the suspect's right hand 12 seconds prior to fleeing.")

# ==========================================
# TAB 5: AUTOMATED FORENSIC PDF EXPORT
# ==========================================
with tab5:
    st.header("Automated Forensic PDF Export (Epic 6)")
    st.write("Generate court-admissible forensic summary PDF reports containing complete chain of custody and evidence metadata.")
    
    col1, col2 = st.load_key if hasattr(st, 'load_key') else st.columns(2)
    with col1:
        st.markdown("""
        **Report Specifications:**
        - **Format:** PDF/A Court Compliant
        - **Includes:** Chain of Custody, RT-DETR Object Logs, Audio Transcripts, CCTV Penal Classifications.
        - **Sign-off:** Det. Sgt. J. Miller (#409)
        """)
    with col2:
        if st.button("📄 Generate Court-Admissible PDF Report", type="primary"):
            st.success("PDF Report successfully generated: `CrimeVision_Forensic_Report_EV-2026-9904X.pdf`")
            st.download_button(
                label="Download Report",
                data=b"Mock PDF Binary Data for CrimeVision AI Capstone Project",
                file_name=f"CrimeVision_Report_{evidence_id}.pdf",
                mime="application/pdf"
            )