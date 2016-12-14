import numpy
import random
# import sympy


class DecodeASecret:
    def __init__(self, vectors, lst_of_teachers):
        self.vectors = vectors
        self.lst_of_teachers = lst_of_teachers

    def decode(self):
        code = []
        for letter, teacher_1 in zip(self.vectors, self.lst_of_teachers):
            tmp_matrix = []
            vector = []
            for teacher in self.choose_teachers():
                tmp_matrix.extend(letter[teacher])
                vector.extend(teacher_1[teacher - 1].get_code())
            tmp_matrix = self.merge(tmp_matrix, vector)
            ans = [int(el) for el in sympy.Matrix(tmp_matrix).rref()[0].col(-1)]
            code.append([numpy.array(ans).dot(letter[0][0]),
                         numpy.array(ans).dot(letter[0][1])])
        return code

    def output(self, code):

        output = ""
        for i in range(0, len(code) - 3, 4):
            k = ''
            for arg in code[i:i + 4]:
                k += str(int(arg[0])) + str(int(arg[1]))
            output += chr(int(k, 2))
        return output

    def merge(self, matrix, vactor):
        return [matrix[i] + [vactor[i]] for i in range(len(matrix))]

    def choose_teachers(self):
        tmp = set()
        while len(tmp) != 3:
            tmp.add(random.randint(1, 4))
        return tmp

    def get_value(self, matrix):
        return [line[-1] for line in matrix]
