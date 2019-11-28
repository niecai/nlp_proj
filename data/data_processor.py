import csv
import pickle
import xml.etree.ElementTree as ET

csv_file = csv.reader(open("./dev_set.csv", "r", encoding='UTF-8'))
data = []
t = True
for line in csv_file:
    if t:
        t = False
        continue
    lines = ""
    for l in line:
        lines += l
    data.append(lines.split("\t")[1:])

with open("./dev_set.pickle", "wb") as f:
    pickle.dump(data, f)
    f.close()

tree = ET.parse("./train_set.xml")
root = tree.getroot()

data = []
for questions in root:
    ele = []
    ele1 = []
    ele2 = []
    for ene in questions:
        if ene.tag == "EquivalenceQuestions":
            for question in ene:
                ele1.append(question.text)
        elif ene.tag == "NotEquivalenceQuestions":
            for question in ene:
                ele2.append(question.text)
        else:
            pass
    ele.append(ele1)
    ele.append(ele2)
    data.append(ele)

new_data = []
for d in data:
    new_data.extend([[x, y, 1] for x in d[0] for y in d[0] if x != y and x is not None and y is not None])
    new_data.extend([[x, y, 0] for x in d[0] for y in d[1] if x is not None and y is not None])

#with open("./train.pickle", "wb") as f:
#    pickle.dump(new_data, f)
#    f.close()

with open("./train_set.csv", "w") as f:
    csv_writer = csv.writer(f, delimiter='\t')
    for i in range(len(new_data)):
        a = [i+1]
        a.extend(new_data[i])
        csv_writer.writerow(a)

