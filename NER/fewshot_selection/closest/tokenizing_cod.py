import sentencepiece as spm
import cohere
import os
import numpy as np 
import pickle
from tqdm import tqdm
import time

def tokenizing_samples_gemini(train_examples, test_examples, path2save):
    sp = spm.SentencePieceProcessor()
    sp.load("YOUR PATH +/tokenizer.model")
    
    tokenized_train = [[sp.encode(example, out_type=int),i] for i,example in enumerate(train_examples)]
    tokenized_test = [[sp.encode(example, out_type=int),i] for i,example in enumerate(test_examples)]
    
    with open(os.path.join(path2save,"tokenized_train.pkl"), "wb") as f:
        pickle.dump(tokenized_train, f)
    
    with open(os.path.join(path2save,"tokenized_test.pkl"), "wb") as f:
        pickle.dump(tokenized_test, f)
    print('ALL SAVED')



def tokenizing_samples_cohere(texts,kind, path2save):
    co = cohere.Client(['YOUR KEY'])
    
    checkpoint_file = os.path.join(path2save, f'checkpoint_{kind}.txt')
    # Carregar o índice de onde continuar
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'r') as f:
            start_index = int(f.read().strip())+1
    else:
        start_index = 0
    
    # Loop através dos textos, começando do índice salvo
    for i in tqdm(range(start_index, len(texts))):
        text = texts[i]
        response = co.tokenize(text=text, model="command-r-plus-08-2024")  
        try:

            np.save(os.path.join(path2save, f'tokenized_{kind}-{i}.npy'), response)
            
            with open(checkpoint_file, 'w') as f:
                f.write(str(i))
        except Exception as e:
            print(f"Erro: {e}.")
            time.sleep(5)  # Espera um pouco antes de tentar novamente
            continue

    print('ALL SAVED')




def jaccard_similarity(list1, list2):
    intersection = len(set(list1).intersection(list2))
    union = len(set(list1).union(list2))
    return intersection / union

# Comparar cada exemplo de teste com todos os de treino e pegar os 3 mais próximos
def find_closest_examples(test_example, tokenized_train, n_fewshot):
    similarities = [(train_example[1], jaccard_similarity(test_example[0], train_example[0])) 
                    for  train_example in tokenized_train]
    
    # Ordenar pelas similaridades e pegar os 3 maiores
    similarities.sort(key=lambda x: x[1], reverse=True)
    tops = similarities[:n_fewshot]
    return tops
    
def closest_samples(test_tokens, train_tokens, n_fewshot):
    closests={}
    for test_example in test_tokens:
        tops = find_closest_examples(test_example, train_tokens, n_fewshot)
        closests[test_example[1]]=[top[0] for top in tops] 
    return closests



def jaccard_similarity(list1, list2):
    intersection = len(set(list1).intersection(list2))
    union = len(set(list1).union(list2))
    return intersection / union



def find_closest_cohere(len_x_train, len_x_test, n_fewshot,path_tokens):
    all_distances = {}
    for i in range(len_x_test):
        training = np.load(os.path.join(path_tokens, f"tokenized_test-{i}.npy"), allow_pickle=True).item().tokens
        distances = list()
        for j in range(len_x_train):
            testing = np.load(os.path.join(path_tokens, f"tokenized_train-{j}.npy"), allow_pickle=True).item().tokens
            distance = [j, jaccard_similarity(testing, training)]
            distances.append(distance)
        
        #print(distances)
        distances.sort(key=lambda x: x[1], reverse=True)
        tops = distances[:n_fewshot]
        all_distances[i]= [top[0] for top in tops] 
    return all_distances
        
        
    
