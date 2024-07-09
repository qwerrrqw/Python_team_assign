import hashlib
# **평가**
# - 클래스와 인스턴스 개념을 설명할 수 있는가?
# - 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
# - 클래스를 정의할 수 있는가?
# - 인스턴스를 생성할 수 있는가?

# ----- 코드 정의 ------
#<담당: 나지수>
class Member:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password): 
        return hashlib.sha256(password.encode()).hexdigest() # 보안을 위해 md5에서 sha256으로 변경
        
    def display(self):
        print(f'이름: {self.name}, 아이디: {self.username}')

''' 코드설명
1. 회원의 정보를 담을 오브젝트 생성 > Member 클레스와 __init__, display 메서드 작성
2. 객체를 생성할 때 마다 초기화하기 위해 초기화 메서드 __init__ 사용
3. __init__()의 0번째 자리 self를 통해 이후에 나열된 메서드들에게 접근할 수 있다.
4. __init__()에서 self.name = name 을 선언해주지 않으면 display()에서 name에 접근 할 수 없다.
5. 인스턴스 메서드 display()을 사용하면 회원정보를 프린트 해줘야하므로 print(f'string로 멘트와 네임, 유저네임을 호출하며 출력)
6. hashlib 모듈 사용을 위해 맨위에 import hashlib 작성
7. def hash_password()인스턴스 메서드를 만들어주고 __init__에 있는 패스워드에 적용해줘서 비밀번호를 받았을때 암호화 되도록함
'''
#</담당: 나지수>

#<담당: 김진영>
class Post:
    # author는 인스턴스 구현에서 username 으로 넣어주면 됨
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        
''' 코드설명
1. Post 클래스 생성.
2. __init__()은 Post객체(인스턴스) 생성 시 초기에 발현되는 메소드. 
3. 클래스 메소드는 일반 메소드와는 달리 매개변수 0번째 자리에는 꼭 self를 넣어야함.
4. title, content, author는 밖에서 가져온 변수인지 인스턴스 안에 있는 변수인지 구분이 안되기 때문에
    인스턴스 안에있는 변수를 다룰 땐 꼭 self.~~~로 컨트롤 함.
'''
#</담당: 김진영>


# ----- 코드 실행 ------

#<담당: 이종화>




# - 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요 
# 맴버 인스턴스 생성
members = []

# m1 = Member('KARINA', 'aespa', 'password') >>>>> 최적화를 위해 삭제
# m2 = Member('HANNI', 'NewJeans', 'password')
# m3 = Member('REI', 'IVE', 'password')
members.append(Member('KARINA', 'aespa', 'password'))
members.append(Member('HANNI', 'NewJeans', 'password'))
members.append(Member('REI', 'IVE', 'password'))

for member in members:
    member.display()

'''코드설명
'Member' 인스터드 생성 및 리스트에 추가하기
1. 'm1', 'm2','m3' 이름으로 세 개의 'Member' 객체를 생성함.
2. 이 객체들을 'members' 리스트에 추가함.
3. 'print(members)'로 리스트를 출력함. (이것은 각 객체의 메모리 주소를 보여줌)
'''

# - 각각의 회원이 게시글을 세개 이상 작성하는 코드, 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장

# 포스터 작성

posts = []
# p1 = Post('supernova', '가능한 모든 가능성 무한 속의 너를 만나', 'aespa') >>>> 최적화를 위해 삭제
# p2 = Post('Armageddon', '악몽은 또 짙게 번져가', 'aespa')
# p3 = Post('Savage', '네 환각들이 점점 너를 구축할 이유가 돼', 'aespa')
posts.append(Post('supernova', '가능한 모든 가능성 무한 속의 너를 만나', 'aespa'))
posts.append(Post('Armageddon', '악몽은 또 짙게 번져가', 'aespa'))
posts.append(Post('Savage', '네 환각들이 점점 너를 구축할 이유가 돼', 'aespa'))

