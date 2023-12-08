# Make BLSA Open and Permissioned Datasets for GAAIN

This project contains code that can be used to make BLSA Open and Permissioned Datasets for GAAIN.

## How to use the project

### Pull or download this repository

Here what the folder structure for the project should look like once you have pulled or downloaded the repository:

```
root/
├── data/
│   ├── input/
│   │   ├── detailed-metadata.csv
│   └── output/    
├── src/
│   ├── gaain_helpers.py    
│   └── make-gaain-open-and-permissioned.py
└── readme.md
```   
 
### Update the value of `path_to_sharing_folder`

In the `make-gaain-open-and-permissioned.py` file, you'll find a variable called `path_to_sharing_folder`.  

#### If you have synced `4-sharing` folder to your computer ...

If you have synced the `4-sharing` folder that's on the BLSA SPO site to your computer, then update the value of this variable so that it points to the `4-sharing` folder on the BLSA SPO site from your computer.

For example:

```
path_to_sharing_folder = "~/National Institutes of Health/NIA BLSA - 4-Share"
```


#### If you haven't  synced `4-sharing` folder to your computer ...

Alternatively, if you haven't synced the `4-sharing` folder to your computer, then download the required datasets from the SPO site and point `path_to_sharing_folder` to the location of the downloaded datasets:

```
path_to_sharing_folder = "path/to/downloaded/datasets"
```

Here is a list of the datasets you'll have to download from the :

- `der_cohort`
- `der_cohort_id`
- `der_demographics`
- `der_anthropometry`
- `der_physicalfunction`
- `der_physicalperformance`
- `der_cognition`
- `der_medicalhx`
- `crbsh_blsaapoe`
- `crbsh_bvr`
- `crbsh_cardrot`
- `crbsh_cvl`
- `crbsh_digitspan`
- `crbsh_mms`
- `crbsh_neubos`
- `crbsh_neuflu`
- `crbsh_neutrails`


### Run the main program

From the `./src` folder, run the following command:

```
python make-gaain-open-and-permissioned.py
```

This should create two datasets in the `./data/output` folder:
- `gaain-open-dataframe.csv`
- `gaain-permissioned-dataframe.csv`
