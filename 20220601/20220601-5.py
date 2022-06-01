class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在觀看Netflix.' % self._name)
        else:
            print('%s正在收聽百靈果Podcast.' % self._name)


class Student(Person):
    """學生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在學習%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老師"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在講%s.' % (self._name, self._title, course))


def main():
    stu = Student('陳叮', 18, '大一')
    stu.study('基礎微積分')
    stu.watch_av()
    t = Teacher('蘇', 45, '老師')
    t.teach('深度解析微積分')
    t.watch_av()


if __name__ == '__main__':
    main()