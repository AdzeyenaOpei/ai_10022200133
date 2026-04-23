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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Lato:wght@300;400;700&family=Source+Code+Pro:wght@400;500&display=swap');

/* ══════════════════════════════════════════════
   ROOT VARIABLES
══════════════════════════════════════════════ */
:root {
    --cream:       #FAFAF7;
    --white:       #FFFFFF;
    --ink:         #1A1A2E;
    --ink2:        #2D2D44;
    --ink3:        #4A4A65;
    --muted:       #8A8AA8;
    --divider:     #E4E4F0;
    --gold:        #C49A2A;
    --gold-bg:     #FEFBF0;
    --blue:        #2962C4;
    --blue-mid:    #4A7FD4;
    --blue-light:  #EEF3FD;
    --green:       #1A7A4A;
    --green-bg:    #F0FBF5;
    --shadow-sm:   0 1px 4px rgba(26,26,46,0.06);
    --shadow-md:   0 4px 20px rgba(26,26,46,0.09);
    --r-sm:        8px;
    --r-md:        14px;
    --r-lg:        20px;
    --font-serif:  'Playfair Display', Georgia, serif;
    --font-body:   'Lato', system-ui, sans-serif;
    --font-mono:   'Source Code Pro', monospace;
}

/* ══════════════════════════════════════════════
   GLOBAL
══════════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
    font-family: var(--font-body) !important;
    background: var(--cream) !important;
    color: var(--ink) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
p, span, div, label { font-family: var(--font-body) !important; }

/* ══════════════════════════════════════════════
   SIDEBAR — dark scholarly panel
══════════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background: #14142A !important;
    border-right: none !important;
    width: 270px !important;
}
section[data-testid="stSidebar"] > div {
    padding: 0 !important;
    overflow-x: hidden;
}
section[data-testid="stSidebar"] * {
    color: #C0C0D8 !important;
    font-family: var(--font-body) !important;
}

/* Sidebar Brand */
.sb-brand {
    padding: 26px 20px 20px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.sb-chip {
    display: inline-block;
    padding: 3px 9px;
    background: rgba(196,154,42,0.15);
    border: 1px solid rgba(196,154,42,0.3);
    border-radius: 20px;
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #EAC84A !important;
    margin-bottom: 12px;
}
.sb-title {
    font-family: var(--font-serif) !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #F0F0FA !important;
    line-height: 1.35 !important;
    margin-bottom: 4px;
}
.sb-sub {
    font-size: 11.5px !important;
    color: #5A5A80 !important;
    line-height: 1.5 !important;
}

/* Sidebar sections */
.sb-sec {
    padding: 16px 20px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.sb-lbl {
    display: block;
    font-size: 9.5px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    color: #44446A !important;
    margin-bottom: 10px;
}

/* Question pills */
.sb-q {
    display: flex;
    gap: 8px;
    align-items: flex-start;
    padding: 8px 10px;
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.045);
    border-radius: var(--r-sm);
    margin-bottom: 5px;
    cursor: default;
    transition: background 0.12s, border-color 0.12s;
}
.sb-q:hover {
    background: rgba(255,255,255,0.055);
    border-color: rgba(196,154,42,0.22);
}
.sb-q-icon { font-size: 13px; flex-shrink: 0; margin-top: 1px; opacity: 0.8; }
.sb-q-text { font-size: 12px !important; color: #9090B8 !important; line-height: 1.45 !important; }

/* Stat rows */
.sb-stat {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 7px 0;
    border-bottom: 1px solid rgba(255,255,255,0.035);
}
.sb-stat:last-child { border-bottom: none; }
.sb-stat-l { font-size: 12px !important; color: #6060A0 !important; }
.sb-stat-r {
    font-family: var(--font-mono) !important;
    font-size: 10.5px !important;
    font-weight: 600 !important;
    color: #EAC84A !important;
    background: rgba(196,154,42,0.1);
    padding: 2px 7px;
    border-radius: 4px;
}

/* Reset button */
.stButton > button {
    width: 100% !important;
    border-radius: var(--r-sm) !important;
    background: rgba(255,255,255,0.04) !important;
    color: #9090B8 !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    font-size: 12.5px !important;
    font-weight: 400 !important;
    padding: 0.55rem 1rem !important;
    font-family: var(--font-body) !important;
    letter-spacing: 0.01em !important;
    transition: all 0.12s !important;
}
.stButton > button:hover {
    background: rgba(255,255,255,0.09) !important;
    color: #F0F0FA !important;
    border-color: rgba(255,255,255,0.18) !important;
}

/* ══════════════════════════════════════════════
   PAGE HEADER
══════════════════════════════════════════════ */
.ph {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
    padding: 30px 36px 26px;
    background: var(--white);
    border-bottom: 1px solid var(--divider);
}
.ph-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-size: 10.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--blue) !important;
    margin-bottom: 9px;
}
.ph-eyebrow-bar {
    width: 18px; height: 2px;
    background: var(--blue);
    border-radius: 1px;
    display: inline-block;
}
.ph-title {
    font-family: var(--font-serif) !important;
    font-size: 27px !important;
    font-weight: 600 !important;
    color: var(--ink) !important;
    line-height: 1.22 !important;
    letter-spacing: -0.01em !important;
    margin-bottom: 8px !important;
}
.ph-sub {
    font-size: 14px !important;
    color: var(--ink3) !important;
    line-height: 1.65 !important;
    font-weight: 300 !important;
    max-width: 500px;
}
.ph-badges { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; flex-shrink: 0; }
.badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 5px 12px; border-radius: 20px;
    font-size: 11px; font-weight: 600; letter-spacing: 0.02em;
}
.badge-live {
    background: var(--green-bg);
    color: var(--green) !important;
    border: 1px solid rgba(26,122,74,0.18);
}
.live-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--green);
    animation: livepulse 2s infinite;
}
@keyframes livepulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
.badge-rag {
    background: var(--blue-light);
    color: var(--blue) !important;
    border: 1px solid rgba(41,98,196,0.14);
}

