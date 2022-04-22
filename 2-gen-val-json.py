from ensurepip import version
from pythainlp.tokenize import word_tokenize
import json
import librosa
import numpy as np
import os
import pandas as pd
import re
import copy
path_start = "."
version="v8"

cv_path = os.path.join(".","cv-corpus-8.0-2022-01-19","th")

wav_path = os.path.join(cv_path,"wavs")

all_path = os.path.join(path_start,version,"validated.tsv")
all_df = pd.read_csv(all_path,sep="\t")

clean_whitespace= re.compile(r'\s\s+')
def build_manifest(df, manifest_path, wav_path):
    with open(manifest_path, 'w') as fout:
        p=0
        for line in list(zip(list(df["path"]),list(df["sentence_fix"]))):
            file, transcript = line
            file2 = copy.copy(file)
            try:
                transcript = transcript#clean_whitespace.sub(' ',(' '.join(word_tokenize(transcript.strip()))).replace('\t',' '))
            except:
                print(line)
                print(df["sentence"][p])
            file = file.replace(".mp3",'.wav')
            audio_path = os.path.join(
                wav_path, file
            )
            duration = librosa.core.get_duration(filename=audio_path)

            # Write the metadata to the manifest
            metadata = {
                "audio_filepath": file2,
                "duration": duration,
                "text": transcript
            }
            json.dump(metadata, fout)
            fout.write('\n')
            p+=1

def find_max(df):
    m=0.0
    for line in list(zip(list(df["path"]),list(df["sentence_fix"]))):
        file, transcript = line
        file = file.replace(".mp3",'.wav')
        audio_path = os.path.join(
            wav_path, file
        )
        duration = librosa.core.get_duration(filename=audio_path)
        if duration > m:
            m = duration
    return m

build_manifest(all_df,os.path.join(path_start,version,"cv-8.0-validated.json"),wav_path)