'''코드설명
'Post' 인스턴스 생성 및 리스트에 추가하기
1. 여러 'post' 객체를 생성해 'posts' 리스트에 추가함.
2. 이 객체들을 'posts' 리스트에 추가함. 
3. 'print(posts)'로 리스트를 출력함. (이것은 각 객체의 메모리 주소를 보여줌)
4. 최적화를 위해 한번만 쓰이는 변수는 따로 선언하지 않고 제거, 직접 append함 (m1~m4, p1~p9)
'''
#</담당: 이종화>

#<담당: 이세준>
# 아무것도 입력안하고 엔터 눌렀을때 skip하게 변경
# 작성자 글 반환
def search_name(author, posts):
    titles = []
    for post in posts:
        작성자가 입력한 author와 같은지 확인
        작성자가 같은 게시글의 제목을 리스트에 추가
    if titles:
        return titles
    return # 이름, 아이디, 패스워드 전부 입력했을때만 회원정보 등록, 아닐경우 초기화기능 추가

# 검색할 작성자 입력 및 출력
사용자로부터 검색할 작성자 입력 받음
if else 조건문과 input값에 맞는 게시글이 있으면 작성자와 게시글제목 출력 아니면 게시글 없다고 출력
오류를 방지하기 위해 if 문에 isinstance 사용해서 input값이 리스트인지 확인
이름, 비밀번호, 아이디 모두 입력했을때만 등록, 아닐경우 전부 입력하도록 유도 문구 출력 후 다시 입력 받음

# 검색어가 포함된 글 반환
def search_include(word, posts):
    titles = []
    for 문으로 게시글 내용에 검색어가 포함되어있는지 확인, 있으면 titles에 append
    제목 리스트가 비어있을경우 대비 if titles: return titles
    return 

# 검색할 검색어 입력 및 출력
사용자로부터 검색할 검색어 입력 받음
검색어에 해당하는 게시글 제목 검색하고 if else로 검색어가 포함된 게시글 출력, 없으면 없다는 문구 출력

# 한번에 나오면 어지러우니까 중간중간 time.sleep()으로 지연 넣음

'''코드설명
1. 글쓴이를 입력했을때 해당글쓴이가 작성한 포스트의 제목을 반환하는 함수작성
2. 사용자로부터 input을 통해 글쓴이를 입력
3. 입력받은 글쓴이가 작성한 게시글이 있으면 출력, 없으면 없다고 출력
4. 검색어를 입력했을때 해당검색어가 들어간 포스트의 제목을 반환하는 함수작성
5. 사용자로부터 검색어를 입력
6. 입력받은 검색어가 들어간 게시글이 있으면 출력, 없으면 없다고 출력
'''
#</담당: 이세준>
# --------------일반 완료 후 회의--------------

# **추가 도전 과제:**
화면 공유로 공동작업
#  - input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
'''
담당: 팀원 전체
가독성 좋게 변수명을 지음
'''
#  - post도 터미널에서 생성할 수 있게 해주세요. 
7554
# #  >> 어서 == 유저네임
'''
담당: 팀원 전체
입력받은 작성자가 members에 없으면 다시 입력하게끔 while 문 작성
while문 안에 for문을 만들어 break를 써도 while문을 빠져나가지 못함.
flag 변수로 탈출을 결정
'''
# <나지수>(심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
# 인터넷 찾아보면서 공부 한 후 작성</나지수>
'''
hashlib 라이브러리 참고 https://docs.python.org/ko/3/library/hashlib.html
형식 >>>>>>>        import hashlib
                    hash_object = hashlib.sha256(string.encode()) 
MD5: 속도가 빠르지만 보안에 취약함. 현재는 보안 목적으로 사용하지 않음.
SHA-1: MD5보다 보안성이 높지만, 현재는 보안 취약점 때문에 사용하지 않음.
SHA-256: 높은 보안성과 적당한 속도로 널리 사용됨.
SHA-512: SHA-256보다 더 높은 보안성을 제공하지만, 그만큼 속도가 느림.

'''