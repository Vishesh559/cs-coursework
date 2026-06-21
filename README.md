# FitMind AI — Intelligent Fitness Platform

A full-stack web app for tracking workouts and nutrition, with an AI coach for personalized fitness guidance.

## 🎯 Problem

Generic fitness apps log data but don't adapt advice to the individual. FitMind AI combines workout/nutrition tracking with an AI coach that gives personalized recommendations based on a user's actual logged activity.

## 🏗️ Architecture

```
[Next.js Frontend] --> [FastAPI Backend] --> [PostgreSQL Database]
                              |
                       [Groq AI Service]
```

- **Frontend:** Next.js 14 (TypeScript) handles UI, dashboards, and client-side state
- **Backend:** FastAPI exposes REST endpoints for workouts, nutrition logs, and AI coaching
- **Database:** PostgreSQL stores users, workout history, and nutrition logs
- **AI Layer:** Groq AI generates personalized fitness/nutrition advice based on logged data

## ✨ Key Features

- Workout and nutrition logging with structured data models
- Real-time dashboard showing progress trends over time
- AI coach that gives personalized advice grounded in the user's actual logged history (not generic tips)
- Type-safe frontend-to-backend contract via TypeScript + FastAPI's typed schemas

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, TypeScript, Tailwind CSS |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| AI | Groq AI |

## 📐 Technical Decisions

- **FastAPI over Flask:** built-in request/response validation via Pydantic models, and automatic OpenAPI docs, which matters for a typed frontend integration.
- **Next.js App Router:** server components reduce client-side JS for data-heavy dashboard pages.

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.10+
- PostgreSQL instance

### Installation
```bash
# Frontend
git clone https://github.com/Vishesh559/fitmind
cd fitmind
npm install

# Backend
git clone https://github.com/Vishesh559/fitmind-backend
cd fitmind-backend
pip install -r requirements.txt
```

### Running locally
```bash
npm run dev          # frontend, in fitmind/
uvicorn main:app --reload   # backend, in fitmind-backend/ (adjust entry-point as needed)
```

## 📸 Demo

*(Add a screenshot or screen recording of the dashboard here.)*

## 📈 Future Improvements

- Add workout plan generation based on user goals
- Integrate wearable device data (e.g., Apple Health, Fitbit)
- Add social/sharing features for progress milestones

## 📄 License

MIT
