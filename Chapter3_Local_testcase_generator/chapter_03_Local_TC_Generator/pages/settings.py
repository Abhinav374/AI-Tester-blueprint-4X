import streamlit as st

import config_store
import jira_client
import llm_client

st.set_page_config(page_title="Settings")

cfg = config_store.read_config()

st.title("⚙️ Settings")

with st.form("settings_form"):
    st.subheader("Jira")
    jira_url = st.text_input("Jira base URL", value=cfg.get("JIRA_URL", ""))
    jira_email = st.text_input("Jira email ID", value=cfg.get("JIRA_EMAIL", ""))
    jira_token = st.text_input("Jira API token", value=cfg.get("JIRA_API_TOKEN", ""), type="password")

    st.subheader("LLM Provider")
    provider = st.selectbox(
        "Default provider",
        options=["ollama", "groq"],
        index=0 if cfg.get("PROVIDER") != "groq" else 1,
        help="Ollama is used by default and falls back to Groq if it is unavailable.",
    )

    st.subheader("Groq (fallback)")
    groq_key = st.text_input("Groq API key", value=cfg.get("GROQ_API_KEY", ""), type="password")

    st.subheader("Model / Endpoint")
    ollama_url = st.text_input("Ollama URL", value=cfg.get("OLLAMA_URL", "http://localhost:11434"))
    ollama_model = st.text_input("Ollama model", value=cfg.get("OLLAMA_MODEL", "gemma3:1b"))
    groq_model = st.text_input("Groq model", value=cfg.get("GROQ_MODEL", "openai/gpt-oss-20b"))

    submitted = st.form_submit_button("Save settings", type="primary")

if submitted:
    config_store.write_config(
        {
            "JIRA_URL": jira_url.strip(),
            "JIRA_EMAIL": jira_email.strip(),
            "JIRA_API_TOKEN": jira_token.strip(),
            "PROVIDER": provider,
            "GROQ_API_KEY": groq_key.strip(),
            "OLLAMA_URL": ollama_url.strip(),
            "OLLAMA_MODEL": ollama_model.strip(),
            "GROQ_MODEL": groq_model.strip(),
        }
    )
    st.success("Settings saved.")


st.divider()
st.subheader("Connection tests")

col1, col2 = st.columns(2)

with col1:
    if st.button("Test Jira connection"):
        if not all([cfg["JIRA_URL"], cfg["JIRA_EMAIL"], cfg["JIRA_API_TOKEN"]]):
            st.error("Jira credentials are incomplete.")
        else:
            try:
                ticket = jira_client.fetch_ticket(
                    cfg["JIRA_URL"], cfg["JIRA_EMAIL"], cfg["JIRA_API_TOKEN"], "KAN-1"
                )
                st.success(f"Jira OK — fetched {ticket['key']}: {ticket['summary']}")
            except jira_client.JiraError as exc:
                st.error(str(exc))

with col2:
    if st.button("Test Groq connection"):
        if not cfg.get("GROQ_API_KEY"):
            st.error("Groq API key is missing.")
        else:
            try:
                result = llm_client._call_groq("Reply with the single word: OK", cfg)
                st.success(f"Groq OK — {result.strip()[:120]}")
            except Exception as exc:  # noqa: BLE001
                st.error(str(exc))