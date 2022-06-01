# Thai CommonVoice Dataset
Thai CommonVoice Dataset (upstream dataset from VISTEC)

This project include script, dataset and more. It is use in ASR lab at VISTEC.

## Steps

1. make validated_clean.tsv
2. split data and increase data from old version.

### Make validated_clean.tsv

run notebook in make_datasets

### Split new data

1. create new folder and copy validated_clean.tsv to that folder.
2. edit 1-merge.py
3. edit 2-gen-val-json.py
4. edit 3-gen.py
5. run