# Import numpy so we can calculate with matrices

import numpy as np

def meetsCrit(num):
    meets = False
    numString = "{}".format(num)
    d = numString[0]
    onRun = False
    foundDouble = False
    for i in numString[1:]:
        if i < d:
            return False
        if i == d and onRun == False:
            meets = True
            onRun = True
        elif i == d and onRun == True:
            meets = False
        if i != d and meets == True:
            foundDouble = True
            onRun = False
        elif i != d and meets == False:
            onRun = False
        d = i
    return meets or foundDouble

def day4():
    print("Day 4")
    numMeets = 0
    for num in range(387638,919123):
        if meetsCrit(num):
            numMeets += 1
    print(numMeets)

# day4()

def traceWire(path, ins):
    x = 0
    y = 0
    steps = 0
    for i in ins:
        direction = i[0]
        distance = int(i[1:])
        if direction == "R":
            for f in range(x, x+distance):
                if (f, y) not in path:
                    path[(f,y)] = steps
                steps = steps + 1
            x = x + distance
        elif direction == "L":
            for f in range(x, x-distance, -1):
                if (f, y) not in path:
                    path[(f,y)] = steps
                steps = steps + 1
            x = x - distance
        elif direction == "U":
            for f in range(y, y+distance):
                if (x, f) not in path:
                    path[(x,f)] = steps
                steps = steps + 1
            y = y + distance
        elif direction == "D":
            for f in range(y, y-distance, -1):
                if (x, f) not in path:
                    path[(x,f)] = steps
                steps = steps + 1
            y = y - distance
    return path

def findCrosses(path, ins):
    x = 0
    y = 0
    steps = 0
    crosses = []
    for i in ins:
        direction = i[0]
        distance = int(i[1:])
        if direction == "R":
            for f in range(x, x+distance):
                if (f, y) in path:
                    crosses.append([f, y, steps+path[(f,y)]])
                steps = steps + 1
            x = x + distance
        elif direction == "L":
            for f in range(x, x-distance, -1):
                if (f, y) in path:
                    crosses.append([f, y, steps+path[(f,y)]])
                steps = steps + 1
            x = x - distance
        elif direction == "U":
            for f in range(y, y+distance):
                if (x, f) in path:
                    crosses.append([x, f, steps+path[(x,f)]])
                steps = steps + 1
            y = y + distance
        elif direction == "D":
            for f in range(y, y-distance, -1):
                if (x, f) in path:
                    crosses.append([x, f, steps+path[(x,f)]])
                steps = steps + 1
            y = y - distance
    return crosses
            
def findsmallestmanhat(crosses):
    minman = 9999999
    for cross in crosses[1:]:
        manhat = abs(cross[0]) + abs(cross[1])
        minman = min(minman, manhat)
    return minman

def findsmalleststeps(crosses):
    minsteps = 9999999
    for cross in crosses[1:]:
        minsteps = min(minsteps, cross[2])
    return minsteps