/* ══════════════════════════════════════════════
   KPI STRIP
══════════════════════════════════════════════ */
.kpi-strip {
    display: flex;
    background: var(--white);
    border-bottom: 1px solid var(--divider);
}
.kpi {
    flex: 1;
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 17px 28px;
    border-right: 1px solid var(--divider);
    transition: background 0.12s;
}
.kpi:last-child { border-right: none; }
.kpi:hover { background: var(--cream); }
.kpi-ico {
    width: 37px; height: 37px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; flex-shrink: 0;
}
.k-gold  { background: var(--gold-bg);   border: 1px solid rgba(196,154,42,0.2); }
.k-blue  { background: var(--blue-light); border: 1px solid rgba(41,98,196,0.14); }
.k-green { background: var(--green-bg);  border: 1px solid rgba(26,122,74,0.14); }
.kpi-lbl {
    font-size: 10px !important; font-weight: 700 !important;
    text-transform: uppercase !important; letter-spacing: 0.1em !important;
    color: var(--muted) !important; margin-bottom: 3px !important;
}
.kpi-val {
    font-family: var(--font-serif) !important;
    font-size: 14.5px !important; font-weight: 600 !important;
    color: var(--ink) !important;
}

/* ══════════════════════════════════════════════
   CHAT SECTION HEADER
══════════════════════════════════════════════ */
.chat-hdr {
    display: flex; align-items: center; justify-content: space-between;
    padding: 13px 28px;
    background: var(--white);
    border-bottom: 1px solid var(--divider);
}
.chat-hdr-title {
    display: flex; align-items: center; gap: 8px;
    font-size: 12px !important; font-weight: 700 !important;
    text-transform: uppercase !important; letter-spacing: 0.1em !important;
    color: var(--ink3) !important;
}
.chat-hdr-bar { width: 3px; height: 14px; background: var(--blue); border-radius: 2px; }

/* ══════════════════════════════════════════════
   MESSAGES — hide avatars, clean bubbles
══════════════════════════════════════════════ */

