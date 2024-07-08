import hashlib
import time


# ----- 코드 정의 ------

# Member 클래스 구현

class Member:

    #맴버 클래스 생성 함수
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    #비밀번호 인코드 함수
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    #맴버 name과 username보여주는 함수
    def display(self):
        print(f'이름: {self.name}, 아이디: {self.username}')

class Post:
    # author는 인스턴스 구현에서 username 으로 넣어주면 됨
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# ----- 코드 실행 ------
members = []

# 맴버 인스턴스 생성
#맴버스에 맴버들 append하는 코드
members.append(Member('KARINA', 'aespa', 'password'))
members.append(Member('HANNI', 'NewJeans', 'password'))
members.append(Member('REI', 'IVE', 'password'))

#맴버스 안에 있는 맴버 출력하는 코드
for member in members:
    member.display()


posts = []
# 포스터 작성
posts.append(Post('supernova', '가능한 모든 가능성 무한 속의 너를 만나', 'aespa'))
posts.append(Post('Armageddon', '악몽은 또 짙게 번져가', 'aespa'))
posts.append(Post('Savage', '네 환각들이 점점 너를 구축할 이유가 돼', 'aespa'))

posts.append(Post('Super Shy', '나 원래 말도 잘하고 그런데 왜 이런지', 'NewJeans'))
posts.append(Post('Bubble Gum', '내 향기가 널 먼저 찾아가', 'NewJeans'))
posts.append(Post('Supernatural', '너와 나 다시 한번 만나게', 'NewJeans'))

posts.append(Post('Accendio', '주문 걸어 아센디오', 'IVE'))
posts.append(Post('I AM', '어제랑 또 다른 짜릿한 나', 'IVE'))
posts.append(Post('LOVE DIVE', '참을 수 없는 이끌림과 호기심', 'IVE'))


# ----------------------

# 작성자 글 반환
def search_name(author, posts):
    titles = []
    for post in posts:
        if post.author == author:
            titles.append(post.title)
    if titles:
        return titles
    return

# 검색할 작성자 입력 및 출력
search_author = input("찾으실 글쓴이를 입력해주세요: ")
search_titles = search_name(search_author, posts)
if isinstance(search_titles, list):
    print(f"{search_author}(이)가 작성한 게시글: {','.join(search_titles)}")
else:
    pass


# 검색어가 포함된 글 반환
def search_include(word, posts):
    titles = []
    if word == '':
        return

    for post in posts:
        if word in post.content:
            titles.append(post.title)
    if titles:
        return titles
    return

# 검색할 검색어 입력 및 출력
search_keyword = input("찾으실 검색어를 입력해주세요: ")
search_titles = search_include(search_keyword, posts)
if isinstance(search_titles, list):
    print(f"{search_keyword}(이)가 들어간 게시글: {','.join(search_titles)}")
elif search_keyword == '':
    pass
else:
    print(f"{search_keyword}(이)가 들어간 게시글이 없습니다.")

#새로운 사용자 만드는 함수, 이름 아이디 패스워드 입력 받을때까지 반복
def create_new_user():
    while True:
        new_name = input("이름을 입력하세요: ")
        new_username = input("아이디를 입력하세요: ")
        new_password = input("패스워드를 입력하세요: ")
        if new_name == "" or new_username == "" or new_password == "":
            print("빠트린 입력값이 있습니다. 다시 입력해주세요!")
            new_name = ""
            new_username = ""
            new_password = ""
        else:
            break

    return Member(new_name, new_username, new_password)


members.append(create_new_user())

#새로운 글 작성, 제목 입력 받을때까지 반복
while True:
    new_post = input("제목을 입력하세요: ")
    new_content = input("내용을 입력하세요: ")
    if new_post == '':
        print("제목 입력이 되지 않았습니다. 다시 입력해주세요.")
    else:
        break

#작성자가 members에 없으면 문구 출력 후, while문을 통해 작성자 다시 입력 받음.
flag = False  # while문 탈출도구
while True:
    new_author = input("작성자를 입력하세요: ")
    for member in members:
        if new_author == member.username:
            posts.append(Post(new_post, new_content, new_author))
            flag = True
            break
    if flag == True:
        break
    print("입력하신 작성자의 아이디를 찾을수 없습니다. 다시 입력하세요!")

#새로운 사용자가 추가된 회원 목록
print("회원 목록")
time.sleep(2)
for member in members:
    member.display()

time.sleep(3)
#새로운 글이 추가된 글 목록
print("작성된 글 목록")

time.sleep(2)
for post in posts:
    print(f"제목: {post.title}, 작성자: {post.author}")

time.sleep(2)