# ⭐ subserve × LOTTE ⭐

#### -서비스를 구독하다.
#### Subserve은 멋쟁이 사자처럼 X 롯데 해커톤 출품을 위한 프로젝트입니다.

<br><br>
## "subsribe to service in LOTTE"

<br><br>

**주요 서비스**
 - 지속적인 구독 서비스
 - 구독서비스 한 곳에 모아보기<br><br>

**구현 기능**
 - 회원가입 및 로그인
 - 구독 및 결제( 익일 자동 환불 처리되니까 맘 놓고 결제해보세요^o^)
 - 메뉴 검색
 - 주변 매장 위치 제공<br>

<br><br>
 
 
**코드 컨벤션**<br>
<ol>
    <li> 
    파일, 함수, 변수명은 자바컨벤션(카멜케이스)을 따릅니다.<br>
        ex. mainAttributes.css <br>
        ex. def exampleOneTwoThree() : <br>
        ex. function exampleOneTwoThree() {} <br>
    </li>
    <li>
        클래스, 모델은 첫글자만 대문자로 작성합니다. <br>
        ex. class Example : Models
    </li> 
    <li>
        함수 작성 시 도입부에 간단한 설명을 주석으로 달아둡니다. <br>
        ex. def func() : <br>
            # 그냥 함수 <br>
        ex. function example() { <br>
           // 자바스크립트 함수 <br>
        }
    </li>
    <li>
     키를 필요로 하는 API등은 keys.json에 추가하고 .gitignore로 보호합니다.
    </li>
    <li>
    html 클래스, id, 장고앱 이름은 전부 소문자로 작성합니다.
   </li>
   <li>
    url, html 클래스, id의 공백은 '-'를 사용합니다. <br>
    ex. div class="ex-one ex-two" id="division-one"
    ex. http://localhost/subserve-example <br>
    </li>
    <li>
    클래스를 상속받거나 프로토콜을 사용할 일이 있을때는 파일을 따로 만들어서 모아둡니다.
    </li>
    <li>
    migrations 디렉토리 안의 파일들은 절대로 지우지 않도록 합니다.
    </li>
</ol>


**실행 방법**
