import os
from glob import glob
import time
from tqdm import tqdm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def recurrent_find_data_path(wd:"str"):
    """
    args
        - wd : 현재 작업중인 경로를 입력받습니다 ex) wd = os.getcwd()
    desc
        - data라는 폴더명을 가진 경로를 상위 경로로 올라가면서 찾으며, 찾게되면 해당 폴더의 경로를 반환합니다.
    return
        - data_path : ex) /aiffel/example/data
    """
    # 현디렉토리의 파일명들을 가져옵니다.
    paths = glob(wd + "/*")
    # data라는 이름의 경로가 존재하면 해당 경로를 반환합니다.
    for path in paths:
        if "data" in path:
            return "".join(path)
    # 존재하지 않는 경우 다음 상위 디렉토리로 이동합니다.
    ex = wd.split("/")
    wd = "/".join(ex[:-1])
    # 상위 디렉토리에서 앞선 과정을 반복합니다.
    return recurrent_find_data_path(wd)


def get_data_paths(data_path:"str"):
    """
    args
        - data_path : recurrent_find_data_path 함수로 구한 data라는 폴더명을 가진 파일의 위치를 입력받습니다.
    desc
        - data 폴더에 있는 전체 하위 경로에 있는 모든 파일을 list에 저장합니다.
    return
        - bucket_file : [파일1, 파일1/파일2.csv, 파일1/파일3.xlsx .....]
    """
    deep_path = data_path
    bucket_file = []
    while True:
        deep_path += "/*"
        files = glob(deep_path)
        if not files:
            break
        bucket_file += [files]
    return sum(bucket_file, [])


def files_to_pd_dict(data_paths:"list"):
    """
    args
        - data_paths : get_data_paths 함수로 가져온 파일로 이루어진 리스트를 입력합니다.
    desc
        - list로 저장되어있는 파일들을 각자 확장자에 맞게 pd.DataFrame으로 불러오고 dict로 저장합니다.
    return
        - file_dict : {key = 파일명1 : value = pd.DataFrame1, key = 파일명2 : value = pd.DataFrame2 ....}
    """
    # data 폴더에 있는 파일들 pd.DataFrame으로 불러오기
    file_dict = defaultdict()
    for file in tqdm(data_paths):
        # 파일이 csv 확장자인 경우
        if ".csv" in file:
            file_name = file.split("/")[-1].split(".")[0]
            file_dict[file_name] = pd.read_csv(file)
        # 파일이 json 확장자인 경우
        elif ".json" in file:
            file_name = file.split("/")[-1].split(".")[0]
            file_dict[file_name] = pd.read_json(file)
        # 파일이 xlsx 확장자인 경우
        elif ".xlsx" in file:
            file_name = file.split("/")[-1].split(".")[0]
            file_dict[file_name] = pd.read_excel(file)

    return dict(file_dict)



def text_prep(x:"str"):
    """
    args
        - x : 전처리 시킬 문장을 입력받음
    desc
        - str 타입의 문장을 입력받아 전처리 후 str 타입으로 반환
    return
        - 전처리가 완료된 str 타입 반환
    """
    x = x.lower()
    x = re.sub("[^0-9a-zㄱ-ㅎ가-힣,?!\"\']+"," ", x)
    x = re.sub("[ ]+"," ", x)
    x = x.strip()
    return x    


def remove_nan(dataset:"pd.DataFrame"):
    """
    args
        - dataset : pandas.DataFrame을 입력으로 받음
    desc
        - 공백만 있는 데이터를 제거
    return
        - pandas.DataFrame
    """
    dataset = dataset.replace(["",'', " ", ' '], np.nan)
    dataset = dataset.dropna()
    return dataset


# 일반 판다스 데이터프레임을 텐서플로우 데이터셋으로 변환
def tensorflow_dataset(input_x, input_y, buffer_size, batch_size):
    tf_data = tf.data.Dataset.from_tensor_slices((input_x, input_y))
    tf_data = tf_data.shuffle(buffer_size)
    tf_data = tf_data.repeat()
    tf_data = tf_data.batch(batch_size)
    tf_data = tf_data.prefetch(buffer_size = -1)
    return tf_data 


# 학습과정 히스토리 시각화
def show_performance(history, title):
    loss, acc, val_loss, val_acc, lr = history.history.values()
    plt.plot(loss, label = "loss")
    plt.plot(acc, label = "acc")
    plt.plot(val_loss, label = "val_loss")
    plt.plot(val_acc, label = "val_acc")
    plt.title(title)
    plt.xlabel("epochs")
    plt.legend()
    plt.show()


# 사전학습된 임베딩 행렬 불러오기
def load_embedding_matrix(path, vocab_size, embedding_size, idx_word):
    word2vec = gensim.models.Word2Vec.load(path)
    embedding_matrix = np.random.rand(vocab_size, embedding_size)
    count = 0
    # embedding_matrix에 Word2Vec 워드 벡터를 단어 하나씩마다 차례차례 카피한다.
    for i in range(2,vocab_size):
        if idx_word[i] in word2vec:
            embedding_matrix[i] = word2vec[idx_word[i]]
            count += 1
    print(f"사전 학습에 사용 가능했던 단어 벡터 갯수 : {count}")
    return embedding_matrix


# Series 타입의 구조에서 원하는 word가 있는 인덱스를 반환하고 해당 문장을 출력
def find_word(word, sentences):
    find_indexes = []
    for idx, sentence in enumerate(sentences):
        if re.findall(word, sentence):
            find_indexes += [idx]
    return sentences[find_indexes]