# Make BLSA Open and Permissioned Datasets for GAAIN

This project contains code that can be used to make BLSA Open and Permissioned Datasets for GAAIN.

## How to use the project

### Set up folder strucutre

Here is the recommended folder structure for the project:

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
 
### Update the path to the `4-sharing` folder

In the `make-gaain-open-and-permissioned.py` file, you'll find a variable called `path_to_sharing_folder`.  
Update the value of this variable so that it points to the `4-sharing` folder on the BLSA SPO site from your computer.

For example:

```
path_to_sharing_folder = "~/National Institutes of Health/NIA BLSA - 4-Share"
```

### Run the main program

From the `./src` folder, run the following command:

```
python make-gaain-open-and-permissioned.py
```

This should create two datasets in the `./data/output` folder:
- `gaain-open-dataframe.csv`
- `gaain-permissioned-dataframe.csv`