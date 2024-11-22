import numpy as np

def finding_label(local, data):
    full = len(data)
    begin, end, label,  = local
    begin, end = int(begin), int(end)
    string = data[begin:end]
    return string, label


def extracting_data_local(data):
    texts = []
    labels = {}
    for i in range(len(data)):
        text = data[i]['text']
        texts.append([text])
        label = data[i]['labels']
        labels[i]=[label]
    texts = np.concatenate(texts)
    return texts, labels


def extract_ground_truth(data, labels):
    targets ={}
    for j in range(len(data)):
        print('data',j)
        dta = data[j]['text']
        shp = np.concatenate(np.array(labels[j])).shape[0]
        targets[j] ={}
        for i in range(shp):
            local = np.concatenate(np.array(labels[j]))[i]
            print(i, local)
            sample, target = finding_label(local = local,
                                            data = dta )
            print(sample, target)
            # Verifica se a chave já existe no dicionário
            if target in targets[j]:
                targets[j][target].append(sample)  # Adiciona à lista existente
            else:
                targets[j][target] = [sample]  # Cria uma nova lista para a chave
    return data, targets








