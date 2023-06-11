from shinigami import Shinigami

def main():
    """
    Generates a Node 16 Dockefile in the current working directory
    """

    Shinigami(lang_os="node", version="16", build=False, verbose=True, color=True).generate_dockerfile()

main()
