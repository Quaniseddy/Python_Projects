# Written by Quan Zhang for COMP9021
import itertools


# define a Sentence Class which have two components: sirs & statement (by this sirs)
class Sentence:
    def __init__(self, sirs=None, statement=None):
        self.sirs = sirs
        self.statement = statement


# break down the paragraph into list of sentences
def parse_sentence(content):
    quote_marker = False
    accumulator = ""
    mix = []
    for c in content:
        if (c == "!" or c == "." or c == "?") and (quote_marker == False):
            accumulator = accumulator + c
            mix.append(accumulator)
            accumulator = ""
        elif c == '"':
            quote_marker = not quote_marker
            accumulator = accumulator + c
            if (quote_marker == False) and (
                accumulator[-2] == "!"
                or accumulator[-2] == "."
                or accumulator[-2] == "?"
            ):
                mix.append(accumulator)
                accumulator = ""
        else:
            accumulator = accumulator + c
    return mix


# break down sentences into information and disgard none-infomative sentences
def parse_info(sentence):
    sentence = sentence.split()
    sirs_flag = sir_flag = quote_flag = False
    sirs = []
    statement = []
    for word in sentence:
        # conditions to store info
        if (sirs_flag == True) and (word != "and"):
            sirs.append("".join(x for x in word if x.isalpha()))
        if (sir_flag == True) and (quote_flag == False):
            sirs.append("".join(x for x in word if x.isalpha()))
            sir_flag = False
        if quote_flag == True:
            statement.append("".join(x for x in word if x.isalpha()))

        # conditions to set the flag of storing info
        if '"' in word:
            quote_flag = not quote_flag
            if word[0] == '"':
                statement.append("".join(x for x in word if x.isalpha()))
        if word == "Sirs":
            sirs_flag = True
        if word == "Sir":
            sir_flag = True

    return Sentence(sirs, statement)


# break down the statement said by sirs and conclude all sirs involved in the paragraph
def parse_statement(statement, all_sirs):
    additional = []
    if statement != []:
        index = 0
        for word in statement:
            if word == "Sir":
                additional.append(statement[index + 1])
            index += 1

    if additional != []:
        for i in additional:
            if i not in all_sirs:
                all_sirs.append(i)

    return all_sirs


