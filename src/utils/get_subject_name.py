import re


def get_subject_name(file_name: str):

    # Original file name:              sXXX_[type_...]_BL.txt
    #                                  -?     ?..-2    -1
    # Submitted transcripts: annotator_sXXX_[type_...]_BL.txt
    #                                  -?     ?..-2    -1
    # Submitted reviews:  A1_review_A2_sXXX_[type_...]_BL.txt
    #                                  -?     ?..-2    -1
    # --> use regex to extract sXXX
    pattern1 = "^s[0-9]+_"  # Look for sXXX_ at start of string.
    pattern2 = "_s[0-9]+_"  # look for _sXXX_ anywhere in string.
    pattern = "(%s|%s)" % (pattern1, pattern2)
    regex = re.compile(pattern)
    result = regex.search(file_name)
    if result is None:
        raise Exception("Could not parse subject name from '%s'." % file_name)
    if len(result.groups()) > 1:
        msg = "Found multiple subject names in '%s'." % file_name
        msg += " Names: %s." % ", ".join(result.groups())
        raise Exception(msg)
    match = result.group(0)
    return match.replace("_", "")
