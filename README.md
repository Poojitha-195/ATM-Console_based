# ATM Console-Based System

## Overview
The **ATM Console-Based System** is a Python-based program that simulates an ATM machine. It enables users to perform basic banking operations, including withdrawing money, depositing funds, checking mini statements, generating and changing PINs, and viewing loan details.

## Features
- Withdraw money from an account.
- Deposit money into an account.
- View account balance and details.
- Generate a PIN for an account.
- Change an existing PIN.
- Check loan details for an account.
- Enhanced error handling and validation.

## Technologies Used
- **Python** (for logic and implementation)
- **Dictionary Data Structure** (to store account details)

## Prerequisites
- Python 3.x installed on your system.

## Installation
1. Clone the repository or download the `atm-console_based.py` file.
   ```sh
   git clone https://github.com/yourusername/atm-console_based.git
   cd atm-console_based
   ```
2. Ensure Python is installed by running:
   ```sh
   python --version
   ```
3. Run the program using:
   ```sh
   python atm-console_based.py
   ```

## Usage
When you run the program, you will see a menu:
```
1. Withdraw
2. Deposit
3. Mini statement
4. PIN generation
5. PIN change
6. Loan details
7. Exit
```
### 1. Withdraw
- Enter your account number.
- Verify your PIN.
- Enter the withdrawal amount.
- If sufficient balance is available, the transaction succeeds.

### 2. Deposit
- Enter your account number.
- Verify your PIN.
- Enter the deposit amount.
- The amount is added to your balance.

### 3. Mini Statement
- Enter your account number.
- Verify your PIN.
- Displays your name, email, and current balance.

### 4. PIN Generation
- Enter your account number.
- If a PIN is not set, create a new PIN and confirm it.

### 5. PIN Change
- Enter your account number.
- Verify your old PIN.
- Set and confirm a new PIN.

### 6. Loan Details
- Enter your account number.
- Displays loan amount if applicable.

### 7. Exit
- Ends the program.

## Account Data Structure
The accounts are stored as a dictionary:
```python
accounts = {
    101: ["user1", "user1@gmail.com", 1234, 3000, None],
    102: ["user2", "user2@gmail.com", 2345, 2200, 5000],
    103: ["user3", "user3@gmail.com", 3456, 1000, None],
    104: ["user4", "user4@gmail.com", None, 3500, None]
}
```
Each account contains:
1. **Account Number** (Key)
2. **User Name**
3. **Email**
4. **PIN (None if not generated)**
5. **Balance**
6. **Loan Amount (None if no loan exists)

## Notes
- PIN validation is enforced.
- Negative transactions are not allowed.
- Multiple incorrect PIN attempts may lock the account.

## Future Enhancements
- Implement a database for account storage.
- Add a graphical user interface (GUI).
- Improve PIN encryption and security.

## License
This project is open-source and available for modification.

## Author
[Poojitha]

