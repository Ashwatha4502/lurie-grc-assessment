import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Lurie Children's Hospital GRC Assessment",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Lurie Children's Hospital — GRC Risk Dashboard")
st.caption("NIST CSF 2.0 | HIPAA | Medical Device OT Risk | January 2024 Rhysida Ransomware Attack")

# --- Load risk register ---
@st.cache_data
def load_risks():
    return pd.read_csv('/home/kali/lurie-grc-assessment/data/risk_register.csv')

df = load_risks()

# --- Metrics ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Risks Identified", len(df))
col2.metric("Critical Risks", len(df[df["Priority"] == "Critical"]), delta="Immediate action required")
col3.metric("Individuals Affected", "791,784", delta="PHI sold on darkweb")
col4.metric("EHR Downtime", "4 Months", delta="Jan 31 - May 20 2024")

st.divider()

# --- NIST CSF Maturity ---
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("📊 NIST CSF 2.0 Maturity Scores")
    nist_data = pd.DataFrame([
        {'Function': 'GOVERN', 'Score': 1.5, 'Rating': 'Critical'},
        {'Function': 'IDENTIFY', 'Score': 1.5, 'Rating': 'Critical'},
        {'Function': 'PROTECT', 'Score': 1.5, 'Rating': 'Critical'},
        {'Function': 'DETECT', 'Score': 1.0, 'Rating': 'Critical'},
        {'Function': 'RESPOND', 'Score': 2.0, 'Rating': 'High'},
        {'Function': 'RECOVER', 'Score': 1.5, 'Rating': 'Critical'},
    ])
    fig = px.bar(nist_data, x='Function', y='Score',
                 color='Rating',
                 color_discrete_map={'Critical': '#e74c3c', 'High': '#f39c12'},
                 range_y=[0, 5],
                 title='Maturity Score by CSF Function (out of 5)')
    fig.add_hline(y=3, line_dash="dash", line_color="green",
                  annotation_text="Target Maturity")
    fig.update_layout(height=350, paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🎯 Risk Priority Breakdown")
    priority_counts = df['Priority'].value_counts().reset_index()
    priority_counts.columns = ['Priority', 'Count']
    fig2 = px.pie(priority_counts, values='Count', names='Priority',
                  color='Priority',
                  color_discrete_map={
                      'Critical': '#e74c3c',
                      'High': '#f39c12',
                      'Medium': '#3498db'
                  },
                  hole=0.4)
    fig2.update_layout(height=350, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# --- Attack Timeline ---
st.subheader("📅 Breach Timeline")
timeline_data = pd.DataFrame([
    {'Date': 'Jan 26', 'Event': 'Initial Access', 'Severity': 5, 'Description': 'Rhysida gains unauthorized access to network'},
    {'Date': 'Jan 26-31', 'Event': 'Dwell Time', 'Severity': 5, 'Description': '5 days undetected — PHI exfiltrated'},
    {'Date': 'Jan 31', 'Event': 'Detection', 'Severity': 4, 'Description': 'Breach detected — all systems taken offline'},
    {'Date': 'Feb 1', 'Event': 'Public Disclosure', 'Severity': 3, 'Description': 'Hospital announces cybersecurity incident'},
    {'Date': 'Feb 7', 'Event': 'FBI Confirms', 'Severity': 3, 'Description': 'FBI confirms investigation of incident'},
    {'Date': 'Feb 27', 'Event': 'Rhysida Claims', 'Severity': 4, 'Description': 'Rhysida lists Lurie on darkweb — demands $3.4M'},
    {'Date': 'Mar 5', 'Event': 'EHR Partial Restore', 'Severity': 2, 'Description': 'Epic EHR partially restored after 33 days'},
    {'Date': 'Mar 8', 'Event': 'Data Sold', 'Severity': 5, 'Description': 'Rhysida claims all data sold on darkweb'},
    {'Date': 'May 20', 'Event': 'Full Recovery', 'Severity': 1, 'Description': 'All patient-facing systems reactivated'},
    {'Date': 'Jul 2024', 'Event': 'Breach Notification', 'Severity': 3, 'Description': '791,784 individuals notified — 6 months late'},
])
fig3 = px.scatter(timeline_data, x='Date', y='Severity', size='Severity',
                  color='Severity', text='Event',
                  color_continuous_scale='Reds',
                  title='Breach Event Timeline — Severity by Phase',
                  size_max=30)
fig3.update_traces(textposition='top center')
fig3.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)',
                   plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# --- Risk Register ---
st.subheader("📋 Risk Register")
priority_filter = st.multiselect("Filter by Priority",
    options=['Critical', 'High', 'Medium'],
    default=['Critical', 'High'])

filtered = df[df['Priority'].isin(priority_filter)]
st.dataframe(
    filtered[['Risk_ID', 'Category', 'Threat', 'Likelihood', 'Impact',
              'Risk_Score', 'HIPAA_Rule', 'Priority', 'Recommended_Control']],
    use_container_width=True, hide_index=True
)

st.divider()

# --- HIPAA Compliance ---
st.subheader("⚖️ HIPAA Compliance Summary")
hipaa_data = pd.DataFrame([
    {'Safeguard': 'Administrative', 'Compliant': 2, 'Non-Compliant': 5, 'Partial': 1},
    {'Safeguard': 'Physical', 'Compliant': 1, 'Non-Compliant': 2, 'Partial': 1},
    {'Safeguard': 'Technical', 'Compliant': 1, 'Non-Compliant': 5, 'Partial': 1},
])
fig4 = px.bar(hipaa_data, x='Safeguard',
              y=['Compliant', 'Partial', 'Non-Compliant'],
              color_discrete_map={
                  'Compliant': '#2ecc71',
                  'Partial': '#f39c12',
                  'Non-Compliant': '#e74c3c'
              },
              barmode='stack',
              title='HIPAA Safeguard Compliance by Category')
fig4.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)',
                   plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.caption("Assessment by Ashwatha Narayan | NIST CSF 2.0 | HIPAA | IEC 62443 | May 2026 | GitHub: github.com/Ashwatha4502")
# hipaa compliance panel
