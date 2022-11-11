s="id,name,age,score\\n1,Jack,NULL,12\\n17,Betty,28,11"
s="id,nameagescore/n1jacknull12/n17betty2811"


s="id,name,age,score"


def remove_null(s):
  init_list = s.split('\\n')
  for value in init_list:
    second_list = value.split(',')
    for value2 in second_list:
      if value2=='NULL':
        init_list.remove(value)
  return '\\n'.join(init_list)

remove_null(s)
