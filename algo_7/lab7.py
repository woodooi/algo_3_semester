class Indiana:
    def __init__(self, rows, cols, corridor):
        self.rows = rows
        self.cols = cols
        self.corridor = corridor
        self.alphabet = set(char for row in corridor for char in row)

        self.character_counts = {char: 0 for char in self.alphabet}

    def _initialize_data_structures(self):
        routes = [[0] * self.cols for _ in range(self.rows)]
        group_routes = {char: 0 for char in self.alphabet}
        routes_in_row = {char: 0 for char in self.alphabet}
        character_count = {char: 0 for char in self.alphabet}
        return routes, group_routes, routes_in_row, character_count

    def _update_counts(self, character):
        for char in self.alphabet:
            self.group_routes[char] += self.routes_in_row[char]
            self.character_counts[char] += self.character_count[char]

    def _update_routes_and_counts(self, i, j, character, prev_character, prev_character_value):
        character_quantity = self.character_counts[character]

        if character == prev_character:
            prev_character_value = -1

        self.routes[i][j] = character_quantity + prev_character_value + self.group_routes[character]
        self.character_count[character] += 1
        self.routes_in_row[character] += self.routes[i][j]

    def all_exits(self):
        count = 0
        self.routes, self.group_routes, self.routes_in_row, self.character_count = self._initialize_data_structures()

        for j in range(self.cols):
            self._update_counts(self.corridor[0][j])

            for char in self.alphabet:
                self.routes_in_row[char] = 0
                self.character_count[char] = 0

            for i in range(self.rows):
                count += 1
                character = self.corridor[i][j]

                if j == 0:
                    self.character_counts[character] = self.character_counts[character] + 1
                else:
                    prev_character = self.corridor[i][j-1]
                    prev_character_value = self.routes[i][j-1]

                    self._update_routes_and_counts(i, j, character, prev_character, prev_character_value)

        if self.rows == 1:
            result = self.routes[0][self.cols - 1] + 1
        else:
            result = self.routes[self.rows - 1][self.cols - 1] + self.routes[0][self.cols - 1] + 2

        print(count)
        return result


def read(rows):
    num_rows, num_cols = 0, 0
    char_array = []

    for row in rows:
        values = row.split()

        if len(values) == 2:
            num_rows, num_cols = map(int, values)
        else:
            char_row = list(map(str.strip, values))
            char_array.append(char_row)

    return num_rows, num_cols, char_array


file_path = 'igones.in'

with open(file_path, 'r') as file:
    file_content = file.readlines()

num_rows, num_cols, char_array = read(file_content)

if __name__ == '__main__':
    indiana = Indiana(num_rows, num_cols, char_array)
    result1 = indiana.all_exits()
    print(result1)
