trans_table = [
  ["<","<","<","<","<mosd","<mosd","<","<mosfd=>MOSFD","<mosd","<mosd","<","<","<"],
  ["<","<","<","m","osd","osd","m",">MOSD","f=F","osd","m","<","<"],
  ["<","<","<mo","o","osd","osd","o",">MOSD","OSD","osfd=OSFD","oFD","<mo","<moFD"],
  ["<","<","<mo","s","d","d","s",">","M","fdO","s=S","<mo","<moFD"],
  ["<","m","osd","d","f","d","f",">",">",">MO",">MO","f=F",">MOSD"],
  ["<","<","<mosd","d","d","d","d",">",">","df>OM","df>OM","<mosd","<mosfd=>MOSFD"],
  ["<","m","o","s","f","d","=",">","M","O","S","F","D"],
  ["<mosfd=>MOSFD","df>OM","df>OM","df>OM",">","df>OM",">",">",">",">",">",">",">"],
  ["<moFD","s=S","fdO","fdO","M","fdO","M",">",">",">",">","M",">"],
  ["<moFD","oFD","osfd=OSFD","fdO","O","fdO","O",">",">",">MO",">MO","OSD",">MOSD"],
  ["<moFD","oFD","oFD","s=S","O","fdO","S",">","M","O","S","D","D"],
  ["<","m","o","o","f=F","osd","F",">MOSD","OSD","OSD","D","F","D"],
  ["<moFD","oFD","oFD","oFD","OSD","osfd=OSFD","D",">MOSD","OSD","OSD","D","D","D"]
]

def remove_duplicates(l):
  return list(dict.fromkeys(l))

def index(character):
  return list("<mosfd=>MOSFD").index(character)

def get_trans_two(rel1, rel2):
  pairwise_results = "".join([trans_table[index(c1)][index(c2)] for c1 in rel1 for c2 in rel2])
  duplicates_removed = remove_duplicates(list(pairwise_results))
  return "".join(duplicates_removed)

def get_trans_list(rel_list):
  if len(rel_list) <= 1:
    return rel_list
  return get_trans_list([get_trans_two(rel_list[0], rel_list[1])] + rel_list[2:])

if __name__ == "__main__":
  print("case 00: ", get_trans_list(["s=S", "<moFD", "s=S"]))
  print("case 01: ", get_trans_list(["s=S", "<mosfd=OSFD", "m"]))
  print("case 02: ", get_trans_list(["s=S", "<moFD", "M"]))
  print("case 03: ", get_trans_list(["s=S", "<mosfd=OSFD", "f=F"]))

  print("case 04: ", get_trans_list(["M", "<", "s=S"]))
  print("case 05: ", get_trans_list(["M", "<mosd", "m"]))
  print("case 06: ", get_trans_list(["M", "<", "M"]))
  print("case 07: ", get_trans_list(["M", "<mosd", "f=F"]))

  print("case 08: ", get_trans_list(["m", "<moFD", "s=S"]))
  print("case 09: ", get_trans_list(["m", "<mosfd=OSFD", "m"]))
  print("case 10: ", get_trans_list(["m", "<moFD", "M"]))
  print("case 11: ", get_trans_list(["m", "<mosfd=OSFD", "f=F"]))

  print("case 12: ", get_trans_list(["f=F", "<", "s=S"]))
  print("case 13: ", get_trans_list(["f=F", "<mosd", "m"]))
  print("case 14: ", get_trans_list(["f=F", "<", "M"]))
  print("case 15: ", get_trans_list(["f=F", "<mosd", "f=F"]))