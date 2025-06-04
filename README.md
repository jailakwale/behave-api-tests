# Behave API Testing Project

This project uses [Behave](https://behave.readthedocs.io/en/stable/) — a Python BDD (Behavior-Driven Development) framework — to test RESTful API endpoints using human-readable Gherkin syntax.

### 🧪 Features

- Written in **Gherkin** for clear, readable test scenarios
- Step definitions using **Python + requests**
- Tests public API: [https://reqres.in](https://reqres.in)
- Easily extensible for any RESTful API

---

### 🚀 Getting Started

# 1. Clone the repo
```bash
git clone https://github.com/jailakwale/behave-api-tests.git
cd behave-api-tests
```
# 2. Create and activate the virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
# 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 4. Run the tests
```bash
behave
```

## Project Structure

<pre>
<code>
```

behave_api_test/
├── features/
│   ├── steps/
│   │   └── api_steps.py
│   ├── example.feature
│   └── environment.py
├── utils/
│   └── api_helpers.py
├── behave.ini
├── .gitignore
├── requirements.txt
└── README.md

```
<code>
<pre>


🛠 Dependencies
	•	Python 3.7+
	•	Behave
	•	Requests

⸻

📬 Contact

Created by @jailakwale
Feel free to contribute or raise issues!


