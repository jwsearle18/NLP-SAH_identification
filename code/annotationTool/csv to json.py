import os
import pandas as pd

def process_csv(group: bool, column1: str, column2: str, path: str = '.', file_name: str = ''):
    df = pd.read_csv(os.path.join(path, file_name), sep=',')

    if group:
        grouped = df.groupby('PatientID')
        df = grouped.agg(lambda x: x.tolist())
        df = df.reset_index()

    # Keep only the specified columns
    df = df[[column1, column2]]
    df = df.rename(columns={column1: 'EMPI', column2: 'Report_Text'})
    # Convert dataframe to JSON
    json_data = df.to_json(orient='records')

    # Write JSON to a JavaScript file with variable assignment and function call
    with open(os.path.join(path, 'data.js'), 'w') as f:
        f.write('var json=')
        f.write(json_data)
        #f.write(';\nreset_empi_loaded_file1();')

# True to group by PatientID, next is the
# path to your csv file


path = "/home/jsearle/bigDrive/NAX/NLP-SAH_identification/code/annotationTool/"
file_name = "final_icd_neg_df.csv"
# replace "note_id" with csv column with the unique id for each note and replace "note_txt" with the csv column containing the note text in the line below.
process_csv(False, "BDSPPatientID", "text", path, file_name)
