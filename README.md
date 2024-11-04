# NPC Data Generator

This project is a simple NPC (Non-Playable Character) data generator written in Python. It generates random attributes for NPCs such as age, height, health, speed, gender, name, and language, and saves the data to a file.

## 📋 Project Overview
The NPC Data Generator allows users to create multiple NPC profiles with randomized characteristics, which can be useful in games or simulations where diverse character data is needed. Each character's data is saved to a file for easy reference.

## 🛠️ Features
- **Randomized Attributes**: Each NPC is assigned random values for attributes like age, height, health, speed, and more.
- **Gender-Specific Names**: Names are generated based on the assigned gender.
- **File Export**: Generated NPC data is saved to a `charecters.txt` file.
- **User Input**: Customize the number of NPCs to generate and set age ranges for each.

## 💻 How It Works
1. **Input**: The program prompts the user for the number of NPCs to create and an age range for each NPC.
2. **Randomization**: The program generates random values for each attribute:
   - **Age**: Random age within the specified range.
   - **Height**: Randomized in feet and inches.
   - **Health**: Range between 1 and 10.
   - **Speed**: Random value from 1 to 100.
   - **Gender**: Randomly assigned as "male" or "female."
   - **Name**: A gender-specific full name.
   - **Language**: Boolean indicating if the NPC speaks English.
3. **Output**: NPC data is displayed on the console and written to a file called `charecters.txt`.

## 💾 Example Output file
```Charecter #1

age: 72
height: 6 feet and 7 inches
health: 4/10
speed: 2
gender: maleName: Steven Norman
English speaker: True


Charecter #2

age: 18
height: 7 feet and 8 inches
health: 3/10
speed: 39
gender: maleName: Duane Jagers
English speaker: True


Charecter #3

age: 75
height: 5 feet and 10 inches
health: 7/10
speed: 27
gender: femaleName: Candice Gates
English speaker: True```
