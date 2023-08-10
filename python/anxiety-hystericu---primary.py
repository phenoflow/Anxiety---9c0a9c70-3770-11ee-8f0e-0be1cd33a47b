# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"E201.00","system":"readv2"},{"code":"E201100","system":"readv2"},{"code":"E201300","system":"readv2"},{"code":"E201500","system":"readv2"},{"code":"E201511","system":"readv2"},{"code":"E201611","system":"readv2"},{"code":"E201612","system":"readv2"},{"code":"E201z00","system":"readv2"},{"code":"E201z12","system":"readv2"},{"code":"Eu41y11","system":"readv2"},{"code":"Eu44.11","system":"readv2"},{"code":"Eu44.13","system":"readv2"},{"code":"Eu45511","system":"readv2"},{"code":"Eu45y12","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-hystericu---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-hystericu---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-hystericu---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
