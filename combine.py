import pandas as pd
import sys
import getopt


def main():
    scores_fn = "eduflow_scores.csv"
    names_fn = "list_of_students.csv"
    output = "out.csv"

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "l:s:o:")

        for o, a in opts:
            if o in "-l":
                names_fn = a
            elif o in "-s":
                scores_fn = a
            elif o in "-o":
                output = a
    except getopt.error as err:
        print(str(err))

    try:
        scores = pd.read_csv(scores_fn, sep=";")
    except FileNotFoundError:
        print(
            f"Could not find the file '{scores_fn}'.\n"
            f"You can input a different filename for scores with -s filename.csv "
        )
        return

    try:
        names = pd.read_csv(names_fn, sep=";")
    except FileNotFoundError:
        print(
            f"Could not find the file '{names_fn}'.\n"
            f"You can input a different filename for the list of students with -l filename.csv "
        )
        return

    # scores['Brukernavn'] = scores['Email'].apply(lambda x: x.split('@')[0])
    print(f"Merging {names_fn} with {scores_fn}")
    names["Fullnavn"] = names[["Fornavn", "Etternavn"]].apply(
        lambda x: " ".join(x), axis=1
    )

    df = names.merge(scores, left_on="Fullnavn", right_on="Name", how="outer")
    df.drop(["Fullnavn"], axis=1, inplace=True)
    df.sort_values(by=["Etternavn", "Fornavn"], inplace=True)

    print(f"Writing the output to {output}")
    df.to_csv(output, index=False, float_format="%.0f", sep=";", encoding="utf-8-sig")


if __name__ == "__main__":
    main()
