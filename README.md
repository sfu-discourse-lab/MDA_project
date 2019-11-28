## MDA_project

This repository contains scripts for parts-of-speech tag (POS-tag) retrieval used in the context of several ongoing multi-dimensional analysis projects. 

### Description of the files

#### postag_counter.py

This script extracts the frequencies of 67 lexico-grammatical features on the basis of parts-of-speech tags. The script was specifically designed to retrieve the tagset used by the *Multidimensional Analysis Tagger* (MAT, https://sites.google.com/site/multidimensionaltagger/home). The script outputs a folder with two csv files: postag_counts.csv and normalized_postag_counts.csv

postag_counts.csv contains the raw frequencies of each of the features as columns and the filenames of the input texts as rows. normalized_postag_counts.csv contains the normalized (per 1000 words of running text) feature frequencies as columns and the filenames of the corpus texts as rows. An exception is the feature AWL (average word length) which is not normalised, and TTR (type-toke-ratio) which is calculated for the first 400 words in each text of the input corpus.

The script takes two arguments, the path to the input corpus (a directory) and the path to the list of POS-tags (see features_to_MATtags.csv). The script can be initialised with
  
    python postag_counter.py path/to/input/corpus path/to/features_to_MATtags.csv


#### features_to_MATtags.csv

A csv file listing each of the POS-tags together with a short description of the feature. This file is required by postag_counter.py
