captions = [9,9,11,13,17]

for i in range(1,6):
    file_name = 'H14_tree{}.tex'.format(i)
    file1 = open(file_name, 'r')
    s = ''
    for line in file1.readlines():
        if not (line.startswith('%')):
            s += line
    index1 = s.index('\\begin{tikzpicture}') 
    s = s[index1 : ]
    index2 = s.index('\\end{tikzpicture}')+len('\end{tikzpicture}')
    s = s[0 : index2]
    caption = 'Ausgangslage'
    if i != 1: caption = 'Baum nach Löschen der {}.'.format(captions[i-1])
    s = '\\begin{figure}[H] \centering \scalebox{.45}{ ' +s+'}{\caption{'+caption+'}\end{figure}'
    file1.close()
    file1 = open(file_name, 'w+')
    file1.write(s)
    file1.close()