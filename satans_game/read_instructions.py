def get_instructions():
    """Returns Satans instructions inside 
       a list in the following order
       (operation, first_coordinate, second coordinate)
    """

    def get_coordinates(str_coord):
        x,y = str_coord.split(',')
        return (int(x), int(y))

    with open('./input', 'r') as f:
        raw_instructions = f.readlines()
        instructions = []

    for step in raw_instructions:
        step = step.replace('\n','').replace(' through','')
        step = step.split(' ')
        first = get_coordinates(step[-2])
        second = get_coordinates(step[-1])
        op = ''.join(step[0:-2])

        op_enum = {
            'turnoff': 0,
            'turnon': 1,
            'toggle': 2
        }

        instructions.append((op_enum[op], first, second))
    return instructions

