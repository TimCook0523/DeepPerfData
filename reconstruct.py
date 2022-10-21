file = open("Data/Apache_AllNumeric.csv")
out = open("ConvertedData/Apache_SCP.txt", "w")
lines = file.readlines()[1:]
param_matrix = []
param_number = len(lines[0].strip().split(','))-1
set_covers = []
perfs = []
costs = []
for i in range(param_number):
    iline = []
    for j in range(param_number):
        iline.append({})
    param_matrix.append(iline)
cur = 1
print('initializing vars')
for line in lines:
    line_ele = line.strip().split(',')
    params, perf = line_ele[:-1], float(line_ele[-1])
    perfs.append(perf)
    for i in range(len(params)):
        for j in range(i+1, len(params)):
            param_pair = (float(params[i]), float(params[j]))
            if param_pair not in param_matrix[i][j]:
                param_matrix[i][j][param_pair] = []
print('initializing sets')
minPerf = min(perfs)
maxPerf = max(perfs)
print(minPerf, maxPerf)
for k in range(len(lines)):
    line_ele = lines[k].strip().split(',')
    params, perf = line_ele[:-1], float(line_ele[-1])
    # cost = p - (p-1) * 1.0 * (perf - minPerf) / (maxPerf - minPerf)
    # cost = maxPerf + minPerf - perf  # for x264
    # cost = 100 * (maxPerf + minPerf - perf)  # for SQL
    # cost = 100 * (maxPerf + minPerf - perf)  # for sac
    # cost = maxPerf + minPerf - perf  # for LLVM
    # cost = (maxPerf + minPerf - perf)/10  # for javagc
    # cost = maxPerf + minPerf - perf  # for hsmgp
    # cost = (maxPerf + minPerf - perf) * 10  # for hipacc
    # cost = (maxPerf + minPerf - perf) / 10  # for Dune
    # cost = (maxPerf + minPerf - perf) / 10  # for BDBJ
    # cost = 100 * (maxPerf + minPerf - perf)  # for BDBC
    cost = (maxPerf + minPerf - perf) / 10  # for Apache
    costs.append(int(cost))
    set_cover_var = []
    for i in range(len(params)):
        for j in range(i+1, len(params)):
            param_pair = (float(params[i]), float(params[j]))
            param_matrix[i][j][param_pair].append(k+1)
print('counting vars')
c = 0
for i in range(param_number):
    for j in range(i+1, param_number):
        c += len(param_matrix[i][j])
out.write(str(c) + ' ' + str(len(lines)))
out.write('\n')

print(str(c) + ' ' + str(len(lines)))

for cost in costs:
    out.write(str(cost) + ' ')
out.write('\n')

print('printing results')
for i in range(param_number):
    for j in range(i+1, param_number):
        for var, sets in param_matrix[i][j].items():
            out.write(str(len(sets)))
            out.write('\n')
            for s in sets:
                out.write(str(s) + ' ')
            out.write('\n')
file.close()
out.close()
