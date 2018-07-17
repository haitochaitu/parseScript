import sys
class Node:
    levelsList = []
    lineList = []
    indexList = []
    starList = []
    fileBuffer = []

    def __init__(self, val=None):
        self.value = val
        self.children = []

    def __repr__(self):
        return "{}".format(self.value)

    def readFile(self):
        #for line in sys.stdin:
        lines = "".join(line for line in sys.stdin if not line.isspace())
        linelist = lines.split("\n")
        for line in linelist:
            self.setLevel(line)
            self.lineList.append(line.replace(".", ""))
        
    def setLevel(self, line):
        if line.count("*") > 0:
           self.levelsList.append(0)
        elif line.count(".") > 0:
           self.levelsList.append(line.count("."))
        else:
           self.levelsList.append(self.levelsList[len(self.levelsList) - 1])

    def traverseLevels(self):
        for level, value in zip(self.levelsList, self.lineList):
            last = root
            for _ in range(level):
                last = last.children[-1]
            if value.startswith(" ") or value.startswith(".") or value.startswith("*"):
                last.children.append(Node(value))
            else:
                temp = str(last.children[len(last.children) - 1])
                temp += "\n" + "    " + value
                last.children[len(last.children) - 1] = Node(temp)

    def processLines(self, root, depth=0):
        for child in root.children:
            '''To handle main trunck indexes'''
            if child.value.count("*") == 1:
                # To set the trunks first index and its star count
                if not self.indexList:
                   self.indexList.append(1)
                   self.starList.append(1)
                else:
                    # To set the trunks next indexes using last trunk index value
                    for i in reversed(range(len(self.starList))):
                        if (self.starList[i] == 1):
                            self.starList.append(1)
                            self.indexList.append(self.indexList[i]+1)
                            break
            #To handle branch indexes
            elif child.value.count("*") > 1:
                for i in reversed(range(len(self.indexList))):
                    if self.indexList[i]:
                        if child.value.count("*") in self.starList:
                            if child.value.count("*") == self.starList[i]:
                                self.indexList.append(self.indexList[i] + 1)
                                self.starList.append(child.value.count("*"))
                                break
                            if child.value.count("*") > self.starList[i]:
                                self.indexList.append(10 * self.indexList[i] + 1)
                                self.starList.append(child.value.count("*"))
                                break
                        else:
                          self.indexList.append(10 * self.indexList[i] + 1)
                          self.starList.append(child.value.count("*"))
                          break
            else:
                self.starList.append(child.value.count("*"))
                self.indexList.append('')

            indexFormatted = ""
            if child.children.__len__() > 0:
                if child.value.count("*") >= 1:
                    child.value = child.value.replace("*", "")
                    index = str(self.indexList[len(self.indexList) - 1])
                    for i in range(len(index)):
                       indexFormatted = indexFormatted + index[i] +  "."
                       self.fileBuffer.append('  ' * depth +  str(indexFormatted) + '%r' % child)
                else:
                    self.fileBuffer.append('  ' * depth + '+' + str(self.indexList[len(self.indexList)-1]) + '%r' % child)
            else:
                self.fileBuffer.append('  ' * depth + '-' + str(self.indexList[len(self.indexList) - 1]) + '%r' % child)
            self.processLines(child, depth + 1)

if __name__ == '__main__':
   root = Node()
   root.readFile() 
   root.traverseLevels()
   root.processLines(root)
   for lines in root.fileBuffer:
       print(lines)
  