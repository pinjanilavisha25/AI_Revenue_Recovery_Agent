import pandas as pd
import streamlit as st
import time
from datetime import datetime

# 1. Page Configuration & Styling
st.set_page_config(
    page_title="AI Revenue Recovery Agent - Enterprise Edition", 
    page_icon="💸", 
    layout="wide"
)

st.title("💸 AI Revenue Recovery Agent (Enterprise Dashboard)")
st.markdown("Autonomous system that detects revenue at risk, enforces financial guardrails, routes exceptions, and executes bounded recovery workflows.")

# 2. Sidebar Configuration & Guardrail Controls
st.sidebar.header("⚙️ Agent Policy & Guardrails")
min_recovery_floor = st.sidebar.number_input("Min Amount Floor (₹) [Skip Micro-Txns]", value=2000, step=500)
auto_approve_high_value = st.sidebar.checkbox("Auto-Approve High Value (>₹20k) Routing", value=True)

st.sidebar.markdown("---")
st.sidebar.info(
    "**Enterprise Architecture Features:**\n"
    "• Deterministic Policy Guardrails\n"
    "• Structured Audit Trail & Timestamping\n"
    "• Human Escalation Exception Queue\n"
    "• Visual Analytics & Breakdown Charts"
)

# 3. Load Dataset Function
@st.cache_data
def load_data():
    return pd.read_csv("transactions.csv")

try:
    df = load_data()
except Exception as e:
    st.error("⚠️ Error: Could not find 'transactions.csv'. Please make sure it is saved in the same directory as app.py.")
    st.stop()

# Ensure unique transaction ID mapping if not present
if 'transaction_id' not in df.columns:
    df.insert(0, 'transaction_id', [f"TXN_{1000 + i}" for i in range(len(df))])

# 4. Overview Metrics Dashboard
st.subheader("📊 Portfolio Overview: Revenue at Risk")
total_risk_amount = df['amount'].sum()
total_records = len(df)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Monitored Records", value=f"{total_records} Txns")
with col2:
    st.metric(label="Total Revenue at Risk", value=f"₹{total_risk_amount:,.2f}")
with col3:
    st.metric(label="Policy Threshold Floor", value=f"₹{min_recovery_floor:,}")

with st.expander("🔍 View Raw Failed Transactions Dataset"):
    st.dataframe(df, use_container_width=True)

# 5. Advanced Autonomous Agent Execution Engine with Guardrails
def run_enterprise_agent(row, floor_limit):
    reason = str(row['failure_reason']).lower()
    name = row['name']
    amount = row['amount']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Policy Guardrail Check: Check economic viability floor
    if amount < floor_limit:
        return {
            "Status": "Skipped (Below Floor)",
            "Action Recommended": "No Action (Cost Inefficient)",
            "Audit Rationale": f"Transaction amount ₹{amount} is below threshold floor (₹{floor_limit}). Saved gateway fee overhead.",
            "Timestamp": timestamp,
            "Queue": "Ignored"
        }
    
    # Exception Handling & Escalation Check
    if "cvv" in reason or "expired" in reason or amount > 25000:
        return {
            "Status": "Escalated",
            "Action Recommended": "Manual Support Escalation",
            "Audit Rationale": f"High risk anomaly detected ({row['failure_reason']}) or high-value ticket. Routed to human operations queue.",
            "Timestamp": timestamp,
            "Queue": "Human Review"
        }
    
    # Standard Automated Workflows
    if "insufficient" in reason or "declined" in reason:
        action = "Automated Discount Offer (SAVE10)"
        message = f"Hi {name}, payment of ₹{amount} failed due to bank decline. Use code SAVE10 for instant retry."
    elif "timeout" in reason or "server down" in reason or "network" in reason:
        action = "Instant UPI Retry Link"
        message = f"Hi {name}, transaction of ₹{amount} hit a network glitch. Click here for direct 1-click UPI recovery."
    else:
        action = "Checkout Recovery Cart Link"
        message = f"Hi {name}, your checkout cart worth ₹{amount} was left incomplete. Complete your payment now."
        
    return {
        "Status": "Resolved / Executed",
        "Action Recommended": action,
        "Audit Rationale": f"Successful automated policy match for failure profile: '{row['failure_reason']}'. Message synthesized.",
        "Timestamp": timestamp,
        "Queue": "Automated"
    }

