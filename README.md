# AIFFEL_3rd_hackerton_TUNiB_DKTC - [TUNiB 공식 Repo](https://github.com/tunib-ai/DKTC)
## 과제 설명 및 목표
AIFFEL 3차 해커톤 TUNiB 기업과제 데이터셋 DKTC으로 DKTC(Dataset of Korean Threatening Converstations)
훈련 데이터의 클래스는 '협박', '갈취', '직장 내 괴롭힘', '기타 괴롭힘' 4가지 클래스로 이루어져 있고 테스트 데이터의 클래스는 '일반' 클래스가 추가된 5가지 클래스입니다.

해당 5종류의 클래스를 문장을 입력으로 넣어서 분류하는 텍스트 다중 분류 모델을 만드는 것이 과제의 목표입니다.

일반 대화 클래스의 경우 [AI hub](https://aihub.or.kr/aihub-data/natural-language/about) 데이터를 활용해야 하며 사용되기 좋다고 생각되는 데이터셋은 다음과 같습니다.  
(일반 대화 클래스는 추천일 뿐 더 좋은게 있으면 사용하고 바꿀 수 도 있습니다.)
- [한국어 대화](https://aihub.or.kr/aidata/85)
- [감성 대화 말뭉치](https://aihub.or.kr/aidata/7978)
- [한국어 SNS](https://aihub.or.kr/aidata/30718)

|클래스|Class No.|# Training|# Test |
|:----:|:------:|:------:|:------------:|
|협박 |00| 896    | 100   |
|갈취  |01|981     | 100 |
|직장 내 괴롭힘  |02|979     |100|
|기타 괴롭힘 |03|1,094      |100|
|일반 |04| - |100|

## 데이터 구조
![image](https://user-images.githubusercontent.com/42150335/149441163-7728a543-5dbd-4fb6-b12f-cae5fc79c6fe.png)

## 프로젝트 진행 과정
![image](https://user-images.githubusercontent.com/51338268/150277973-96b1e4b7-d235-420e-b559-7fee01e9dacf.png)

## 과제에 사용되는 도구
- 화상 회의 플랫폼 : 구글미트
- 프로젝트 협업툴 : Github
- 프로젝트 회의록, 참고사이트 아카이브 : Notion
- 프로그래밍 언어 : 파이썬 3.x
- 딥러닝 프레임워크 : 텐서플로우 2.x, Huggingface

## 프로젝트 진행 과정 리더보드
|시도한 방법|F1-score|
|:-|:-:|
|일반 대화 : 한국어 대화 데이터 4000개 </br> 모델 : Soft voting 앙상블(klue/bert-base, skt/kogpt2, LSTM) </br> epoch : 1|0.673|
|일반 대화 : 무작위 SNS 데이터 4000개 + 한국어 대화 데이터 4000개 </br> 모델 : klue/bert-base(단일 모델) </br> epoch : 1|0.821|
|일반 대화 : 무작위 SNS 데이터 4000개 + 한국어 대화 데이터 4000개 </br> 모델 : klue/bert-base(단일 모델) </br> epoch : 3 </br> lr_scheduler : 0.5|0.829|
|일반대화 : 무작위 SNS 5000개, 한국어 대화 5000개, 감성 말뭉치 5000개, 오분류 SNS데이터 350개 </br> 모델 : klue/bert-base(단일 모델) </br> epoch : 5 </br> lr_schduler : 0.2|0.865|
|일반대화 : 무작위 SNS 5000개, 한국어 대화 5000개, 감성 말뭉치 5000개, 오분류 SNS데이터 350개, 역번역 데이터(영어, 중국어, 일본어) </br> 모델 : 일반대화 데이터로 사전학습시킨 klue/bert-base (TAPT 적용) </br> epoch : 4 </br> lr_schduler : 0.2|0.875|
|일반대화 : 무작위 SNS 5000개, 한국어 대화 5000개, 감성 말뭉치 5000개, BERT오분류 SNS데이터 350개 </br> 모델 : 일반대화 데이터로 사전학습시킨 klue/bert-base (TAPT 적용) </br> epoch : 2 </br> lr_schduler : 0.2|0.882|

## [참고 자료 회의록 아카이브](https://www.notion.so/modulabs/X-AI-6bac1355f3ae449eb339ce870a488675)

불균형 데이터
- [불균형 텍스트 데이터 참고 사이트](https://d2.naver.com/helloworld/7753273)
- [한국어 텍스트 데이터 증강 방법 KorEDA](https://catsirup.github.io/ai/2020/04/28/nlp_data_argumentation_code.html)
- [한국어 텍스트 증강 패키지](https://github.com/jucho2725/ktextaug)
- [텍스트 생성 모델 서베이(조사) 논문](https://arxiv.org/pdf/2105.10311.pdf)
    
다중 분류 모델
- [튜닙 감성 분석](https://www.youtube.com/watch?v=aKKDvdel5O4)
- [한국어 기반 트랜스포머 모델 비교 서베이 논문](https://arxiv.org/pdf/2112.03014.pdf)
- [최신 텍스트 분류 모델 추세](https://paperswithcode.com/sota/text-classification-on-ag-news)
- [딥러닝을 이용한 자연어 처리 깃허브 튜토리얼](https://github.com/ukairia777/tensorflow-nlp-tutorial)
    
설명 가능한 AI
- [Explainable AI demo 사이트](https://lrpserver.hhi.fraunhofer.de/)
- [EXplainable AI LRP 설명 동영상](https://youtu.be/4twkQWYTXpw)
- [XAI NLP 강의](https://www.youtube.com/watch?v=3tnrGe_JA0s)
- [Explaining Recurrent Neural Network Predictions in Sentiment Analysis](https://arxiv.org/abs/1606.07298)
    
기존의 혐오표현과 욕설을 잡아내는 연구들
1. [딥러닝 기술을 활용한 차별 및 혐오 표현 탐지](https://www.koreascience.or.kr/article/JAKO202005653790577.pdf)
2. [클린봇 2.0: 문맥을 이해하는 악성 댓글(단문) 탐지 AI](https://d2.naver.com/helloworld/7753273)
3. [ㅅ111발" 도 잡아내는 욕설 탐지기, 딥러닝으로 만들기](https://www.inven.co.kr/webzine/news/?news=198156)
    
Github
- [Github 사용 참고 자료](https://github.com/sda96/AIFFEL_3rd_hackerton_TUNiB_DKTC/blob/main/reference/git_ref.md)
- [Github 협업 프로젝트 과정 참고 사이트](https://www.freecodecamp.org/news/how-to-use-git-and-github-in-a-team-like-a-pro/)
- [LaTex 표기법 정리 참고 사이트](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:TeX_%EB%AC%B8%EB%B2%95)
    
기타 참고 사이트
- [기술 블로그 45개 정리 사이트](https://brunch.co.kr/@sicle-official/35)
    
GAN을 NLP에 적용 (seqGAN)
1. 작사가 인공지능 노드 참고
2. [seqGAN](https://www.koreascience.or.kr/article/CFKO201832073078975.pdf)
