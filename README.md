# AIFFEL_3rd_hackerton_TUNiB_DKTC
## [참고 자료, 회의록 아카이브](https://www.notion.so/AIFFEL-3-TUNiB-de4ca87a991c4f12bd2a0c0858c5103a)

## 기대되는 프로젝트 수행 과정 순서
1. coggle.it에서 아이디어 브레인스토밍 + 회의내용 기록
2. 회의내용 및 참고 사이트 Notion에 Archiving
3. 회의내용 기반으로 주차별 Github Project 생성 후 각자 업무에 맞는 Card 생성
4. 각자 Card에 맞는 업무 수행
5. 업무 수행중 문제 발생시 issue 로 문제점 공시
6. 정해진 업무와 issue가 해결되면 sub-branch에 업무내용 반영후 main-branch에 Pull-request 요청
7. main-branch는 요청 받은 Pull-request를 확인하고 문제없으면 merge

## 과제에 사용되는 도구
- 회의 내용 녹화 방법 : 윈도우키 + G, 클로바노트(음성녹음 + 녹음내용 필기)
- 프로젝트 협업툴 : Github
- 프로젝트 회의록, 참고사이트 아카이브 : Notion
- 프로그래밍 언어 : 파이썬 3.x
- 딥러닝 프레임워크 : 텐서플로우 2.x


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

## 하루 일과
- 아침 10:00 오전 회의
- 점심 12:00 점심시간
