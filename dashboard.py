import json
import os

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="AgentArmor Dashboard",
    layout="wide"
)

st.title("🛡️ AgentArmor Dashboard")

REPORT_PATH = "reports/latest_report.json"

if not os.path.exists(REPORT_PATH):
    st.warning("No benchmark report found.")
    st.stop()

with open(REPORT_PATH) as f:
    report = json.load(f)

df = pd.DataFrame(report)

st.metric(
    "Tests Executed",
    len(df)
)

st.metric(
    "Average Score",
    round(df["score"].mean(), 2)
)

passed = int(df["passed"].sum())

failed = len(df) - passed

col1, col2 = st.columns(2)

with col1:
    st.metric("Passed", passed)

with col2:
    st.metric("Failed", failed)

st.subheader("Attack Results")

st.dataframe(df)

st.subheader("Average Score by Attack")

attack_scores = (
    df.groupby("attack_name")["score"]
    .mean()
    .reset_index()
)

st.bar_chart(
    attack_scores.set_index(
        "attack_name"
    )
)

st.subheader("Raw JSON")

st.json(report)