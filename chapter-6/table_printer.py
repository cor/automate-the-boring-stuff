def print_table(table):
    column_widths = [max([len(item) for item in column]) for column in table]

    for row in range(len(table[0])):
        for column in range(len(table)):
            cell_content = table[column][row]
            column_width = column_widths[column]
            print(cell_content.rjust(column_width), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)



