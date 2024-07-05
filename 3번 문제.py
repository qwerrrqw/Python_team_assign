import hashlib
# ----- 코드 정의 ------
import hashlib

# Member 클래스 구현


class Member:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f'이름: {self.name}, 아이디: {self.username}')


class Post:
    # author는 인터페이스 구현에서 username 으로 넣어주면 됨
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# ----- 코드 실행 ------
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


# ----------------------

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

new_name = input("이름을 입력하세요: ")
new_user_name = input("아이디를 입력하세요: ")
new_password = input("패스워드를 입력하세요: ")
m4 = Member(new_name, new_user_name, new_password)
members.append(m4)

new_post = input("제목을 입력하세요: ")
new_content = input("내용울 입력하세요: ")

flag = False  # while문 탈출도구
while True:
    new_author = input("작성자를 입력하세요: ")
    for member in members:
        if new_author == member.username:
            post10 = Post(new_post, new_content, new_author)
            posts.append(post10)
            flag = True
            break
    if flag == True:
        break
    print("입력하신 작성자의 아이디를 찾을수 없습니다. 다시 입력하세요!")

print("회원 목록")
for member in members:
    member.display()

print("작성된 글 목록")
for post in posts:
    print(f"제목: {post.title},작성자: {post.author}")
