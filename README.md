# Password-Generator

![Static Badge](https://img.shields.io/badge/Downloads-blue)


Create strong and secure passwords effortlessly with  Python Password Generator script. Choose from predefined complexity levels or customize your criteria, including digits, lowercase, uppercase, and special characters. Generate single or multiple passwords quickly, with options to save them to a file for easy access and management.

## Features

- Generate passwords with different complexity levels: simple, moderate, or strong.
  
- Customize the length and composition of passwords.
  
- Output passwords to a file for easy access and storage

## Usage

1. Clone the repository or download `git clone https://github.com/Prashanth-0/Password-Generator.git`
  
2. Install the required dependencies using
   `pip install termcolor`

3. Run the Script
   `python3 pass_gen.py -h`

**python pass_gen.py [options]**

Options:
- `-n`, `--numbers`: Number of digits in the password.
- `-l`, `--lowercase`: Number of lowercase characters in the password.
- `-u`, `--uppercase`: Number of uppercase characters in the password.
- `-s`, `--special-chars`: Number of special characters in the password.
- `-c`, `--complexity`: Password complexity level (`simple`, `moderate`, or `strong`).
- `-t`, `--total-length`: The total password length.
- `-a`, `--amount`: Number of passwords to generate (default is 1).
- `-o`, `--output-file`: Output file to save the passwords.
- `--version`: Display version information.

## Examples
1. Generate a simple password with default options:

python pass_gen.py -c moderate -t 10 -a 5 -o passwords.txt
