SSAFY 220715 Markdown 정리
Git 기본
mkdir 새폴더 만들기
pwd 현재 위치
cd 현재위치이동 cd ~ 홈디렉토리이동
ls 리스트보기 ls -al 모든 파일 리스트보기
rm 파일 삭제 rm -r 폴더 삭제
Working Directory : 내가 작업하고 있는 실제 디렉토리 → git add 파일명 또는 git add .
Staging Area : 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 → git commit -m "메세지 입력"
Repository : 커밋(commit)들이 저장되는 곳 → 버전 하나가 완성
- git status 현재 git으로 관리되는 있는 파일들의 상태를 알 수 있음
git init 으로 깃 생성
git status 로 현재상태확인
git add 로 깃 추가
git commit -m "메세지" 커밋메세지 추가
git log 로 기록 확인

git log --oneline 한줄로 확인 가능
git remote add origin {remote_repo}
git push -u origin master

git clone {remote_repo}
git push origin master