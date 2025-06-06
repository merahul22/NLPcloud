



### ✅ `README.md`

````markdown
# 🧠 NLP Desktop App using Tkinter + NLPCloud API

This is a desktop application built using **Python**, **Tkinter**, and the **NLPCloud API**. It performs:

- ✅ Sentiment Analysis  
- ✅ Named Entity Recognition (NER)  
- ✅ Language Detection  
- 🧑‍💻 User Registration & Login using a custom JSON-based database

---

## 🚀 Features

### 📊 NLP Features (via NLPCloud)
- **Sentiment Analysis**: Detect positive/negative/neutral tone in a sentence.
- **NER (Named Entity Recognition)**: Extract names, locations, organizations, etc.
- **Language Detection**: Identify the language of the given input.

### 🧑‍💼 User Authentication
- Built-in user **registration & login**
- Uses `db.json` as a lightweight local storage for user credentials.

### 🖥 GUI (Tkinter)
- Simple and intuitive UI built using **Tkinter**
- Input field, buttons, and result area for analysis output

---

## 🔧 Tech Stack

| Layer           | Technology      |
|----------------|-----------------|
| GUI            | Tkinter         |
| NLP Backend    | [NLPCloud API](https://nlpcloud.io/) |
| Data Storage   | JSON file (`db.json`) |
| IDE            | PyCharm         |
| Python Version | 3.12+           |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2. Install Required Packages

```bash
pip install nlpcloud
```

> ✅ Tkinter comes built-in with Python (no need to install).

### 3. Create or Initialize `db.json`

Create a `db.json` file in your project root with the following content to avoid JSON errors:

```json
{}
```

### 4. Add Your NLPCloud API Key

In your code (`TextAnalysisAPI` class or similar), replace:

```python
self.client = nlpcloud.Client(
    "finetuned-llama-3-70b",
    "your_api_key_here",
    gpu=True
)
```

with your actual API key from [NLPCloud.io](https://nlpcloud.io/).

---



## 💡 Future Improvements

* Add spell checking or grammar correction
* Integrate voice input/output
* Add visual charts for sentiment output
* Use SQLite or PostgreSQL for persistent user database

---

## 📝 License

This project is open-source. Feel free to fork and build upon it.

---

## 🙌 Acknowledgements

* [NLPCloud.io](https://nlpcloud.io/)
* Python & Tkinter


