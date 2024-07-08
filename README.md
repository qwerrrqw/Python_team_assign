- 프로젝트: 간단한 소셜 미디어 플랫폼만들기 

    - 설명: 이 프로젝트는 회원과 게시물을 관리하는 간단한 소설 미디어 프로그램을 만드는것 입니다. 회원 정보를 등록하고, 게시물을 작성할 수 있으며, 특정 회원이 작성한 게시물이나 특정 단어가 포함된 게시물을 검색 할 수도 있습니다. 또한 사용자로부터 새로운 회원의 이름, 아이디, 비밀번호를 입력받아 회원을 생성하고 리스트에 추가할 수 있습니다.

* 팀원 및 역할

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

  - 공동 작업(화면공유): 사용자 입력을 통한 회원 및 게시글 생성

- 사용법

    1. Python 실행시 회원 이름과 아이디가 출력됨.
    
    2. '찾으실 글쓴이를 입력해주세요'에서 아이디 입력시 해당 회원이 작성한 글 출력됨 만약 없다면 없다는 맨트 출력, 해당 기능을 이용하지 않을경우 엔터를 눌러 스킵
    3. '찾으실 검색어를 입력해주세요:'에서 해당 검색어가 들어간 게시글 검색 가능, 검색어의 내용이 들어간 게시글이 존재할 경우 게시글의 제목이 출력됨
    
    4. 작성 완료하면 회원 리스트에 추가됨 
        - 이름을 입력하세요: 
        - 아이디를 입력하세요:
        - 패스워드를 입력하세요:
        
    5. 작성 완료시 게시글 리스트에 추가됨 
        - 제목을 입력하세요:
        - 내용을 입력하세요:
        
    6. 입력한 회원과 게시글이 잘 등록되었는지 확인하고 싶으면 '작성자를 입력하세요:'에 등록한 회원 아이디를 입력하면 확인가능. 만약 없는 맴버거나 아이디가 다르다면 재입력 멘트 출력됨
    
    7. 추가된 회원 이름과 아이디를 포함된 목록이 출력됨
        
    




