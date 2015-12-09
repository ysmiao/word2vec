from nltk import word_tokenize

if __name__ == '__main__':
	fin = open(sys.argv[1],'r')
	fout = open(sys.argv[2],'w')
	while 1:
	    line = fin.readline()
	    if not line:
	        break
	    data = line.decode("ascii",'ignore')
	    words = word_tokenize(data.encode('UTF-8'))
	    for word in words:
	        fout.write(word.lower()+' ')
	    fout.write('\n')
	fin.close()
	fout.close()
