import pandas as pd
from pathlib import Path
from tools import subset_of_columns

THIS_FILE = Path(__file__)
THIS_DIR = THIS_FILE.parent
INTERIM_DATA = THIS_DIR.joinpath("../../data/interim/")
PROCESSED_DATA = THIS_DIR.joinpath("../../data/processed/")

FULL_DB = "ripa-2018.csv"

data = pd.read_csv(INTERIM_DATA.joinpath(FULL_DB))

race_ethinicity = subset_of_columns('RAE_', data.columns)
gender = subset_of_columns('G_', data.columns)
disability = subset_of_columns('PD_', data.columns)
reason_for_stop = subset_of_columns('RFS_', data.columns)
action_taken = subset_of_columns('ADS_', data.columns)
basis_for_search = subset_of_columns('BFS_', data.columns)
contraband_evidence_discovered = subset_of_columns('CED_', data.columns)
basis_for_property_seizure = subset_of_columns('BPS_', data.columns)
type_of_property_seized = subset_of_columns('TPS_', data.columns)
result_of_stop = subset_of_columns('ROS_', data.columns)

# Create unique numeric id
data['UNIQUE_ID'] = data['DOJ_RECORD_ID'] + data['PERSON_NUMBER'].astype(str).str.zfill(2)
unique_id_mapping = {}
for idx,value in enumerate(data['UNIQUE_ID'].values, start=1_000_000):
    unique_id_mapping[value] = idx

data['UNIQUE_ID'] = data['UNIQUE_ID'].map(unique_id_mapping)
identifiers = ['UNIQUE_ID']

## Build dfs
race_ethinicity_df = data[identifiers + race_ethinicity].copy()
gender_df = data[identifiers + gender].copy()
disability_df = data[identifiers + disability].copy()
reason_for_stop_df = data[identifiers + reason_for_stop].copy()
action_taken_df = data[identifiers + action_taken].copy()
basis_for_search_df = data[identifiers + basis_for_search].copy()
contraband_evidence_discovered_df = data[identifiers + contraband_evidence_discovered].copy()
basis_for_property_seizure_df = data[identifiers + basis_for_property_seizure].copy()
type_of_property_seized_df = data[identifiers + type_of_property_seized].copy()
result_of_stop_df = data[identifiers + result_of_stop].copy()

columns_left = [
    col for col in data.columns if
    col not in race_ethinicity and
    col not in gender and
    col not in disability and
    col not in reason_for_stop and
    col not in action_taken and 
    col not in basis_for_search and
    col not in contraband_evidence_discovered and
    col not in basis_for_property_seizure and
    col not in type_of_property_seized and
    col not in result_of_stop
]

base = data[columns_left].copy()

# Cleaning ADS
for col in action_taken_df.columns:
    if action_taken_df[col].dtype == 'object':
        action_taken_df[col] = action_taken_df[col].astype(str)

## Saving
base.set_index("UNIQUE_ID", inplace = True)
race_ethinicity_df.set_index("UNIQUE_ID", inplace = True)
gender_df.set_index("UNIQUE_ID", inplace = True)
disability_df.set_index("UNIQUE_ID", inplace = True)
reason_for_stop_df.set_index("UNIQUE_ID", inplace = True)
action_taken_df.set_index("UNIQUE_ID", inplace = True)
basis_for_search_df.set_index("UNIQUE_ID", inplace = True)
contraband_evidence_discovered_df.set_index("UNIQUE_ID", inplace = True)
basis_for_property_seizure_df.set_index("UNIQUE_ID", inplace = True)
type_of_property_seized_df.set_index("UNIQUE_ID", inplace = True)
result_of_stop_df .set_index("UNIQUE_ID", inplace = True)

print("Saving datasets...")
base.to_csv(PROCESSED_DATA / "aa_main_table.csv", encoding='utf-8')
race_ethinicity_df.to_csv(PROCESSED_DATA / "race_ethnicity.csv", encoding='utf-8')
gender_df.to_csv(PROCESSED_DATA / "gender.csv", encoding='utf-8')
disability_df.to_csv(PROCESSED_DATA / "disability.csv", encoding='utf-8')
reason_for_stop_df.to_csv(PROCESSED_DATA / "reason_for_stop.csv", encoding='utf-8')
action_taken_df.to_csv(PROCESSED_DATA / "action_taken.csv", encoding='utf-8')
basis_for_search_df.to_csv(PROCESSED_DATA / "basis_for_search.csv", encoding='utf-8')
contraband_evidence_discovered_df.to_csv(PROCESSED_DATA / "contraband_evidence_discovered.csv", encoding='utf-8')
basis_for_property_seizure_df.to_csv(PROCESSED_DATA / "basis_for_property_seizure.csv", encoding='utf-8')
type_of_property_seized_df.to_csv(PROCESSED_DATA / "type_of_property_seized.csv", encoding='utf-8')
result_of_stop_df.to_csv(PROCESSED_DATA / "resulf_of_stop.csv", encoding='utf-8')