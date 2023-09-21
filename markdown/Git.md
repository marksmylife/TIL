# Git
* 코드 관리 도구(SCM, Source Code Management Tool)

## 1. 코드 관리 도구로서의 Git
* 버전 관리 도구(VCS, Version Control System) : 버전을 통해 코드 관리 도구
* 분산형 버전 관리 도구(Distribute VCS) : 분산된 형태로 버전을 통해 코드 관리 도구

## 2. Git Commands
> Git 폴더/디렉토리 단위로 프로젝트/저장소/코드를 관리한다.
>

### 2.1 `git init`
```
Initialized empty Git repository in C:/Users/chm44/intro/.git/
> 비어있는 Git 저장소/프로젝트를 시작함(.git)
```
1. `.git` 폴더 생성
2. `(master)` 또는 `(main)` 프롬프트(브렌치 이름)

### 2.2 Git 프로젝트 관리 중단
  * rm - r .git > 폴더 지우기
  * `git init` : 켰다가 / `rm -r .git` : 껏다가
  
### 2.3 `git status`
Git 상태 출력

#### 2.3.1 최초상태

On branch master : master 브런치에 있음

No commits yet : commit 아직 없음

nothing to commit : commit 할 것도 없음, 추적하라면 파일 만들고 git add 사용해

#### 2.3.2 파일생성

On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)

#### 2.3.3 `git add` 직후

On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

`git rm --cached a.txt` > unstage

#### 2.3.4 `git commit -m "txt"` 직후

On branch master

nothing to commit, working tree clean


### `git add [파일/폴더]` > Stage에 파일 추가

### `git commit -m "커밋 메시지` > 커밋하기

### `git log --oneline` > 한줄로

### 결국 요 루틴?
|순서|명령어|활용|
|---|---|---|
||git status|
||git log|
||git log --oneline|log 한줄로|
||||
||touch [파일명]|
||git add [파일명]|
||git commit -m "커밋 메시지"|
||||
||git diff|변화 체크|
|git checkout 해쉬|과거로 회귀||
|git checkout main|현실 원복||
|git clone [주소]|주소에서 자료 다운||
|git remote add origin [주소]|최초 주소 연결||
|git push origin|업로드||
|git pull|다운로드||
|git remote -v|||

---
touch [파일]
git status
git add [파일]
git commit -m "설명"
git push
---
git pull
```git log --oneline```

git branch : 조회
git branch [인자] : 생성
git merge [합병 branch] : 원하는 branch에서 실행할 것