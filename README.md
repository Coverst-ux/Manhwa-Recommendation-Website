# 📚 Manhwa Recommendation Website

> An AI-powered manhwa recommendation engine that learns your taste and suggests what to read next. No account required.

---

## Why I Built This

This project marks the start of my journey into AI/ML engineering. After a break from programming, I wanted to build something that actually meant something to me, and manhwa is something I genuinely love. It also gave me a real reason to explore local LLM inference, API integration, and full-stack architecture from scratch.

---

## What It Does

- Search for manhwas by title using the ComicK API
- Build a personal reading list (or import it via CSV)
- Get AI-powered recommendations based on your taste using a local LLM
- No login, no account. Fully anonymous via session IDs

---

## Tech Stack

| Layer | Tool |
|---|---|
| Backend | FastAPI (Python) |
| AI | Ollama (Llama 3.1:8b, local inference) |
| Database | SQLite |
| External Data | ComicK API (via proxy) |
| Frontend | Vanilla HTML / CSS / JS |

---

## Architecture

```
User (Browser)
    │
    │  HTTP requests
    ▼
FastAPI Backend
    ├── ComicK Proxy API  →  fetch manhwa metadata
    ├── SQLite Database   →  store/retrieve user lists
    └── Ollama (local)    →  generate recommendations
    │
    ▼
Response back to Browser
```

**Recommendation flow:**
1. User builds a manhwa list (min. 3 titles)
2. FastAPI retrieves the session's list from SQLite
3. List metadata is sent to Ollama with a structured prompt
4. Ollama returns JSON recommendations
5. Results are paginated and returned to the frontend (4 per scroll)

---

## Technical Decisions

**Anonymous Sessions:** No user accounts. A UUID is generated on first visit and stored in `localStorage`. The schema is designed so swapping to a proper `user_id` FK later is trivial.

**Local LLM via Ollama:** Recommendations run entirely on-device using Llama 3.1:8b. No API keys, no costs, no data leaving the machine.

**ComicK Proxy:** The direct ComicK API returns 403s, so requests are routed through a proxy. All requests include `tachiyomi=True` as a query param.

**HID-based lookup:** Manhwas are identified by ComicK's unique `hid`. Search returns results filtered by `hid` match for reliable lookups.

**Infinite scroll pagination:** Recommendations load 4 at a time. Each scroll sends the already-seen titles back to the backend to prevent repeats. 

---

## Project Structure

```
manhwa-recommender/
├── main.py              ← FastAPI init, CORS, route mounting
├── routes/
│   ├── session.py       ← POST /session
│   ├── manhwa.py        ← search, add, get, delete
│   └── recommend.py     ← Ollama integration + pagination
├── services/
│   ├── comick.py        ← ComicK API logic
│   └── ai.py            ← Ollama prompt + response parsing
├── database.py          ← SQLite setup + CRUD
├── static/
│   ├── index.html       ← Landing / search
│   ├── list.html        ← My List
│   └── recommendations.html
└── requirements.txt
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/session` | Create anonymous session |
| POST | `/manhwa/search` | Search ComicK by title |
| POST | `/manhwa/list` | Add manhwa to session list |
| GET | `/manhwa/list/{session_id}` | Get current list |
| DELETE | `/manhwa/list/{item_id}` | Remove manhwa from list |
| POST | `/recommend` | Get AI recommendations (paginated) |

---

## Local Setup

### Prerequisites
- Python 3.12+
- [Ollama](https://ollama.com/) installed and running
- Llama 3.1:8b pulled: `ollama pull llama3.1:8b`

### Installation

```bash
git clone https://github.com/Coverst-ux/Manhwa-Recommendation-Website
cd Manhwa-Recommendation-Website
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### Run

```bash
uvicorn main:app --reload
```

Then open `http://localhost:8000` in your browser.

---

## Status

🚧 **In active development.** Backend routes and frontend in progress.

---

*Built as a portfolio project. First step into AI/ML engineering.*
