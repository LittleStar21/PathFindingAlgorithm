import csv

path = [1718165260, 1718165257, 1718165254, 4308577535, 1718165245, 1718165242, 4308577537, 316622556, 316622557, 4447117347, 1986413696, 316622558, 4308577515, 316622574, 1371261642, 4308577520, 316622589, 2903217080, 361552950, 361552953, 1101582347, 2628010851, 361552960, 2628010869, 361552964, 1477986274, 1477986278, 1482254014, 1482255436, 1477986292, 1482253606, 361552968, 1477986289, 1554230232, 1987064875, 1987064893, 1099409473, 1987064896, 1987064903, 1099409357, 4421628633, 4421628634, 4421628635, 1987064926, 5601255521, 316622614, 5601254520, 5601255523, 2628011042, 1554230272, 1554230252, 318919585, 318919586, 1371261651, 1714279084, 4153548979, 429592649, 2773378648, 1514959422, 4413461770, 318919601, 1919128613, 4413461771, 3226679876, 321706315, 7916358972, 1705800177, 3226679872, 1983226968, 1983226972, 4413461774, 318919602, 1983226974, 1984416742, 1986435995, 2130983101, 1984416738, 1984416735, 2631338128, 1984416740, 1984416747, 3226656259, 1984416748, 1984416750, 2270099690, 1946526319, 1984416756, 1984416769, 1984416782, 1984416788, 1984416790, 1984416789, 1986413819, 1084310039, 1632848884, 1984416784, 1984416786, 1984416792, 1984416795, 318919610, 1984416807, 4279628661, 3357222498, 3357222497, 4279628669, 1984416809, 1984416815, 1984416819, 1984416822, 1984416827, 1984416831, 4413450839, 4429427767, 1984416832, 1984416835, 1984416838, 1984416841, 1984416845, 4383459631, 1984416849, 1984416850, 1984416852, 1984416853, 1984416855, 1984416857, 1984416859, 1984416860, 1984416862, 1984416864, 1984416867, 1984416870, 1984416884, 318919628, 1984387099, 1163353714, 1984387100, 318919638, 427515899, 318919640, 1984387105, 1984387106, 1984387107, 1388692536, 426526840, 318919652, 2905733961, 2905733957, 1984387109, 423743087, 424652484, 318919653, 5365901142, 5365901139, 3479084595, 1959272031, 1076646621, 6843921739, 1941922163, 420547139, 1941922182, 4413454756, 1779179564, 318919665, 322800791, 3307250555, 2337126697, 2384319075, 1953248332, 2989548204, 3335310397, 3335310393, 426886941, 6333711654, 2989548201, 3951170837, 2320725484, 1163353721, 2909017356, 2390401896, 2900239902, 1163353680, 322800777, 2905733426, 1151193141, 2384319124, 1084310110, 2560226750, 1151193544, 322800776, 4413415503, 1151193291, 4413415504, 1151193614, 2384319144, 1373613636, 1373613638, 1307159522, 3356076996, 1678645322, 2381663270, 431540545, 2381663271, 1168830409, 2384319148, 3356050891, 2384319149, 431411922, 1168830691, 1168830643, 1168830307, 1168830738, 426886933, 4413520826, 3325080843, 3718018444, 3718018446, 6884384337, 3724528897, 1957092204, 3724528889, 426886935, 3724528896, 3718018450, 3718018447, 3718018465, 1871016662, 4419531248, 4419531265, 4419531272, 1871016663, 431174270, 4419531288, 8342421257, 3724528903, 3724528890, 2826776860, 418575654, 3724528908, 2826776859, 3724528906, 2826776857, 2826776858, 3375919222, 1747621169, 1747621171, 3375916352, 3724528905, 3375916351, 418575657, 3375916350, 3724528910, 3375916349, 1747621176, 418575658, 418575660, 4413446522, 4382889554, 4382889555, 2135602621, 418575661, 3375919207, 3724528911, 1072288177, 4413435823, 4413435824, 4382889553, 2135550958, 4448324765, 2135559156, 2135623788, 2135559193, 2135545025, 4413410438, 426882047, 2135551768, 1747621177, 4448311616, 2135569698, 418575662, 4418950190, 2135622504, 2135570690, 1156712654, 4584751463, 426882055, 4679610782, 4413395061, 426882048, 2136831318, 315310715, 418760276, 8209698427, 4408377478, 2989530405, 315310714, 7537285910, 4448328969, 4526522054, 4679610769, 7537285898, 6303177433, 6303177406, 6048727525, 7537285917, 4526522049, 7537285915, 6048727505, 7537285836, 7537285862, 7537285835, 7537285865, 6048727504, 3355299872, 7537285809, 3355299871, 3355299870, 7537285807, 7537285808, 3355299869, 3355299868, 7537285802, 4832691381, 5698312304, 7537285805, 1072288405, 7537285804, 6073140590, 6432553864, 4009308661, 6432553877, 7537285790, 1072287920, 7537285788, 7537285724, 924215682, 7537285725, 7537285726, 1072288414, 8513026829, 7537285727, 7537285728, 7537285729, 8513026827]

graph = {}
with open("edges.csv", "r") as file:
    reader = csv.DictReader(file)

    speeds = []
    avg_speed = 0

    for row in reader:
        start_node = int(row["start"])
        end_node = int(row["end"])
        distance = float(row["distance"])
        speed_limit = float(row["speed limit"]) * 5 / 18

        time_taken = distance / speed_limit

        speeds.append(speed_limit)
        avg_speed += speed_limit

        if not start_node in graph:
            graph[start_node] = [(time_taken, end_node)]
        else:
            graph[start_node].append((time_taken, end_node))
    
    print(avg_speed / len(speeds))