# jikimi 멀티캠퍼스 융복합 프로젝트

진행기간 : 2023.01.03 ~ 2023.02.16

주제 : 학교폭력예방 및 대응
  - 학교폭력위험지표개발(학교폭력위험점수, 학교폭력위험단계)
  - 학교에 설치된 CCTV에서 폭력 감지 시 학교선생님께 SMS 전송 

팀원 
  - 빅데이터 : 박수은, 서혁준, 유영일
  - 클라우드 : 박예서(팀장), 유승지, 이기복
  - Iot : 김준무


## **학교폭력위험 지표**
학교폭력발생에는 다양한 원인이 존재한다. 
한 개인이 어떤 사람으로 자라며 어떻게 행동하는가는 그 사람의 의식 구조에 따라 결정되는 수가 많으며 
그 의식 구조의 형성에는 개인이 자라온 가정, 환경, 학교, 사회의 환경에 의해서 결정된다. 
CPTED(셉테드) 범죄예방 디자인 연구센터에 따르면 학교 폭력은 학교 내 외부의 환경과 연관이 있다고 말하고 있다. 
따라서 학교폭력의 사회 환경적 요인에 환경지표, 학교폭력의 학교 개별환경적 요인으로 위해지표, 경감지표로 분류하여
서울특별시 고등학교 학교폭력위험지표를 개발하였다. 


## **데이터 명세**
#### A. 서울열린데이터광장
1. 서울시 저소득 한부모 가족(29 rows × 15 columns)
2. 서울시 소득인식 수준(240 rows × 5 columns)
3. 서울시 자치구 단위 생활인구(219000 rows × 32 columns)
4. 서울시 다문화가정(28 rows × 11 columns)
5. 서울시 보통가구(3600 rows × 7 columns)
6. 서울시 CCTV설치현황(83734 rows × 7 columns)

#### B. 스마트치안빅데이터플랫폼
1. 학교폭력(1966 rows × 43 columns)
2. 청소년비행/학교폭력영향데이터(247 rows × 14 columns) 
3. 112신고영향요소융(273 rows × 28 columns) 

#### C. 공공데이터포털
1. 경찰관서 위치 주소(2037 rows × 8 columns) 
2. 소상공인진흥공단 상권정보(377724 rows × 39 columns)

#### D. 나이스
1. 학교기본정보(1421 rows × 25 columns)

#### E. 학교알리미(크롤링)
1. 학교폭력 조사참여 현황
2. 학교폭력 피해시간
3. 학교폭력 피해신고현황
4. 학교폭력 피해유형
5. 학교폭력 피해장소
6. 학교폭력 예방교육시간


## **YOLO**
학습데이터 : roboflow Violence Detection dataset 1500개 이미지 사용

링크 : https://universe.roboflow.com/nuscrimesocietydatasets/violence-9gmjx



## IoT & Web Interface

### CCTV 구조

![image](https://user-images.githubusercontent.com/12217092/220604062-1c2a3ee0-9af0-487e-91cf-52da002148a4.png)


### CCTV 작동 모습

![image](https://user-images.githubusercontent.com/12217092/220603217-2877a945-6d48-4b55-98b2-58d005f217bf.png)


### Web interfaces

Django 4.1.1 기반으로 작성됨 

PC

![image](https://user-images.githubusercontent.com/12217092/220603318-f9574569-7878-4e0c-9785-1b80d711bdcd.png)

![image](https://user-images.githubusercontent.com/12217092/220604524-09f21847-f75f-46da-a2d8-3608c1aff94f.png)

Mobile

![image](https://user-images.githubusercontent.com/12217092/220603352-a5e1b1ea-3f48-47d9-b09b-80c4f29c93b2.png)

### SMS 서비스
학교폭력 발생 시 서버에서 SMS를 보내 담당교사에게 알림

![image](https://user-images.githubusercontent.com/12217092/220605051-a7ddd25d-8e55-4af8-94bb-6cb1ff0fb2b9.png)
