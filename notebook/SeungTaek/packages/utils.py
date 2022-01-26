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
