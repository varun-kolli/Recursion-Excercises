# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []



def perm_gen_lex(str_in, smt = "", l = []):
    if smt == "" and len(l) > 0:
        l.clear()
    if str_in == "" and smt == "":
        return l
    if len(str_in) == 0:
        l.append(smt)
    for char in range(len(str_in)):
        passer = smt + str_in[char]
        simp_string = str_in.replace(str_in[char], "")
        perm_gen_lex(simp_string, passer, l)
    return l




