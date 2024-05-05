import requests as r


def kpit():
    x = r.get('https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9171870/')
    print("\nresponse headers: \n\n", x.headers)


if __name__ == "__main__":
    kpit()


