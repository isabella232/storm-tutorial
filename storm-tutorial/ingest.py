import os
import sys

import synapse.lib.output as s_output
import synapse.tools.ingest as s_ingest


def main(argv, outp=None):

    if outp is None:  # pragma: no cover
        outp = s_output.OutPut()

    if len(argv) != 2:
        outp.printf('usage: python ingest.py core.db path_to_ingests/')
        return 1

    core_path = argv[0]
    ingest_dir_path = argv[1]

    for fname in sorted(os.listdir(ingest_dir_path)):
        fpath = os.path.join(ingest_dir_path, fname)
        s_ingest.main(['--core', core_path, '--progress', fpath])

if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
