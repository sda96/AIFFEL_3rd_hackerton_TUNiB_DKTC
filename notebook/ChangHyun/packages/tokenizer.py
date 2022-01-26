import re
import matplotlib.pyplot
from tqdm import tqdm
from collections import defaultdict
import sentencepiece as spm
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Mecab



def bin_dict(sentences:"2-D list"):
    """
    args
        - sentences : 2차원의 리스트 또는 리스트를 원소로 갖는 Series
    desc
        - 말뭉치에 있는 단어들의 갯수를 세고 내림차순으로 정렬한 dict 타입의 사전 생성
    return
        - dict(key : 단어, value : 말뭉치에서 해당 단어가 출현한 횟수)
    
    """
    dic = defaultdict()
    for sentence in sentences: # 말뭉치내의 모든 문장들
        for word in sentence: # 문장내의 모든 단어들
            if word in dic: # 각 단어들을 dict의 key에 등록
                dic[word] += 1
            else:
                dic[word] = 0

    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True) # 빈도 내림차순
    dic = dict(dic)
    return dic


# Mecab의 단어-인덱스, 인덱스-단어 사전 구축
def word_index(dic:"dict", vocab_size:"int"):
    """
    args
        - dic : bin_dict 함수로 만들어진 단어 빈도 사전이 들어옵니다.
        - vocab_size : 최대 단어 개수
    desc
        - vocab_size 크기의 단어 - ID 사전, ID - 단어 사전을 만듭니다.
        - 0 -> <pad> 토큰
        - 1 -> <unk> 토큰
        - 2 -> <sos> 토큰
        - 3 -> <eos> 토큰
    return
        - word_to_index : dict 타입의 결과물로 key는 단어 value는 index를 의미합니다.
        - index_to_word : dict 타입의 결과물로 key는 index value는 단어를 의미합니다.
    """
    word_to_index = defaultdict()
    index_to_word = defaultdict()
    
    
    dic = list(dic.items())[:(vocab_size - 4)]
    dic = dict(dic)
    for ind, word in enumerate(dic):
        word_to_index[word] = ind + 4
        index_to_word[ind + 4] = word
    
    word_to_index["<pad>"] = 0
    index_to_word[0] = "<pad>"
    word_to_index["<unk>"] = 1
    index_to_word[1] = "<unk>"
    word_to_index["<sos>"] = 2
    index_to_word[2] = "<sos>"
    word_to_index["<eos>"] = 3
    index_to_word[3] = "<eos>"

    word_to_index = dict(word_to_index)
    index_to_word = dict(index_to_word)
    return word_to_index, index_to_word


#  Mecab 토큰화, 패딩 적용
def tokenization(corpus, dictionary, max_length = 0, padding = "post"):
    tokens = []
    for setence in corpus:
        # 1은 unk 토큰의 인덱
        tmp = [dictionary[word] if word in dictionary else 1 for word in setence]
        
        if max_length < len(tmp):
            max_length = len(tmp)
        tokens += [tmp]

    # 패딩
    tokens = pad_sequences(tokens, maxlen = max_length, value = 0, padding = padding)
    
    return tokens


# spm 모델 생성 및 단어장 생성
def SentencePiece(model_type, data, vocab_size, add, train_test, temp_file = None):
    if not temp_file:
        temp_file = f"./model/02_SentencePiece/{model_type}_{vocab_size}_pre{add}_{train_test}.tmp"
    
    with open(temp_file, 'w') as f:
        for row in data:
            f.write(str(row) + '\n')
    spm_input = f"""
    --input={temp_file} 
    --model_prefix={model_type}_{vocab_size}_{train_test}_spm 
    --vocab_size={vocab_size} 
    --model_type={model_type}
    --unk_id=0 
    --pad_id=1 
    --bos_id=2 
    --eos_id=3 
    --user_defined_symbols=<pad>,<bos>,<eos>
    """
    spm_input = re.sub("\n", "", spm_input)
    spm.SentencePieceTrainer.Train(spm_input)

    s = spm.SentencePieceProcessor()
    s.Load(f'{model_type}_{vocab_size}_{train_test}_spm.model')
    return s