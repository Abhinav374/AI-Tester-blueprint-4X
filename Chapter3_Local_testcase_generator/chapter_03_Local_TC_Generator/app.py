import re
from pathlib import Path

import streamlit as st

import config_store
import jira_client
import llm_client

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "templates" / "testcase_creator.md"

# Matches standard Jira keys like KAN-1, JIRA-102, PROJ-42
TICKET_KEY_RE = re.compile(r"\b[A-Z][A-Z0-9]*-\d+\b")

st.set_page_config(page_title="RICE-POT", page_icon="🍚")
st.title("🍚 RICE-POT — Jira Test Case Generator")


def load_template() -> str:
    if not TEMPLATE_PATH.exists():
        st.error(f"Template not found at {TEMPLATE_PATH}")
        st.stop()
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def build_prompt(template: str, ticket: dict) -> str:
    requirements = (
        f"Ticket: {ticket['key']}\n"
        f"Summary: {ticket['summary']}\n"
        f"Description:\n{ticket['description'] or '(not specified)'}\n"
        f"Acceptance Criteria:\n{ticket['acceptance_criteria'] or '(not specified)'}"
    )
    return template.replace("[PASTE REQUIREMENTS HERE]", requirements)


def is_configured(cfg: dict) -> bool:
    return bool(cfg.get("JIRA_URL") and cfg.get("JIRA_EMAIL") and cfg.get("JIRA_API_TOKEN"))


# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role": "assistant", "content": "Hi! Ask me to create test cases for a Jira ticket, e.g. `create test cases for KAN-1`."}
    ]

cfg = config_store.read_config()

if not is_configured(cfg):
    st.warning("Jira credentials are not set. Go to **Settings** to configure them.")
    st.page_link("pages/settings.py", label="Open Settings")

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me to create test cases for a Jira ticket..."):
    st.session_state.chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    match = TICKET_KEY_RE.search(prompt)
    if not match:
        with st.chat_message("assistant"):
            st.warning("I couldn't find a Jira key in your message (e.g. `KAN-1`).")
        st.session_state.chat.append(
            {"role": "assistant", "content": "No valid Jira key found."}
        )
        st.stop()

    ticket_key = match.group(0)
    with st.chat_message("assistant"):
        with st.status(f"Fetching {ticket_key}…", expanded=True) as status:
            try:
                ticket = jira_client.fetch_ticket(
                    cfg["JIRA_URL"], cfg["JIRA_EMAIL"], cfg["JIRA_API_TOKEN"], ticket_key
                )
                status.write(f"**{ticket['summary']}**")

                template = load_template()
                status.write("Loaded template, building prompt…")
                prompt_text = build_prompt(template, ticket)

                status.write(f"Calling provider **{cfg.get('PROVIDER', 'ollama')}**…")
                output = llm_client.generate(prompt_text, cfg)
                status.update(label="Done", state="complete")
            except jira_client.JiraError as exc:
                st.error(str(exc))
                st.session_state.chat.append(
                    {"role": "assistant", "content": f"⚠️ {exc}"}
                )
                st.stop()
            except llm_client.LLMError as exc:
                st.error(str(exc))
                st.session_state.chat.append(
                    {"role": "assistant", "content": f"⚠️ LLM error: {exc}"}
                )
                st.stop()
            except Exception as exc:  # noqa: BLE001 - surface anything to the UI
                st.error(f"Unexpected error: {exc}")
                st.session_state.chat.append(
                    {"role": "assistant", "content": f"⚠️ Unexpected error: {exc}"}
                )
                st.stop()

        st.markdown(output)
        st.session_state.chat.append({"role": "assistant", "content": output})