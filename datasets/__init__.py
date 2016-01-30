"""Methods for importing the datasets in python-usable format."""

from collections import Counter

import random


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
    train_data, train_labels = shuffle_data(join_batches(0, 4, 'data'), join_batches(0, 4, 'labels'))
    test_data, test_labels = shuffle_data(join_batches(4, 6, 'data'), join_batches(4, 6, 'labels'))

    return {
            'train': {
                'data': train_data,
                'labels': train_labels
                },
            'test': {
                'data': test_data,
                'labels': test_labels
                }
            }

def shuffle_data(data, labels):
    z = zip(data, labels)
    random.shuffle(z)
    return zip(*z)


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

def sentiment(bag_size=100):
    data_ = sentiment_imdb() + sentiment_amazon() + sentiment_yelp()

    # Calculate the bag_size most common words.
    all_words = Counter()
    for example, _ in data_:
        for word in example.split(' '):
            all_words[word] += 1
    bag_of_words = all_words.most_common(bag_size)

    print bag_of_words

    # Create features (whether example has each of the words in bag).
    data = []
    labels = []
    word_in_example = lambda word, example: 1 if word in example else 0
    for example, label in data_:
        labels.append(label)
        data.append([word_in_example(word, example) for word, _ in bag_of_words])

    # Shuffle data and separate into train and test set.
    data, labels = shuffle_data(data, labels)
    offset = int(len(data) * 0.7)
    return {
            'train': {
                'data': data[0:offset],
                'labels': labels[0:offset]
                },
            'test': {
                'data': data[offset:],
                'labels': labels[offset:]
                }
            }
