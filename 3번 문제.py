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
