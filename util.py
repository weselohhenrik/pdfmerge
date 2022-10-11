
def check_txt(filename):
    if (filename[-3:] != "txt"):
        return filename + ".txt"
    else:
        return filename


def check_pdf(filename):
    if (filename[-3:] != "pdf"):
        return filename + ".pdf"
    else:
        return filename