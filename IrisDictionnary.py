iris = {}

def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    dic = {id_n:
    {'species' : species,
    'petal_length' : petal_length,
    'petal_width' : petal_width}
    }
    for key,value in kwargs.items():
        if kwargs :
            dic[id_n][key] = value
    iris.update(dic)


add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac', petal_h= 'pale lilac')
print(iris)

''' # autre maniere de faire
iris = {}

def add_iris(id_n, species, petal_length, petal_width, **new_features):
    iris[id_n] = {
        "species": species,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    for key, feature in new_features.items():
        iris[id_n][key] = feature'''