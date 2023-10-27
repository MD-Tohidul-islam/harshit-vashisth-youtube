with open('index.html','r') as webpage:
    with open('output.txt','a') as wf:
        for line in webpage.readlines():
            if '<a href=' in line:
                pos = line.find('<a href=')
                first_quete = line.find('\"',pos)
                second_quote = line.find('\"',first_quete)
                url = line[first_quete+1:second_quote]
                wf.write(url +'\n')
