#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########

def merge_lists(all_lst):
    """ Merges n sorted lists into 1 list
    """
    def is_list_empty(lst):
        return len(lst) == 0
    
    def all_lists_empty():
        for lst in all_lst:
            if not is_list_empty(lst):
                return False
        return True
    
    def find_first_elements():
        result = []
        for lst in all_lst:
            if not is_list_empty(lst):
                result.append(lst[0])
        return result

    def remove_element_from_all_lst(elt):
        """ Assumes the element to be removed is the 1st element
        of a sublist within all_lst
        """
        for lst in all_lst:
            if not is_list_empty(lst):
                if elt == lst[0]:
                    lst.remove(elt)
                    break
        return all_lst
            
    result = []

    while not all_lists_empty():
        first_elements = find_first_elements()
        element_to_be_merged = min(first_elements)
        # print(element_to_be_merged)
        result.append(element_to_be_merged)
        # print(f"all_lst: {all_lst}")
        remove_element_from_all_lst(element_to_be_merged)

    return result

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
print("## Q1a ##")
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]


###########
# Task 1b #
###########

def merge(lists, field):
    """ Sorts module lists based on fields.
    """
    def is_list_empty(lst):
        return len(lst) == 0
    
    def all_lists_empty():
        for lst in lists:
            if not is_list_empty(lst):
                return False
        return True
    
    def find_first_modules_in_sublists():
        result = []
        for lst in lists:
            if not is_list_empty(lst):
                first_module = lst[0]
                result.append(first_module)
        return result

    def remove_mod_from_lists(target_mod):
        """ Assumes the module to be removed is the 1st element
        of a sublist within all_lst
        """
        for lst in lists:
            if not is_list_empty(lst):
                first_mod = lst[0]
                if first_mod == target_mod:
                    lst.remove(first_mod)
                    break
        return lists
        
    result = []

    while not all_lists_empty():
        first_modules_in_sublists = find_first_modules_in_sublists()
        target_mod = min(first_modules_in_sublists,
                         key=lambda module: field(module))
        result.append(target_mod)
        # print(f"result: {result}")
        remove_mod_from_lists(target_mod)

    return result


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
print("## Q1b ##")
print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########

def merge_sort(lst, k, field):
    def divisible_by(a,b):
        return a % b == 0
    
    def split_list(lst, k):
        """ Splits lst into k sorted chunks

        len(lst) will always >= 2

        List[Module] -> List[List[Module]]
        """
        result = []
        lst_len = len(lst)
        lists_remaining = k
        lower_index = 0
        if divisible_by(lst_len, k):
            next_list_len = lst_len // k       
        else:
            next_list_len = (lst_len // k) + 1
        for _ in range(k):
            upper_index = lower_index + next_list_len
            next_list = lst[lower_index:upper_index]
            next_list = merge_sort(next_list, k, field)
            result.append(next_list)
            lower_index = upper_index
        return result

    if len(lst) <= 1:
        return lst
    else:
        sorted_sublists = split_list(lst, k)
        result = merge(sorted_sublists, field)            
        return result


# For your own debugging
modules = read_json('modules_small.txt')
for module in merge_sort(modules, 2, module_prof):
    print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
test('modules_small')
test('modules')
test('modules_empty')
