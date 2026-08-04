# JARVIS OS Architecture

## Overview

JARVIS OS follows a modular architecture where every component has a single responsibility.

```
                    USER
                      │
                 Assistant
                      │
                  AI Brain
          ┌──────────┼──────────┐
          │          │          │
     Memory      LLM Service   Tools
          │
      SQLite Database
```

---

## Modules

### Brain

Responsible for reasoning and coordinating responses.

---

### Memory

Stores user profile and conversation history.

---

### LLM Service

Provides a single interface for communicating with local or cloud language models.

---

### Prompt System

Stores prompt templates separately from Python code.

---

### Future Modules

- Voice
- Vision
- Tool Calling
- Planner
- Browser Automation
- Desktop Automation
- Multi-Agent Coordination