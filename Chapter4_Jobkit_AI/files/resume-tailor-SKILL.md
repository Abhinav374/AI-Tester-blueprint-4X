---
name: resume-tailor
description: Tailor a resume to a specific job description, producing 2-3 targeted variations as clean Markdown ready to paste into Google Docs. Use this whenever the user shares a job description — pasted as text/a list, or in an uploaded file (.xlsx, .csv, .docx, .pdf, .txt) — and wants a resume customized, optimized, updated, or matched to it. Trigger on phrases like "tailor my resume for this," "update my resume for this JD," "help me apply to this role," or when the user pastes a job posting and their intent to apply is clear, even if they don't explicitly ask for "multiple versions" — default to producing a few variations unless told otherwise.
---

# Resume Tailor

Turns a job description + the user's base resume into a small set of tailored resume
variations, each aimed at a different angle on the same job, so the user can pick the
one that reads best and paste it into Google Docs.

The two things that make this work well are (1) actually understanding what the job
is asking for before touching the resume, and (2) never inventing anything. Everything
below serves one of those two goals.

## Step 1: Gather the inputs

**The job description.** It might arrive as pasted text/a bullet list right in the
chat, or as an uploaded file. If it's a file:
- `.xlsx` / `.csv` → read the `xlsx` skill first, the JD is probably one row or one
  column of requirements rather than free text — don't assume the layout, inspect it.
- `.docx` → read the `docx` skill (or `file-reading` skill if content isn't already in
  context).
- `.pdf` → read the `pdf-reading` skill.
- Plain `.txt` you can just read directly.

**The base resume.** The user uploads this fresh each session — check
`/mnt/user-data/uploads` and the conversation for it. If it's not there, **stop and ask
for it before doing anything else.** Don't proceed on a remembered or assumed resume
from earlier in the conversation if it's genuinely absent — and never draft placeholder
or generic resume content to fill the gap. If the resume is a `.docx` or `.pdf`, use
the matching skill to read it accurately rather than skimming.

If either input is missing or too thin to work with (e.g. a job title with no other
detail), ask a single direct question to fill the gap rather than guessing — a resume
built on a guessed-at job description is worse than useless to the user.

## Step 2: Actually read the job description

Before touching the resume, work out:
- Job title, seniority level, and team/function
- Must-have hard skills, tools, and qualifications (the non-negotiables)
- Nice-to-haves / preferred qualifications
- The 3-5 core responsibilities that will matter most day-to-day
- Language and phrasing the posting repeats or emphasizes — this is very likely the
  exact vocabulary an ATS keyword filter or a hiring manager's skim will key on

You don't need to show this analysis to the user, but do it explicitly before writing
anything — it's the difference between a resume that's reworded and one that's
actually targeted.

## Step 3: Map the resume against it — honestly

Go through the resume's actual content and identify:
- Which existing bullets, roles, or projects are most relevant to this JD, and would
  benefit from being surfaced higher or expanded
- Which quantifiable results (numbers, scope, outcomes) in the resume speak to what
  this job cares about
- Genuine gaps — things the JD wants that the resume doesn't support

**Hard rule: never invent.** Don't add skills, tools, employers, titles, dates,
responsibilities, or metrics that aren't in the source resume, even to close an
obvious gap. Reframing, reordering, re-emphasizing, and rewording existing true
content is the entire toolkit here. If there's a real gap, it's fine to leave it —
that's more useful to the user than a resume that oversells them into an interview
they can't back up.

## Step 4: Produce 2-3 variations, each with a genuinely different angle

Not three copies with synonyms swapped — three resumes that make a different case for
the same person. Pick whichever 2-3 angles actually fit this JD and this resume; don't
force a third if there's no meaningfully different angle to offer, and say so instead
of padding. Common angles to choose from:

- **Keyword/ATS-aligned** — mirrors the JD's exact terminology where the resume
  genuinely supports it, reorders the skills section to match the JD's stated
  priorities. Best when the posting reads like it'll go through a keyword screen.
- **Achievement/metrics-led** — leads with quantified outcomes and impact, trims
  narrative description. Best for results-driven roles (sales, growth, ops).
- **Domain/responsibility-framed** — reframes the summary and bullet emphasis around
  the specific day-to-day responsibilities and domain of this job (e.g. leans
  leadership vs. individual-contributor, or reframes generalist experience into the
  target industry's language). Best when the resume's background is adjacent rather
  than a dead-on match.

Every variation still needs to be a complete, coherent, standalone resume — not a diff
or a set of suggestions.

## Step 5: Format for a clean paste into Google Docs

Since these get copied into Google Docs, keep the structure simple so it survives the
paste:
- Standard resume skeleton: name/contact line, professional summary, skills, experience
  (reverse chronological), education, and any certifications/projects worth keeping.
- Use `#`/`##` for headers and `-` for bullets — don't use tables, columns, or
  nested formatting. Google Docs pasting handles plain headers and bullets far more
  reliably than anything more elaborate.
- Tell the user to copy from the rendered preview (not raw text) when pasting, so the
  bold/headers carry over as real formatting in Docs rather than literal `**`/`#`
  characters.
- Keep to roughly one page's worth of content unless the source resume itself is
  clearly a multi-page/senior-level document — don't pad length to fill space.

## Step 6: Save, present, and explain

- Save each variation as its own file in `/mnt/user-data/outputs`, named descriptively:
  `Resume_<Company>_<JobTitle>_v1_<Angle>.md`, `..._v2_...`, etc. (omit `<Company>` if
  unknown).
- Use `present_files` to hand them over.
- Don't reprint the full resume text again in the chat — the files are the deliverable.
  After presenting, give a short per-version note (2-3 bullets each) covering: the
  angle it takes, and the specific changes made versus the source resume (what moved
  up, what got trimmed, what got reframed) — so the user knows what they're choosing
  between and can sanity-check the edits fast.
- If you spotted a real gap between the JD and the resume in Step 3 that no honest
  reframing could close, mention it briefly — that's useful signal for the user even
  if this skill can't fix it.
