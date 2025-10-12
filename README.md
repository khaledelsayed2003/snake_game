🐍 Snake Game (Python Turtle)

A clean beginner-friendly Snake game built with Python’s built-in turtle module.
Move the snake with the arrow keys, eat food to grow, and try not to hit the walls or your own tail!



✨ Features

    Smooth snake movement with segment following

    Arrow-key controls (Up/Down/Left/Right)

    Random food spawns with instant refresh

    Scoreboard at the top; updates on each bite

    Game Over screen on wall or tail collision




🎮 Controls

    ↑ Move Up

    ↓ Move Down

    ← Turn Left

    → Turn Right



📦 Requirements

    Python 3.8+

    Uses only the standard library (turtle, time, random) — no extra installs



🗂️ Project Structure
snake_game/
├─ main.py          # game loop & screen setup
├─ snake.py         # Snake class (movement, turning, extend)
├─ food.py          # Food class (random position, refresh)
├─ scoreboard.py    # Score class (display & game over)
└─ assets/          # (optional) shapes, background, screenshots
   ├─ Start_Game.png
   ├─ Score_starting0.png
   ├─ Score_refresh.png
   └─ Wall_collision.png
   └── Tail_collision.png
       




🧩 How It Works (quick notes)

The snake is a list of turtle.Turtle segments; the head drives movement.

Each frame, segments copy the previous segment’s position → “follow” effect.

Eating food:

    Food.refresh() teleports the food to a new random spot.

    Score.refresh() increments the score.

    Snake.extend() adds a new tail segment.

Collisions:

    Wall collision if head x/y crosses ±285 (600×600 screen).

    Tail collision if the head is within distance < 10 of any body segment.