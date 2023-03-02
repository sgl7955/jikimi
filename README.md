![image](https://user-images.githubusercontent.com/112363000/222334904-342f7b68-5474-4977-8f82-b2023424c6b9.png)

# 슬기로운 지키미(학교폭력 방지 CCTV 모니터링)

### 멀티캠퍼스 융복합 프로젝트(빅데이터, IoT, 클라우드)

### 팀명 : 슬기로운 지키미

### 팀원 : 빅데이터 - 박수은, 서혁준, 유영일

### IoT - 김준무

### 클라우드 - 류승지, 박예서(팀장), 이기복

### 주제 : 학교폭력 방지 CCTV 모니터링

### 진행기간 : 2023.01.03 ~ 2023.02.16

# 💭서비스 개발 동기 및 소개
- **온라인수업에서 대면수업으로 전환되며 학교에서 생활하는 학생들이 학교폭력에 노출되지 않도록 CCTV 모니터링을 통한 대처 및 예방**
- **CCTV 영상을 AI가 판별하여 폭력 감지 및 AWS SNS 서비스로 학교 측의 빠른 인지**
- **학교폭력 위험도 평가를 통해 지역구 및 학교별로 학교폭력 위험지수를 확인하여 취약환경 개선에 도움**

시연영상 : https://www.youtube.com/watch?v=bLmdtzOP5Uk

# 🗳️데이터 추출 방법
- **환경지표 + 위해지표 - 경감지표 = 학교폭력위험점수, 점수를 바탕으로 위험도를 5단계로 분류**
- **데이터명세 : 학교알리미, 나이스, 공공데이터포털, 서울열린데이터광장, 스마트치안빅데이터플랫폼**
- **유의미한 변수 파악을 위해 상관 분석을 진행(상관분석 결과에 사회환경적 요인의 변수로 Standard Scaler를 진행하여 scale이 큰 feature의 영향이 비대해지는 것을 방지)**
- **데이터를 그룹으로 클러스터링 하는 것이기 때문에 비지도학습인 K-Means를 채택(다른 군집화 모델에 비해 간단하고 확장성이 좋으며 대규모의 데이터셋을 효율적으로 처리)**
- **3개 이상의 변수를 2차원에 나타내고, 데이터들간의 상대적 거리를 보존하기 위해 kmeans에서 TSNE를 사용하여 군집화를 진행**
- **군집화를 진행할 때 최적의 K를 선정하기 위해 Elbow Method와 Silhouette Score를 사용하여 진행**

# ⚙️기술스택 & 아키텍처 구성
![image](https://user-images.githubusercontent.com/112363000/222336259-c878b864-6623-4ba8-8073-4008fdf8e0f1.png)

### 아키텍처 구성도
![image](https://user-images.githubusercontent.com/12217092/221348484-94daeedc-4942-4293-b5fc-ed1355ebdd94.png)
![image](https://user-images.githubusercontent.com/112363000/222336489-f2903200-0525-41fe-a759-eadf80bc955c.png)


# ✉️SMS 서비스
![image](https://user-images.githubusercontent.com/12217092/220605051-a7ddd25d-8e55-4af8-94bb-6cb1ff0fb2b9.png)
### 학교폭력 발생 시 서버에서 SMS를 보내 담당교사에게 알림


# 🕸️Django AWS로 배포(nginx, uwsgi)
- **인스턴스(t2.micro ubuntu 20.04)를 사용하여 mobaXterm에서 작업**
- **제작한 웹 페이지를 home/ubuntu에서 깃 클론을 한 후 virtualenv를 이용하여 가상환경 구축**
- **웹 앱(Django) 서버(nginx) 사이를 연결해주는 uwsgi 설치**

### [uwsgi.ini]
chdir=/home/ubuntu/jikimi/jikimki


module=config.wsgi:application


master=True


pidfile=/tmp/project-master.pid


vacuum=True


max-requests=<span style="color:brown">5000</span>


daemonize=/home/ubuntu/jikimi/jikimi/django.log


home=/home/ubuntu/jikimi/jikimi/venv


virtualenv=/home/ubuntu/jikimi/jikimi/venv


socket=/home/ubuntu/jikimi/jikimi/uwsgi.sock


chmod-socket=666

### /etc/nginx/nginx.conf
user ubuntu;<br/>
...<br/>
http {<br/>
    upstream django {<br/>
        server unix:/home/ubuntu/jikimi/jikimi/uwsgi.sock;<br/>            
    }
    
### /etc/nginx/sites-enabled
server_name .jikimi.link; //구입한 도메인 주소

location / {<br/>
    include /etc/nginx/uwsgi_params;<br/>
    uwsgi_pass django;<br/>
    proxy_buffer_size          128k;<br/>
    proxy_buffers              4 256k;<br/>
    proxy_busy_buffer_size     256k;  //502 에러 방지를 위해 buffer 사이즈 키우기<br/>
}

location /static/ {<br/>
    alias /home/ubuntu/jikimi/jikimi/static; //css등 적용 위해 static 경로 지정<br/>
}<br/>
...<br/>
    if ($http_x_forwarded_proto = 'http') {<br/>
   return 301 https://$host$request_uri; //https 접속<br/>
   }<br/>
}
# 🔒보안정책 구현(HTTPS, WAF)
- **학교폭력 데이터는 민감데이터기 때문에 HTTPS(암호화된 통신 프로토콜)과 WAF(웹 애플리케이션 보호)를 사용**
- **HTTPS**

-Route 53에서 발급받은 도메인과 ACM에서 발급받은 SSL 인증서를 ALB에 적용

-리스너에서 서비스 포트의 프로토콜을 443으로 변경하여 보안 정책과 SSL 인증서를 적용

- **WAF와 HTTPS 사용을 위해 ALB 구축**

-ALB가 대신하여 SSL 인증서를 이용한 암호화 통신을 하기 때문에 서버에 부담이 덜 됨

- **WAF ACL**

-IpBlacklist : 공격을 시도했던 Ip들을 설정해서 접속을 차단
-CountryBlcok : 한국에서만 서비스가 가능하도록 함
-matchSQLi : Query String을 통한 sql 인젝션, url 인코딩된 값으로 sql 인젝션인지 아닌지를 판단하기 어렵게 우회하는 패턴의 공격을 방어
-AWS-ManagedRulesCommonRuleSet : aws 관리형 규칙으로 http 헤더를 통한 제어, 불량 봇, 쿠키, URI 경로, XSS 등 종합적으로 공격을 방어함
-AWS-AWSManagedRulesSQLiRuleSet : 쿼리 파라미터, 본문, 쿠키 헤더와 URI 경로에서 악성 SQL 코드와 일치하는 패턴을 제어
-RateBased : 디도스(짧은 시간에 수많은 요청을 보내 서버를 마비)공격을 방어하기 위해 5분 동안 1,000번 이상 요청 시 접속을 차단함
![스크린샷_20230207_041729](https://user-images.githubusercontent.com/112363000/222340189-5970008c-8617-4121-8f45-fbc218d6ce1e.png)
### → 접속을 차단한 모습

# 📝서기 및 분위기메이커
- **회의록 및 멘토링 피드백 작성**
- **각 파트별 애로사항 인지 및 의견 조율**
- **날짜별 프로젝트 참석 확인(불참 시 전달해줄 자료 정리 및 전달)**
- **각종 자료 문서화**
![스크린샷_20230220_042611](https://user-images.githubusercontent.com/112363000/222340883-7783a8b3-dbb3-4928-964c-5c03c65fbafb.png)

# 🤝팀원들의 평가
![image](https://user-images.githubusercontent.com/112363000/222341398-62be161c-a769-4d7d-b108-d3ec55c4baf4.png)
![image](https://user-images.githubusercontent.com/112363000/222341472-9fb29ca6-f2cd-46ad-a456-b20fbade610d.png)
![image](https://user-images.githubusercontent.com/112363000/222341500-d942dbf0-8ae7-4586-aa78-2b27d4a62af3.png)

# 🌳느낀 점/배운 점
- **개발자는 코드만 짜는 사람이 아니다.**

-프로젝트를 진행하면서 가장 많이 느낀 점은 개발자가 코드만 작성하는 사람이 아니라는 것이다. 코드를 짜고 뭔가를 구축하는 것도 중요하지만 아이디어 회의, 산출물 정리 및 문서화, 시각적으로 핵심만을 나타내기 위한 ppt 제작, 발표가 지루해지지 않기 위한 대본 작성, 회의 진행 사항을 기록하는 등 눈에 보이지 않는 수많은 일들이 개발과정에서 큰 부분을 차지했다. 그리고 나는 누가 알아주지 않더라도 이런 일들을 도맡아서 했다. 이런 일을 함으로써 팀원들이 좀 더 개발에 집중할 수 있는 환경이 눈에 보여 내심 뿌듯했다.

- **나는 협업이 즐거운 사람이다.**

-프로젝트를 진행하면서 각 파트별로 팀원에게 내가 모르는 부분을 질문하고 팀원이 모르는 부분을 내가 알려주는 과정이 즐거웠다. 각 파트별로 작업이 어떻게 진행되는지 알아야 효율적으로 소통을 하며 개발이 진행될 수 있었다. 그리고 위에서 말한 눈에 보이지 않는 작업을 도맡아 하고 각 파트별로 의견을 조율하고 즐거운 분위기를 만들고 팀원들의 멘탈관리를 해주려 했던 노력들을 팀원들이 알아주고 너무 감사하다고, 많이 배웠다는 말을 해줘서 나도 너무 감사했다. 혼자서만 일하는 개발자보다 팀원과 협업하는 개발자가 얼마나 즐겁게 일할 수 있는지 알게 됐던 시간이었다.
