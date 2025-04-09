# Python Practice Projects (`py_prac`)

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  ![Last Commit](https://img.shields.io/github/last-commit/hpv333/py_prac)

A growing collection of **bite‑sized Python console apps and mini‑games** I built to practise fundamentals—loops, functions, data structures, and a dash of ASCII art—on my journey from beginner to object‑oriented Pythonista.

> **Why keep them in one repo?** It’s a time‑capsule of learning milestones: each script solves a small, well‑defined problem while introducing a new concept or library. Fork it, run it, tweak it, and level‑up alongside me!

---

## 🎮 What’s Inside

| File | Category | TL;DR |
|------|----------|-------|
| `BLACKJACK_GAME.py` | Game | Play a simplified round of Blackjack against a computer dealer. Handles Aces (11/1) and detects Blackjacks. |
| `number_guessing.py` | Game | Guess a secret number between 1‑100 in *Easy* (10 tries) or *Hard* (5 tries) mode. |
| `rock_paper_scissors.py` | Game | Classic Rock‑Paper‑Scissors with emoji/ASCII art feedback. Best‑of‑n option. |
| `password_generator.py` | Utility | Generates cryptographically strong passwords of custom length using letters, numbers, and symbols. |
| `quiz_game/` *(coming soon)* | Game | Multiple‑choice trivia powered by the Open Trivia DB API. |

Each script is **self‑contained**—no external dependencies beyond the Python standard library.

---

## 🏗️ Project Structure

```
py_prac/
├─ BLACKJACK_GAME.py        #  → python BLACKJACK_GAME.py
├─ number_guessing.py       #  → python number_guessing.py
├─ rock_paper_scissors.py   #  → python rock_paper_scissors.py
├─ password_generator.py    #  → python password_generator.py
├─ README.md                #  ← you are here
└─ LICENSE
```

> **Tip:** Want all games in one launcher? Clone the repo and create your own `main_menu.py` that `import`s each script as a module—great exercise in functions and dictionaries!

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/hpv333/py_prac.git
   cd py_prac
   ```
2. **Run any script** with Python 3.10 or later:
   ```bash
   python BLACKJACK_GAME.py
   ```
   *(Replace the filename with the game you want to play.)*

### Optional Virtual Env

```bash
python -m venv .venv && source .venv/bin/activate  # Linux/macOS
# or
py -m venv .venv && .venv\Scripts\activate        # Windows
```
No external packages are required, but a venv keeps things tidy.

---

## 📚 Learning Highlights

- **Functions & Return Values** – `deal_card()`, `calculate_score()` in Blackjack.
- **Control Flow** – nested `while` / `for` loops, `if‑elif‑else` chains.
- **Randomness** – `random.choice`, `random.randint` for unpredictable gameplay.
- **Lists & Dictionaries** – storing hands of cards, RPS choices, and ASCII art.
- **User Input Validation** – looping until a valid response is entered.
- **ASCII Art & f‑Strings** – making the CLI a little less boring. 😄

Feel free to dive into the code and leave comments or PRs with refactors—every suggestion is a learning opportunity.

---

## 🗺️ Roadmap

- [ ] Refactor games into **classes** to practise OOP patterns.
- [ ] Add **unit tests** with `unittest` and `pytest`.
- [ ] Build a **Tkinter GUI** wrapper for Blackjack.
- [ ] Integrate **type hints** and run `mypy`.
- [ ] Containerise with **Docker** for easy execution anywhere.

---

## 🤝 Contributing

Got an idea for a new mini‑project? Found a bug? Open an issue or PR! Please follow these simple steps:

1. Fork the repo and create your branch: `git checkout -b feat/awesome-game`.
2. Commit your changes using *Conventional Commits*.
3. Push and open a pull request with a clear description.

All skill levels are welcome—this is a sandbox for experimentation.

---

## 📝 License

This repository is licensed under the **MIT License**—do whatever you want, just give credit where due.

---

## 🙋‍♀️ Author

**Hari Priya Vedala**  – [LinkedIn](https://www.linkedin.com/in/haripriyav3) • [Portfolio](https://hpv333.github.io/blog-build/) • [GitHub](https://github.com/hpv333)

> Made with curiosity, caffeine, and countless `print()` statements.

