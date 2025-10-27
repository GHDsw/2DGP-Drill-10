#game 내 객체들의 생성과 소멸을 관리하는 모듈

world = []

def add_object(o):
    world.append(o)

def update():
    for o in world:
        o.update()

#이거 clear_canvas 안씀 왜? 독립적으로 만들어야 다른데서 쓸 수 있으니까
def render():
    for o in world:
        o.draw()