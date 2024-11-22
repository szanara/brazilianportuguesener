import numpy as np

def processar_entidades(texto):
    entidades = []
    
    # Dividindo o texto por linhas
    linhas = texto.splitlines()
    
    # Label atual será usada para diferenciar Pessoa de Organização
    label_atual = None
    
    # Iterar sobre cada linha
    for linha in linhas:
        linha = linha.strip()  # Remove espaços extras
        
        # Verifica se é um rótulo
        if "Pessoa:" in linha:
            label_atual = "PESSOA"
        elif "Organização:" in linha:
            label_atual = "ORGANIZAÇÃO"
        elif linha.startswith('-'):  # Verifica se a linha é uma entidade
            entidade = linha[1:].strip()  # Remove o traço e espaços, mantém a entidade original
            entidades.append((entidade, label_atual))
    
    return entidades



def identificar_entidades(texto):
    # Dividir o texto em seções
    secoes = texto.split("\n\n")
    
    entidades_label = []
    
    for secao in secoes:
        # Extrair o label (parte antes do ':') e as entidades (parte depois do ':')
        linhas = secao.split('\n')
        label = linhas[0].replace(':', '').strip()  # Remove ':' e espaços desnecessários
        
        # Iterar pelas entidades (linhas subsequentes)
        for entidade in linhas[1:]:
            entidade = entidade.replace('-','').strip()
            if entidade:  # Ignora linhas vazias
                entidades_label.append((entidade, label))
    
    return entidades_label




def identificar_entidades_com_parenteses(texto):
    entidades_label = []
    
    # Dividir o texto em linhas
    linhas = texto.split("\n")
    
    for linha in linhas:
        linha = linha.strip()
        if linha:  # Ignora linhas vazias
            # Dividir a linha em entidade e label usando os parênteses
            entidade, label = linha.rsplit(' (', 1)
            label = label.replace(")", "")  # Remover o parêntese final do label
            entidades_label.append((entidade.replace('-','').strip(), label.strip()))
    
    return entidades_label




def identificar_entidades_formato_simples(texto):
    entidades_label = []
    
    # Dividir o texto em linhas
    linhas = texto.split("\n")
    
    for linha in linhas:
        linha = linha.strip()
        if linha:  # Ignora linhas vazias
            # Dividir entidade e label pelo último hífen
            entidade, label = linha.rsplit(' - ', 1)
            entidades_label.append((entidade.replace('-','').strip(), label.strip()))
    
    return entidades_label




def identificar_entidades_com_novo_formato(texto):
    entidades_label = []
    
    # Dividir o texto em linhas
    linhas = texto.split("\n")
    #print(linhas)
    # Variável para armazenar o label atual
    label_atual = None
    
    for linha in linhas:
        linha = linha.strip()
        
        if "**" in linha and "(" in linha and ")" in linha:
            #print(linha)
            # Se encontrar uma linha com label e tipo entre parênteses
            label_atual = linha.split("(")[-1].replace(")", "").strip()
        elif linha.startswith("-") and label_atual:
            # Se encontrar uma linha com uma entidade
            entidade = linha.replace("-", "").strip()
            if entidade:
                entidades_label.append((entidade, label_atual.replace('**','').replace(':','')))
    
    return entidades_label





def identificar_entidades_com_labels_especiais(texto):
    entidades_label = []
    
    # Dividir o texto em seções separadas por "\n\n"
    secoes = texto.split("\n\n")
    
    for secao in secoes:
        secao = secao.strip()
        if secao:
            # Separar o label da lista de entidades usando ":"
            label_parte, entidades_parte = secao.split(": ", 1)
            
            # Remover os asteriscos e espaços desnecessários no label
            label = label_parte.replace("**", "").strip()
            
            # Separar as entidades pela vírgula
            entidades = entidades_parte.split(", ")
            
            # Adicionar cada entidade ao resultado com o label correspondente
            for entidade in entidades:
                entidade = entidade.strip()
                if entidade:
                    entidades_label.append((entidade, label))
    
    return entidades_label




