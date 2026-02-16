import pandas as pd
import os

file_path = "d:/apsche internship/ProjectFiles/Dataset/flood_dataset.xlsx"
output_file = "d:/apsche internship/ProjectFiles/Flask/dataset_info.txt"

try:
    df = pd.read_excel(file_path)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Columns: " + str(list(df.columns)) + "\n")
        f.write("Means:\n" + str(df.mean(numeric_only=True)) + "\n")
        f.write("Max:\n" + str(df.max(numeric_only=True)) + "\n")
        
except Exception as e:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
