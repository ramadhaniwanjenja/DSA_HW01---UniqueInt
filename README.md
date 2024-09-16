## UniqueInt Assignment
**Overview**
This project solves the problem of identifying unique integers from an input file and writing the sorted unique integers to an output file. The integers range from -1023 to 1023 and can have various formatting challenges (e.g., empty lines, invalid input, multiple numbers per line). The program adheres to the requirements provided by the assignment.

## File Structure ##
**UniqueInt.py:** The main Python script that processes input files and generates output files.
**sample_inputs/:** Folder containing input files.
**sample_results/:** Folder where output files will be stored.

## How to Use
**Prepare the Input File:**

Place your input file in the sample_inputs/ folder. Each line should contain one integer between **-1023 and 1023.** Invalid lines (e.g., empty, non-integer, or multiple integers per line) will be skipped.

**Run the Program:**

Open a terminal or command prompt and run the following command:

python3 UniqueInt.py

**Check the Output:**

After running the program, the output file will be generated in the sample_results/ folder. The filename will be in the format: input_filename_results.txt.
## Example
**For an input file (sample_02.txt) containing:**

5

14

5

-9

62

-1

-9


**The output file will contain:**


-9

-1

5

14

62

## Key Features
1. Handles various input errors (e.g., empty lines, non-integer lines).
2. ses a boolean array to track unique integers for efficient memory usage.
3. Sorts the unique integers in ascending order.
4. No use of built-in libraries for sorting or arrays, ensuring custom logic for these tasks.
5. Requirements
**Python 3.x**

## Author
Created by **Ramadhani Shafii wanjenja**