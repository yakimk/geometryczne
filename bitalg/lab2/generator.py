# ! = \{    @ =\} 
spec = [[[100, 1000, 10000, 100000, 1000000], [100, 1000, 10000, 100000, 1000000]],
 [[100, 1000, 10000], [100, 1000, 10000]],
 [[100, 1000, 10000, 100000, 1000000], [100, 1000, 10000, 100000, 1000000]],
 [[100, 1000, 10000, 100000, 1000000], [100, 1000, 10000, 100000, 1000000]]]
times = [[0.0005893707275390625,
  0.0005006790161132812,
  0.007127523422241211,
  0.01019287109375,
  0.08750700950622559,
  0.10708951950073242,
  1.2220854759216309,
  1.7707273960113525,
  15.013105869293213,
  25.266388654708862],
 [0.0008351802825927734,
  0.007752656936645508,
  0.011487483978271484,
  0.6783807277679443,
  0.12983942031860352,
  70.70918583869934],
 [0.0026688575744628906,
 0.001031637191772461,
 0.043378591537475586,
 0.014216184616088867,
 0.4688549041748047,
 0.15799760818481445,
 7.028165817260742,
 1.727832555770874,
 82.46651887893677,
 17.558522701263428],
 [0.0015366077423095703,
  0.0007996559143066406,
  0.026697397232055664,
  0.011160135269165039,
  0.2120823860168457,
  0.07677173614501953,
  2.8156211376190186,
  0.9206950664520264,
  37.919477462768555,
  9.709136724472046]]
def gen_tab(spec, test_set):
    letter = ['a', 'b', 'c', 'd']
    letter = letter[test_set]
    n = len(spec[1])

    points = graham = jarvis= ""
    for i in range(n):
        points += "& "
        points += str(spec[1][i])
        graham += "& "
        graham += str(round(times[test_set][2* i], 3))
        jarvis += "& "
        jarvis += str(round(times[test_set][2*i + 1], 3))

    s = '''
\\begin!table@[ht]
    \\centering
\\begin!tabular@!l  {rs}@
    & \\multicolumn!{n}@!c@!\\textbf!Liczba punktów@@ \\\\ \\cline!2-{np}@     
    \\multicolumn!1@!l|@!\\textbf!Algorytm@@ {points} \\\\
   \\hline
   \\hline
   \\multicolumn!1@!l|@!\\textbf!Graham@@ {Graham} \\\\
   \\hline
   \\multicolumn!1@!l|@!\\textbf!Jarvis@@ {Jarvis} \\\\
   \\cline!2-{np}@
\\end!tabular@
\\caption*!Tabela {test_set}: Czasy wykonania algorytmów na zbiorze testowym ${letter}$.@
\\end!table@
'''.format(rs = "r|" * n, n=n, np = n+1, points= points, Graham = graham, Jarvis = jarvis, test_set  = test_set+1, letter = letter)
    s = s.replace("@", "}")
    s = s.replace("!", "{")
    s = s.replace("[ht]", "[!ht]")
    print(s)

gen_tab(spec[3], 3)