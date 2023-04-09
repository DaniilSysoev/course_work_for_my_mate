class Matrix:
    def __init__(self, l = None, h = None) -> None:
        if l == None and h == None:
            self.arr = []
        else:
            self.arr = [[0]*l]*h
    
    def __str__(self) -> str:
        return '\n'.join(['  '.join([str(i) for i in j]) for j in self.arr]) + '\n'
    
    def keybord_input(self) -> None:
        if self.arr != []:
            print(f'Введите матрицу длиной {len(self.arr[0])} и высотой {len(self.arr)}:')
            for i, subarr in enumerate(self.arr):
                line = list(map(int, input().split()))
                if len(line) == len(subarr):
                    self.arr[i] = line
                else:
                    print('Ошибка!\nДлина не совпадает')
                    break
        else:
            l, h = map(int, input('Введите длину и высоту матрицы:\n').split())
            for i in range(h):
                line = list(map(int, input().split()))
                if len(line) == l:
                    self.arr.append(line)
                else:
                    print('Ошибка!\nДлина не совпадает')
                    break
    
    def file_input(self, path: str) -> None:
        with open(path, 'r') as f:
            self.arr = [list(map(int, i.split())) for i in f.readlines()]
    
    def resize(self, h: int, l: int) -> None:
        if h > len(self.arr):
            self.arr.append([0]*len(self.arr[0]))
        elif h < len(self.arr):
            self.arr.pop()
        if l > len(self.arr[0]):
            for i, subarr in enumerate(self.arr):
                self.arr[i].append(0)
        elif l < len(self.arr[0]):
            for i, subarr in enumerate(self.arr):
                self.arr[i].pop()
    
    def clear(self) -> None:
        self.arr = [[0]*len(self.arr[0])]*len(self.arr)

    def __add__(self, other):
        if len(self.arr) == len(other.arr) and len(self.arr[0]) == len(other.arr[0]):
            c = Matrix()
            for i, subarr in enumerate(self.arr):
                line = []
                for j, el in enumerate(subarr):
                    line.append(el+other.arr[i][j])
                c.arr.append(line)
            return c
        else:
            return IndexError
    
    def __mul__(self, other):
        if isinstance(other, int):
            c = Matrix()
            c.arr = [[i*other for i in j] for j in self.arr]
            return c
        elif isinstance(other, Matrix):
            if len(self.arr[0]) == len(other.arr):
                c = Matrix()
                c.arr = [[0 for i in range(len(other.arr[0]))] for j in range(len(self.arr))]
                for i in range(len(self.arr)):
                    for j in range(len(other.arr[0])):
                        for k in range(len(other.arr)):
                            c.arr[i][j] += self.arr[i][k] * other.arr[k][j]
                return c
            else:
                return IndexError


class Calculator:
    def __init__(self):
        self.matrix1 = None
        self.matrix2 = None
        self.run()

    def run(self):
        print("""Список команд:

1 - Ввести матрицу 1
2 - Ввести матрицу 2
3 - Изменить размер
4 - Очистить
5 - Сложить
6 - Умножить на число
7 - Перемножить
8 - Показать матрицы
9 - Выход
""")
        while True:
            command = input("Введите команду:\n")
            if command == "Ввести матрицу 1" or command == '1':
                self.matrix1 = Matrix()
                type_reading = input('Ввод с клавиатуры(1) или из файла(2)?\n')
                if type_reading == '1':
                    self.matrix1.keybord_input()
                elif type_reading == '2':
                    path = input('Введите путь до файла:\n')
                    self.matrix1.file_input(path)
                else:
                    print('Неверная команда')
            elif command == 'Ввести матрицу 2' or command == '2':
                self.matrix2 = Matrix()
                type_reading = input('Ввод с клавиатуры(1) или из файла(2)?\n')
                if type_reading == '1':
                    self.matrix2.keybord_input()
                elif type_reading == '2':
                    path = input('Введите путь до файла:\n')
                    self.matrix2.file_input(path)
                else:
                    print('Неверная команда')
            elif command == 'Изменить размер' or command == '3':
                first_or_second = input('У какой матрицы? (1/2)\n')
                if first_or_second == '1':
                    h, l = map(int, input('Введите высоту и длину матрицы:\n').split())
                    self.matrix1.resize(h, l)
                elif first_or_second == '2':
                    h, l = map(int, input('Введите высоту и длину матрицы:\n').split())
                    self.matrix2.resize(h, l)
                else:
                    print('Неверная команда')
            elif command == "Очистить" or command == '4':
                first_or_second = input('Какую матрицу? (1/2)\n')
                if first_or_second == '1':
                    self.matrix1.clear()
                elif first_or_second == '2':
                    self.matrix2.clear()
                else:
                    print('Неверная команда')
            elif command == 'Сложить' or command == '5':
                print(self.matrix1 + self.matrix2)
            elif command == 'Умножить на число' or command == '6':
                first_or_second = input('Какую матрицу? (1/2)\n')
                digit = int(input('Введите число:\n'))
                if first_or_second == '1':
                    print(self.matrix1 * digit)
                elif first_or_second == '2':
                    print(self.matrix2 * digit)
                else:
                    print('Неверная команда')
            elif command == 'Показать матрицы' or command == '8':
                print(self.matrix1)
                print(self.matrix2)
            elif command == 'Перемножить' or command == '7':
                print(self.matrix1 * self.matrix2)
            elif command == 'Выход' or command == '9':
                break
            else:
                print('Неизвестная команда')


def main():
    calc = Calculator()

main()