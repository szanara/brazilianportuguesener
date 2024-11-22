import cohere
import numpy as np
import pandas as pd
import re

def extract_entities(text: str):
    key = '[YOUR_KEY]' 
    co = cohere.Client(api_key=key)
    response = co.chat(
    model="command-r-plus",
    message=f"Identifique as entidades nomeadas na frase: {text} e de a sua classe"
         )
    gen = response.text
 
    return gen
    
def extract_entities_tip(text: str, labels:list):
    key = '[YOUR_KEY]' 
    co = cohere.Client(api_key=key)
    response = co.chat(
    model="command-r-plus",
    message=f"Identifique as entidades nomeadas no texto {text}.Os labels esperados sao {labels}. Retorne no formato  LISTA DE TUPLAS com o formato (entidade, label)"
         )
    gen = response.text
 
    return gen


def extract_entities_fewshot(text: str, examples:list):
    key = '[YOUR_KEY]'
    co = cohere.Client(api_key=key)
    response = co.chat(
    model="command-r-plus",
    message=f"Identifique as entidades nomeadas no texto {text}, baseando-se no exemplo:{examples}.  Retorne no formato  LISTA DE TUPLAS com o formato [(entidade1, label1),...]"
         )
    gen = response.text
 
    return gen

def extract_entities_fewshot_tip(text: str, examples:list,waited:list):
    
    key = '[YOUR_KEY]'
    co = cohere.Client(api_key=key)
    response = co.chat(
    model="command-r-plus",
    message=f"Identifique as entidades nomeadas no texto {text}, baseando-se nos exemplos {examples}. Os labels esperados sao:{waited}. Retorne no formato  lista de tuplas com o formato(entidade, label)"
         )
    gen = response.text
 
    return gen


def converting(input_string):
    # Divide a string em linhas
    lines = input_string.strip().split('\n')
    extracted_entities = []

    try:
        for line in lines:
            if line.strip().lower() == "classes:":
                break
            
            # Verifica se a linha contém um "-"
            if '-' in line:
                # Divide a linha em duas partes: antes e depois do ":"
                part_before, part_after = line.split(':', 1)
                
                # Verifica se existem múltiplos valores
                if ',' in part_after:
                    all_values = part_after.strip().split(',')
                else:
                    all_values = [part_after.strip()]  # Mantém em uma lista, mesmo se houver apenas um valor
                
                # Remove espaços em branco e o símbolo "-"
                entity = part_before.replace('-', '').strip()
                
                # Adiciona a entidade e seus valores
                extracted_entities.append(f"({entity}, {', '.join(value.strip() for value in all_values)})")

        # Se a lista extraída estiver vazia, tenta outro formato
        if not extracted_entities:
            raise ValueError("No entities found in the first format.")
    
    except ValueError as e:
        # Implementar aqui o segundo formato de leitura, caso necessário
        print(f"Attempting alternative format due to: {e}")
        
        # Tente o segundo formato (defina o que isso significa)
        for line in lines:
            if line.strip().lower() == "classes:":
                break
            
            # Novo formato pode ser apenas um exemplo de lógica de leitura
            if ':' in line:
                part_before, part_after = line.split(':', 1)
                extracted_entities.append(f"({part_before.strip()}, {part_after.strip()})")

        # Se ainda estiver vazio, lança um erro
        if not extracted_entities:
            raise ValueError("No entities found in any format.")

    # Retorna as entidades unidas por vírgulas
    return ', '.join(extracted_entities)
