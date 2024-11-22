import google.generativeai as genai
import typing


# Configurar a chave da API
genai.configure(api_key=['YOUR KEY'])


class Entity(typing.TypedDict):
    entity: str
    label: str

def extract_entities(text: str) -> list[Entity]:
    # Usando um modelo de NER
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    # Geração do conteúdo
    resultado = model.generate_content(
        f"Identifique as entidades nomeadas no texto {text}.Os labels esperados sao {labels}. Retorne no formato  LISTA DE TUPLAS com o formato (entidade, label)",
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )
    #print(resultado)
    # Assuming 'resultado' is your GenerateContentResponse object
    try:
        # Accessing the text directly
        output = resultado.candidates[0].content.parts[0].text
        #print(output)
    except Exception as e:
        print("An error occurred:", e)
 
    return output



def extract_entities_tip(text: str,labels:list) -> list[Entity]:
    # Usando um modelo de NER
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    # Geração do conteúdo
    resultado = model.generate_content(
        f"Identifique as entidades nomeadas no texto {text}.Os labels esperados sao {labels}. Retorne no formato  lista de tuplas com o formato(entidade, label)",
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )
    #print(resultado)
    # Assuming 'resultado' is your GenerateContentResponse object
    try:
        # Accessing the text directly
        output = resultado.candidates[0].content.parts[0].text
        #print(output)
    except Exception as e:
        print("An error occurred:", e)
 
    return output



import json

def converting(entities):
    # Sua string JSON
    json_string = entities
    
    # Convertendo a string JSON em um dicionário
    data_dict = json.loads(json_string)
    
    # Exibindo o dicionário resultante
    #print(data_dict)
    configured_entities = {(label, entity) for label in data_dict.keys() for entity in data_dict[label]}
    return configured_entities






def extract_entities_fewshot(text: str, examples:list) -> list[Entity]:
    # Usando um modelo de NER
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    # Geração do conteúdo
    resultado = model.generate_content(
        f"IIdentifique as entidades nomeadas no texto {text}, baseando-se nos exemplos {examples}. Retorne no formato  lista de tuplas com o formato(entidade, label)",
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )
    #print(resultado)
    # Assuming 'resultado' is your GenerateContentResponse object
    try:
        # Accessing the text directly
        output = resultado.candidates[0].content.parts[0].text
        #print(output)
    except Exception as e:
        print("An error occurred:", e)
    return output

def extract_entities_fewshot_tip(text: str, examples:list, waited:list) -> list[Entity]:
    # Usando um modelo de NER
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    # Geração do conteúdo
    resultado = model.generate_content(
        f"Identifique as entidades nomeadas no texto {text}, baseando-se nos exemplos {examples}. Os labels esperados sao:{waited}. Retorne no formato  lista de tuplas com o formato(entidade, label)",
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )
    #print(resultado)
    # Assuming 'resultado' is your GenerateContentResponse object
    try:
        # Accessing the text directly
        output = resultado.candidates[0].content.parts[0].text
        #print(output)
    except Exception as e:
        print("An error occurred:", e)
    return output



def converting_fewshot(entities):
    try: 
        json_string = entities  # Assuming `entities` is a JSON string
        print('Testando 1')
        
        # Attempt to convert JSON string into a dictionary (First format)
        data_dict = json.loads(json_string)  
        data_dict = data_dict.get('ner', {})  # Fetch 'ner' key if it exists
        
        # Configure entities based on the first format
        configured_entities = {(label, entity) for label in data_dict.keys() for entity in data_dict[label]}
        
        if not configured_entities:
            raise ValueError("No entities found in the first format.")
        
    except (ValueError, json.JSONDecodeError) as e:
        print('Testando 2')
        print(f"Attempting alternative format due to: {e}")
        
        try:
            # Attempt the second trial, assuming the format might be different
            json_string = entities  # Again assuming `entities` is a JSON string
            data_dict = json.loads(json_string)  # Convert string to dict
            
            # Configure entities in the alternative format
            configured_entities = {(label, entity) for label in data_dict.keys() for entity in data_dict[label]}
            
            if not configured_entities:
                raise ValueError("No entities found in the second format.")
        
        except (ValueError, json.JSONDecodeError) as e2:
            print('Testando 3')
            print(f"Attempting final format due to: {e2}")
            
            try:
                # Final trial assuming `entities` might already be a Python dictionary
                data_dict = entities.get('ner', {})  # Directly access 'ner' if entities is a dictionary
                
                # Configure entities in the final format
                configured_entities = {(label, entity) for label in data_dict.keys() for entity in data_dict[label]}
                
                if not configured_entities:
                    raise ValueError("No entities found in the final format.")
            
            except ValueError as e3:
                print('Testando 4')
                print(f"Final failure: {e3}")
                
    return configured_entities
