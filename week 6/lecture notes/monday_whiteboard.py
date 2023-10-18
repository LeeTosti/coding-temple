# Example 1:
# input: ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST']
# output:['WEST','WEST']
# In ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST'] 'NORTH' and 'SOUTH' are not directly opposite but they become directly opposite after reduction of 'EAST' and 'WEST'. The whole path can be reduced to ['WEST','WEST'].
# Example 2:
# input: ['EAST','NORTH','WEST','SOUTH']
# output:['EAST','NORTH','WEST','SOUTH']
# Not all paths are reducible. The path ['EAST','NORTH','WEST','SOUTH'] is not reducible. 'EAST' and 'NORTH', 'NORTH' and 'WEST', 'WEST' and 'SOUTH' are not directly opposite of each other and thus can't be reduced. The resulting path has not changed from the original path: ['EAST','NORTH','WEST','SOUTH']
#up and around a mountain maybe?

def directions(in_list):
    out_list = []
    logic_dict = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    for n in in_list:
        if len(out_list) != 0 and n == logic_dict[out_list[-1]]:
            out_list.pop()
        else:
            out_list.append(n)
    return out_list

print(directions(['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST']))