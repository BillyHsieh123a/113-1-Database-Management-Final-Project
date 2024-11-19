import os

def concatenate_sql_files(input_directory, output_file):
    """
    Concatenate all SQL queries in multiple files into a single SQL file.

    :param input_directory: Directory containing SQL files to be concatenated
    :param output_file: Path to the output SQL file
    """
    try:
        # Ensure the directory for the output file exists
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Create the directory if it doesn't exist

        # Open the output file in write mode (this will create the file if it doesn't exist)
        with open(output_file, 'w') as outfile:
            # Iterate through each file in the input directory
            for filename in os.listdir(input_directory):
                if filename.endswith('.sql'):
                    file_path = os.path.join(input_directory, filename)
                    
                    # Open each SQL file and append its contents to the output file
                    with open(file_path, 'r') as infile:
                        outfile.write(f"-- Start of {filename}\n")
                        outfile.write(infile.read())
                        outfile.write(f"\n-- End of {filename}\n\n")

        print(f"All SQL files have been concatenated into {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_directory = r'.\Create_Tables'  # Use raw string literals to avoid issues with escape characters
output_file = r'combined_queries.sql'  # Ensure this path is correct
concatenate_sql_files(input_directory, output_file)
