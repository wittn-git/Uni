for i in range(0, 4):
    file1 = open('d{}.dot.tex'.format(i), 'r')
    s = ''
    for line in file1.readlines():
        if not (line.startswith('%')):
            s += line
    index1 = s.index('\\begin{tikzpicture}') 
    s = s[index1 : ]
    index2 = s.index('\\end{tikzpicture}')+len('\end{tikzpicture}')
    s = s[0 : index2]

    file1.close()
    file1 = open('d{}.dot.tex'.format(i), 'w+')
    file1.write(s)
    file1.close()