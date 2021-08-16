for i in range(1, 2):
    file_name = 'H13_tree{}.tex'.format(i)
    file1 = open(file_name, 'r')
    s = ''
    for line in file1.readlines():
        if not (line.startswith('%')):
            s += line
    index1 = s.index('\\begin{tikzpicture}') 
    s = s[index1 : ]
    index2 = s.index('\\end{tikzpicture}')+len('\end{tikzpicture}')
    s = s[0 : index2]
    s = '\\begin{figure}[H] \centering \scalebox{.6}{ ' +s+'}\end{figure}'
    file1.close()
    file1 = open(file_name, 'w+')
    file1.write(s)
    file1.close()