def processar_entidades_nomeadas2(texto):
    entidades = []
    
    # Dividindo o texto por linhas
    linhas = texto.splitlines()
    
    # Iterar sobre cada linha
    for linha in linhas:
        linha = linha.strip()  # Remove espaços extras
        
        # Verifica se a linha contém uma entidade nomeada no formato "- "Entidade" (CLASSE)"
        if linha.startswith('-'):
            # Separar a entidade e o label
            try:
                entidade = linha.split('"')[1]  # Extrai o texto entre aspas
                label = linha.split('(')[1].split(')')[0].strip()  # Extrai o label entre parênteses
                entidades.append((entidade, label))
            except IndexError:
                pass  # Ignorar linhas mal formatadas
    
    return entidades





import re

# Sua string original
def caso1(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    
    for strg in resultados:
        s = strg.split(',')
        new_dados.append((s[0].replace("'",''),s[1].split('(')[1]))
    return new_dados

def caso2(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    
    for strg in resultados:
        s = strg.split(',')
        r= s[0].split('(')
        #print(r)
        if len(r)==2:
            #print(r[0], r[1])
            new_dados.append((r[0],r[1]))
    return new_dados

def caso3 (dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s)
        new_dados.append((s[0].replace('"',''),s[1].strip() ))
    return new_dados

def caso4(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s)
        new_dados.append((s[0].replace("'",''),s[1].strip() ))
    return new_dados

def caso5(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        d_int = []
        for c in s[1:]:
            d_int.append((c.strip(),s[0]))
        new_dados.append(d_int)
    return new_dados
    
def caso6(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s[0].replace('*',''))
        d_int = []
        for c in s[1:]:
            d_int.append((c.strip(),s[0].replace('*','')))
        new_dados.append(d_int)
    return new_dados

def caso7(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('), (')
    for i,conj in enumerate(spliting):
        #print(i, conj)
        con = conj.split(',')
        d = []
        for c in con:
            if '(' in c and ')' in c:
                continue
            elif '(' in c:
                c = c.replace('(','')
            elif ')' in c: 
                c = c.replace(')','')
                #print(c)
            d.append(c)
        new_dados.append(d)
    
    right = []
    for data in new_dados:
        for elem in data[1:]:
            right.append((elem.strip(), data[0].strip()))
    return right


def caso8(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.split('\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        if len(strg)>2:
            #print(strg)
            a =strg.split(',')
            d = []
            for i,ele in  enumerate(a):
                #print(i,ele, '[' in ele)
    
                if '[' in ele and ']' in ele:
                    continue
                elif '[' in ele:
                    ele = ele.replace('[','')
                    #print(ele)
                elif ']' in ele: 
                    ele = ele.replace(']','')
                    #print('aq')
                d.append(ele)
            new_dados.append(d)
    right = []
    for data in new_dados:
        for elem in data[1:]:
            right.append((elem.replace("'",'').strip(), data[0].strip()))
    return right

def caso9(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = data_string.split('), (')
    #print(resultados)
    for result in resultados:
        s = result.split(',')
        #print(result,'r')
        match = s[0].replace(')', '').split('(')
        if len(match)==3:
            s[0]=match[2]
        else:
            s[0]=match[1]
        #print(s[0], 'h')
        d = []
        for sp in s[1:]:
            if ')' in sp:
                sp = sp.replace(')','')
            if '.' in sp:
                sp = sp.replace('.','')
            d.append((s[0],sp.strip()))
        new_dados.append(d)
    return new_dados

def caso10(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = data_string.split('), (')
    #print(resultados)
    for result in resultados:
        sentences = result.split(',')
        print(sentences[0])
        if '-' in sentences[0]:
            sentences[0] = sentences[0].replace('-','')
        if '(' in sentences[0]:
           sentences[0] = sentences[0].replace('(','')
        if '.' in sentences[0]:
            sentences[0] = sentences[0].replace('.', '')
        d = []
        for sent in sentences[1:]:
            if '.' in sent:
                sent = sent.replace('.', '')
            if len(sent[0])==0 or len(sent.strip()) == 0:
                continue
            else:
                d.append((sent.strip(), sentences[0].strip()))
    
        new_dados.append(d)
    return new_dados


def caso11(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('), (')
    #print(spliting)
    for splited in spliting:
        sp = splited.split(',')
        #print(sp)
        d = []
        for c in sp:
            print(c)
            if '(' in c and ')' in c:
                c = c.split('(')[1].replace(')','')
                #print(c,'d')
            elif '(' in c:
                c = c.replace('(','')
            elif ')' in c: 
                c = c.replace(')','')
            #print(c)
            d.append(c.replace('"',''))
        new_dados.append(d)
    return new_dados



def caso12(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('), (')
    #print(spliting)
    for splited in spliting:
        sp = splited.split(',')
        #print(sp)
        d = []
        for c in sp:
            dd =c.split(',')
            if '(' in dd[0]:
                new = dd[0].split('(')
                #print(new, 'new', len(new))
                if len(new) >2:
                    new = new[1:]
                    #print(data,'d')
                dd = new[1].replace(')','')
                #print(dd,'s')
                d.append((new[0], dd))
            #print(d)
        new_dados.append(d)    
    return new_dados


def caso13(dados,virg):
    new_dados = []
    virg = virg
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s,'i')
        if len(s)>2:
            da = s[2].strip()
        if virg and len(s)>2 and '(' not in s[1]:
            dd = s[0]+s[1]
            new_dados.append((dd.replace("'",'').strip(),da ))
        else:
            new_dados.append((s[0].replace("'",''),s[1].split('(')[0].strip() ))
    return new_dados


def caso14(dados):
    
    new_dados = []
    data_string = dados
    spliting = dados.split('), (')
    for i,conj in enumerate(spliting):
        #print(i, conj)
        cc = conj.split(',')
        for c in cc[:-1]:
            print(c,'c')
            if '(' in c:
                c = c.replace('(','')
            new_dados.append((c.replace("'",'').strip(),cc[-1].strip()))
    return new_dados


def caso16(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        d_int = []
        for c in s[:-1]:
            d_int.append((c.strip(),s[-1].strip()))
        new_dados.append(d_int)
    return new_dados


def caso17(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s)
        new_dados.append((s[0].replace("'",'').replace('**',''),s[1].strip() ))
    return new_dados
    
    
def identificar_entidades_com_novo_formato2(texto):
    entidades_label = []
    
    # Dividir o texto em linhas
    linhas = texto.split("\n")
    #print(linhas)
    # Variável para armazenar o label atual
    label_atual = None
    
    for linha in linhas:
        linha = linha.strip()
        
        if "**" in linha :
            #print(linha)
            # Se encontrar uma linha com label e tipo entre parênteses
            #label_atual = linha.split(":")[-1].replace(")", "").strip()
            label_atual = linha.split(":")[0].replace("**",'').replace("-", "").strip()
            #print(l)
            for demais in  linha.split(":")[1:]:
                for entidade in demais.split(','):
                    entidades_label.append((entidade.strip().replace('.',''), label_atual.strip()))
        elif linha.startswith("-") and label_atual:
            # Se encontrar uma linha com uma entidade
            entidade = linha.replace("-", "").strip()
            if entidade:
                entidades_label.append((entidade, label_atual.replace('**','').replace(':','')))
    
    return entidades_label





def caso18(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('], ')
    #print(spliting, len(spliting))
    for splited in spliting:
        sp = splited.split(',')
        #print(sp)
        d = []
        if ':' not in sp[0]:
            
            for c in sp[1:]:           
                new1 = sp[0].replace('{','').replace('**','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                d.append((new1.replace("'",'').strip(),new2.replace("'",'').strip()))
        else:
            #print('here',len(sp[1:]))
            if len(sp[1:])>=2:
                for c in sp[1:]:
                    u = sp[0].split(':')
                    x = u[0].replace("'",'').replace('**','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                    y = u[1].replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').replace("'",'')
                    new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                    d.append((x.strip(),new2.replace("'",'').strip()))
            else:
              
                u = sp[0].split(':')
                x = u[0].replace("'",'').replace('**','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                y = u[1].replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').replace("'",'')
            d.append(  (x,y))         
        new_dados.append(d)
    return new_dados



def caso18_v2(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('], ')
    #print(spliting, len(spliting))
    for splited in spliting:
        sp = splited.split(',')
        #print(sp)
        d = []
        if ':' not in sp[0]:
            
            for c in sp[1:]:           
                new1 = sp[0].replace('{','').replace('**','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                d.append((new1.replace('"','').strip(),new2.replace('"','').strip()))
        else:
            #print('here',len(sp[1:]))
            if len(sp[1:])>=2:
                for c in sp[1:]:
                    u = sp[0].split(':')
                    x = u[0].replace("'",'').replace('**','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                    y = u[1].replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').replace("'",'')
                    new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                    d.append((x.strip(),new2.replace('"','').strip()))
            else:
              
                u = sp[0].split(':')
                x = u[0].replace("'",'').replace('**','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                y = u[1].replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').replace('"','')
            d.append(  (x,y))         
        new_dados.append(d)
    return new_dados


def caso18_v3(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('], ')
    #print(spliting, len(spliting))
    for splited in spliting:
        sp = splited.split(',')
        #print(sp)
        d = []
        if ':' not in sp[0]:
            
            for c in sp[1:]:           
                new1 = sp[0].replace('{','').replace('**','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                d.append((new1.replace('"','').strip(),new2.replace('"','').strip()))
        else:
            #print('here',len(sp[1:]))
            if len(sp[1:])>=2:
                for c in sp[1:]:
                    u = sp[0].split(':')
                    x = u[0].replace('"','').replace('**','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                    y = u[1].replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').replace("'",'')
                    new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                    d.append((x.strip(),new2.replace('"','').strip()))
            else:
              
                u = sp[0].split(':')
                x = u[0].replace('"','').replace('**','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
                y = u[1].replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').replace('"','')
            d.append(  (x,y))         
        new_dados.append(d)
    return new_dados



def caso15(dado):
    x = dado.split('ner')[1].replace(':','').strip().split('],')
    new_dado = []
    for dado in x:
        #print(dado, 'i')
        vv = []
        for label in dado.split('[')[1:]:
            classe = dado.split('[')[0].replace(',','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').strip()
            lbl = label.split(',')
            for entity in lbl:
                ent = entity.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').strip()
                vv.append((classe.replace("'",'').strip(),ent.replace("'",'').strip()))
            new_dado.append(vv)
    return new_dado

def caso15_v2(dado):
    x = dado.split('ner')[2].replace(':','').strip().split('],')
    new_dado = []
    for dado in x:
        #print(dado, 'i')
        vv = []
        for label in dado.split('[')[1:]:
            classe = dado.split('[')[0].replace(',','').replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').strip()
            lbl = label.split(',')
            for entity in lbl:
                ent = entity.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','').strip()
                vv.append((classe.replace("'",'').strip(),ent.replace("'",'').strip()))
            new_dado.append(vv)
    return new_dado


def caso19(dados):
    new_dados = []
    data_string = dados
    spliting = dados.split('), ')
    #print(spliting, len(spliting))
    for splited in spliting:
        sp = splited.split(',')
        #print(sp)
        uu = []
        for c in sp[1:]:           
            new1 = sp[0].replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
            new2 = c.replace('{','').replace(')','').replace('(','').replace('}','').replace('[','').replace(']','')
            #print(new1,new2)
            uu.append((new1.replace("'",''),new2.replace("'",'')))
        new_dados.append(uu)
    return new_dados



import ast  # Importando o módulo ast


def caso20(texto):
    # Lista para armazenar as tuplas (ner, label)
    lista_ner = []
    
    # Regex para capturar as entidades nomeadas
    padrao_ner = re.compile(r"'(\w+)': \[([^\]]*)\]")
    
    # Divide o texto em blocos por "\n\n"
    entradas = texto.split('\n\n')
    
    # Itera sobre cada bloco de texto
    for entrada in entradas:
        # Para cada correspondência da regex no bloco
        for correspondencia in padrao_ner.findall(entrada):
            label = correspondencia[0]  # Nome da categoria (PESSOA, LOC, ORG)
            entidades = correspondencia[1].split(", ")  # Lista de entidades
            # Limpa as aspas simples ao redor das entidades
            entidades = [entidade.strip("'") for entidade in entidades]
            # Adiciona as tuplas (entidade, label) à lista
            for entidade in entidades:
                if entidade:  # Evita adicionar strings vazias
                    lista_ner.append((entidade, label))

    return lista_ner



def caso21(texto):
    # Usamos regex para capturar as entidades e os labels
    regex = r"\[([^\]]+)\],\s*'(\w+)'"
    correspondencias = re.findall(regex, texto)
    
    tuplas = []
    for entidades_str, label in correspondencias:
        # Retirar espaços extras e as aspas das entidades
        entidades = [entidade.strip().strip("'") for entidade in entidades_str.split(",")]
        for entidade in entidades:
            tuplas.append((entidade, label))
    
    return tuplas



def caso22(texto):
    # Usamos regex para capturar as entidades e os labels
    regex = r"\('([^']+)', '(\w+)'\)"
    correspondencias = re.findall(regex, texto)
    
    tuplas = [(entidade, label) for entidade, label in correspondencias]
    return tuplas


def caso23(texto):
    # Regex para capturar a entidade e o rótulo entre parênteses
    regex = r"- ([\w\sÀ-ÿ',]+) \((\w+)\)"
    correspondencias = re.findall(regex, texto)
    
    # Criação das tuplas (entidade, label)
    tuplas = [(entidade.strip(), label) for entidade, label in correspondencias]
    
    return tuplas




def caso24(texto):
    # Regex para capturar a entidade e o rótulo dentro de parênteses
    regex = r"\(\s*([^,]+)\s*,\s*(\w+)\s*\)"
    correspondencias = re.findall(regex, texto)
    
    # Criação das tuplas (entidade, label)
    tuplas = [(entidade.strip(), label) for entidade, label in correspondencias]
    
    return tuplas


def caso25(texto):
    tuplas = []
    
    # Regex para capturar o label e as entidades
    regex = r"(\w+):\s*([^\n]+)"
    correspondencias = re.findall(regex, texto)
    
    # Para cada correspondência (label, entidades)
    for label, entidades in correspondencias:
        # Separar as entidades por vírgula
        lista_entidades = entidades.split(',')
        
        # Adicionar cada entidade junto com seu label à lista de tuplas
        for entidade in lista_entidades:
            tuplas.append((entidade.strip(), label.upper()))  # Usamos upper() para padronizar os labels em maiúsculas
    
    return tuplas



def caso26(s):
    # Remove possíveis colchetes extras e formata a string corretamente
    s = s.replace(']','').replace('}','').strip()
    s = s+'}'
    #print(s)
    
    # Converte a string em um dicionário
    dicionario = ast.literal_eval(s)
    
    # Cria uma lista de tuplas (entidade, label)
    lista_tuplas = [(entidade, label) for entidade, label in dicionario.items()]
    
    return lista_tuplas
    
def caso29(s):
    # Define a expressão regular para capturar as entidades e labels
    padrao = r"\{'(.+?)',\s*'(\w+)'\}"
    
    # Encontra todas as correspondências no texto
    matches = re.findall(padrao, s)
    
    # Cria uma lista de tuplas (entidade, label)
    lista_tuplas = [(entidade.strip(), label) for entidade, label in matches]
    
    return lista_tuplas



def caso27(s):
    # Define a expressão regular para capturar as entidades e labels
    padrao = r'\{\s*(.+?)\s*,\s*label:\s*(\w+)\s*\}'
    
    # Encontra todas as correspondências no texto
    matches = re.findall(padrao, s)
    
    # Cria uma lista de tuplas (entidade, label)
    lista_tuplas = [(entidade.strip(), label) for entidade, label in matches]
    
    return lista_tuplas



def caso28(s):
    # Define a expressão regular para capturar as entidades e labels
    padrao = r"\{'(.+?)',\s*'(\w+)'\}"
    
    # Encontra todas as correspondências no texto
    matches = re.findall(padrao, s)
    
    # Cria uma lista de tuplas (entidade, label)
    lista_tuplas = [(entidade.strip(), label) for entidade, label in matches]
    
    return lista_tuplas



def caso30(s):
    # Define a expressão regular para capturar categorias e suas entidades
    padrao = r'- \*\*(.+?)\*\*:\s*([^-\n]*)'
    
    # Encontra todas as correspondências no texto
    matches = re.findall(padrao, s)
    #print(matches,'m')
    # Cria um dicionário para armazenar as entidades por categoria
    dicionario_entidades = []
    
    for categoria, entidades in matches:
        # Divide as entidades por vírgula e remove espaços
        lista_entidades = [entidade.strip() for entidade in entidades.split(',')]
        dicionario_entidades.append([[categoria , entidade ]for entidade in lista_entidades])
    
    return dicionario_entidades




def caso31(s):
    # Define a expressão regular para capturar o texto e a categoria (ner)
    padrao = r"\{'texto': '(.+?)', 'ner': '(\w+)'\}"
    
    # Encontra todas as correspondências no texto
    matches = re.findall(padrao, s)
    
    # Cria um dicionário para armazenar as entidades por categoria
    dicionario_entidades = []
    
    for texto, ner in matches:
        # Adiciona a entidade ao dicionário
        #print(texto)    
        dicionario_entidades.append([ner,texto.replace(']','')])
    
    return dicionario_entidades




def caso32(input_string):
    # Remove os colchetes externos e divide a string em partes
    clean_string = input_string.strip("[]")
    parts = clean_string.split("]['")
    
    # Inicializa a lista de tuplas
    entities = []
    
    for part in parts:
        # Divide cada parte em entidade e label
        entity_label = part.split("', '")
        if len(entity_label) == 2:
            # Remove as aspas restantes
            entity = entity_label[0].strip("'")
            label = entity_label[1].strip("'")
            entities.append((entity, label))
    
    return entities



def caso33(input_string):
    # Inicializa um dicionário para armazenar as entidades por tipo
    entities_dict  = []
    
    # Divide a string por espaços para separar os tipos
    sections = input_string.split('\n\n')
    #print(sections)
    for section in sections:
        if ':' in section:
            # Obtém o tipo e a lista de entidades
            label, entity_str = section.split(': ', 1)
            #print(entity_str.split(','))
            entities_dict.append([[label,entities.replace('[','').replace(']','').replace("'",'').strip()] for entities in entity_str.split(',')])

    return entities_dict





def caso34(input_string):
    # Remove os parênteses externos e separa os itens
    items = input_string.strip('()').split(')(')
    
    # Cria uma lista de tuplas a partir dos itens
    result = []
    for item in items:
        # Remove espaços em branco extras e divide o item
        entity, label = item.split(', ', 1)  # O 1 limita a divisão a no máximo duas partes
        result.append((entity.strip(), label.strip()))  # Remove espaços em branco
    return result




def caso35(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s)
        new_dados.append((s[0].replace("'",'').replace('**',''),s[1].replace("'",'').strip() ))
    return new_dados





def caso36(string):
    # Remove espaços em branco e separa as partes
    partes = string.strip().split('\n',1)
    #print( partes[0].split(','))
    # Converte as strings das listas em listas reais usando json.loads
    entidades = [ entit.replace('[','').replace("'",'').replace('[','').replace('\n','').strip() for entit in partes[0].split(',')]
    labels = [lab.replace('[','').replace("'",'').replace('[','').replace('\n','').strip() for lab in partes[1].split(',')]

    # Cria a lista de tuplas
    return [(entidade, label) for entidade, label in zip(entidades, labels)]





def caso35_v2(dados):
    new_dados = []
    data_string = dados
    # Encontrando todos os conteúdos dentro dos parênteses
    resultados = re.findall(r'\((.*?)\)', data_string)
    #print(resultados)
    for strg in resultados:
        s = strg.split(',')
        #print(s)
        new_dados.append((s[0].replace('"','').replace('**',''),s[1].replace("'",'').strip() ))
    return new_dados






def caso37(string):
    # Remove espaços em branco e separa as linhas
    linhas = string.strip().split('\n')
    
    # Cria a lista de tuplas a partir das linhas
    resultado = [tuple(linha.strip().replace("'",'').strip("[]").split(', ')) for linha in linhas]
    
    return resultado



import json

def caso38(input_string):
    # Remove espaços em branco no início e no fim da string
    input_string = input_string.strip()
    
    # Converte a string em uma lista
    input_list = json.loads(input_string)
    
    # Inicializa a lista de resultados
    resultados = []
    
    # Verifica se a lista tem um número par de elementos
    if len(input_list) % 2 != 0:
        raise ValueError("A lista deve conter um número par de elementos.")
    
    # Itera sobre a lista, pegando pares de elementos
    for i in range(0, len(input_list), 2):
        entidade = input_list[i]
        label = input_list[i + 1]
        resultados.append((entidade, label))
    
    return resultados


def caso39(input_string):
    import json
    
    # Converte a string de entrada em um dicionário
    data = json.loads(input_string)
    
    # Inicializa a lista de resultados
    resultados = []
    
    # Percorre cada chave e valor no dicionário
    for label, entidades in data.items():
        for entidade in entidades:
            resultados.append((entidade, label))
    
    return resultados
