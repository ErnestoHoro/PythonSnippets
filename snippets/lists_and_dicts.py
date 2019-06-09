# MEMO ONLY! THIS IS WRONG IN ALL WAYS! IGNORE!

my_dict_02 = {}
try:
    my_dict_02['Key_A_01']['Key_C_01'].append('String_02')
except:
    try:
        my_dict_02['Key_A_01'].update({'Key_C_01': ['String_02']})
    except:
        my_dict_02['Key_A_01'] = {'Key_C_01': ['String_02']}

print my_dict_02

#--------------------------------------

try:
    my_dict_02['Key_A_01']['Key_C_01'].append('String_03')
except:
    try:
        my_dict_02['Key_A_01'].update({'Key_C_01': ['String_03']})
    except:
        my_dict_02['Key_A_01'] = {'Key_C_01': ['String_03']}

print my_dict_02

#--------------------------------------

try:
    my_dict_02['Key_A_01']['Key_C_02'].append('String_01')
except:
    try:
        my_dict_02['Key_A_01'].update({'Key_C_02': ['String_01']})
    except:
        my_dict_02['Key_A_01'] = {'Key_C_02': ['String_01']}

print my_dict_02
