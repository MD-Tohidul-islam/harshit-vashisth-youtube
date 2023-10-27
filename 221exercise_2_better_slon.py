with open('index.html','r') as webpage:
    with open('output2.txt','a') as wf:
        pasge = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quete = page.find('\"', pos)
                second_quote = page.find('\"', first_quete)
                url = page[first_quete + 1:second_quote]
                wf.write(url + '\n')
                pasge = pasge[second_quote:]