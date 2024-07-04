#<담당: 이종화>


# - 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
# > 임시 유저 이름 : 'A', 'B', 'C'
# > 멤버스.어펜드('A')
# > 멤버스.어펜드('B')
# > 멤버스.어펜드('')
members = []

m1 = Member('name', 'username', 'password')
m2 = Member('name', 'username', 'password')
m3 = Member('name', 'username', 'password')

members.append(m1)
members.append(m2)
members.append(m3)

print(members)

# - members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
for member in members:
    print(member.name)

posts = []

# - 각각의 회원이 게시글을 세개 이상 작성하는 코드, 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장
# > ex) posts.append(post('네임', '내용 아무거나', '유저네임'))

p1 = Post('네임', '내용 아무거나', 'user1')
p2 = Post('네임', '내용 아무거나', 'user1')
p3 = Post('네임', '내용 아무거나', 'user1')
posts.append(p1)
posts.append(p2)
posts.append(p3)

p4 = Post('네임', '내용 아무거나', 'user2')
p5 = Post('네임', '내용 아무거나', 'user2')
p6 = Post('네임', '내용 아무거나', 'user2')
posts.append(p4)
posts.append(p5)
posts.append(p6)

p7 = Post('네임', '내용 아무거나', 'user3')
p8 = Post('네임', '내용 아무거나', 'user3')
p9 = Post('네임', '내용 아무거나', 'user3')
posts.append(p7)
posts.append(p8)
posts.append(p9)

print(posts)

