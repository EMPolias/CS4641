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