- 코드 설명

    - 백엔드:

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
        ```

        - 코드 설명(class Member)
            1. 회원의 정보를 담을 오브젝트 생성 > Member 클래스와 **init**, display 인스턴스 메서드 작성
            2. 객체를 생성할 때마다 초기화하기 위해 초기화 메서드 **init** 사용
            3. **init**()의 첫 번째 매개변수 self를 통해 이후에 나열된 메서드와 속성에 접근할 수 있다.
            4. **init**()에서 self.name = name 을 선언해주지 않으면 display()에서 name에 접근할 수 없다.
            5. 인스턴스 메서드 display()를 사용하면 회원 정보를 출력해준다. 이 때 print(f'string') 형식을 사용하여 name과 username을 출력.
            6. hashlib 모듈을 사용하기 위해 맨 위에 import hashlib 작성
            7. hash_password() 인스턴스 메서드를 만들어서 **init**에서 패스워드를 해시화함
            8. hexdigest() 메서드를 사용하여 암호를 16진수 문자열로 변환

        ```
        class Post:
            def __init__(self, title, content, author):
                self.title = title
                self.content = content
                self.author = author
        ```
        - 코드 설명(class Post)
            1. Post 클래스 생성.
            2. __init__()은 Post 객체(인스턴스) 생성 시 초기에 발현되는 메소드. 
            3. 클래스 메소드는 일반 메소드와는 달리 매개변수 0번째 자리에는 꼭 self를 넣어야함.
            4. title, content, author는 밖에서 가져온 변수인지 인스턴스 안에 있는 변수인지 구분이 안되기 때문에
            인스턴스 안에있는 변수를 다룰 땐 꼭 self.~~~로 컨트롤 함.




    - 프론트엔드:
        - 사용자와 상호작용하고, 데이터를 입력받고, 출력을 처리합니다.
        - 콘솔에서 입력을 받아 회원과 게시글을 생성합니다.
        - 특정 조건에 따라 데이터를 검색하고 출력합니다.

        ```
        members = []

        # 맴버 인스턴스 생성
        m1 = Member('KARINA', 'aespa', 'password')
        m2 = Member('HANNI', 'NewJeans', 'password')
        m3 = Member('REI', 'IVE', 'password')

        members.append(m1)
        members.append(m2)
        members.append(m3)

        for member in members:
            member.display()
        ```
        - 코드설명(인스턴스 생성 및 리스트 관리)
            1. 'Member' 인스터드 생성 및 리스트에 추가하기
            2. 'm1', 'm2', 'm3' 이름으로 세 개의 'Member' 객체를 생성함.
            3. 이 객체들을 'members' 리스트에 추가함.
            4. 'for' 루프를 사용하여 각 객체의 정보를 출력하기 위해 'display()' 메서드를 호출함.

        ```
        posts = []

        # 포스터 작성
        p1 = Post('supernova', '가능한 모든 가능성 무한 속의 너를 만나', 'aespa')
        p2 = Post('Armageddon', '악몽은 또 짙게 번져가', 'aespa')
        p3 = Post('Savage', '네 환각들이 점점 너를 구축할 이유가 돼', 'aespa')
        posts.append(p1)
        posts.append(p2)
        posts.append(p3)

        p4 = Post('Super Shy', '나 원래 말도 잘하고 그런데 왜 이런지', 'NewJeans')
        p5 = Post('Bubble Gum', '내 향기가 널 먼저 찾아가', 'NewJeans')
        p6 = Post('Supernatural', '너와 나 다시 한번 만나게', 'NewJeans')
        posts.append(p4)
        posts.append(p5)
        posts.append(p6)

        p7 = Post('Accendio', '주문 걸어 아센디오', 'IVE')
        p8 = Post('I AM', '어제랑 또 다른 짜릿한 나', 'IVE')
        p9 = Post('LOVE DIVE', '참을 수 없는 이끌림과 호기심', 'IVE')
        posts.append(p7)
        posts.append(p8)
        posts.append(p9)
        ```
        - 코드설명(게시글 작성 및 리스트 관리)
            1. 'Post' 인스턴스 생성 및 리스트에 추가하기
            2. 여러 'Post' 객체를 생성하여 'posts' 리스트에 추가함.
            3. 각 게시글 객체를 'posts' 리스트에 추가함.
            4. 특정 조건에 따라 게시글의 제목을 출력하거나, 검색 결과를 출력함.
        ```
        def search_name(author, posts):
            titles = []
            for post in posts:
                if post.author == author:
                    titles.append(post.title)
            if titles:
                return titles
            return

        search_author = input("찾으실 글쓴이를 입력해주세요: ")
        search_titles = search_name(search_author, posts)
        if isinstance(search_titles, list):
            print(f"{search_author}가 작성한 게시글: {','.join(search_titles)}")
        else:
            print(f"{search_author}가 작성한 게시글이 없습니다.")
        ```
        - 코드설명(특정 회원의 게시글 검색)
            1. 글쓴이를 입력받아 해당 글쓴이가 작성한 게시글의 제목을 반환하는 함수 search_name 작성
            2. 사용자로부터 글쓴이 이름을 입력받음
            3. 입력받은 글쓴이가 작성한 게시글이 있으면 제목을 출력, 없으면 해당 글쓴이가 작성한 게시글이 없다고 출력

        ```
        def search_include(word, posts):
            titles = []
            for post in posts:
                if word in post.content:
                    titles.append(post.title)
            if titles:
                return titles
            return

        search_keyword = input("찾으실 검색어를 입력해주세요: ")
        search_titles = search_include(search_keyword, posts)
        if isinstance(search_titles, list):
            print(f"{search_keyword}가 들어간 게시글: {','.join(search_titles)}")
        else:
            print(f"{search_keyword}가 들어간 게시글이 없습니다.")

        ```
        - 코드설명(특정 단어가 포함된 게시글 검색)
            1. 검색어를 입력받아 해당 검색어가 포함된 게시글의 제목을 반환하는 함수 search_include 작성
            2. 사용자로부터 검색어를 입력받음
            3. 입력받은 검색어가 포함된 게시글이 있으면 제목을 출력, 없으면 해당 검색어가 포함된 게시글이 없다고 출력
        ```
        new_name = input("이름을 입력하세요: ")
        new_user_name = input("아이디를 입력하세요: ")
        new_password = input("패스워드를 입력하세요: ")
        m4 = Member(new_name, new_user_name, new_password)
        members.append(m4)

        new_post = input("제목을 입력하세요: ")
        new_content = input("내용을 입력하세요: ")

        flag = False  # while문 탈출 도구
        while True:
            new_author = input("작성자를 입력하세요: ")
            for member in members:
                if new_author == member.username:
                    post10 = Post(new_post, new_content, new_author)
                    posts.append(post10)
                    flag = True
                    break
            if flag:
                break
            print("입력하신 작성자의 아이디를 찾을 수 없습니다. 다시 입력하세요!")

        print("회원 목록")
        for member in members:
            member.display()

        print("작성된 글 목록")
        for post in posts:
            print(f"제목: {post.title}, 작성자: {post.author}")
        ```
        - 코드설명
            1. 사용자로부터 새로운 회원의 이름, 아이디, 비밀번호를 입력받아 Member 객체를 생성하고 members 리스트에 추가
            2. 사용자로부터 새로운 게시글의 제목과 내용을 입력받음
            3. 작성자의 아이디를 입력받아 members 리스트에서 유효한 작성자인지 확인
            4. 유효한 작성자일 경우 Post 객체를 생성하여 posts 리스트에 추가
            5. 유효한 작성자가 아닐 경우 다시 입력받음
            6. 모든 회원과 작성된 게시글을 출력함

