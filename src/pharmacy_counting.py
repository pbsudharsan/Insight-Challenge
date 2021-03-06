import time
import sys
start_time = time.time()
input_fname, output_fname = sys.argv[1:]

# total cost for  drug
drug_cost = dict()

# Keeps track of unique patient names for each drug
pat_names = dict(set())


with open(input_fname, 'r') as inp_f:

    pres = inp_f.readline()
    pres= inp_f.readline()

    while len(pres) > 0:
        
        pres = pres.split(',')

        # Make sure that each row has 5 columns
        if len(pres) != 5:
            print('\033[91mFAIL\033[0m: A row must have 5 columns but found this row')
            print(','.join(pres))
            sys.exit(0)
            
        # PAtient  name
        pat = ' '.join(pres[1:3])

        
        try:
            pat_names[pres[3]].add( pat )
            drug_cost[pres[3]] += float(pres[-1])
        except KeyError:
            pat_names[pres[3]] = { pat }
            drug_cost[pres[3]] = float(pres[-1])

        pres = inp_f.readline()



# Write the output file
with open(output_fname, 'wb') as out_f:
    # Write header 
    out_f.write(b'drug_name,num_prescriber,total_cost\n')

    # Sort by the values of drug_cost and  drug name in case of conflict.
    for drug, value in sorted(drug_cost.items(), key=lambda x: (x[1], x[0]), reverse=True):
        next_line = ','.join([drug, str(len(pat_names[drug])), str(round(drug_cost[drug], 2))])
        next_line += '\n'
        out_f.write(bytes(next_line, 'utf8'))
end_time = time.time()
print('Runtime:',str(end_time - start_time)+'s')