# break down the logic behind statement by identifying key logic word
# eliminate the impossiblity from the default combo(mapping)
def parse_logic(mapping, all_sirs, v):
    state = v.statement
    if ("least" in state) or ("or" in state):
        if "least" in state:
            s = [
                c
                for c in state[state.index("of") + 1 : state.index("is")]
                if (c != "Sir") and (c != "and")
            ]
            if s == "us" or s == ["us"]:
                s = all_sirs
        if "or" in state:
            s = [c for c in state[: state.index("is")] if (c != "Sir") and (c != "or")]

        k = state[state.index("a") + 1 :]
        if k == ["Knave"]:
            k = 0
        else:
            k = 1

        tmp = []

        if "I" in s:
            s[s.index("I")] = v.sirs[0]

        for posi in mapping:
            flag = True
            count = 0
            for x in s:
                if posi[all_sirs.index(x)] == k:
                    count += 1
            if posi[all_sirs.index(v.sirs[0])] == 0:
                if count >= 1:
                    flag = False
            if posi[all_sirs.index(v.sirs[0])] == 1:
                if count < 1:
                    flag = False
            if flag == True:
                tmp.append(posi)

        mapping = tmp

    elif "most" in state:
        s = [
            c
            for c in state[state.index("of") + 1 : state.index("is")]
            if (c != "Sir") and (c != "and")
        ]
        if s == "us" or s == ["us"]:
            s = all_sirs
        k = state[state.index("a") + 1 :]
        if k == ["Knave"]:
            k = 0
        else:
            k = 1

        tmp = []

        if "I" in s:
            s[s.index("I")] = v.sirs[0]

        for posi in mapping:
            flag = True
            count = 0
            for x in s:
                if posi[all_sirs.index(x)] == k:
                    count += 1

            if posi[all_sirs.index(v.sirs[0])] == 0:
                if count <= 1:
                    flag = False
            else:
                if count > 1:
                    flag = False

            if flag == True:
                tmp.append(posi)

            mapping = tmp

    elif ("exactly" in state) or ("Exactly" in state):
        s = [
            c
            for c in state[state.index("of") + 1 : state.index("is")]
            if (c != "Sir") and (c != "and")
        ]
        if s == "us" or s == ["us"]:
            s = all_sirs
        k = state[state.index("a") + 1 :]
        if k == ["Knave"]:
            k = 0
        else:
            k = 1

        tmp = []

        if "I" in s:
            s[s.index("I")] = v.sirs[0]

        for posi in mapping:
            flag = True
            count = 0
            for x in s:
                if posi[all_sirs.index(x)] == k:
                    count += 1

            if posi[all_sirs.index(v.sirs[0])] == 0:
                if count == 1:
                    flag = False
            else:
                if count != 1:
                    flag = False

            if flag == True:
                tmp.append(posi)

            mapping = tmp

    elif ("all" in state) or ("All" in state):
        s = all_sirs
        k = state[state.index("are") + 1 :]
        if k == ["Knaves"]:
            k = 0
        else:
            k = 1

        tmp = []

        for posi in mapping:
            flag = True
            count = 0
            for x in s:
                if posi[all_sirs.index(x)] == k:
                    count += 1

            if posi[all_sirs.index(v.sirs[0])] == 0:
                if count == len(all_sirs):
                    flag = False
            else:
                if count != len(all_sirs):
                    flag = False

            if flag == True:
                tmp.append(posi)

            mapping = tmp

    elif "am" in state:
        s = v.sirs[0]
        k = state[state.index("a") + 1 :]
        if k == ["Knave"]:
            k = 0
        else:
            k = 1

        tmp = []

        for posi in mapping:
            flag = True
            if posi[all_sirs.index(s)] == 0:
                if k == 0:
                    flag = False
            else:
                if k == 0:
                    flag = False
            if flag == True:
                tmp.append(posi)

        mapping = tmp

    else:
        if "is" in state:
            s = state[state.index("Sir") + 1 : state.index("is")]
            k = state[state.index("a") + 1 :]
            if k == ["Knave"]:
                k = 0
            else:
                k = 1

            tmp = []

            for posi in mapping:
                flag = True
                if posi[all_sirs.index(v.sirs[0])] == 0:
                    if posi[all_sirs.index(s[0])] == k:
                        flag = False
                else:
                    if posi[all_sirs.index(s[0])] != k:
                        flag = False

                if flag == True:
                    tmp.append(posi)

            mapping = tmp

        if "are" in state:
            s = [
                c for c in state[: state.index("are")] if (c != "Sir") and (c != "and")
            ]
            k = state[state.index("are") + 1 :]
            if k == ["Knaves"]:
                k = 0
            else:
                k = 1

            if "I" in s:
                s[s.index("I")] = v.sirs[0]

            tmp = []

            for posi in mapping:
                flag = True
                count = 0
                for x in s:
                    if posi[all_sirs.index(x)] == k:
                        count += 1

                if posi[all_sirs.index(v.sirs[0])] == 0:
                    if count == len(s):
                        flag = False
                else:
                    if count != len(s):
                        flag = False

                if flag == True:
                    tmp.append(posi)

            mapping = tmp

    return mapping


# the whole parsing process involving all the above steps
def parser(content):
    mix = parse_sentence(content)
    info = []
    for sentence in mix:
        sent = parse_info(sentence)
        if sent.sirs != []:
            info.append(sent)

    all_sirs = []
    for i in info:
        [all_sirs.append(j) for j in i.sirs if j not in all_sirs]
        all_sirs = parse_statement(i.statement, all_sirs)

    all_sirs = sorted(all_sirs)
    prt = "The Sirs are: " + " ".join(x for x in all_sirs)
    print(prt)

    # default mapping of all possible scenario with 1s and 0s represent knights and knaves
    mapping = []
    for numbers in itertools.product([0, 1], repeat=len(all_sirs)):
        mapping.append(numbers)

    for v in info:
        if v.statement != []:
            mapping = parse_logic(mapping, all_sirs, v)

    if len(mapping) == 0:
        print("There is no solution.")
    elif len(mapping) == 1:
        print("There is a unique solution:")
        for n in range(len(mapping[0])):
            if mapping[0][n] == 1:
                id = "Knight"
            else:
                id = "Knave"
            print("Sir " + all_sirs[n] + " is a " + id)
    else:
        print("There are " + str(len(mapping)) + " solutions.")


def main():
    print("Which text file do you want to use for the puzzle?", end="")
    txt_file_name = input()
    txt_file = open(txt_file_name)
    content = txt_file.read()
    txt_file.close()
    parser(content)


if __name__ == "__main__":
    main()
