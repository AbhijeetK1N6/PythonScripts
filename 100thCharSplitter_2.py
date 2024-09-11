#Code By : K1N6
#Source Code available on GitHub : https://github.com/AbhijeetK1N6/PythonScripts/edit/main/100thCharSplitter.py
# Define the input and output file paths
input_file = "D:\Embedded C\ABHIJEET_K1N6\JESIKA G\Creat logo1 (1).txt"
output_file = "D:\Embedded C\ABHIJEET_K1N6\JESIKA G\Thanks_Abhijeet_OUTPUT.txt"
# Define the split length
split_length = 100
try:
    # Open the input file and read the single line
    with open(input_file, 'r') as file:
        line = file.readline().strip()
    # Split the line every 100 characters
    lines = [line[i:i+split_length] for i in range(0, len(line), split_length)]
    # Write the split lines to the output file
    with open(output_file, 'w') as file:
        for split_line in lines:
            file.write(split_line + '\n')
    print(f"Split lines have been written to {output_file}")
#Code By : K1N6
#Source Code available on GitHub : https://github.com/AbhijeetK1N6/PythonScripts/edit/main/100thCharSplitter.py
except FileNotFoundError:
    print(f"Error: The file {input_file} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
