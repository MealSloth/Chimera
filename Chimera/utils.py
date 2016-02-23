from django.core.serializers import serialize


def model_to_dict(model):
    dictionary = {}
    model_dictionary = serialize('python', [model, ])[0].get('fields')
    print(model_dictionary)
    for key, value in model_dictionary.iteritems():
        dictionary[key] = value
    return dictionary
