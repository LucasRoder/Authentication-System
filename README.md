# Login Monitor

## Overview
Login Monitor is a Python command-line program that simulates a basic user authentication system. It allows users to create accounts, log in, and change passwords while enforcing simple password rules and account security features.

## Features
- Create a new account
- Log in to an existing account
- Change a password
- Lock an account after 3 failed login attempts
- Unlock a locked account using a secret answer
- Check password length and spaces
- Display password strength as weak, medium, or strong

## How the Program Works

### 1. Account Class
The `Account` class represents a single user account. Each account stores:
- `password`
- `secret_answer`
- `locked` status

### 2. LoginMonitor Class
The `LoginMonitor` class manages all accounts and handles the menu system. It includes methods for:
- validating passwords
- creating accounts
- logging in
- changing passwords
- displaying the menu
- running the program loop

## Password Rules
A valid password must:
- be at least 8 characters long
- contain no spaces

The program also checks password strength based on whether the password contains:
- numbers
- uppercase letters
- lowercase letters
- special characters

## Default Account
When the program starts, it includes a default admin account:

- **Username:** `admin`
- **Password:** `admin123`
- **Secret Answer:** `admin`

## Menu Options
When you run the program, you will see these options:

1. Login  
2. Create new account  
3. Change password  
4. Exit

## Example Use Cases
- A user creates a new account with a secure password
- A user logs in successfully with the correct username and password
- A user enters the wrong password 3 times and gets locked out
- A locked user unlocks the account by answering the secret question
- A user changes their password after confirming their identity

## How to Run
1. Make sure Python is installed.
2. Save the code in a Python file, for example `login_monitor.py`.
3. Open a terminal or command prompt.
4. Run:

```bash
python login_monitor.py
```

## File Structure
- `Account` class: stores account data
- `LoginMonitor` class: controls the login system
- `main()` function: starts the program

## Skills Demonstrated
This project demonstrates:
- object-oriented programming
- classes and objects
- dictionaries
- loops
- conditionals
- input validation
- method design
- basic authentication logic

## Limitations
This project is designed for learning purposes. It stores passwords in plain text and does not save accounts after the program closes.

## Possible Future Improvements
- hash passwords for better security
- save account data to a file
- add username rules
- require stronger passwords
- add an option to delete accounts
- add better error handling

## Author
Created as a Python authentication system project.
