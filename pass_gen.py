from argparse import ArgumentParser
import secrets
import random
import string
from termcolor import colored

# Setting up the Argument Parser
parser = ArgumentParser(
    prog=colored('Password Generator', 'cyan'),
    description=colored('Generate any number of passwords and Customizable Complexity Levels with this tool.', 'green')
)

# Complexity levels
complexity_levels = {
    'simple': {'numbers': 2, 'lowercase': 4, 'uppercase': 2, 'special_chars': 0},
    'moderate': {'numbers': 4, 'lowercase': 6, 'uppercase': 4, 'special_chars': 2},
    'strong': {'numbers': 6, 'lowercase': 8, 'uppercase': 6, 'special_chars': 4}
}

# Adding the arguments to the parser
parser.add_argument("-n", "--numbers", type=int, help=colored("Number of digits in the password", 'cyan'))
parser.add_argument("-l", "--lowercase", type=int, help=colored("Number of lowercase chars in the password", 'cyan'))
parser.add_argument("-u", "--uppercase", type=int, help=colored("Number of uppercase chars in the password", 'cyan'))
parser.add_argument("-s", "--special-chars", type=int, help=colored("Number of special chars in the password", 'cyan'))
parser.add_argument("-c", "--complexity", choices=['simple', 'moderate', 'strong'], help=colored("Password complexity level", 'cyan'))
parser.add_argument("-t", "--total-length", type=int, help=colored("The total password length", 'cyan'))
parser.add_argument("-a", "--amount", default=1, type=int, help=colored("Number of passwords to generate", 'cyan'))
parser.add_argument("-o", "--output-file", help=colored("Output file to save the passwords", 'cyan'))


parser.add_argument("--version", action="version", version=colored("%(prog)s 1.0", 'magenta'))

# Parsing the command line arguments.
args = parser.parse_args()

# Validate total length and complexity level
if args.total_length and args.complexity:
    print(colored("Please specify either a total length or a complexity level, not both.", 'red'))
    exit()

# list of passwords
passwords = []

# Looping through the amount of passwords.
for _ in range(args.amount):
    # Set defaults based on complexity level
    if args.complexity:
        complexity = complexity_levels[args.complexity]
        numbers = complexity['numbers']
        lowercase = complexity['lowercase']
        uppercase = complexity['uppercase']
        special_chars = complexity['special_chars']
    else:
        numbers = args.numbers or 0
        lowercase = args.lowercase or 0
        uppercase = args.uppercase or 0
        special_chars = args.special_chars or 0

    # Generate password based on complexity or custom values
    if args.total_length:
        # generate random password with the length
        # of total_length based on all available characters
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation)
                for _ in range(args.total_length)]))
    else:
        password = []
        # If / how many numbers the password should contain  
        for _ in range(numbers):
            password.append(secrets.choice(string.digits))

        # If / how many uppercase characters the password should contain   
        for _ in range(uppercase):
            password.append(secrets.choice(string.ascii_uppercase))
        
        # If / how many lowercase characters the password should contain   
        for _ in range(lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        # If / how many special characters the password should contain   
        for _ in range(special_chars):
            password.append(secrets.choice(string.punctuation))

        # Shuffle the list with all the possible letters, numbers and symbols.
        random.shuffle(password)

        # Join the characters to form the password.
        password = ''.join(password)

        # Append this password to the overall list of passwords.
        passwords.append(password)

# Store the password to a .txt file.
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))

# Print the generated passwords.
print(colored('\n'.join(passwords), 'red'))
