def is_similar_sp(a, b):
    xor = a ^ b
    count = 0
    while (xor):
        xor = xor & (xor - 1)
        count += 1
    
    if count <= 4:
      return True
    
    return False

video_list = [
  # video 1
  [1611, 3712, 8324, 1747, 1612, 1611],
  # video 2
  [1611, 1611, 8323, 9012, 9015],
  # video 3
  [1747, 1747, 1610],
  # video 4
  [8324, 1612, 1747, 3711]
]

from collections import defaultdict

finger_dict = defaultdict(set)

for video_index, video_value in enumerate(video_list):
  for finger_number in video_value:

    finger_dict[finger_number].add(video_index)
 

finger_pairs = defaultdict(int)

for video in video_list:
  for i in range(len(video)):
    for j in range(i+1, len(video)):
      finger1 = video[i]
      finger2 = video[j]
      if is_similar_sp(finger1, finger2):
        pair = (finger1, finger2) if finger1 < finger2 else (finger2, finger1)
        finger_pairs[pair] = len(finger_dict[finger1] | finger_dict[finger2])



    # output = finger_pairs: 
    # {(1611, 1747): 4, 
    # (1611, 1612): 3, 
    # (1611, 1610): 3, 
    # (1611, 3711): 3, 
    # (8324, 8323): 3, 
    # (1747, 1610): 3, 
    # (1612, 1610): 3, 
    # (9012, 9015): 1}

