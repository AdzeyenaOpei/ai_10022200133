import streamlit as st
from src.retrieval import retrieve_documents
from src.prompt import build_prompt
from src.generator import generate_response

st.set_page_config(
    page_title="Kobina Opei's AI Assistant for Academic City University",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional HCI-focused UI
st.markdown("""
<style>

/* Base Layout */
.stApp {
    background: #F8FAFC;
}

.main {
    background: #F8FAFC;
}

/* Header Card */
.hero-card {
    background: #FFFFFF;
    border-radius: 20px;
    padding: 28px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    margin-bottom: 20px;
}

.hero-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #000000;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 1rem;
    color: #000000;
    line-height: 1.6;
}

/* KPI Cards */
.metric-card {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 18px;
    border: 1px solid #E2E8F0;
    text-align: center;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
}

.metric-title {
    font-size: 0.9rem;
    color: #000000;
}

.metric-value {
    font-size: 1.3rem;
    font-weight: 700;
    color: #000000;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #E2E8F0;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    background: #2563EB;
    color: white;
    border: none;
    font-weight: 600;
    padding: 0.75rem;
}

.stButton > button:hover {
    background: #1D4ED8;
    color: white;
}

/* Chat */
.stChatMessage {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 14px;
}

/* Input */
[data-testid="stChatInput"] {
    border-top: 1px solid #E2E8F0;
    background: #FFFFFF;
}



/* Force all visible text to black */
html, body, [class*="css"], .stMarkdown, .stText, p, span, div, label, h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

/* Sidebar text visibility */
section[data-testid="stSidebar"] * {
    color: #000000 !important;
}

/* Chat input placeholder */
input, textarea {
    color: #000000 !important;
}

/* Chat messages */
[data-testid="stChatMessageContent"] {
    color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Welcome 👋 I’m your AI assistant. Ask me about election results, inflation targets, GDP projections, or budget insights."
        }
    ]

# Top Hero Section
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🎓 Kobina Opei's AI Assistant for Academic City University</div>
    <div class="hero-subtitle">
        Investor-ready Retrieval-Augmented Generation (RAG) platform for structured decision support.<br>
        Designed to answer high-value questions from election datasets and national budget reports with speed, clarity, and trust.
    </div>
</div>
""", unsafe_allow_html=True)

# KPI Section for investor confidence
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Knowledge Sources</div>
        <div class="metric-value">2 Core Datasets</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Response Model</div>
        <div class="metric-value">RAG + OpenAI</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">User Experience</div>
        <div class="metric-value">Persistent Chat</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Chat Area
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input stays persistent
user_question = st.chat_input("Ask a strategic question...")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing documents..."):
            try:
                docs, scores = retrieve_documents(user_question)
                prompt = build_prompt(user_question, docs)
                answer = generate_response(prompt)
            except Exception as e:
                docs, scores = [], []
                answer = f"System Error: {str(e)}"

            # Show final answer first
            st.markdown(answer)

            # Dropdown for retrieved chunks
            if docs:
                with st.expander("View Retrieved Chunks"):
                    for i, (doc, score) in enumerate(zip(docs, scores), 1):
                        st.markdown(f"### Chunk {i}")
                        st.write(doc)
                        st.caption(f"Similarity Score: {score:.4f}")
                        st.divider()

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# Sidebar
with st.sidebar:
    st.markdown("## Executive Dashboard")
    st.caption("Quick access tools for presentation, investor demonstrations, and strategic decision support")

    if st.button("Reset Conversation"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Conversation reset successfully. Ask a new question."
            }
        ]
        st.rerun()

    st.markdown("---")
    st.markdown("### High-Impact Demo Questions")
    st.markdown("• Who won Ghana's 2020 presidential election?")
    st.markdown("• What is the inflation target for 2025?")
    st.markdown("• What is the projected GDP growth target for 2025?")
    st.markdown("• Which party dominated the Ashanti Region?")

    st.markdown("---")
    st.markdown("### Core Business Value")
    st.markdown("✔ Faster decision support")
    st.markdown("✔ Reduced manual document search")
    st.markdown("✔ Higher retrieval precision")
    st.markdown("✔ Investor-grade conversational analytics")