# 6. Trigger Scan Button
st.markdown("---")
if st.button("🚀 Run Autonomous Agent Recovery Loop", type="primary"):
    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    total_rows = len(df)

    for index, row in df.iterrows():
        status_text.text(f"Executing agent logic for {row['transaction_id']} ({row['name']})...")
        time.sleep(0.01) # Smooth progress visual
        
        agent_output = run_enterprise_agent(row, min_recovery_floor)
        
        results.append({
            "Transaction ID": row['transaction_id'],
            "Customer Name": row['name'],
            "Amount (₹)": row['amount'],
            "Failure Reason": row['failure_reason'],
            "Days Overdue": row['days_overdue'],
            "Execution Status": agent_output["Status"],
            "Action Recommended": agent_output["Action Recommended"],
            "Audit Rationale": agent_output["Audit Rationale"],
            "Queue Routing": agent_output["Queue"],
            "Timestamp": agent_output["Timestamp"]
        })
        
        progress_bar.progress((index + 1) / total_rows)

    status_text.text("✅ Autonomous pipeline execution complete!")
    progress_bar.empty()

    st.success("🎉 Enterprise Revenue Recovery Scan finished successfully across all layers!")
    
    result_df = pd.DataFrame(results)
    
    # 7. Comprehensive Presentation Tables & Audit Logs
    st.subheader("🎯 Structured Audit Trail & Execution Log")
    st.dataframe(result_df, use_container_width=True)
    
    # Split Queues for Human Review vs Automated
    st.markdown("### 🗂️ Workflow Queue Segregation")
    q_col1, q_col2 = st.columns(2)
    
    with q_col1:
        st.markdown("#### 🤖 Automated Recovery Queue")
        auto_df = result_df[result_df["Queue Routing"] == "Automated"]
        st.dataframe(auto_df[["Transaction ID", "Customer Name", "Amount (₹)", "Action Recommended"]], use_container_width=True)
        
    with q_col2:
        st.markdown("#### 👤 Human Support Escalation Queue")
        human_df = result_df[result_df["Queue Routing"] == "Human Review"]
        st.dataframe(human_df[["Transaction ID", "Customer Name", "Amount (₹)", "Failure Reason"]], use_container_width=True)

    # 8. Visual Analytics & Insights Charts
    st.markdown("### 📈 Visual Analytics & Impact Metrics")
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    resolved_count = len(result_df[result_df["Execution Status"] == "Resolved / Executed"])
    escalated_count = len(result_df[result_df["Execution Status"] == "Escalated"])
    skipped_count = len(result_df[result_df["Execution Status"] == "Skipped (Below Floor)"])
    
    with metric_col1:
        st.metric(label="Successfully Automated", value=f"{resolved_count} Txns")
    with metric_col2:
        st.metric(label="Escalated to Humans", value=f"{escalated_count} Txns")
    with metric_col3:
        st.metric(label="Guardrail Skipped", value=f"{skipped_count} Txns")

    # Failure Reason Distribution Chart
    st.markdown("#### 📉 Revenue Loss Distribution by Failure Categories")
    failure_chart_data = df.groupby('failure_reason')['amount'].sum().reset_index()
    failure_chart_data = failure_chart_data.set_index('failure_reason')
    st.bar_chart(failure_chart_data)

    # Download Reports Button
    csv_output = result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Compliance & Audit Report (CSV)",
        data=csv_output,
        file_name="enterprise_revenue_recovery_audit_report.csv",
        mime="text/csv",
    )