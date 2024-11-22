import random 
import pandas as pd 
import numpy as np
import os 

def fewshot_samples(texts_train, labels_train, nfewshot_value, path2save):
    indices = random.sample(range(len(texts_train)), k=nfewshot_value)
    
    # Selecionar amostras e labels correspondentes
    amostras = texts_train[indices]
    #print(indices)
    labels_all = []
    for ind in indices:
        labels_all.append(labels_train[ind])
    
    # Exibir as amostras e labels correspondentes
    #print("Amostras selecionadas:", amostras)
    #print("Labels correspondentes:", labels_all)
    exemplo = []
    
    for sample, label in zip(amostras, labels_all):
        # Adiciona um novo dicionário com as chaves 'texto' e 'ner' para cada iteração
        exemplo.append({'texto': sample, 'ner': label})

    np.save(os.path.join(path2save, f'amostras_selecionadas_{nfewshot_value}.npy'), exemplo) 
    
    return exemplo