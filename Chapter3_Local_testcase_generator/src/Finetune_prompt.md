# RICE-POT Prompt — Jira Test Case Generator App

## Role
You are a senior Python full-stack engineer and AI application architect, experienced in building lightweight internal tools with Streamlit, integrating REST APIs (Jira Cloud/Server), and orchestrating LLM backends across local (Ollama) and hosted (Groq) providers with automatic fallback logic.

## Instructions
[Mandatory] Build a **two-screen Streamlit application**:
- **Screen 1 — Chat**: A ChatGPT-style interface with a text input box and a Send button. The user types natural-language requests such as "create test cases for JIRA-102" and clicks Send.
- **Screen 2 — Settings**: A configuration screen to input and persist: Jira URL, Jira email ID, Jira API token, LLM provider choice (Ollama / Groq), and Groq API key.

[Critical] Default LLM backend is **Ollama**, running locally, model `gemma3:1b`, connecting to the existing local Ollama server (`http://localhost:11434`). Do not re-pull or re-download the model — assume it is already present.

[Mandatory] Provide a **fallback to Groq** (groq.com) when Ollama is unavailable or the user explicitly opts out. The Groq API key is read from the Settings screen, never hardcoded.

[Mandatory] End-to-end flow when the user requests test cases for a Jira ID:
1. Parse the Jira ticket key from the chat message.
2. Fetch ticket details (summary, description, acceptance criteria) via the Jira REST API using the stored credentials.
3. Load the test case template from a local `/templates` folder.
4. Generate test cases with the selected LLM, using the fetched ticket content merged into the template structure.
5. Render the generated test cases back in the chat pane.

[Don't] Don't hardcode any credentials (Jira token, Groq key) in source code — persist them via a local config layer (e.g. JSON file or SQLite), excluded from version control.

[Don't] Don't call Groq unless Ollama is unavailable or the user has explicitly selected it as the provider.

[Output] **Plan first.** Before writing any code, output the proposed file structure, the two screens, and the data flow between them. Wait for my approval. Only then build step by step, one module at a time.

## Context
This is an internal QA productivity tool, not a production SaaS product. It exists to take a single Jira ticket and turn it into a test case draft, using either a small local model or a hosted fallback, with minimal setup and no unnecessary abstraction.

## Example
Sample interaction:
> User types: `create test cases for KAN-1` → clicks Send
> App fetches ticket KAN-1 from Jira → merges its description/acceptance criteria into the template from `/templates` → sends the combined prompt to Ollama (or Groq, if selected) → renders the structured test cases in the chat pane, the same way a ChatGPT response would appear.

## Parameters
- Jira base URL, Jira email ID, Jira API token — provided separately, entered/saved via the Settings screen
- Ollama endpoint (`http://localhost:11434`) and model tag (`gemma3:1b`) — already running locally
- Groq API key — provided separately, entered/saved via the Settings screen, used only as fallback

## Output
Deliver exactly:
- `app.py` — main chat screen
- `pages/settings.py` (or equivalent Streamlit multipage settings screen)
- `config_store.py` — handles reading/writing persisted settings (Jira + Groq credentials, provider choice)
- `jira_client.py` — fetches ticket details from Jira REST API
- `llm_client.py` — handles both Ollama and Groq calls, with fallback logic between them
- `templates/` — folder with at least one sample test case template
- `requirements.txt`

## Tone
Technical, precise, minimal dependencies, no over-engineered abstractions — working code only, structured clearly enough that each module can be reviewed independently before moving to the next.