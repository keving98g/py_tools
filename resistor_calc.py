import math

E12 = [1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
E24 = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

def find_closest(res_list, res):
    index_min = 0
    index_max = len(res_list) + 1
    index = math.floor((index_min + index_max)/2)
    i = 0
    while (index_max - index_min) > 1 and i < 100:
        if res_list[index] == res:
            break
        elif (res_list[index] > res):
            index_max = index
        elif (res_list[index] < res):
            index_min = index
        index = math.floor( (index_min + index_max) / 2)
        i+=1
    if (index < len(res_list)):
        tol1 = abs(res_list[index] / res - 1.0)
        tol2 = abs(res_list[index + 1] / res - 1.0)
        if (tol1 < tol2):
            return index
        else:
            return (index + 1)
    else:
        return index

def calc_res(res_list, rd):
    # r1, r2, r1_idx, rres, rres_tol, best_tol, out_idx, op
    # out_prres, out_vrres
    #i, j
    iteration = 0 #number of iterations

    # compute assuming resistors in series
    # locate nearest approximation with standard resistor values
    r1_idx = find_closest(res_list, rd)
    r1 = res_list[r1_idx]
    #other resistor
    # r2 = Number.POSITIVE_INFINITY
    r2 = 0
    rres = r1
    rres_tol = (rres - rd) / rd # relative tolerance
    best_tol = rres_tol

    out_idx = 0
    out_r1[out_idx] = r1
    out_r2[out_idx] = r2
    out_op[out_idx] = "+"
    out_rres[out_idx] = rres
    out_tol[out_idx++] = rres_tol

    #for (; R[r1_idx] >= rd / 2.0; r1_idx--) {
    for res_index in res_list >= rd / 2.1 : r1_idx--
        iteration++
        r1 = res_list[r1_idx]

        r2d = rd - r1 # this is the value needed
        if (r2d < 0)
            continue # might happen...

        r2_idx = find_closest(res_list, r2d)
        r2 = res_list[r2_idx]  # get the nearest standard value 
        rres = r1 + r2 # compute the resulting composition
        rres_tol = rres / rd - 1.0 # and its tolerance


        if (abs(rres_tol) < abs(best_tol))
            #best_tol = rres_tol
            out_r1[out_idx] = r1
            out_r2[out_idx] = r2
            out_op[out_idx] = "+"
            out_rres[out_idx] = rres
            out_tol[out_idx++] = rres_tol

        rd = 1.0 / rd; # convert to conductance

        # compute assuming resistors in parallel
        r1_idx = find_closet(cond_list, rd);
        # for (; G[r1_idx] >= rd / 2.1; r1_idx--) {
        for res_index in cond_list >= rd / 2.1 : r1_idx--
            iteration++
            r1 = G[r1_idx]

            r2d = rd - r1; # this is the value needed
            if (r2d < 0)
                continue # might happen...

            r2_idx = find_closest(cond_list, r2d)
            r2 = cond_list[r2_idx]  # get the nearest standard value 
            rres = r1 + r2 # compute the resulting composition
            rres_tol = rd / rres - 1.0 # and its tolerance

            if (abs(rres_tol) < abs(best_tol)) {
            # best_tol = rres_tol
            # use values from R array to avoid rounding errors 
            #   which will lead to something like 6800.0000001...
                out_r1[out_idx] = rest_list[n_max - r1_idx] // 1.0 / r1
                out_r2[out_idx] = res_list[n_max - r2_idx] // 1.0 / r2
                out_op[out_idx] = "||"
                out_rres[out_idx] = 1.0 / rres
                out_tol[out_idx++] = rres_tol
        

      # sort the results
      for (i = 1; i < out_idx; i++)
        r1 = out_r1[i]
        r2 = out_r2[i]
        op = out_op[i]
        rres = out_rres[i]
        rres_tol = out_tol[i]
        for (j = i - 1; (j >= 0) && 
             Math.abs(out_tol[j]) > Math.abs(rres_tol); j--) {
          out_r1[j + 1] = out_r1[j]
          out_r2[j + 1] = out_r2[j]
          out_op[j + 1] = out_op[j]
          out_rres[j + 1] = out_rres[j]
          out_tol[j + 1] = out_tol[j]
        }
        out_r1[j + 1] = r1
        out_r2[j + 1] = r2
        out_op[j + 1] = op
        out_rres[j + 1] = rres
        out_tol[j + 1] = rres_tol

        for (r1_idx = 0; r1_idx < out_idx; r1_idx++) {
        out_prres = (Math.round(out_rres[r1_idx] * 1000)) / 1000
        out_vrres = out_prres.toString()
        if(out_vrres.length < 8) out_vrres = out_vrres + "\t"
        document.getElementById('texta').value += 
          out_r1[r1_idx] + "\t" + 
          out_op[r1_idx] + "\t" + 
          out_r2[r1_idx] + "\t=\t" + 
          /* leave three decimal digits maximum */
          out_vrres + "\t(" + 
          (Math.round(out_tol[r1_idx] * 100000)) / 1000 + " %)\n"
      }

print(E12[find_closest(E12, 1.8)])
