# Taste

## Resume tailoring workflow (Chapter4_Jobkit_AI)
- For resume-tailoring tasks (job description + resume → tailored versions), expects multiple tailored versions per company, with filenames embedding company name, role, version, and angle (e.g., `Resume_Insperity_AutomationEngineer_v1_ATS.csv`), written to an `output` folder in the Chapter4 project. Confidence: 0.7
- Wants tailored resume deliverables in PDF format as the final output — explicitly asked to delete the generated `.csv` files and produce clean PDFs instead (one per resume); Markdown/CSV serve as intermediate steps, and the output folder should not keep formats the user has asked to remove. Confidence: 0.8
- Supplies input files (resume PDF, job-description docx) as absolute Windows paths outside the project workspace (e.g., `c:\Users\hp\Downloads\...`, `c:\Users\hp\Documents\...`); expects the agent to verify and read them from those exact paths. Confidence: 0.7
- Wants contact details (name, job title, phone, LinkedIn, email) carried into every tailored resume output. Confidence: 0.6
