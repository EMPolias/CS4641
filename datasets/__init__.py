"""Methods for importing the datasets in python-usable format."""

def cifar_train():
    import cPickle
    data = {}
    for batch_num in range(1, 6):
        with open('datasets/cifar-10-batches-py/data_batch_' + batch_num, 'rb') as f:
            data['batch_' + batch_num] = cPickle.load(f)
    return data

def cifar_test():
    import cPickle
    with open('datasets/cifar-10-batches-py/test_batch', 'rb') as f:
        data = cPickle.load(f)
    return data

def cifar():
    data = cifar_train()
    data['test_batch'] = cifar_test()
    return data


def read_sentiment_data(f_name):
    data = []
    with open('datasets/sentiment_labelled_sentences/' + f_name, 'rb') as f:
        review = ''
        for line in f:
            if line[-2] in ['0', '1']:
                data.append((review + line[:-3], line[-2]))
                review = ''
            else:
                review += line
    return data

def sentiment_imdb():
    return read_sentiment_data('imdb_labelled.txt')

def sentiment_amazon():
    return read_sentiment_data('amazon_cells_labelled.txt')

def sentiment_yelp():
    return read_sentiment_data('yelp_labelled.txt')

