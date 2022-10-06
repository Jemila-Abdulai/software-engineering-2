"""
What is this for?

This module is to automate the creation of a Markdown TOC.
The aim is to take input from a file that looks like this:
# Main Title 1
words
## Sub Title 1\1
words
words
### SubSub Title 1\1\1
words
words
words
### SubSub Title 1\1\2
words
words
words
## Sub Title 1\2
words
words
words
words
# Main Title 2
words
words

 and give something like this:
 - Main Title 1 (#main-title-1)
   - Sub Title 1\1 (#sub-title-1\1)
     - SubSub Title 1\1\1 (#subsub-title-1\1\1)
     - SubSub Title 1\1\2 (#subsub-title-1\1\2)
   - Sub Title 1\2 (#sub-title-1\2)
 - Main Title 2 (#main-title-2)

in order that this will allow me to more easily write up documentation by 
automating the creation of the TOC. 

In short: it reads the .md file you create and then generates the TOC. 
It will show relative title levels and subtitles with differing indent levels - to 
help show the structure of the document at a glance. 

Side Note - Where there are numerous discrete sections, might look into converting the 
"********" breaks into new TOCs but undecided on this as of yet. 

"""

# title_half = indent + "- " + Title  - DONE, testable and tested
# linker_half = "(#" + Link_title ")"
# TOC_line = title_half + linker_half


# Trusted, used in other modules, no tests.
def get_text_lines(file):
    lines_list = []
    with open(file, "r", encoding="UTF-8") as text:
        data = text.readlines()
    for line in data:
        lines_list.append(line)
    lines_list = remove_newlines(lines_list)
    lines_list = handle_code_segments(lines_list)
    return lines_list


# Trusted, used in other modules, no tests.
def remove_newlines(list):
    for i in range(0, len(list)):
        list[i] = list[i].strip()
    return list


# Code segments include:
# `this`
# and
# ```
# this sort of thing
# ```
def handle_code_segments(line_list):
    # We must remove the multiline blocks first or the indicators of the multiline blocks (the ```s) may be lost
    line_list = remove_multiline_back_ticked_blocks(line_list)
    # now we want to remove the #s that may be lurking within ``s
    for line in line_list:
        if detect_back_ticks_in_line(line):
            remove_back_ticked_hashes(line)
    return line_list


def detect_back_ticks_in_line(line):
    if "`" in line:
        return True
    else:
        return False


# Remove # in `#something` from lines
# Titles may have back ticked items in them legally, but if the # appears within the ``s then we don't want to consider this
def remove_back_ticked_hashes(line):
    within_backticks = False
    wanted_chars = []

    for char in line:
        if char == "`":
            within_backticks = not within_backticks
        if within_backticks:
            if char == "#":
                continue
        wanted_chars.append(char)
    cleaned_line = "".join(char for char in wanted_chars)
    return cleaned_line


# Remove lines between
# ```
# something
# ```
# ... as these often have #'d comments that aren't titles and so want ignoring.
def remove_multiline_back_ticked_blocks(
    line_list,
):  # remove the ```s and the lines between them; we don't want to evaluate comments in code
    # Note, if they have ``` in the line at the end of something, e.g. "foo bar baz ```" then the whole line is lost - potential bug / feature
    within_backticks = False
    wanted_lines = []

    for line in line_list:
        if "```" in line:
            within_backticks = not within_backticks
            continue  # Skip rest of iteration, we don't want to collect any ```s
        if within_backticks:
            continue
        else:
            wanted_lines.append(line)
    return wanted_lines


def isVerbose(change_command=False):
    verbose = False
    if change_command:
        verbose = True
    return verbose


def error_message(
    message_content="",
    message_prefix="ERROR - ",
):
    if isVerbose():
        print(message_prefix + message_content)


def get_indent_lvl_from_banner_hashes(line):
    indent_lvl = 0
    try:
        if isinstance(line, str):
            if "######" == line[:6] and " " == line[6]:
                indent_lvl = 6
            elif "#####" == line[:5] and " " == line[5]:
                indent_lvl = 5
            elif "####" == line[:4] and " " == line[4]:
                indent_lvl = 4
            elif "###" == line[:3] and " " == line[3]:
                indent_lvl = 3
            elif "##" == line[:2] and " " == line[2]:
                indent_lvl = 2
            elif "#" == line[:1] and " " == line[1]:
                indent_lvl = 1
            else:
                indent_lvl = 0
    except:
        indent_lvl = 0
    return indent_lvl


