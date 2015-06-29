def textinfo(path):
    """
    Takes a file path and returns figures about the text file contained therein.
    """
    
    from nltk.corpus import PlaintextCorpusReader
    from nltk import FreqDist
    corpusReader = PlaintextCorpusReader(text, '.*')

    print "Total word count:", len([word for sentence in corpusReader.sents() for word in sentence])
    print "Unique words:", len(set(corpusReader.words()))
    print "Sentences:", len(corpusReader.sents())
    print "Average sentence length in words:", (len([word for sentence in corpusReader.sents() for word in sentence]) / len(corpusReader.sents()))
    
textinfo('/Users/christopherstewart/Desktop/work/DS_bootcamps/Galvanize/tech_challenge/py_scripts/_1/')