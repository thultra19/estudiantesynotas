# Student Grade Management Program

## 📚 Description

This is a simple **Python program** that registers a group of students, records their grades, and calculates their academic results.

The program asks the user to enter the number of students to register. For each student, it collects their name and three grades. Then it calculates the student's average grade and determines whether the student **passed or failed**.

Finally, the program displays:

* The **average grade of the class**
* The **number of students who passed**
* The **number of students who failed**

---

## ⚙️ How the Program Works

1. The user enters the **number of students** to register.
2. The program loops through each student.
3. For every student:

   * The user enters the **student's name**.
   * The user enters **three grades**.
4. The program validates that each grade is between **0 and 5**.
5. The program calculates the **average grade** using the formula:

```
average = (grade1 + grade2 + grade3) / 3
```

6. The program determines:

   * **Passed** if the average is **3.0 or higher**
   * **Failed** if the average is **below 3.0**
7. At the end, the program calculates the **overall class average** and displays the results.

---

## 🧮 Grading System

| Grade Range | Result |
| ----------- | ------ |
| 3.0 – 5.0   | Passed |
| 0 – 2.9     | Failed |

Grades must always be **between 0 and 5**.

---

## ▶️ How to Run the Program

1. Make sure you have **Python installed** on your computer.
2. open the folder and find the application script named:

```
main.py
```

3. Run the program from the terminal or command prompt:

```
python main.py
```

4. Follow the instructions displayed in the console.

---

## 💻 Example Output

```
Please enter how many students will be registered
2

What is the name of student number 1?
Carlos
Enter the first grade for Carlos
4
Enter the second grade for Carlos
3.5
Enter the third grade for Carlos
4.2

Carlos's average grade is: 3.9
Carlos has passed.

What is the name of student number 2?
Ana
Enter the first grade for Ana
2
Enter the second grade for Ana
2.5
Enter the third grade for Ana
2.8

Ana's average grade is: 2.43
Ana has failed.

The class average is: 3.165
Number of students who passed: 1
Number of students who failed: 1
```

---

## 🛠 Technologies Used

* **Python**

---

## 📌 Notes

* The program assumes the grading system ranges from **0 to 5**, which is commonly used in some educational systems.
* Invalid grades outside this range will trigger an error message.
