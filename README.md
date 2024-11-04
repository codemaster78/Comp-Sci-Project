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
