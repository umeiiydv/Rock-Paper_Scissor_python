# Project Statement

## Rock Paper Scissor Game

**Name:** Umesh Yadav  
**Registration Number:** 26BCE10104  
**Institute:** VIT Bhopal University  
**Programming Language:** Python

---

## 1. Project Statement

The project is a simple Python-based **Rock Paper Scissor Game** in which a user plays against the computer.

The program provides three choices to the user: Rock, Scissor, and Paper. The computer also selects one of these three choices randomly. The program compares the user's choice with the computer's choice and decides the result of each round.

The game is played for **five rounds**, and the scores of the user and computer are maintained throughout the game. After all five rounds are completed, the program compares the final scores and displays the result of the game series.

---

## 2. Rules of the Game

The program uses the following rules:

1. Rock defeats Scissor.
2. Scissor defeats Paper.
3. Paper defeats Rock.
4. If both players select the same option, the round is treated as a draw.

These rules are directly used in the conditional statements of the program.

---

## 3. Input

The program takes input from the user in two stages.

### Starting the Game

The user is asked whether they want to start the game:

```text
1 Yes
2 No | Exit
```

### Selecting a Move

For every round, the user selects one of the following:

```text
1 Rock
2 Scissor
3 Paper
```

---

## 4. Processing

The program first creates a list containing the three possible moves:

```python
moves = ["rock","scissor","paper"]
```

The computer selects one move randomly using the `random.choice()` function.

The user's numerical choice is converted into the corresponding move:

- `1` → rock
- `2` → scissor
- `3` → paper

The program then compares the two moves using `if`, `elif`, and `else` statements.

The game runs for five rounds using a `for` loop.

Two variables are used to maintain the scores:

```python
user_score = 0
comp_score = 0
```

The scores are updated according to the result of each round.

---

## 5. Winning Conditions Used

The user wins a round when any one of these conditions is true:

```text
User = Rock    and Computer = Scissor
User = Paper   and Computer = Rock
User = Scissor and Computer = Paper
```

If both moves are the same, the program displays:

```text
Game Draw
```

If the user's winning conditions are not satisfied and the moves are not the same, the program displays:

```text
Computer Win
```

---

## 6. Number of Rounds

The program uses:

```python
for a in range(1,6):
```

Therefore, the game runs for five rounds.

After the fifth round, the program compares:

```python
user_score
comp_score
```

and displays the final game-series result.

---

## 7. Output

For each round, the program displays:

- Computer's selected value
- User's selected value
- Result of the round

At the end of the five-round series, it displays:

- Final result
- User score
- Computer score

The final result can be:

```text
Final Game series draw...
```

or

```text
Final You Win the Game series...
```

or

```text
Computer Win the Game series
```

---

## 8. Python Concepts Applied

This project applies the following basic concepts:

- Importing a module using `import random`
- Creating and using a list
- Taking user input
- Converting input to integer using `int()`
- Variables
- `while` loop
- `for` loop
- `if`, `elif`, and `else`
- Comparison operators
- Logical `and` and `or`
- `random.choice()`
- Updating variable values
- Displaying output using `print()`
- Using `break` to exit the program

---

## 9. Basic Working Flow

```text
Start
   ↓
Ask user to start the game
   ↓
Start the game
   ↓
Run 5 rounds
   ↓
Take user's choice
   ↓
Convert choice into Rock / Scissor / Paper
   ↓
Computer selects a random move
   ↓
Compare user's move and computer's move
   ↓
Display round result
   ↓
Update score
   ↓
Next round
   ↓
After 5 rounds, compare scores
   ↓
Display final result
   ↓
End
```

---

## 10. Project Objective

The objective of this project is to make a basic interactive game using Python and understand how different programming concepts can work together in one program.

The project mainly uses conditional statements, loops, lists, user input, random selection, and variables for maintaining the score.

---

## 11. Project Outcome

The completed program provides a working five-round Rock Paper Scissor game where the user plays against a computer-controlled random choice.

The program demonstrates how basic Python statements can be combined to create an interactive program.
