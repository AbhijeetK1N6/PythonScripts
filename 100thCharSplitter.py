import sys
import os
#Code By : K1N6
#Source Code available on GitHub : https://github.com/AbhijeetK1N6/PythonScripts/edit/main/100thCharSplitter.py
def split_line(input_file, output_file, split_length=100):
    try:
        # Open the input file and read the single line
        with open(input_file, 'r') as file:
            line = file.readline().strip()
        # Split the line every `split_length` characters
        lines = [line[i:i+split_length] for i in range(0, len(line), split_length)]
        # Write the split lines to the output file
        with open(output_file, 'w') as file:
            for split_line in lines:
                file.write(split_line + '\n')
        print(f"Split lines have been written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
#Code By : K1N6
#Source Code available on GitHub : https://github.com/AbhijeetK1N6/PythonScripts/edit/main/100thCharSplitter.py
def main():
    if len(sys.argv) != 2:
        print("Usage: Drag and drop a file onto this script.")
        return
    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + '_output.txt'
    # Call the function with the provided input file
    split_line(input_file, output_file)

if __name__ == "__main__":
    main()
#Code By : K1N6
#Source Code available on GitHub : https://github.com/AbhijeetK1N6/PythonScripts/edit/main/100thCharSplitter.py
