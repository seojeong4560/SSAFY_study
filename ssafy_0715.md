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
---

# 20220715
- 절대경로: 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
- 상대경로: 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
  ./ 현재 작업하고 있는 폴더
  ../ 현재 작업하고 있는 폴더의 부모 폴더
---
- 마크다운: 텍스트 기반의 가벼운 마크업 언어
  문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
- 마크업: 태그를 이용하여 문서의 구조를 나타내는 것
- 참고: https://www.markdownguide.org/cheat-sheet/
- ```py enter ```
```python
arr = [1, 5, 2, 7, 9]
# 최대값을 구하시오.
max_value = 0
for i in range(len(arr)):
    if max_value < arr[i]:
        max_value = arr[i]
print(max_value)
max_idx = 0
for i in range(len(arr)):
    if arr[max_idx] < arr[i]:
            max_idx = i
print(max_idx)
print(arr[max_idx])

url: ctrl+k  ex ssafy
img ctrl+shift+i
mummoo


Bold Italic strikeout *을_로 대체 가능
수평선 ---


표 ctrl T
번호	이름	전화번호
1	홍길동	010-123-1234
2	김길동	010-456-4567
3	이길동	010-789-7890

주석 >



Repository: 특정 디렉토리를 버전 관리하는 저장소 git init 명령어로 로컬 저장소를 생성
특정 버전으로 남긴다 = "커밋한다"
Working Directory: 내가 작업하고 있는 실제 디렉토리
Staging Area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 Untracked :point_right_light_skin_tone: (git add) Staged :point_right_light_skin_tone: (git commit) Committed
git add .: 추적되지 않은 모든 파일과 추적하고 있는 파일 중 수정된 파일을 모두 Staging Area에 올림
git commit -m "커밋 메세지"
git clone {remote_repo}: remote repo를 local로 복사
TIL

매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것
Github 관리의 가장 첫 걸음, 제일 중요한 장기 프로젝트