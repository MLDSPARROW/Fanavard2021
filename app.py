class Thing:
    size = 0

    def __init__(self, size):
        self.size = size


class Box:
    #returns True if there is free size inside of the Box
    size = 0
    free_size = 0
    things = []
    is_full = False

    def __init__(self, size):
        self.size = size
        self.free_size = size

    def insert(self, thing):
        if self.free_size >= thing.size:
            self.free_size = self.free_size-thing.size
            return True
        else:
            return False


def start(m_boxes_count, k_boxes_size, things_size):
    #main function to find the Maximum number of things to box
    for t in things_size:
        thing = Thing(t)
        things.append(thing)

    picked_thing = {}
    for i in range(0, len(things)):
        picked_thing[i] = 0
        j = i
        last_box = 0
        boxes = []
        for q in range(0, m_boxes_count):
            box = Box(k_boxes_size)
            boxes.append(box)

        while last_box < len(boxes):
            thing = things[j]
            box = boxes[last_box]
            if box.insert(thing):
                picked_thing[i] += 1
                j += 1
                if j >= len(things):
                    break
                continue
            else:
                last_box += 1

    d = max(picked_thing.values())
    print(f"Max thing you can box is {d}")


try:
    n_things_count, m_boxes_count, k_boxes_size = [int(x) for x in input().split(' ')]
    things_size = [int(x) for x in input().split(" ")]
    things = []
    start(m_boxes_count, k_boxes_size, things_size)
except Exception as e:
    pass




