- 프로젝트명: 회원 및 게시물 관리 프로그램

- 설명: 이 프로젝트는 회원과 게시물을 관리하는 간단한 소설 미디어 플랫폼을 만드는것 입니다. 회원 정보를 등록하고, 게시물을 작성할 수 있으며, 특정 회원이 작성한 게시물이나 특정 단어가 포함된 게시물을 검색 할 수도 있습니다. 


- 팀원 및 역할

    - 나지수(팀장, 백엔드 담당):
        - class Member 및 인스턴스 메서드 작성
        - 패스워드 암호화

    - 김진영(백엔드 및 코드 리뷰, 피드백 담당):
        - class Post 작성
        - 공동 작업 부분 진행

    - 이세준(프론트엔드 담당):
        - 게시글 검색 기능 구현

    - 이종화(프론트엔드 담당):
        - 멤버 인스턴트 생성
        - 게시글 작성

공동 작업(화면공유): 사용자 입력을 통한 회원 및 게시글 생성

- 사용법(코드설명)

백엔드:
    - 데이터와 로직을 처리하고, 데이터베이스와 상호작용합니다.
    - Member와 Post 클래스를 정의하여 데이터를 모델링합니다.
    - 해시 함수와 같은 로직을 구현합니다.
    ```
    import hashlib

    class Member:

        def __init__(self, name, username, password):
            self.name = name
            self.username = username
            self.password = self.hash_password(password)

        def hash_password(self, password):
            return hashlib.sha256(password.encode()).hexdigest() 

        def display(self):
            print(f'이름: {self.name}, 아이디: {self.username}')
    


프론트엔드:
    - 사용자와 상호작용하고, 데이터를 입력받고, 출력을 처리합니다.
    - 콘솔에서 입력을 받아 회원과 게시글을 생성합니다.
    - 특정 조건에 따라 데이터를 검색하고 출력합니다.