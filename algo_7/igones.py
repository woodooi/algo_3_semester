class Indiana:
    def __init__(self, rows, cols, corridor):
        self.rows = rows
        self.cols = cols
        self.corridor = corridor
        self.alph = set(char for row in corridor for char in row)

        self.count = {char: 0 for char in self.alph}

    def all_exits(self):
        count = 0
        routes = [[0] * self.cols for _ in range(self.rows)]
        group_routes = {char: 0 for char in self.alph}
        routes_in_row = {char: 0 for char in self.alph}
        char_count = {char: 0 for char in self.alph}

        for j in range(self.cols):
            for char in self.alph:
                group_routes[char] += routes_in_row[char]
                self.count[char] += char_count[char]

            for char in self.alph:
                routes_in_row[char] = 0
                char_count[char] = 0

            for i in range(self.rows):
                count += 1
                char = self.corridor[i][j]

                if j == 0:
                    self.count[char] = self.count[char] + 1
                else:
                    char_quantity = self.count[char]
                    prev_char = self.corridor[i][j-1]
                    prev_char_value = routes[i][j-1]

                    if char == prev_char:
                        prev_char_value = -1

                    routes[i][j] = char_quantity + prev_char_value + group_routes[char]
                    char_count[char] += 1
                    routes_in_row[char] += routes[i][j]

        if self.rows == 1:
            result = routes[0][self.cols - 1] + 1
        else:
            result = routes[self.rows - 1][self.cols - 1] + routes[0][self.cols - 1] + 2

        print(count)
        return result

def read(rows):
    H, W = 0, 0
    char_array = []

    for row in rows:
        values = row.split()

        if len(values) == 2:
            H, W = map(int, values)
        else:
            char_row = list(map(str.strip, values))
            char_array.append(char_row)

    return H, W, char_array

file_path = 'igones.in'

with open(file_path, 'r') as file:
    file_content = file.readlines()

H, W, char_array = read(file_content)

if __name__ == '__main__':
    indiana = Indiana(H, W, char_array)
    result1 = indiana.all_exits()
    print(result1)
