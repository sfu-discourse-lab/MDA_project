import os
import pandas as pd
import sys

def word_length(word):
	""" figure out whether the word is a word

	Args:
		word  A string may be a word
	Return:
		The length of the characters in the word
	"""
	length = 0
	for i in word:
		if ord(i.lower()) in range(ord('a'), ord('z') + 1):
			length += 1
	return length


def count_postag(postag_dict, text_file):
	text_size = 0.0
	word = []
	ttr = 0
	AWL = 0.0 #average word length
	num_words = 0
	with open(text_file) as f:
		for line in f:
			#print(line) # TESTING PURPOSE
			text_size += 1
			if len(line.strip().split('_')) != 2:
				continue
			w, p = line.strip().split('_')
			word.append(w)
			wl = word_length(w)
			if wl:
				num_words += 1
				AWL += wl
			postags = p.split()
			for postag in postags:
				postag = postag.strip('[]') # clean bracks from postag
				if postag in postag_dict:
					postag_dict[postag] += 1
			if text_size == 400:
				ttr = len(set(word)) / text_size*100
	result = list(postag_dict.values())
	normalized_result = [x/text_size * 1000 for x in result]
	if ttr == 0:
		ttr = len(set(word)) / text_size
	AWL = AWL / num_words
	return [result, normalized_result, ttr, AWL]

def main(corpus_folder_dir, feature_file):
	out_folder = "postag_count_result"
	POSTAG_POS = 1
	if not os.path.exists(out_folder):
		os.makedirs(out_folder)
	if not os.path.exists(corpus_folder_dir):
		raise Exception("There is no such corpus folder!", corpus_folder_dir)

	files = os.listdir(corpus_folder_dir)
	counts_file = out_folder + "/postag_counts.csv"
	normalized_counts_file = out_folder + "/normalized_postag_counts.csv"

	try:
		postag_lst = pd.read_csv(feature_file).iloc[:,POSTAG_POS].tolist()
		postag_lst = [p.strip() for p in postag_lst] #remove unnecessary whitespaces
		postag_dict = dict(zip(postag_lst, [0]*len(postag_lst)))
		#write header
		header = postag_dict.keys()
		header_counts = "file_names, " + ','.join(header) + ', TTR, AWL\n'
		with open(counts_file, "w") as out:
			out.write(header_counts)
		header_norm = "file_names, " + ','.join(header) + ', TTR, AWL\n'
		with open(normalized_counts_file, "w") as out:
			out.write(header_norm)

		for f in files:
			postag_dict = dict(zip(postag_lst, [0]*len(postag_lst)))
			result, normalized_result, ttr, AWL= \
			count_postag(postag_dict, corpus_folder_dir + "/" + f)
			result = f + ', ' + \
			str(result).strip('[]') + ', ' + str(ttr) + ', ' + str(AWL) + '\n'
			normalized_result = f + ', ' + \
			str(normalized_result).strip('[]') \
			+ ', ' + str(ttr) + ', ' + str(AWL) + '\n'
			with open(counts_file, "a") as out:
				out.write(result)
			with open(normalized_counts_file, "a") as out:
				out.write(normalized_result)
	
	except IOError:
		print("fail to open features file: " + feature_file)

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description='count the postag frequence\
	 in different corpus')
	parser.add_argument('corpus_path', type=str,
                    help='the path to corpus folder')
	parser.add_argument('postag_file', type=str,
                    help='the path to postag file')
	args = parser.parse_args()
	main(args.corpus_path, args.postag_file)
