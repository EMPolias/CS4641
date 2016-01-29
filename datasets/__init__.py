"""Methods for importing the datasets in python-usable format."""

def cifar_batches():
    import cPickle
    data = []
    for batch_num in range(1, 6):
        with open('datasets/cifar-10-batches-py/data_batch_' + str(batch_num), 'rb') as f:
            data.append(cPickle.load(f))
    return data

def cifar_test_batch():
    import cPickle
    with open('datasets/cifar-10-batches-py/test_batch', 'rb') as f:
        data = cPickle.load(f)
    return data

def cifar():
    data_ = cifar_batches() + [cifar_test_batch()]
    join_batches = lambda r1, r2, cat: [x for sublist in [batch[cat] for batch in data_[r1:r2]] for x in sublist]
    return {
            'train': {
                'data': join_batches(0, 4, 'data'),
                'labels': join_batches(0, 4, 'labels')
                },
            'test': {
                'data': join_batches(4, 6, 'data'),
                'labels': join_batches(4, 6, 'labels')
                }
            }


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

