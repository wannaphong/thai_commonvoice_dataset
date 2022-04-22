import os
import pandas as pd
import glob

path_start = "."
before = os.path.join(path_start,"v7")
after = os.path.join(path_start,"v8")

all_file = []

for i in glob.glob(os.path.join(before,'*.tsv')):
    df = pd.read_csv(i, sep='	')
    all_file.extend(list(df['path']))

validated_df = pd.read_csv(os.path.join(after,"validated_clean.tsv"),sep="\t")
# เอาเฉพาะประโยคใหม่
validated_df_clean = validated_df[~validated_df['path'].isin(all_file)]
validated_df_clean.to_csv(os.path.join(after,"validated.tsv"), sep="\t", index=False)
# เก็บประโยคก่อนหน้าไว้
validated_df_in = validated_df[validated_df['path'].isin(all_file)]
validated_df_in.to_csv(os.path.join(after,"validated_in.tsv"), sep="\t", index=False)