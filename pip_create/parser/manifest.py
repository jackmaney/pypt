from distutils.text_file import TextFile
from distutils.filelist import FileList


def get_manifested_files(manifest_file="MANIFEST.in"):
    """
    Uses distutils to parse MANIFEST.in (or a file using the same rules
    as MANIFEST.in) to get a list of files specifically included by the
    manifest in the distribution.
    """

    # Inspired by:
    # https://github.com/python/cpython/blob/2.7/Lib/distutils/command/sdist.py#L386

    template = TextFile(manifest_file,
                        strip_comments=1,
                        skip_blanks=1,
                        join_lines=1,
                        lstrip_ws=1,
                        rstrip_ws=1,
                        collapse_join=1)

    filelist = FileList()

    while True:
        line = template.readline()

        if line is None:
            break

        filelist.process_template_line(line)

    template.close()

    return [x for x in filelist.files]
