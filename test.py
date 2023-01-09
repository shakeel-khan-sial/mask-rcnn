import pdb

a = {'filename': 'IMG_3183.jpg', 'size': 877509, 'regions': [{'shape_attributes': {'name': 'polygon', 'all_points_x': [642, 728, 709, 617], 'all_points_y': [669, 707, 728, 690]}, 'region_attributes': {'Shape': {'BrownSpot': True}}}], 'file_attributes': {}}
print(type(a))

for i in [a]:
    print(i['regions'])
    print([s['region_attributes']['Shape'] for s in a['regions']])
