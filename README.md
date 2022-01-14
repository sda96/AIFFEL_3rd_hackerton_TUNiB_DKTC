# AIFFEL_3rd_hackerton_TUNiB_DKTC

## 과제 설명 및 목표
AIFFEL 3차 해커톤 TUNiB 기업과제 데이터셋 DKTC으로 DKTC(Dataset of Korean Threatening Converstations)
훈련 데이터의 클래스는 '협박', '갈취', '직장 내 괴롭힘', '기타 괴롭힘' 4가지 클래스로 이루어져 있고 테스트 데이터의 클래스는 '일반' 클래스가 추가된 5가지 클래스입니다.

일반 대화 클래스의 경우 [AI hub](https://aihub.or.kr/aihub-data/natural-language/about) 데이터를 활용해야 하며 사용되기 좋다고 생각되는 데이터셋은 다음과 같습니다.  
(일반 대화 클래스는 추천일 뿐 더 좋은게 있으면 사용하고 바꿀 수 도 있습니다.)
- [한국어 대화](https://aihub.or.kr/aidata/85)
- [민원(콜센터) 질의 응답](https://aihub.or.kr/aidata/30716)

|클래스|Class No.|# Training|# Test |
|:----:|:------:|:------:|:------------:|
|협박 |00| 896    | 100   |
|갈취  |01|981     | 100 |
|직장 내 괴롭힘  |02|979     |100|
|기타 괴롭힘 |03|1,094      |100|
|일반 |04| - |100|

## 데이터 구조
![image](https://user-images.githubusercontent.com/42150335/149441163-7728a543-5dbd-4fb6-b12f-cae5fc79c6fe.png)

## 참고 자료 아카이브
- [불균형 텍스트 데이터 참고 사이트](https://d2.naver.com/helloworld/7753273)
- [Github 사용 참고 자료](https://github.com/sda96/AIFFEL_3rd_hackerton_TUNiB_DKTC/blob/main/reference/git_ref.md)
- [Github 협업 프로젝트 과정 참고 사이트](https://github.com/sda96/AIFFEL_3rd_hackerton_TUNiB_DKTC/blob/main/reference/git_ref.md)
