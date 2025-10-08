# 🪐 Asteroids Game

A simple, classic-style **Asteroids** video game built using **Python** and **Pygame**.  
Fly your ship through space, avoid asteroids, and shoot them down before they hit you!  
This project demonstrates **object-oriented programming**, **multi-file Python project structure**, and how to use **Pygame** for real-world game development.

---

## 🚀 Learning Goals

- Understand how to organize a **multi-file Python project**
- Apply **object-oriented programming (OOP)** concepts in a fun, interactive way
- Learn to use **Pygame** for drawing graphics, animations, and handling user input
- Gain experience working with **virtual environments** and dependency management using `uv`
- Build and run a complete interactive game from scratch 🎮

---

## 🧰 Prerequisites

Before getting started, ensure you have the following installed:

- **Python 3.10+**
- **uv** project and package manager
- Access to a **Unix-like shell** (e.g., `zsh`, `bash`, or WSL on Windows)

If you don’t already have Python or uv set up, refer to your **BookBot project setup guide** or Python installation docs.

---

## 🧩 Installation & Setup

### 1. Create a new uv project

```bash
uv init asteroids
cd asteroids
```

### 2. Create a new uv project

```bash
uv venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate

You should now see your environment name at the start of your terminal prompt, for example:
(Asteroids) user@MacBook-Pro asteroids %
```

### 4. Add pygame as a dependency

```bash
uv add pygame==2.6.1
```

### 5. Verify pygame installation

```bash
uv run -m pygame
```

### 6. Running the Game

```bash
python main.py
```
