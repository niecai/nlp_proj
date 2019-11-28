from lxml import etree

tree = etree.parse('./data/train_set.xml')
root = tree.getroot()

for questions in root:
    for eq in questions:
        for q in eq:
            print(q.text)
    for neq in questions:
        for q in neq:
            print(q.text)
    break


