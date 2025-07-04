import sys
import numpy as np
import pandas as pd

# Step 1: Define the sequence dictionary (sequence_dict)
sequence_dict = {'snap':"TGTTGGTG",'crackle':"GACTCTGA",
                  'pop':"TCTGGTCA",'tony':"CTGAGACT",
                  'crunch':"CTGAGACT",'yogi':"TGATGGAC"}

# Step 2: Check 
def check_hamming_distance(seq1, seq2, threshold=3):
    """Check if the Hamming distance from seq1 to seq2 is less than to the threshold."""
    if len(seq1) != 23:
        return(False)
    else:
        return (sum(c1 != c2 for c1, c2 in zip(seq1[:8], seq2))< threshold)

# Step 2: Read the CSV file into a DataFrame
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.dropna()

def compare_sequences(df, sequence_dict):
    # Assuming the DataFrame has a column named 'Sequence' for comparison
    results = {}
    
    for index, row in df.iterrows():
        sequence = row['Sequence']  # Adjust based on your column name
        match_found = False
        
        # Compare with the sequences in sequence_dict
        for key, seq in sequence_dict.items():
            if check_hamming_distance(sequence, seq):
                match_found = True
                results[key] = results.get(key, 0) + 1
                break

    return results

# Step 4: Run the comparison and display the results
def run_comparison(file_path):
    # Read the CSV file into a DataFrame
    df = read_csv(file_path)
    # Get the number of rows in df
    df_row = df.shape[0]

    # Compare the sequences
    comparison_results = compare_sequences(df, sequence_dict)
    print(f"This is the result of '{file_path}':\n {comparison_results}")


def read_csv_from_user_input(filename):

    try:
        # Attempt to read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        print("CSV file successfully loaded!")
        run_comparison(filename)
    
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: The file at '{filename}' was not found. Please try again.")
        return None


def main(): 
    args = sys.argv[1:]
    for filename in args:
        read_csv_from_user_input(filename)


if __name__ == '__main__':
    main()


### Example of terminal prompt: "python3 SEQ115_NGS_analysis_script.py ./UniqueSeq/*_Seq.csv > results.txt"
