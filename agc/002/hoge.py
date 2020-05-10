current_data = ['a', 'b', 'c', 'd']

def my_input(data):
    for d in data:
        yield d

# input を上書き
input = my_input(current_data).__next__

# テストしたい関数
def solve():
    for _ in range(4):
        c = input()
        if c == 'c':
            print('ABC')
        else:
            print('ARC')


if __name__ == '__main__':
    solve()

