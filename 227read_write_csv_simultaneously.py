from csv import DictReader,DictWriter
with open('file4.csv','r') as rf:
    with open('file2.csv','w') as wf:
        csv_reader = DictReader(rf)
        csv_writer  = DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age = row['first name'],row['last name'],row['age']
            csv_writer.writerow({
                'first_name':fname,
                'last_name':lname,
                'age':age
            })