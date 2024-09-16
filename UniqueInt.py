class UniqueInt:
    def __init__(self):
        # Boolean array to track which integers from -1023 to 1023 are seen.
        self.seen_integers = [False] * 2047  # [-1023 to 1023] -> index 0 to 2046

    def processFile(self, inputFilePath, outputFilePath):
        """
        Processes the input file, identifies unique integers, and writes the sorted result to the output file.
        """
        try:
            with open(inputFilePath, 'r') as input_file:
                for line in input_file:
                    item = self.readNextItemFromFile(line)
                    if item is not None:
                        self.seen_integers[item + 1023] = True  # Adjust index for range [-1023, 1023]

            with open(outputFilePath, 'w') as output_file:
                for i in range(-1023, 1024):
                    if self.seen_integers[i + 1023]:  # Check if the integer was seen
                        output_file.write(f"{i}\n")

        except FileNotFoundError:
            print(f"Error: File not found - {inputFilePath}")

    def readNextItemFromFile(self, line):
        """
        Reads the next valid integer from a line.
        :param line: str, a line from the input file
        :return: int or None, the parsed integer or None if invalid
        """
        line = line.strip()
        if line and len(line.split()) == 1:  # Ensure the line has exactly one item
            try:
                number = int(line)
                if -1023 <= number <= 1023:  # Only allow integers in the valid range
                    return number
            except ValueError:
                return None
        return None


# Example usage:
if __name__ == "__main__":
    unique_int = UniqueInt()
    input_file = r'C:\Users\Dell\Desktop\UniqueInt\dsa\hw01\sample_inputs\sample_02.txt'
    output_file = r'C:\Users\Dell\Desktop\UniqueInt\dsa\hw01\sample_results\sample_input_02.txt_results.txt'
    unique_int.processFile(input_file, output_file)
