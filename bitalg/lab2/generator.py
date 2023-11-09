# ! = \{    @ =\} 
spec = [[[100, 1000, 10000, 100000, 1000000], [100, 1000, 10000, 100000, 1000000]],
 [[100, 1000, 10000], [100, 1000, 10000]],
 [[100, 1000, 10000, 100000, 1000000], [100, 1000, 10000, 100000, 1000000]],
 [[100, 1000, 10000, 100000, 1000000], [100, 1000, 10000, 100000, 1000000]]]
times = [[0.001558542251586914,
  0.0015578269958496094,
  0.0184018611907959,
  0.013007164001464844,
  0.06888508796691895,
  0.09339404106140137,
  0.8698828220367432,
  1.1809422969818115,
  11.753052711486816,
  15.655795097351074],
 [0.0006287097930908203,
  0.006094455718994141,
  0.007782697677612305,
  0.6571652889251709,
  0.0970926284790039,
  71.20626544952393],
 [0.00296783447265625,
  0.0011258125305175781,
  0.04553675651550293,
  0.00944066047668457,
  0.5676238536834717,
  0.10296130180358887,
  7.713114261627197,
  1.0305302143096924,
  93.6686463356018,
  9.840947151184082],
 [0.002003908157348633,
  0.0018165111541748047,
  0.025503873825073242,
  0.013608932495117188,
  0.2722208499908447,
  0.16427183151245117,
  3.9748377799987793,
  2.000063180923462,
  47.53985142707825,
  21.827919483184814]]
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