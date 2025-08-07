the whole text below is (obviously) made by AI cause I don't like writing. it is detailed and all, but the short version is that the app takes three inputs inthe bash:
'total steps (default = 1000): '
'marbels number initial (default = 2): '
'initial value: (default = 1) '
and it returns a matplotlib graph of all the steps of the way. y is the probability of the marble being chosen and x is the steps. 
the third input is also an add on, it isn't in the original model and it is supposed to show a buffering effect on the whole thing.(and how drastically the outcomes might change simply with more buffered starts)
enjoy, and if you need read the following.(I didn't :D)


# 🎲 Pólya Urn Simulation (Generalized Version)

This Python script simulates a generalized version of the **Pólya Urn Model**, a classic example of **reinforcement dynamics** in probability theory and social systems.

Instead of just two colors (as in the classic model), this version allows for any number of distinct colors, and introduces an additional parameter to control the *initial quantity* of each color.

---

## 🧠 What Is the Pólya Urn Model?

The Pólya Urn process is a feedback-based probabilistic model where:

1. You draw a marble from an urn.
2. You return it **and add another marble of the same color**.
3. Over time, the color distribution becomes **self-reinforcing**, with one color likely dominating.

This model is used to explain phenomena such as:
- Opinion formation and polarization
- "Rich-get-richer" dynamics
- Echo chambers and viral trends

---

## 🔧 How This Simulation Works

The script takes **three inputs** from the user:

1. **Number of Colors**  
   The number of unique colors to start with.  
   For example: `3` means Red, Blue, Yellow.

2. **Number of Rounds**  
   How many iterations of the process should be run.  
   For example: `1000` means the draw-add cycle is repeated 1000 times.

3. **Initial Count Per Color**  
   Instead of starting with just one marble per color, you can specify a higher number.  
   For example: `10` means the urn starts with 10 marbles of each color.

---

## 📈 Why the Third Input Matters

The **Initial Count Per Color** affects how quickly reinforcement kicks in:

- A low initial value (like 1) allows early random fluctuations to snowball and dominate.
- A high initial value (like 50) dampens this effect, making the system more stable and resistant to early bias.

This is a simple way to visualize how **initial conditions influence long-term outcomes**, even in fair systems.

---

## ▶️ How to Run

Make sure you have Python 3 installed, then simply run:

```bash
python polyas_urn.py
