# Taste
- Uses structured, role-based prompts (RICEPOT format: Role, Instructions, Context, Example, Parameters, Output, Tone) when requesting AI-generated code. Confidence: 0.9
- Marks requirements with explicit constraint tags ([Critical], [Mandatory], [Don't], [Generate], [Output]) to make specifications unambiguous. Confidence: 0.9
- Values enterprise-grade, production-quality code with "zero bad coding practices" — dislikes code comments, Thread.sleep, and hardcoded values. Confidence: 0.9
- Prefers generated code output strictly limited to the exact files and content requested (e.g., only 1 Page Object, 2 TestNG scripts, Maven project) — runnable code only, no explanations, comments, or extra files. Confidence: 0.8
- Wants a written plan (e.g., a test plan) as an intermediate deliverable for complex tasks, and reviews/approves it before implementation proceeds; after approval, gives an explicit execute command (e.g., "go for it") to trigger implementation. Confidence: 0.8
- Expects completed code to be committed and pushed to a GitHub repository as part of delivery (gives an explicit "commit the code and push it to <repo>" instruction when done). Confidence: 0.8
- Works on Windows (cmd.exe / PowerShell 5.1); bash-only shell syntax (heredocs, `<<<`) is unavailable — use `git commit -F` with a temp message file or PowerShell-compatible commands instead. Confidence: 0.8
- Practices careful git hygiene when setting up a repository: creates a `.gitignore` excluding build artifacts (target/, test-output/, screenshots), IDE files, and credential-containing configs; writes descriptive commit messages; and verifies the working tree is clean and up to date after pushing. Confidence: 0.8
