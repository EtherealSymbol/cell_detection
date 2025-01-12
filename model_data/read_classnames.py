class_names = []
with open('coco_classes.txt') as f:
    for n in f.readlines():
        class_names.append(n.strip())


print(class_names)