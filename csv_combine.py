import os

def main(corpusFolder):
	fout = open(corpusFolder + "normalized_postag_counts.csv", 'a')

	categories = ["06_ID", "07_I_recipe", "09_O_blog", "10_O_advice", "11_O_religion", \
				"12_O_review", "16_IP_sale", "19_N_personal", "20_N_travel", \
				"21_N_sport", "22_N_news", "27_IDE_faq", "28_IDE_pers", "29_IDE_blog", \
				"30_IDE_ency", "31_IDE_res"]

	for cat in categories:
		f = open(corpusFolder + "%s_normalized_postag_counts" % cat + ".csv")
		i = 0
		for line in f:
			if i == 0:
				i += 1
				continue
			fout.write(line)
			i += 1
		f.close()
	fout.close()

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='rename files to not contain spaces')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
