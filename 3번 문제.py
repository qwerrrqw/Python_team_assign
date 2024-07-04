# ----- 코드 정의 ------
class Member:
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

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
posts = []

# TODO : 코드 구현이 필요합니다.




#----------------------

def search_name(author, posts):
    titles = []
    for post in posts:
        if post.author == author:
            titles.append(post.title)
    if titles:
        return titles
    return "없음."  #없음을 반환할시 출력되는 글이 부자연스러워서 없음 으로 수정
# 글쓴이를 입력했을때 해당글쓴이가 작성한 포스트의 제목을 반환하는 함수작성
search_author = input("찾으실 글쓴이를 입력해주세요: ")
# 사용자로부터 검색할 글쓴이 입력받기
search_titles = search_name(search_author, posts)
print(f"{search_author}가 작성한 게시글: {','.join(search_titles)}")
# 입력받은 글쓴이가 작성한 포스트의 제목들 출력

def search_include(word, posts):
    titles = []
    for post in posts:
        if word in post.content:
            titles.append(post.title)
    if titles:
        return titles
    return "없음." #없음을 반환할시 출력되는 글이 부자연스러워서 없음 으로 수정
# 검색어를 입력했을때 해당검색어가 들어간 포스트의 제목을 반환하는 함수작성
search_keyword = input("찾으실 검색어를 입력해주세요: ")
# 사용자로부터 검색할 검색어 입력받기
search_titles = search_include(search_keyword, posts)
print(f"{search_keyword}가 들어간 게시글: {','.join(search_titles)}")
# 입력받은 검색어가 들어간 포스트의 제목을 출력
