#### CREATES A REQUIREMENTS.TXT FILE
import subprocess

# Name of the file containing the list of library names
LIBRARY_FILE = 'libraries.txt'

# Name of the file to output the requirements to
OUTPUT_FILE = 'requirements.txt'

# Read the library names from the file
with open(LIBRARY_FILE, 'r') as f:
    libraries = [line.strip() for line in f.readlines()]

# Run pip freeze | grep for each library and append the output to the output file
with open(OUTPUT_FILE, 'w') as f:
    for library in libraries:
        command = f'pip freeze | grep {library}'
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        f.write(output)