def create_indent(indent_lvl, indent_block="  "):
    if indent_lvl == 0:
        return "ERROR - THERE WAS AN ERROR WITH THIS LINE'S INDENT LVL, LIKELY NO HASHES IN THE GIVEN LINE OR TOO MANY HASHES (max 4)!"
    return indent_block * indent_lvl


def create_full_indent_section(line, list_indicator="- "):
    """
    Will create the full indent, with the "- "
    """
    indent_lvl = get_indent_lvl_from_banner_hashes(line)
    if 7 > indent_lvl > 0:
        indent = create_indent(indent_lvl)
    else:
        error_message("indent_lvl not of correct value, must be in range 1-4")
        return None
    return indent + list_indicator


def extract_titles(line):
    """
    Will extract the title for the title halves.
    Will not include the #s of the line it reads.
    """
    if line[0] == "#":
        line = line.replace("#", "")
        line = line.strip()
    else:
        error_message("Line is not a title line" + line)
        return None
    return line


def create_title_half(line):
    """
    Will create the title half, including the indent and "- " and [ ]s.
    Creates the
    [<title>]
    ... where <title> is essentially the line.
    """
    var1 = create_full_indent_section(line)
    title_sans_hashes = extract_titles(line)
    title_half = ""
    try:
        title_half_interim = "[" + title_sans_hashes + "]"
        title_half = var1 + title_half_interim
    except TypeError:
        error_message("There has been an issue creating the title half")
        title_half = None
    return title_half


def translate_to_lower(line):
    return line.lower()


def remove_punctuation(lower_case_title):
    lower_case_title_no_punctuation = "".join(
        char
        for char in lower_case_title
        if char.isalnum() or char == "-" or char == " "
    )
    return lower_case_title_no_punctuation


def convert_spaces_to_dashes(line):
    char_array = []
    for char in line:
        if char == " ":
            char = "-"
        char_array.append(char)
    dashed_string = "".join(i for i in char_array)
    return dashed_string


def construct_link_section(line):
    return "(#" + line + ")"


def create_linker_half(line):
    linker_half = None
    try:
        title_sans_hashes = extract_titles(line)
        all_lower_title = translate_to_lower(title_sans_hashes)
        lower_title_no_punc = remove_punctuation(all_lower_title)
        linker_no_prefix_or_suffix = convert_spaces_to_dashes(lower_title_no_punc)
        linker_half = construct_link_section(linker_no_prefix_or_suffix)
    except:
        error_message(
            "There appears to have been an error here, likely not a good input like for creating a TOC entry for - skipping"
        )
    return linker_half


def create_full_line(line):
    title_half = create_title_half(line)  # The [] bit
    linker_half = create_linker_half(line)  # The () bit
    # print(title_half)
    # print(linker_half)
    if title_half != None and linker_half != None:
        return title_half + linker_half
    else:
        if title_half == None:
            error_message(
                'The title_half (create_full_line) has a None value, this is generated in a line that ends with "#" but doesn\'t have anything after that'
            )
        elif linker_half == None:
            error_message("The linker_half (create_full_line) has a None value")
        else:
            error_message("Weird Error in create_full_line - investigate")
    return


def create_TOC(lines):
    TOC_lines = []
    for line in lines:
        if len(line) > 0 and line[0] == "#":
            TOC_line = create_full_line(line)
            if TOC_line == None:
                pass
            else:
                TOC_lines.append(create_full_line(line))
    return TOC_lines


def main(text_loc):
    lines = get_text_lines(text_loc)
    TOC_lines = create_TOC(lines)
    for i in TOC_lines:
        print(i)
    return


if __name__ == "__main__":
    verbose = False
    text_loc = "C:/Users/SamReece/AppData/Local/Programs/Python/Python37-32/own_work_projects/createMDTOC/text.txt"
    # text_loc = 'C:\Users\SamReece\Documents\GitHub\Knowledge\groot-squad-bible\Developer-Edition.md'
    main(text_loc)

    # lines = get_text_lines(text_loc)
