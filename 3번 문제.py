import hashlib
# ----- 코드 정의 ------
class Member:
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)   
    
    def hash_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()
        
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

m1 = Member('name', 'username', 'password')
m2 = Member('name', 'username', 'password')
m3 = Member('name', 'username', 'password')

members.append(m1)
members.append(m2)
members.append(m3)

print(members)

posts = []

# TODO : 코드 구현이 필요합니다.

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

print(posts)


#----------------------

def search_name(author, posts):
    titles = []
    for post in posts:
        if post.author == author:
            titles.append(post.title)
    if titles:
        return titles
    return
# 글쓴이를 입력했을때 해당글쓴이가 작성한 포스트의 제목을 반환하는 함수작성
search_author = input("찾으실 글쓴이를 입력해주세요: ")
# 사용자로부터 검색할 글쓴이 입력받기
search_titles = search_name(search_author, posts)
if isinstance(search_titles, list):
    print(f"{search_author}가 작성한 게시글: {','.join(search_titles)}")
else:
    print(f"{search_author}가 작성한 게시글이 없습니다.")
# 입력받은 글쓴이가 작성한 포스트의 제목들 출력

def search_include(word, posts):
    titles = []
    for post in posts:
        if word in post.content:
            titles.append(post.title)
    if titles:
        return titles
    return
# 검색어를 입력했을때 해당검색어가 들어간 포스트의 제목을 반환하는 함수작성
search_keyword = input("찾으실 검색어를 입력해주세요: ")
# 사용자로부터 검색할 검색어 입력받기
search_titles = search_include(search_keyword, posts)
if isinstance(search_keyword, list):
    print(f"{search_keyword}가 들어간 게시글: {','.join(search_titles)}")
else:
    print(f"{search_keyword}가 들어간 게시글이 없습니다.")
# 입력받은 검색어가 들어간 포스트의 제목을 출력
