## MDA_project

This repository contains scripts for data pre-processing and parts-of-speech tag (POS-tag) retrieval used in the context of several ongoing multi-dimensional analysis projects:

* [Analysing online comments and traditional registers](https://github.com/sfu-discourse-lab/MDA-OnlineComments)

* [Analysing online commments and other online registers](https://github.com/sfu-discourse-lab/MDA-OnlineRegisters)

### Description of the files for POS-retrieval

#### postag_counter.py

This script extracts the frequencies of 67 lexico-grammatical features on the basis of parts-of-speech tags. The script was specifically designed to retrieve the tagset used by the *Multidimensional Analysis Tagger* (MAT, https://sites.google.com/site/multidimensionaltagger/home). The script outputs a folder with two csv files: postag_counts.csv and normalized_postag_counts.csv

postag_counts.csv contains the raw frequencies of each of the features as columns and the filenames of the input texts as rows. normalized_postag_counts.csv contains the normalized (per 1000 words of running text) feature frequencies as columns and the filenames of the corpus texts as rows. An exception is the feature AWL (average word length) which is not normalised, and TTR (type-toke-ratio) which is calculated for the first 400 words in each text of the input corpus.

The script takes two arguments, the path to the input corpus (a directory) and the path to the list of POS-tags (see features_to_MATtags.csv). The script can be initialised with
  
    python postag_counter.py path/to/input/corpus path/to/features_to_MATtags.csv


#### features_to_MATtags.csv

A csv file listing each of the POS-tags together with a short description of the feature. This file is required by postag_counter.py

### Description of the files for data pre-processing

#### CORE_cleanup.py

This script removes artifacts from the data collection process in the [Corpus of Online Registers of English](https://www.english-corpora.org/core/) (CORE).

#### csv_combine.py

Description coming soon.

#### dataSelection.py

This script samples all comment threads comprised in the [SFU Opinion and Comments Corpus](https://github.com/sfu-discourse-lab/SOCC) (SOCC) with a minimum length of 700 words.

#### SOCC_cleanup.py

This script removes artifacts from the data collection process in the [SFU Opinion and Comments Corpus](https://github.com/sfu-discourse-lab/SOCC) (SOCC).



