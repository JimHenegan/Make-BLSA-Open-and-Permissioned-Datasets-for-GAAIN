import pandas as pd

from gaain_helpers import (
    make_df_metadata_gaain, 
    make_df_gaain_permissioned_cohort,
    make_df_gaain_open_cohort,
    make_df_base_gaain,
    make_df_gaain_permissioned,
    make_df_gaain_open    
)

"""
Make "open" and "permissioned" datasets for GAAIN

# Inputs
# ------

- detailed-metadata.csv : a CSV file of metadata downloaded from the BLSA-Explore-ME
- path_to_sharing_data_csv_folder : the path you use to access the "4-sharing" folder of BLSA Data 

# Main steps
# ----------

- Make df_metadata_gaain: a dataframe containing metadata about the variables that have been selected for GAAIN 
  
- Establish the "cohorts" for GAAIN
  - Make df_gaain_permissioned_cohort: determine which idno + visit pairs are going to the permissioned dataset
  - Make df_gaain_open_cohort: determine which idno + visit pairs are going to the open dataaset  

- Create df_base_gaain : a dataset containing the GAAIN variables (plus the real BLSA idno) for *all* BLSA participants

- Use the "cohorts" with df_base_gaain to make df_gaain_open and df_gaain_permissioned
"""

# Setup
# -----

# Input
path_to_detailed_metadata = "../data/input/detailed-metadata.csv" 
path_to_sharing_data_csv_folder = "YOUR_PATH_TO_SHARING_DATA_CSV_FOLDER" 
path_to_der_cohort = f'{path_to_sharing_data_csv_folder}/der_cohort.csv'
path_to_der_cohort_id = f'{path_to_sharing_data_csv_folder}/der_cohort_id.csv'

# Output
path_to_open_gaain_dataset = "../data/output/gaain-open-dataframe.csv"
path_to_permissioned_gaain_dataset = "../data/output/gaain-permissioned-dataframe.csv"

# Constants
DATA_ECOSYSTEM_LIST = ['ADDI, GAAIN', 'GAAIN']

# Helper Functions
# ----------------

# Main Program
# ------------

# Make df_metadata_gaain: a dataframe containing metadata about the variables that have been selected for GAAIN
df_metadata_gaain = make_df_metadata_gaain(path_to_detailed_metadata, DATA_ECOSYSTEM_LIST)

# Establish the "cohorts" for GAAIN
df_gaain_permissioned_cohort = make_df_gaain_permissioned_cohort(path_to_der_cohort_id)
df_gaain_open_cohort = make_df_gaain_open_cohort(path_to_der_cohort_id)

# Create df_base_gaain : a dataset containing the GAAIN variables (plus the real BLSA idno) for *all* BLSA participants
df_base_gaain = make_df_base_gaain(path_to_der_cohort, df_metadata_gaain, path_to_sharing_data_csv_folder)

# Use the "cohorts" with df_base_gaain to make df_gaain_open and df_gaain_permissioned
df_gaain_open = make_df_gaain_open(df_gaain_open_cohort, df_base_gaain)
df_gaain_permissioned = make_df_gaain_permissioned(df_gaain_permissioned_cohort, df_base_gaain)

# Write to disk
df_gaain_open.to_csv(path_to_open_gaain_dataset, index=False)
df_gaain_permissioned.to_csv(path_to_permissioned_gaain_dataset, index=False)