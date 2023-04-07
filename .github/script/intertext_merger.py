import sys
from intertext_files_merger.main import main

if __name__ == "__main__":
    commit_msg= sys.argv[1]
    main(commit_msg)
