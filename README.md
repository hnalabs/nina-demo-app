🕸️ Nina — Structured Case Assistant for Scam Victims

Nina is an AI-powered assistant built to help victims of financial scams organize their story into a full legal-grade casefile — calmly, carefully, and respectfully.

This app is part of the FiCAP project by Eight Legged Forensics, designed to turn chaos into structure, and pain into power.

⸻

📦 Folder Structure
```bash
/nina-app
  ├── app.py           # Streamlit frontend
  ├── nina_chain.py     # LangChain backend (v0.3.x upgraded)
  ├── prompt.txt        # Final master prompt for Nina's system behavior
  └── requirements.txt  # Dependency list
```


⸻

## 🚀 Launch Instructions

**1.	Install dependencies:**

```bash
pip install -r requirements.txt
```


**2.	Start the app:**

```bash
streamlit run app.py
```


✅ Nina will be fully live, operating only based on the master forensic-empathetic prompt.

⸻

🧠 Key Features:
- Master Prompt Controlled: Nina’s behavior is governed entirely by a transparent, auditable system prompt (prompt.txt).
- Modern LangChain 0.3 Architecture: Built with modular Runnables, ChatPromptTemplates, and future-proof memory handling.
- Structured Forensic Outputs: Nina organizes all user inputs into a clean, prosecutable structure: timeline, evidence, emotional manipulation tags.
- Emotionally Intelligent: Carefully balances forensic precision with empathy and user empowerment.
- Streamlit UI (v1.32+): Ultra-clean, distraction-free chat interface.

⸻

📜 Nina’s Guiding Principles
- Consent First: Always ask before processing sensitive data.
- Timeline Anchoring: Every event is connected to a date or timeframe.
- Flexible Evidence Handling: Smart detection and respectful prompts for uploads (documents, audio, images).
- Mid-Session Reassurance: Encourages user strength, validates courage.
- Structured Saving: Every detail is added to a final casefile draft — ready for export.
- Privacy and Trust: No data sharing, selling, or exploitation.

⸻

🔧 Tech Stack
```
Component	Version
Streamlit	1.32.0+
LangChain	0.3.0+
LangChain-OpenAI	0.0.7+
OpenAI SDK	1.14.3+
Python-Dotenv	1.0.1+
Tiktoken	0.6.0+
```


⸻

⚙️ Future Enhancements (Optional)

If desired, Nina can be easily expanded with:
- 📅 Timeline visualization (inside Streamlit)
- 📂 Evidence upload with live forensic hashing
- 📥 Downloadable casefile drafts (JSON export)
- 📜 PDF structured reports for prosecutors

Just say “Yes, timeline + evidence upload + download casefile too!” to activate expansion features.

⸻

🎯 Mission Statement

> Help victims turn chaos into structure.
> Help them move from pain into power — one small, respectful step at a time.
> Deliver structure without exploitation. Deliver hope without hype.

⸻

🕸️ Structured truth defeats organized deception.
Powered by FiCAP and Eight Legged Forensics.

⸻
