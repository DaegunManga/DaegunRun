# DaegunRun


<div align="center">
<img src="https://img.shields.io/badge/Python-white?style=flat&logo=Python&logoColor=blue"/> 
</div>
<hr/>
<br>

![daegunrun](https://user-images.githubusercontent.com/69490709/224370762-b4c7951c-5fab-4796-8140-ecda5b805e60.png)

<br> <hr />

## index
1. [메인 코드](##daegunrun_main.py-:-메인-실행-코드)
2. [보스 공격 함수](##ATKpy.py-:-보스-공격-함수)
3. [라운드 판별 함수](##RNDpy.py-:-라운드-판별-함수)
4. [엑셀 관련 정보 처리 함수](##openpyxl.py-:-엑셀-관련-정보-정리-함수)
5. [장애물 처리 함수](##OBJpy.py--장애물-처리-함수)

<br>

## daegunrun_main.py : 메인 실행 코드
<hr />

#### judge_conflict 함수 : x, y 값을 가지고 충돌 판별
#### Button 함수 : 버튼 모양 텍스트 생성 함수
#### initGame 함수 : 기본 설정 세팅 함수
#### StartGame 함수 : 시작 화면 함수
#### Graph 함수 : 순위 관련 시각화 정보 제공 함수
#### staff 함수 : 제작자 화면 제공 함수
#### option 함수 : 환경 설정 함수 (주석으로 인해 버튼 눌러도 실행 X)
#### runGame 함수 : 주요 게임 실햄 함수
#### boss 함수 : 보스 단계 게임 실행 함수
#### end 함수 : 종료 화면 함수

<br>

## ATKpy.py : 보스 공격 함수
<hr />

#### __init__ 함수 : 기본 환경 설정 함수
#### create_ATK 함수 : 공격 객체 (파이어볼) 생성 함수
#### move_ATK 함수 : 공격 객체 이동 함수
#### del_ATK 함수 : 부딪혔을때 공격 객체 삭제 함수

<br>

## RNDpy.py : 라운드 판별 함수
<hr />

#### __init__ 함수 : 기본 환경 설정 함수
#### startgame 함수 : 10초마다 한번씩 라운드 변경
#### round 함수 : 장애물 생성 함수

<br>

## openpyxl.py : 엑셀 관련 정보 정리 함수
<hr />

#### __init__ 함수 : 기본 환경 설정 함수
#### save_value 함수 : 값 저장 함수
#### id_return 함수 : id 정보 제공 함수
#### save_Data_IMG 함수 : 데이터 시각화 사진 저장 함수

<br>

## OBJpy.py : 장애물 처리 함수
<hr />

#### __init__ 함수 : 기본 환경 설정 함수
#### append_OBJ 함수 : 장애물 생성 함수
#### delete_OBJ 함수 : 장애물 삭제 함수
#### move_OBJ 함수 : 장애물 이동 함수

## mp3 : 음질은 좋지 않지만, 음악 나올 수 있음 (현재 주석 처리, 나오지 않음.)

<br>

<span style='color: red'>boss_img.png, ttf 파일의 부재 등으로 바로 실행은 불가능함.</span>


