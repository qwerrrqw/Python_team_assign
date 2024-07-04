# **평가**
# - 클래스와 인스턴스 개념을 설명할 수 있는가?
# - 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
# - 클래스를 정의할 수 있는가?
# - 인스턴스를 생성할 수 있는가?


# ----- 코드 정의 ------
#<담당: 나지수>
class Member:
    
    # - 회원 이름 (**`name`**)
    # - 회원 아이디 (**`username`**)
    # - 회원 비밀번호 (**`password`**) 
    def __init__(self, name, username, password):
        셀프.네임 = 네임
        셀프.유저네임 = 유저네임
        셀프.페스워드 = 페스워드
    
    def display(self):
        
        # 회원 정보를 print해주는 display 
        # (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
        print(f'이름:{셀프.네임}, 아이디:{셀프.유저네임}')
        pass
''' 코드설명
1. 회원의 정보를 담을 오브젝트 생성 > Member 클레스와 __init__, display 인스턴스 메서드 작성
2. 객체를 생성할 때 마다 초기화하기 위해 초기화 메서드 __init__ 사용
3. __init__()의 0번째 자리 self를 통해 이후에 나열된 메서드들에게 접근할 수 있다.
4. __init__()에서 self.name = name 을 선언해주지 않으면 display()에서 name에 접근 할 수 없다.
5. 인스턴스 메서드 display()을 사용하면 회원정보를 프린트 해줘야하므로 print(f'string로 멘트와 네임, 유저네임을 호출하며 출력)
'''
#</담당: 나지수>

#<담당: 김진영>
class Post:
    
    # - 게시물 제목 (**`title`**)   (done)
    # - 게시물 내용 (**`content`**)   (done)
    # - 작성자 (**`author`**) : 회원의 `username`   (done)
#author는 인터페이스 구현에서 username 으로 넣어주면 됨
def __init__(self, title, content, author):

    셀프.타이틀 = 타이틀
    셀프.컨텐트 = 컨텐트
    셀프.어서 = 어서 
#</담당: 김진영>


# ----- 코드 실행 ------

#<담당: 이종화>
members = []
posts = []


# - 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요 
> 임시 유저 이름 : 'A', 'B', 'C'
> 멤버스.어펜드('A')
> 멤버스.어펜드('B')
> 멤버스.어펜드('')


# - members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
for i in members:
    멤버.디스플레이


# - 각각의 회원이 게시글을 세개 이상 작성하는 코드, 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장
> ex) posts.append(post('네임', '내용 아무거나', '유저네임'))
>
>

>
>
>

>
>
>
#</담당: 이종화>

#<담당: 이세준>
# - for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
for i in posts:
    'A'유저가 쓴 글만 검색해야함 > 포스트 유저네임이 'A'면 프린트
    

# - for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요.
for i in posts:
    if 특정단어 in 포스트.컨텐트:
        프린트(f'컨텐트에 {특정단어}가 포함된 포스트의 제목 : {포스트.타이틀}')
#</담당: 이세준>
# --------------일반 완료 후 회의--------------

# **추가 도전 과제:**

#  - input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.

#  - post도 터미널에서 생성할 수 있게 해주세요. 
# #  >> 어서 == 유저네임

#  - (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
# 인터넷 찾아보면서 공부 한 후 작성
'''
담당: 나지수
hashlib 라이브러리 참고 https://docs.python.org/ko/3/library/hashlib.html

형식 >>>>>>>        import hashlib
                    hash_object = hashlib.sha256(string.encode()) 

MD5: 속도가 빠르지만 보안에 취약함. 현재는 보안 목적으로 사용하지 않음.
SHA-1: MD5보다 보안성이 높지만, 현재는 보안 취약점 때문에 사용하지 않음.
SHA-256: 높은 보안성과 적당한 속도로 널리 사용됨.
SHA-512: SHA-256보다 더 높은 보안성을 제공하지만, 그만큼 속도가 느림.

'''