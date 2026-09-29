# Rock Paper Scissor Game

![Project Cover](README_Cover.svg)

## Student Details

**Name:** Umesh Yadav  
**Registration Number:** 26BCE10104  
**Institute:** VIT Bhopal University  
**Project:** Rock Paper Scissor Game  
**Language Used:** Python

---

## 1. About the Project

This project is a simple **Rock Paper Scissor game** made using Python.

The program allows the user to play a **5-round game series** against the computer. The computer randomly selects rock, scissor, or paper in every round.

The program keeps separate scores for the user and the computer and displays the result after every round. At the end of five rounds, it displays the final result of the game series.

---

## 2. Rules Used in the Program

The program follows these three rules:

- Rock vs Paper → Paper wins
- Rock vs Scissor → Rock wins
- Paper vs Scissor → Scissor wins

If both the user and computer choose the same move, the round is treated as a draw.

---

## 3. Python Concepts Used

The following Python concepts are used in this project:

- `import random`
- Lists
- `while` loop
- `for` loop
- `if`, `elif`, and `else`
- `input()`
- `print()`
- Variables
- Integer conversion using `int()`
- `random.choice()`
- Logical `and` and `or` operators
- Comparison operators
- Score variables and updating their values

---

## 4. How the Program Works

### Step 1: Starting the Game

When the program starts, it asks the user:

```text
Game start....
1 Yes
2 No | Exit
```

If the user enters `1`, the game starts.

If the user enters another value, the program exits using `break`.

### Step 2: Five Rounds

The program uses a `for` loop to run the game **five times**.

In every round, the user selects:

```text
1 Rock
2 Scissor
3 Paper
```

The selected number is converted into the corresponding word.

### Step 3: Computer's Move

The program stores the three possible moves in a list:

```python
moves = ["rock","scissor","paper"]
```

The computer selects one move randomly using:

```python
random.choice(moves)
```

### Step 4: Comparing the Moves

The program first checks whether the user and computer selected the same move.

If they are the same, the round is declared a draw.

Otherwise, the program checks the three winning conditions for the user:

- User chooses rock and computer chooses scissor
- User chooses paper and computer chooses rock
- User chooses scissor and computer chooses paper

If none of these conditions are true, the computer wins the round.

### Step 5: Updating the Score

The program uses two score variables:

```python
user_score = 0
comp_score = 0
```

The scores are updated after every round.

In a draw, both scores are increased by 1 in the current program.

### Step 6: Final Result

After five rounds, the program compares the two scores.

There are three possible final results:

- Final game series draw
- User wins the game series
- Computer wins the game series

The final user score and computer score are also displayed.

---

## 5. Main Logic of the Program

The basic flow of the program is:

```text
Start
  ↓
Ask whether to start the game
  ↓
If Yes
  ↓
Run 5 rounds
  ↓
Take user's move
  ↓
Computer randomly selects a move
  ↓
Compare both moves
  ↓
Update scores
  ↓
Repeat until 5 rounds are completed
  ↓
Compare final scores
  ↓
Display final result
  ↓
End
```

---

## 6. Sample Interaction

A typical round can display information like:

```text
Computer Value rock
User Value scissor
Computer Win
```

The exact computer value and result can change because the computer's move is selected randomly.

---

## 7. Project Objective

The purpose of this project is to create a basic interactive game in Python while applying programming concepts such as loops, conditional statements, lists, user input, random selection, and score calculation.

---

## 8. Files in This Project

- `Rock paper Scissor Game Project.py` — Python program of the game
- `README.md` — Project documentation
- `statement.md` — Project statement and explanation
- `README_Cover.svg` — Cover image used at the beginning of this README

---

## 9. Conclusion

This project demonstrates a simple Rock Paper Scissor game using basic Python programming concepts. The program takes input from the user, generates a random move for the computer, compares both moves, maintains scores, and displays the final result after five rounds.
