num_list = [i for i in range(1,10)]

poss_sol_list = []

for i in num_list:
	for j in num_list:
		for k in num_list:
			if (i != j != k) and (i+j+k==15):
				poss_sol = (i,j,k)
				poss_sol_list.append(poss_sol)



for i in poss_sol_list:
	for j in poss_sol_list:
		for k in poss_sol_list:			
			if (i[0] not in j) and (i[0] not in k) and (i[1] not in j) and (i[1] not in k) and (i[2] not in j) and (i[2] not in k) and (i[0]+j[0]+k[0]==15) and (i[0]+j[1]+k[2]==15) and (i[1]+j[1]+k[1]==15) and (i[2]+j[2]+k[2]==15) and (i[2]+j[1]+k[0]==15):
				print(i,j,k)
					
				#if (i[0]!=j[0]!=j[1]!=j[2]!=k[0]!=k[1]!=k[2]) and (i[0]+j[0]+k[0]==15) and (i[0]+j[1]+k[2]==15) and (i[1]+j[1]+k[1]==15) and (i[2]+j[2]+k[2]==15):
				#if (i[l]!=j[l]!=k[l]) and (i[0]+j[0]+k[0]==15) and (i[0]+j[1]+k[2]==15) and (i[1]+j[1]+k[1]==15) and (i[2]+j[2]+k[2]==15):
					#print(i,j,k)
