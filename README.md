Ref: [52nlp](http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C)

1. Download Wiki Dump:

    https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

2. Prerocess:

        python process_wiki.py enwiki-latest-pages-articles.xml.bz2 wiki.en.text

3. Train 

    python train_word2vec_model.py wiki.en.text wiki.en.text.model wiki.en.text.vector
