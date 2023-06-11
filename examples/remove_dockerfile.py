from shinigami import Shinigami

def main():
    """
    Deletes the Dockerfile in the current working directory
    """

    Shinigami(verbose=True, color=True).remove_dockerfile()

main()
