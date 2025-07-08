# ❌⭕ Tic Tac Toe Game Using Python (Tkinter GUI)

This project is a classic **Tic Tac Toe (X-O)** game built with **Python's Tkinter library** for the graphical user interface. Two players take turns playing on a 3×3 grid, with real-time visual feedback, automatic win/draw detection, and game restart functionality.

---

## 🕹️ Features

- 🔁 Random starting player (X or O)
- 🎨 Color-coded buttons and display updates
- 🚫 Automatic disabling of clicked cells
- 🧠 Win and draw detection with highlighted winning path
- 🔄 Restart button after game over or draw
- 🖤 Dark-themed interface with white tiles and red highlights

---

ey Components in `tic_tac_toe.py`:
- `start_game()` – Resets board, sets up random first player
- `click()` – Handles cell clicks, toggles turns, checks win/draw
- `check_result()` – Evaluates game board for winning conditions
- GUI Layout – Built using `Tk`, `Frame`, and `Button` widgets in rows

---

## 🛠 How to Run

1. Ensure Python 3.x is installed.
2. Save the script as `tic_tac_toe.py`.
3. Run the game:
   ```bash
   python tic_tac_toe.py

## 🎨 Customization Ideas

- 🎭 **Theme Modes**: Add light/dark UI skins or fun visual themes (e.g., neon, chalkboard, galaxy).
- 🧠 **AI Opponent**: Implement basic or advanced AI using random logic or minimax algorithm.
- ⏱️ **Turn Timer**: Add countdown functionality to limit decision time per move.
- 🎧 **Sound Effects**: Integrate audio feedback on moves, wins, or errors.
- 🔢 **Score Tracking**: Record and display scores across multiple rounds; allow player name inputs.

## 💡 Other Suggestions

- 🗃️ **Executable Build**: Use PyInstaller to bundle into a `.exe` (Windows) or `.app` (macOS) file.
- 🌐 **Multilingual Support**: Let users switch between languages within the UI.
- 🧪 **Unit Testing**: Write tests to ensure game logic (win checks, draw, turn rotation) works reliably.
- 📸 **Gameplay Capture**: Save move history or enable match replay functionality.
- 🚀 **Web-Based Version**: Port to PyScript, Flask, or Streamlit to allow browser-based play.