/* Hide the avatar column entirely */
[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"],
[data-testid="stChatMessageAvatar"] {
    display: none !important;
}

[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 5px 36px !important;
    gap: 0 !important;
}

/* Full-width content column once avatar is gone */
[data-testid="stChatMessage"] > div:last-child {
    width: 100% !important;
    min-width: 0 !important;
}

[data-testid="stChatMessageContent"] {
    width: 100% !important;
}

[data-testid="stChatMessageContent"] p {
    font-size: 14.5px !important;
    line-height: 1.75 !important;
    color: var(--ink2) !important;
    font-weight: 400 !important;
    margin: 0 !important;
}

/* User bubble — right-aligned */
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"])
    [data-testid="stChatMessageContent"] {
    display: flex !important;
    justify-content: flex-end !important;
}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"])
    [data-testid="stChatMessageContent"] p {
    background: var(--ink) !important;
    color: #E4E4F8 !important;
    border-radius: var(--r-md) var(--r-md) 4px var(--r-md) !important;
    padding: 11px 16px !important;
    display: inline-block !important;
    max-width: 68% !important;
    font-size: 14px !important;
    line-height: 1.65 !important;
    box-shadow: var(--shadow-sm) !important;
    float: none !important;
}

/* Assistant bubble — left-aligned */
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"])
    [data-testid="stChatMessageContent"] p {
    background: var(--white) !important;
    color: var(--ink2) !important;
    border: 1px solid var(--divider) !important;
    border-radius: 4px var(--r-md) var(--r-md) var(--r-md) !important;
    padding: 13px 17px !important;
    display: block !important;
    max-width: 80% !important;
    font-size: 14.5px !important;
    line-height: 1.75 !important;
    box-shadow: var(--shadow-sm) !important;
}

/* ══════════════════════════════════════════════
   EXPANDER (retrieved chunks)
══════════════════════════════════════════════ */
[data-testid="stExpander"] {
    background: var(--cream) !important;
    border: 1px solid var(--divider) !important;
    border-radius: var(--r-md) !important;
    margin-top: 10px !important;
    overflow: hidden !important;
    box-shadow: none !important;
}
[data-testid="stExpander"] summary {
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    color: var(--ink3) !important;
    padding: 12px 16px !important;
    background: var(--cream) !important;
    transition: background 0.12s !important;
    list-style: none !important;
}

/* Hide the native browser/Streamlit arrow that was leaking as _arr */
[data-testid="stExpander"] summary::-webkit-details-marker { display: none !important; }
[data-testid="stExpander"] summary::marker               { display: none !important; }
[data-testid="stExpander"] summary svg                   { display: none !important; }

[data-testid="stExpander"] summary:hover { background: #EDEDE8 !important; }
[data-testid="stExpander"] > div > div {
    background: var(--white) !important;
    padding: 14px !important;
}
.stCaption {
    font-family: var(--font-mono) !important;
    font-size: 11px !important;
    color: var(--blue) !important;
    background: var(--blue-light) !important;
    padding: 2px 8px !important;
    border-radius: 4px !important;
    display: inline-block !important;
    font-weight: 500 !important;
}
hr { border-top: 1px solid var(--divider) !important; margin: 12px 0 !important; }

/* ══════════════════════════════════════════════
   CHAT INPUT
══════════════════════════════════════════════ */
[data-testid="stChatInput"] {
    background: var(--white) !important;
    border-top: 2px solid var(--divider) !important;
    padding: 14px 28px 18px !important;
}
[data-testid="stChatInput"] textarea {
    background: var(--cream) !important;
    border: 1.5px solid var(--divider) !important;
    border-radius: var(--r-md) !important;
    color: var(--ink) !important;
    font-family: var(--font-body) !important;
    font-size: 14px !important;
    padding: 12px 17px !important;
    line-height: 1.6 !important;
    transition: border-color 0.2s, box-shadow 0.2s, background 0.15s !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: var(--blue) !important;
    background: var(--white) !important;
    box-shadow: 0 0 0 3px rgba(41,98,196,0.08) !important;
    outline: none !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: var(--muted) !important;
    font-style: italic !important;
    font-weight: 300 !important;
}
[data-testid="stChatInput"] button {
    background: var(--blue) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    transition: background 0.15s, transform 0.1s !important;
}
[data-testid="stChatInput"] button:hover {
    background: var(--blue-mid) !important;
    transform: scale(1.06) !important;
}

/* ══════════════════════════════════════════════
   MISC
══════════════════════════════════════════════ */
.stSpinner > div { border-top-color: var(--blue) !important; }
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--divider); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #C8C8DC; }
.divider-line { height: 1px; background: var(--divider); margin: 0; }
</style>
""", unsafe_allow_html=True)

# ── Session State ──────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Welcome 👋 I'm your AI assistant. Ask me about election results, inflation targets, GDP projections, or budget insights."
        }
    ]

# ══════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-chip">🎓 CS4241 · ACity · 2026</div>
        <div class="sb-title">Kobina Opei's<br>AI Assistant</div>
        <div class="sb-sub">Academic City University<br>RAG Intelligence Platform</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-sec" style="padding-top:14px;padding-bottom:10px;">', unsafe_allow_html=True)
    if st.button("↺  New Conversation"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Conversation reset. What would you like to know?"
        }]
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sb-sec">
        <span class="sb-lbl">Try asking</span>
        <div class="sb-q"><span class="sb-q-icon">🗳</span><span class="sb-q-text">Who won Ghana's 2020 presidential election?</span></div>
        <div class="sb-q"><span class="sb-q-icon">📈</span><span class="sb-q-text">What is the inflation target for 2025?</span></div>
        <div class="sb-q"><span class="sb-q-icon">💹</span><span class="sb-q-text">What is the projected GDP growth for 2025?</span></div>
        <div class="sb-q"><span class="sb-q-icon">🏛</span><span class="sb-q-text">Which party dominated the Ashanti Region?</span></div>
    </div>
    <div class="sb-sec">
        <span class="sb-lbl">System</span>
        <div class="sb-stat"><span class="sb-stat-l">Knowledge Base</span><span class="sb-stat-r">2 sources</span></div>
        <div class="sb-stat"><span class="sb-stat-l">Retrieval</span><span class="sb-stat-r">Top-K RAG</span></div>
        <div class="sb-stat"><span class="sb-stat-l">Generator</span><span class="sb-stat-r">OpenAI</span></div>
        <div class="sb-stat"><span class="sb-stat-l">Memory</span><span class="sb-stat-r">Persistent</span></div>
    </div>
    <div class="sb-sec">
        <span class="sb-lbl">Capabilities</span>
        <div class="sb-stat"><span class="sb-stat-l">Faster decisions</span><span style="font-size:14px;color:#22C55E!important">✓</span></div>
        <div class="sb-stat"><span class="sb-stat-l">No manual search</span><span style="font-size:14px;color:#22C55E!important">✓</span></div>
        <div class="sb-stat"><span class="sb-stat-l">High precision</span><span style="font-size:14px;color:#22C55E!important">✓</span></div>
        <div class="sb-stat"><span class="sb-stat-l">Source-grounded</span><span style="font-size:14px;color:#22C55E!important">✓</span></div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# PAGE HEADER
# ══════════════════════════════════════════════
st.markdown("""
<div class="ph">
    <div>
        <div class="ph-eyebrow">
            <span class="ph-eyebrow-bar"></span>
            Academic City University &nbsp;·&nbsp; Introduction to AI
        </div>
        <div class="ph-title">Kobina Opei's AI Assistant</div>
        <div class="ph-sub">
            A Retrieval-Augmented Generation platform for structured decision support —
            grounded answers drawn directly from Ghana election data and national budget reports.
        </div>
    </div>
    <div class="ph-badges">
        <div class="badge badge-live"><div class="live-dot"></div>System Online</div>
        <div class="badge badge-rag">RAG · Grounded</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# KPI STRIP  (uses st.columns for proper layout)
# ══════════════════════════════════════════════
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="kpi">
        <div class="kpi-ico k-gold">📚</div>
        <div><div class="kpi-lbl">Knowledge Sources</div><div class="kpi-val">2 Core Datasets</div></div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="kpi">
        <div class="kpi-ico k-blue">⚡</div>
        <div><div class="kpi-lbl">Response Model</div><div class="kpi-val">RAG + OpenAI</div></div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="kpi">
        <div class="kpi-ico k-green">💬</div>
        <div><div class="kpi-lbl">User Experience</div><div class="kpi-val">Persistent Chat</div></div>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# CHAT SECTION HEADER
# ══════════════════════════════════════════════
st.markdown("""
<div class="chat-hdr">
    <div class="chat-hdr-title">
        <div class="chat-hdr-bar"></div>
        Conversation
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# MESSAGES
# ══════════════════════════════════════════════
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ══════════════════════════════════════════════
# INPUT & RESPONSE LOGIC  (unchanged)
# ══════════════════════════════════════════════
user_question = st.chat_input("Ask about elections, budget targets, or economic policy...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            try:
                docs, scores = retrieve_documents(user_question)
                prompt = build_prompt(user_question, docs)
                answer = generate_response(prompt)
            except Exception as e:
                docs, scores = [], []
                answer = f"System Error: {str(e)}"

        st.markdown(answer)

        if docs:
            with st.expander(f"📄  {len(docs)} Source Chunk{'s' if len(docs) != 1 else ''} Retrieved  —  These are the document passages the answer was built from"):
                for i, (doc, score) in enumerate(zip(docs, scores), 1):
                    st.markdown(f"**Chunk {i}**")
                    st.write(doc)
                    st.caption(f"Similarity Score: {score:.4f}")
                    if i < len(docs):
                        st.divider()

    st.session_state.messages.append({"role": "assistant", "content": answer})