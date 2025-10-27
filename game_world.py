#game 내 객체들의 생성과 소멸을 관리하는 모듈

#world[0] : 0차 오브젝트들
#world[1] : 1차 오브젝트들
world = [[],[]]

def add_object(o, depth = 0):
    world[depth].append(o)



def update():
    for layer in world:
        for o in layer:
            o.update()

#이거 clear_canvas 안씀 왜? 독립적으로 만들어야 다른데서 쓸 수 있으니까
def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            world.remove(o)

    raise Exception("No object")