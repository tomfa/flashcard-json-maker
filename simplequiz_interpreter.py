#coding: utf-8
'''
    This script reads a Q-A txt-file and generates JSON output.

    USAGE:
        Save your Q-A file 

    FORMAT:

    Chapter 1 - cakes. The whole line is a part of the chapter title. 
    Q: Question that we wonder about?
    A: Answer telling us what we want to know?

    Q: Empty lines are ignored. If the question goes across multiple lines,
    that's perfectly fine. We just add the new line to what we added last.
    A: That goes for answers as well. Chapters do however need to be on a 
    single line.

'''


class Question:
    """Et spørsmål"""
    def __init__(self, number, question):
        self.question = question  # String
        self.explaination = "Ingen forklaring gitt"
        self.chapter = ""
        self.qnum = number

    def append_line_to_question(self, more_question):
        self.question += " " + more_question

    def add_explaination(self, explaination):
        self.explaination = explaination

    def append_explaination(self, explaination):
        self.explaination += " " + explaination

    def setChapter(self, chapter):
        self.chapter = chapter


def readQuiz(path):
    f = open(path, 'r')
    lines = f.read().split('\n')
    questions = []
    readingQ = False  # Are we currently reading a question?
    readingA = False  # Are we currently reading an answer?
    currentchapter = ""
    qnum = -1
    for line in lines:
        line = line.strip()

        if is_ignorable(line):
            continue

        if line_defines_chapter(line):
            currentchapter = line
            continue

        if line_defines_question(line):
            qnum += 1
            readingQ = True
            readingA = False
            # line[3:] is to skip the 'q: '. Not pretty
            questions.append(Question(qnum, line[3:]))
            questions[len(questions)-1].setChapter(currentchapter)

        elif line_defines_answer(line):
            readingA = True
            readingQ = False
            # line[3:] is to skip the 'a: '. Not pretty
            questions[len(questions)-1].add_explaination(line[3:])

        # If the line doesn't start with anything interesting, we append to
        elif (readingA):
            questions[len(questions)-1].append_explaination(line)
        elif (readingQ):
            questions[len(questions)-1].append_line_to_question(line)

    return questions


def is_ignorable(line):
    '''
    returns true if line can safely be ignored
    parameter:
    * line: string 
    '''
    return len(line) < 1


def line_defines_question(line):
    return line.lower().startswith('q: ')


def line_defines_answer(line):
    return line.lower().startswith('a: ')


def line_defines_chapter(line):
    return line.lower().startswith('chapter ')


if __name__ == "__main__":
    import sys

    exams = {}
    args = sys.argv[1:]
    if not args:
        print("Usage: Run as 'python flash_interpreter.py myfile.txt'")
        sys.exit()
    
    questions = readQuiz(args[0])
    f = open('data.js', 'w')
    f.write('var questions = [\n')
    for q in questions:
        f.write('{\n')
        f.write('   "id":"' + str(q.qnum) + '",\n')
        f.write('   "chapter":"' + str(q.chapter) + '",\n')
        f.write('   "question":"' + q.question + '",\n')
        f.write('   "answer":"' + q.explaination + '"\n')
        f.write('},\n\n')
    f.write('];')
    print "We're fine. totes fine."
    print "Output saved as data.js"
