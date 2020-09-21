# CheckMate
**Mate(user)** 를
**Check(출석체크)** 하다.  
<br>  

## 개요
 딥러닝 기반의 얼굴 인식 기술을 이용한 출석 관리 프로그램입니다. 데이터베이스에 강의 별 수강 학생들의 사진이 등록되어 있으며, 카메라에 제공되는 영상 속 학생들의 얼굴을 강의가 진행되는 동안 지속적인 인식을 통해 출석 체크를 하고, 학생들에게 실시간으로 출석 여부를 제공해 줍니다. 

<br>

## 제공 기능
[필수기능]
1.	교수님 및 선생님 -> 강의 등록 UI
2.	학생 -> 본인의 정보 및 얼굴 사진 등록 UI
3.	프로그램이 동작하는 동안 자동 출석체크
4.	교수님 및 선생님 -> 쉬는 시간, 화장실 등 자리를 비우기 위한 최대 시간 설정 UI
5.	출석 여부 확인을 위한 UI  

[추가할 수 있는 부가기능]
1.	졸음, 자리 비움 횟수 등의 태도 점수 제공
2.	마스크, 모자 등의 객체 탐지를 통해 최초에 한 번 off 요청
3.	선택적으로 강의 내 사용자들에게 자신의 영상 노출
4. 가족 또는 지인에게 출석 여부 알림  

<br>

## 프로젝트 환경 및 주요 라이브러리
anaconda: <https://www.anaconda.com/>  

```python 3.7(anaconda env) >conda create -n [환경명] python=3.7```  
```pip install dlib``` <https://pypi.org/project/dlib/>  
```pip install opencv-python``` <https://pypi.org/project/opencv-python/>

<br>

## 현재 진행하고 있는 단계
동양인(주로 한국인) 인식을 위한 data set 수집 & 신경망 모델링 고민
<br>
<br>
<br>
  
### CONTRIBUTOR
* 정성진: <https://github.com/on1ystar>
* 김희연: <https://github.com/hiyony>
* 구예지: <https://github.com/gyj0518>
