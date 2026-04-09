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


## File Structure
- `Account` class: stores account data
- `LoginMonitor` class: controls the login system
- `main()` function: starts the program


