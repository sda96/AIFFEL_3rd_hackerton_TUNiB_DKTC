### git 환경설정

git config --help
git config --global --help
git config --global user.name "sy"

### local에서 github 업로드 과정

1. git add(staging 수정된 파일 모아줍니다.)
   git add README.md 

2. git commit -m "다시 추가

3. git push origin(별칭) master(브랜치)
   push를 하기전까지는 local만 영향을 줍니다.

### github내용 local로 업데이트

git pull origin master
git pull

### git log

지금까지 github push log를 불러옵니다

### git checkout 시점

git log로 나온 token(시점)으로 .git의 버전을 되돌립니다.

### git status

파일이 수정된 것을 보여줍니다.

### git rm -r 폴더명

github repo에 있는걸 제거해줍니다.

### git checkout -b 브랜치명

설정된 repository에 새로운 브랜치 생성합니다.

### git reset --hard HEAD

git commit까지 했던 내용들 모두다 초기화 합니다. (사용시 주의 요망)

### git clone -b {branch_name} --single-branch {저장소 URL}

특정 브랜치 clone 합니다.

### git remote add origin (user.name):(git.token)@(저장소 url)

github repo 연결합니다.

### git fetch origin

원격 저장소로부터 가져온 모든 브랜치 헤드를 파일에 기록합니다.

https://mylko72.gitbooks.io/git/content/remote/remote_sync.html

### git remote -v

현재 연결된 repository 를 보여줍니다.

### git remote show

연결된 repository의 이름들을 출력합니다.

### git remote rm 이름

이름에 맞는 repository를 연결을 제거합니다.

### git diff

https://wani.kr/posts/2014/07/15/git-2-git-diff/

### private repository clone error

remote: Repository not found 에러 발생, 단 privacy repo에 push 하는 경우 collaborator 추가
참고 사이트 --- https://o-yeon.tistory.com/90
초대 보내면 초대한 아이디의 등록 이메일주소로 초대장 보냄

### add, commit 취소 방법

git reset HEAD <- git add 내용 취소

git log를 나가는 방법은 q를 누르면 됨
git push, pull 을 사용하면 merge 편집기는 shift zz를 누르면 나가짐, :wq 를 사용하면 저장하고 편집기를 나감

(https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html) git add, git commit, git push 내용 취소

### 취소한 내용 되돌리기
(https://88240.tistory.com/284)

### 숨김 파일 제거 사용 주의
https://jongkunkim.tistory.com/30


### github 빈 파일 만들기

gitignore.io   ---------- gitignore
gitkeep이 비어있는 폴더

### 기타등등

git log  origin은 github의 repo임

git clone

목차별 gitkeep 추가
01 tab

- [x] 저거하기 체크만들기 ex) - [x] 

closed #2
fixed #2