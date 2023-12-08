import pandas as pd

def make_df_metadata_gaain(path_to_detailed_metadata, DATA_ECOSYSTEM_LIST):
    
    # Load the detailed-metadata.csv file
    df_metadata = pd.read_csv(path_to_detailed_metadata)
    
    # Select relevant columns
    df_metadata_selected = df_metadata[
        [
            'table_name',
            'var_name',
            'open_access',
            'data_ecosystem'
        ]
    ]
    
    # Filter to variables that are going to GAAIN
    df_metadata_selected_filtered = df_metadata_selected[df_metadata_selected['data_ecosystem'].apply(lambda x: x in DATA_ECOSYSTEM_LIST)]    
    return df_metadata_selected_filtered


def make_df_gaain_permissioned_cohort(path_to_der_cohort_id):
    df_der_cohort_id = pd.read_csv(path_to_der_cohort_id, low_memory=False)
    df_der_cohort_id_selected = df_der_cohort_id[['id_gaain', 'idno', 'visit']]
    df_der_cohort_id_selected_filtered_to_gaain = df_der_cohort_id_selected[df_der_cohort_id_selected['id_gaain'].notna()]
    return df_der_cohort_id_selected_filtered_to_gaain


def make_df_gaain_open_cohort(path_to_der_cohort_id):
    df_der_cohort_id = pd.read_csv(path_to_der_cohort_id, low_memory=False)
    df_der_cohort_id_selected = df_der_cohort_id[['id_gaain', 'idno', 'visit', 'openrow']]
    df_der_cohort_id_selected_filtered_to_gaain = df_der_cohort_id_selected[df_der_cohort_id_selected['id_gaain'].notna()]
    df_der_cohort_id_selected_filtered_to_gaain_open = df_der_cohort_id_selected_filtered_to_gaain[df_der_cohort_id_selected_filtered_to_gaain['openrow'] == 1]
    return df_der_cohort_id_selected_filtered_to_gaain_open


def make_df_base_gaain(path_to_der_cohort, df_metadata_gaain, path_to_sharing_folder):
                       
    # Begin by creating df_base : a "base dataframe" containing the 'idno' and 'visit' columns from the der_cohort table
    df_base = pd.read_csv(path_to_der_cohort, low_memory=False)[['idno', 'visit']]

    # Merge in variables from other tables
    # ------------------------------------

    # Make a list of table_name's from df_metadata_gaain
    list_of_table_names = df_metadata_gaain['table_name'].unique()

    # For each table in list_of_table_names...
    for table_name in list_of_table_names:    

        # Filter df_metadata_gaain to variables in that table
        df_metadata_gaain_filtered = df_metadata_gaain[df_metadata_gaain['table_name'] == table_name]

        # Store the resulting var_names
        list_of_var_names = df_metadata_gaain_filtered['var_name'].to_list()

        # load the table
        path_to_table = f'{path_to_sharing_folder}/{table_name}.csv'
        df = pd.read_csv(path_to_table, low_memory=False)   

        # Rename Idno and Visit columns (may be necessary for CRBShare tables)
        df_renamed = df.rename(columns={"Idno" : "idno", "Visit"  : "visit"})    

        # Figure out the joiners and the keep_vars for this table        
        joiner_vars = ['idno']
        keep_vars = ['idno']     

        if 'visit' in df_renamed.columns:
            keep_vars += ['visit']
            joiner_vars += ['visit']

        keep_vars += [v for v in list_of_var_names if v not in keep_vars and v != "Visit"] 

        # Select the variables that you need to keep
        df_renamed_selected = df_renamed[keep_vars]

        # Filter to rows where 'visit' is an integer
        # (relevant for CRBShare cognition data)
        if 'visit' in df_renamed_selected.columns:
            df_renamed_selected_filtered = df_renamed_selected[df_renamed_selected['visit'].astype(int) == df_renamed_selected['visit']].copy()    
            df_renamed_selected_filtered['visit'] = df_renamed_selected_filtered['visit'].astype(int)

        else:
            df_renamed_selected_filtered = df_renamed_selected

        # merge with df_base
        df_base = df_base.merge(df_renamed_selected_filtered, on=joiner_vars, how='left')

    # Rearrange columns
    new_col_order = ['idno', 'id_gaain', 'visit']
    new_col_order += [c for c in df_base.columns if c not in new_col_order]
    df_base_rearranged = df_base[new_col_order]
    
    return df_base_rearranged


def make_df_gaain_permissioned(df_gaain_permissioned_cohort, df_base_gaain):
    df_gaain_permissioned = df_gaain_permissioned_cohort.merge(df_base_gaain, how='left').drop(columns=['idno'])
    df_gaain_permissioned['id_gaain'] = df_gaain_permissioned['id_gaain'].astype(int)
    df_gaain_permissioned_sorted = df_gaain_permissioned.sort_values(['id_gaain', 'visit'])
    return df_gaain_permissioned_sorted


def make_df_gaain_open(df_gaain_open_cohort, df_base_gaain):
    df_gaain_open = df_gaain_open_cohort.merge(df_base_gaain, how='left').drop(columns=['idno', 'openrow'])
    df_gaain_open['id_gaain'] = df_gaain_open['id_gaain'].astype(int)
    df_gaain_open_sorted = df_gaain_open.sort_values(['id_gaain', 'visit'])
    return df_gaain_open_sorted

