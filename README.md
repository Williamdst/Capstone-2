The algorithm ignores distances and focuses on double backs; which
is what the algorithm is trying to minimize. Additionally, it is
coming up with a circuit and not a path. 


I HAVE A PROBLEM WITH THE matched_pairs_w_dupes. The old networkx function
max.weight_matching must have returned a dictionary but the new networkx is 
returning a set. 