def day3():
    wire1 = "R1008,U336,R184,D967,R451,D742,L235,U219,R57,D439,R869,U207,L574,U670,L808,D675,L203,D370,L279,U448,L890,U297,R279,D613,L411,D530,L372,D88,R986,U444,R319,D95,L385,D674,R887,U855,R794,U783,R633,U167,L587,D545,L726,D196,R681,U609,R677,U881,R153,D724,L63,U246,R343,U315,R580,U872,L516,U95,R463,D809,R9,U739,R540,U670,L434,D699,L158,U47,L383,D483,L341,U61,R933,D269,R816,D589,R488,D169,R972,D534,L995,D277,L887,D657,R628,D322,R753,U813,L284,D237,R676,D880,L50,D965,L401,D619,R858,U313,L156,U535,R664,U447,L251,U168,L352,U881,L734,U270,L177,D903,L114,U998,L102,D149,R848,D586,L98,D157,R942,U496,R857,U362,R398,U86,R469,U358,L721,D631,R176,D365,L112,U472,L557,D153,R97,D639,L457,U566,R570,U106,R504,D292,L94,U499,R358,U653,L704,D627,R544,D24,L407,U513,R28,U643,L510,U579,R825,D376,L867,U999,R134,D734,R654,D989,L920,U872,R64,U626,R751,D425,R620,U274,L471,D83,R979,U577,L43,D320,R673,D187,R300,U134,L451,D717,R857,U576,R570,U988,R745,U840,R799,U809,R573,U354,L208,D976,L417,U473,L555,U563,L955,U823,R712,D869,L145,D735,L780,D74,R421,U42,L158,U689,R718,D455,L670,U128,L744,U401,R149,U102,L122,U832,R872,D40,R45,D325,L553,U980,L565,D497,L435,U647,L209,D822,L593,D28,R936,U95,R349,U511,L243,U895,R421,U336,L986,U264,R376,D183,R480,D947,R416,D706,R118,D799,R424,D615,R384,U185,L338,U14,R576,D901,L734,D417,L62,D254,R784,D973,R987,D848,R32,D72,L535,D633,L668,D664,R308,D474,L418,D39,L473,U388,L518,D544,R118,D948,L844,D956,R605,U14,L948,D78,L689,U443,L996,U932,R81,D879,R556,D633,R131"
    wire2 = "L993,U227,L414,U228,L304,U53,R695,U765,R162,D264,L530,U870,R771,D395,R27,D200,L235,D834,L559,D128,R284,U912,L959,U358,R433,U404,L539,U799,R271,D734,L104,U261,R812,D15,L474,U887,R606,U366,L694,U156,R385,D667,L329,D434,R745,U776,L319,U756,R208,D457,R705,U999,R284,U98,L657,U214,R639,D937,R675,U444,L891,D587,L914,D4,R294,D896,R534,D584,L887,U878,L807,U202,R505,U234,L284,D5,R667,U261,L127,D482,R777,D223,L707,D468,L606,U345,L509,D967,R437,U995,R28,D376,L2,D959,L814,U702,L38,D154,L79,D439,L259,U143,L376,U700,R894,U165,L300,D58,R631,D47,R684,U935,R262,D857,R797,D599,L705,U792,R439,D444,R398,D887,L81,D40,R671,U332,L820,U252,R691,U412,L794,D661,R810,U157,R858,U566,R892,D543,R10,D725,L653,D812,R733,D804,R816,U862,R994,U221,L33,U271,R766,D591,R575,D970,R152,D693,L916,U404,L658,D847,L605,D433,L583,U587,L129,D103,R407,U780,L901,D676,L846,D687,L9,D47,R295,D597,L808,U134,L186,D676,L62,U305,L73,D369,L468,U30,L472,U280,L413,U961,L98,D966,R308,D178,L21,D789,L871,D671,R665,U927,L906,U633,L135,D894,R110,D205,R324,D665,R143,D450,L978,U385,R442,D853,L518,U542,R211,U857,R119,D872,L246,U380,L874,U463,R153,U982,R832,D784,L652,U545,R71,U386,R427,D827,R986,U870,R959,U232,R509,U675,R196,U389,R944,U149,R152,U571,R527,U495,L441,U511,L899,D996,L707,D455,L358,D423,L14,D427,R144,D703,L243,U157,R876,D538,R26,D577,L385,U622,L149,D852,L225,U475,L811,D520,L226,U523,L338,D79,R565,U766,L609,U496,L189,D446,R63,U396,L629,U312,L841,D639,R466,U808,L60,D589,L146,U114,R165,U96,L809,D704,L61"
    #wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    #wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    # wire1 = "R8,U5,L5,D3"
    # wire2 = "U7,R6,D4,L4"
    wire1a = wire1.split(",")
    wire2a = wire2.split(",")
    path = {}
    path = traceWire(path, wire1a)
    crosses = findCrosses(path, wire2a)
    minman = findsmallestmanhat(crosses)
    minsteps = findsmalleststeps(crosses)
    print(minman)
    print(minsteps)
    print("done")
    
# day3()


def rec_fuel(module):
    fuel_req = np.floor(module / 3) -2
    if fuel_req <= 0:
        return 0
    else:
        return (fuel_req + rec_fuel(fuel_req))

def simp_fuel(module):
    return np.floor(module / 3) -2

def day2():
    # Create matrix with the input
    matrix_input = [71764, 58877, 107994, 72251, 74966, 87584, 118260, 144961, 86889, 136710, 52493, 131045, 101496, 124341, 71936, 88967, 106520, 125454, 113463, 81854, 99918, 105217, 120383, 61105, 103842, 125151, 139191, 143365, 102168, 69845, 57343, 93401, 140910, 121997, 107964, 53358, 57397, 141456, 94052, 127395, 99180, 143838, 130749, 126809, 70165, 92007, 83343, 55163, 95270, 101323, 99877, 105721, 129657, 61213, 130120, 108549, 90539, 111382, 61665, 95121, 53216, 103144, 134367, 101251, 105118, 73220, 56270, 50846, 77314, 59134, 98495, 113654, 89711, 68676, 98991, 109068, 129630, 58999, 132095, 98685, 91762, 88589, 73846, 124940, 106944, 133882, 104073, 78475, 76545, 144728, 72449, 118320, 65363, 83523, 124634, 96222, 128252, 112848, 139027, 108208]
    init_prog_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0]

    target = 19690720

    for noun in range(100):
        for verb in range(100):
            print(noun, verb)
            prog_input = init_prog_input.copy()
            prog_input[1] = noun
            prog_input[2] = verb

            ip = 0
            while prog_input[ip] != 99:
                if prog_input[ip] == 1: # add
                    prog_input[prog_input[ip+3]] = prog_input[prog_input[ip+1]]+prog_input[prog_input[ip+2]]
                    ip += 4
                elif prog_input[ip] == 2: # mult
                    prog_input[prog_input[ip+3]] = prog_input[prog_input[ip+1]]*prog_input[prog_input[ip+2]]
                    ip += 4
                else: # error
                    print("error")
                    break
            if prog_input[0] == target:
                print("found it")
                print(noun*100+verb)
                return
            

def day1():
    # Calculate the output
    tot_fuel = 0
    for module in matrix_input:
        tot_fuel += rec_fuel(module)
    # Print the output
    print(tot_fuel)


