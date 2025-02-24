## MDA_project

This repository contains scripts for data pre-processing and parts-of-speech tag (POS-tag) retrieval used in the context of several ongoing multi-dimensional analysis projects:

* [Analysing online comments and traditional registers](https://github.com/sfu-discourse-lab/MDA-OnlineComments)

* [Analysing online commments and other online registers](https://github.com/sfu-discourse-lab/MDA-OnlineRegisters)

* [Analysing podcasts vs. spoken registers and vs. computer-mediated communication](https://github.com/sfu-discourse-lab/MDA-podcasts)

## Related publications

* Ehret, K., L. Bosman, A. Babayode, N. Chan, I. Fong, N. Harris, A. Hewton, D. Reid, R. Wong and M. Taboada (to appear) Podcasts as an emerging register of computer-mediated communication. _Register Studies_.

* Ehret, K. and M. Taboada (2021) [Characterising online news comments: A multi-dimensional cruise through online registers](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.643770/full). _Frontiers in Artificial Intelligence – Language and Computation_ 4(79): 10.3389/frai.2021.643770.

* Ehret, K. and M. Taboada (2021) [The interplay of complexity and subjectivity in opinionated discourse](https://www.sfu.ca/~mtaboada/docs/publications/Ehret_Taboada_DiscourseStudies.pdf). _Discourse Studies_ 23(2): 141-165.

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

This script removes artifacts from the data collection process in the [Corpus of Online Registers of English](https://www.english-corpora.org/core/) (CORE). The script removes all occurences of html tags within the data as well as strings of dashes, underscores and tildes that are longer than 4 tokens. The script also removes the initial lines of each CORE file since they contain metadata about where the data was collected.

The script takes one argument, the path to the input corpus (a directory). The script can be called with 

    python CORE_cleanup.py path/to/input/corpus/

#### csv_combine.py

This script combines the individual postag_counts.csv files into one combined postag_counts.csv for all subcorpora of CORE. The same can be done for the normalized_postag_counts.csv files by replacing the name of the file on line 4 and line 12 with 'normalized_postag_counts'.

Keep in mind that this script only works if the individual postag_counts.csv files were renamed by prepending the corresponding subcorpora identifier to the file name such as "06_ID__postag_counts.csv".

The script takes one argument, the path to the directory containing the .csv files. The script can be called with

    python csv_combine.py path/to/input/directory/

#### dataSelection.py

This script samples all comment threads comprised in the [SFU Opinion and Comments Corpus](https://github.com/sfu-discourse-lab/SOCC) (SOCC) with a minimum length of 700 words. The script retrieves all comment threads with a minimum length of 700 words and stores them in a folder named 'threads' at a location specified by the user.

The script takes two arguments, the path to the SOCC csv file and the path to the location where the 'threads' folder will be created. The script can be called with

    python dataSelection.py /path/to/input/csv/ /path/to/storage/location/

#### SOCC_cleanup.py

This script removes artifacts from the data collection process in the [SFU Opinion and Comments Corpus](https://github.com/sfu-discourse-lab/SOCC) (SOCC). The script removes all occurences of html tags within the data as well as strings of dashes, underscores and tildes that are longer than 4 tokens.

The script takes one argument, the path to the input corpus (a directory). The script can be called with 

    python SOCC_cleanup.py path/to/input/corpus/



