import requests


class JiraError(Exception):
    """Raised when a Jira ticket cannot be fetched."""


def fetch_ticket(base_url: str, email: str, api_token: str, key: str) -> dict:
    """Fetch summary, description, and acceptance criteria for a Jira issue."""
    # API v3 is the current Jira Cloud API. Some accounts still serve v2; fall back if needed.
    url = f"{base_url.rstrip('/')}/rest/api/3/issue/{key.strip()}"
    auth = (email, api_token)
    params = {"fields": "summary,description,issuetype,customfield_10020"}

    try:
        resp = requests.get(url, auth=auth, params=params, timeout=30)
    except requests.RequestException as exc:
        raise JiraError(f"Could not reach Jira: {exc}") from exc

    if resp.status_code == 404:
        raise JiraError(f"Ticket '{key}' not found on this Jira instance.")
    if resp.status_code == 401:
        raise JiraError("Jira authentication failed. Check email and API token.")
    if resp.status_code != 200:
        raise JiraError(f"Jira request failed: HTTP {resp.status_code} — {resp.text[:300]}")

    fields = resp.json().get("fields", {})

    def _clean_text(value):
        if value is None:
            return ""
        # ADF (Atlassian Document Format) descriptions come as nested content arrays
        if isinstance(value, dict):
            text = []
            for node in value.get("content", []):
                for para in node.get("content", []):
                    if para.get("type") == "text":
                        text.append(para.get("text", ""))
            return "\n".join(text).strip()
        return str(value).strip()

    return {
        "key": key.strip(),
        "summary": _clean_text(fields.get("summary")),
        "description": _clean_text(fields.get("description")),
        # Replace with the real Accept Criteria field id for your Jira instance
        "acceptance_criteria": _clean_text(fields.get("customfield_10020")),
    }