from shapely.geometry import Point, Polygon

p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)

print(poly)
print(f"p1 : {p1}  is in poly : {p1.within(poly)}")
print(f"p2 : {p2}  is in poly : {p2.within(poly)}")

print('End Test1')

coords1 = [(124.749756,23.956136),(124.782715,25.799891),(124.881592,26.32296),(125.299072,26.401711),(125.48584,26.303264),(125.518799,26.046913),(125.474854,25.710837),(125.452881,24.916331),(125.672607,24.696934),(126.013184,24.637031),(126.397705,24.896402),(126.375732,25.443275),(126.287842,25.948166),(126.265869,26.431228),(126.551514,26.55905),(126.881104,26.39187),(126.958008,25.344026),(126.936035,24.186847),(127.364502,23.865745),(127.573242,23.463246),(127.353516,22.948277),(126.694336,22.674847),(126.013184,22.543001),(124.672852,22.684984),(124.255371,23.120154),(124.343262,23.644524),(124.749756,23.956136)]
poly1 = Polygon(coords1)
p1_0 = Point(124.78375, 25.81535)
p1_1 = Point(125.9967, 24.68445)
p1_2 = Point(127.24365, 24)
p1_3 = Point(125.24963, 22.60006)
p1_4 = Point(124.30206, 23.14793)
p1_5 = Point(125.73646, 24.68546)
p1_6 = Point(125.18646, 26.17761)
p1_7 = Point(127.35275, 22.94923)

print(poly1)
print(f"p0 : {p1_0}  is in poly : {p1_0.within(poly1)}")
print(f"p1 : {p1_1}  is in poly : {p1_1.within(poly1)}")
print(f"p2 : {p1_2}  is in poly : {p1_2.within(poly1)}")
print(f"p3 : {p1_3}  is in poly : {p1_3.within(poly1)}")
print(f"p4 : {p1_4}  is in poly : {p1_4.within(poly1)}")
print(f"p5 : {p1_5}  is in poly : {p1_5.within(poly1)}")
print(f"p6 : {p1_6}  is in poly : {p1_6.within(poly1)}")
print(f"p7 : {p1_7}  is in poly : {p1_7.within(poly1)}")

print('End Test2')
