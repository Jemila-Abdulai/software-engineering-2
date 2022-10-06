import main

## Tests


def isVerbose_should_return_False_when_called_no_change_command():
    # Arrange
    change_command = None
    results_array = []
    expected_results = [False]

    # Act
    results_array.append(main.isVerbose())

    # Assert
    try:
        assert results_array == expected_results
    except:
        print("isVerbose_should_return_False_when_called_no_change_command")
        print(results_array)
        print(expected_results)
    return


def isVerbose_should_return_true_when_called_with_true_change_command():
    # Arrange
    change_command = True
    results_array = []
    expected_results = [True]

    # Act
    results_array.append(main.isVerbose(change_command))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print("isVerbose_should_return_true_when_called_with_true_change_command")
        print(results_array)
        print(expected_results)
    return


def get_indent_lvl_from_banner_hashes_should_return_correct_lvl_from_good_lines():
    # Arrange
    lines = [
        "# main",
        "## main2",
        "### main3",
        "#### main4",
        "##### main5",
        "###### main6",
    ]
    results_array = []
    expected_results = [1, 2, 3, 4, 5, 6]

    # Act
    for line in lines:
        results_array.append(main.get_indent_lvl_from_banner_hashes(line))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "get_indent_lvl_from_banner_hashes_should_return_correct_lvl_from_good_lines"
        )
        print(results_array)
        print(expected_results)
    return


def get_indent_lvl_from_banner_hashes_should_return_0_when_lines_not_appropriate():
    # Arrange
    lines = ["main", "####### main2", "#main3", "main4### ", "m# 0", 1]
    results_array = []
    expected_results = [0, 0, 0, 0, 0, 0]

    # Act
    for line in lines:
        results_array.append(main.get_indent_lvl_from_banner_hashes(line))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "get_indent_lvl_from_banner_hashes_should_return_0_when_lines_not_appropriate"
        )
        print(results_array)
        print(expected_results)
    return


def create_indent_should_create_correctly_with_valid_input():
    # Arrange
    indent_levels = [1, 2, 3, 4]
    results_array = []
    expected_array = ["  ", "    ", "      ", "        "]

    # Act
    for indent_lvl in indent_levels:
        results_array.append(main.create_indent(indent_lvl))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_indent_should_create_correctly_with_valid_input")
        print(results_array)
        print(expected_array)
    return


def create_indent_should_return_error_string_if_indent_lvl_0():
    # Arrange
    indent_levels = [0]
    results_array = []
    expected_array = [
        "ERROR - THERE WAS AN ERROR WITH THIS LINE'S INDENT LVL, LIKELY NO HASHES IN THE GIVEN LINE OR TOO MANY HASHES (max 4)!"
    ]

    # Act
    for indent_lvl in indent_levels:
        results_array.append(main.create_indent(indent_lvl))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_indent_should_return_error_string_if_indent_lvl_0")
        print(results_array)
        print(expected_array)
    return


def extract_titles_should_create_valid_halves_when_input_good():
    # Arrange
    lines = ["# Main", "## main2", "### MAIN3", "#### maIn4"]
    results_array = []
    expected_array = ["Main", "main2", "MAIN3", "maIn4"]

    # Act
    for line in lines:
        results_array.append(main.extract_titles(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_title_half_should_create_valid_halves_when_input_good")
        print(results_array)
        print(expected_array)
    return


def extract_titles_should_fail_to_create_valid_halves_when_input_bad():
    # Arrange
    lines = ["Main", "main2", "MAIN3", "maIn4"]
    results_array = []
    expected_array = [None, None, None, None]

    # Act
    for line in lines:
        results_array.append(main.extract_titles(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("extract_titles_should_fail_to_create_valid_halves_when_input_bad")
        print(results_array)
        print(expected_array)
    return


def create_full_indent_section_should_create_correctly_with_valid_input():
    # Arrange
    lines = ["# Main", "## main2", "### MAIN3", "#### maIn4"]
    # indent_levels = [1,2,3,4]
    results_array = []
    expected_array = ["  - ", "    - ", "      - ", "        - "]

    # Act
    for line in lines:
        results_array.append(main.create_full_indent_section(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_full_indent_section_should_create_correctly_with_valid_input")
        print(results_array)
        print(expected_array)
    return


def create_full_indent_section_should_return_none_if_not_title_line():
    # Arrange
    lines = ["Main"]
    results_array = []
    expected_array = [None]

    # Act
    for line in lines:
        results_array.append(main.create_full_indent_section(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_full_indent_section_should_return_none_if_not_title_line")
        print(results_array)
        print(expected_array)
    return


def create_title_half_should_create_valid_halves_when_input_good():
    # Arrange
    lines = ["# Main", "## main2", "### MAIN3", "#### maIn4"]
    results_array = []
    expected_array = [
        "  - [Main]",
        "    - [main2]",
        "      - [MAIN3]",
        "        - [maIn4]",
    ]

    # Act
    for line in lines:
        results_array.append(main.create_title_half(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_title_half_should_create_valid_halves_when_input_good")
        print(results_array)
        print(expected_array)
    return


def create_title_half_should_fail_to_create_valid_halves_when_input_bad():
    # Arrange
    lines = ["Main", "main2", "MAIN3", "maIn4"]
    results_array = []
    expected_array = [None, None, None, None]

    # Act
    for line in lines:
        results_array.append(main.create_title_half(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("extract_titles_should_fail_to_create_valid_halves_when_input_bad")
        print(results_array)
        print(expected_array)
    return


def translate_to_lower_should_return_all_lower_case_when_input_good():
    # Arrange
    lines = ["Main", "main2", "MAIN3", "maIn4"]
    results_array = []
    expected_array = ["main", "main2", "main3", "main4"]

    # Act
    for line in lines:
        results_array.append(main.translate_to_lower(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("translate_to_lower_should_return_all_lower_case_when_input_good")
        print(results_array)
        print(expected_array)
    return


def remove_punctuation_should_return_without_any_punctuation_when_punctuation_present():
    # Arrange
    lines = ["!main", "main#2", "ma;n3", ",main4"]
    results_array = []
    expected_array = ["main", "main2", "man3", "main4"]

    # Act
    for line in lines:
        results_array.append(main.remove_punctuation(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print(
            "remove_punctuation_should_return_without_any_punctuation_when_punctuation_present"
        )
        print(results_array)
        print(expected_array)
    return


def remove_punctuation_should_return_same_as_input_when_no_punctuation_present():
    # Arrange
    lines = ["main", "main2", "main3", ",main4"]
    results_array = []
    expected_array = ["main", "main2", "main3", "main4"]

    # Act
    for line in lines:
        results_array.append(main.remove_punctuation(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print(
            "remove_punctuation_should_return_same_as_input_when_no_punctuation_present"
        )
        print(results_array)
        print(expected_array)
    return


def remove_punctuation_should_preserve_solo_dashes_when_present():
    # Arrange
    # lines = ["ma - in", "- main2", "main - 3", "main4 -"]
    lines = ["!ma - in", "- main#2", "ma;n - 3", ",main4 -"]
    results_array = []
    expected_array = ["ma - in", "- main2", "man - 3", "main4 -"]

    # Act
    for line in lines:
        results_array.append(main.remove_punctuation(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print(
            "remove_punctuation_should_return_same_as_input_when_no_punctuation_present"
        )
        print(results_array)
        print(expected_array)
    return


def convert_spaces_to_dashes_should_convert_spaces_to_dashes_when_spaces_present():
    lines = [
        "main title",
        "main2 title",
        "main3ti tile",
        "main4 ti t i l e",
        "m-ain_5 - the reckoning",
        "main 2",
    ]
    results_array = []
    expected_array = [
        "main-title",
        "main2-title",
        "main3ti-tile",
        "main4-ti-t-i-l-e",
        "m-ain_5---the-reckoning",
        "main-2",
    ]

    # Act
    for line in lines:
        results_array.append(main.convert_spaces_to_dashes(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print(
            "convert_spaces_to_dashes_should_convert_spaces_to_dashes_when_spaces_present"
        )
        print(results_array)
        print(expected_array)
    return


def convert_spaces_to_dashes_should_not_convert_anything_to_dashes_when_no_spaces_present():
    lines = ["main-title", "main2title", "main3ti*tile", "main4_ti_t_i_l_e"]
    results_array = []
    expected_array = ["main-title", "main2title", "main3ti*tile", "main4_ti_t_i_l_e"]

    # Act
    for line in lines:
        results_array.append(main.convert_spaces_to_dashes(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print(
            "convert_spaces_to_dashes_should_not_convert_anything_to_dashes_when_no_spaces_present"
        )
        print(results_array)
        print(expected_array)
    return


def construct_link_section_should_return_prefixed_and_suffixed_linker_half():
    lines = ["main-title", "main2title", "main3ti*tile", "main4_ti_t_i_l_e"]
    results_array = []
    expected_array = [
        "(#main-title)",
        "(#main2title)",
        "(#main3ti*tile)",
        "(#main4_ti_t_i_l_e)",
    ]

    # Act
    for line in lines:
        results_array.append(main.construct_link_section(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print(
            "convert_spaces_to_dashes_should_not_convert_anything_to_dashes_when_no_spaces_present"
        )
        print(results_array)
        print(expected_array)
    return


def create_linker_half_should_return_correct_half_when_input_good():
    # Arrange
    lines = ["# Main", "## main 2", "### MAIN3!", "#### maIn4 the prequel"]
    results_array = []
    expected_array = ["(#main)", "(#main-2)", "(#main3)", "(#main4-the-prequel)"]

    # Act
    for line in lines:
        results_array.append(main.create_linker_half(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_linker_half_should_return_correct_half_when_input_good")
        print(results_array)
        print(expected_array)
    return


def create_linker_half_should_return_none_when_input_bad():
    # Arrange
    lines = ["Main", "main2", "MAIN3", "maIn4"]
    results_array = []
    expected_array = [None, None, None, None]

    # Act
    for line in lines:
        results_array.append(main.create_linker_half(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_linker_half_should_return_none_when_input_bad")
        print(results_array)
        print(expected_array)
    return


# create_full_line
def create_full_line_should_create_good_lines_when_input_good():
    # Arrange
    lines = ["# Main", "## main 2", "### MAIN3", "#### maIn4 the prequel"]
    results_array = []
    expected_array = [
        "  - [Main](#main)",
        "    - [main 2](#main-2)",
        "      - [MAIN3](#main3)",
        "        - [maIn4 the prequel](#main4-the-prequel)",
    ]

    # Act
    for line in lines:
        results_array.append(main.create_full_line(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_full_line_should_create_good_lines_when_input_good")
        print(results_array)
        print(expected_array)
    return


# create_TOC
def create_TOC_should_create_good_toc_array_when_input_good():
    # Arrange
    # As we are providing an array, using this framework of everything in a self contained array, we have to ensure that
    # the response is also expected as an array entry too.
    # Therefore, don't miss the [[]] for lines and expected array! We are expecting an array back!
    lines = [
        [
            "# Main",
            "## main 2",
            "this is a dummy line",
            "### MAIN3",
            "this is another dummy line",
            "#### maIn4 the prequel",
        ]
    ]
    results_array = []
    expected_array = [
        [
            "  - [Main](#main)",
            "    - [main 2](#main-2)",
            "      - [MAIN3](#main3)",
            "        - [maIn4 the prequel](#main4-the-prequel)",
        ]
    ]

    # Act
    for line in lines:
        results_array.append(main.create_TOC(line))

    # Assert
    try:
        assert results_array == expected_array
    except:
        print("create_full_line_should_create_good_lines_when_input_good")
        print(results_array)
        print(expected_array)
    return


def create_TOC_when_line_ends_with_a_hash():
    # Arrange
    input_array = [" #"]
    expected_results = [
        []
    ]  # In this case, we actually want nothing returned so we want an empty list to be the output.
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.create_TOC(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print("create_TOC_when_line_ends_with_a_hash")
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


# detect_back_ticks_in_line
def detect_back_ticks_in_line_should_return_true_when_backticks_present():
    # Arrange
    input_array = [
        "`",
        " `",
        "woehfowfewf`dsofosidjf`",
        "`hello`",
        "#`hello`",
        "`#hello`",
        "`1234`",
        "`12`34",
        "13`24",
    ]
    expected_results = [True, True, True, True, True, True, True, True, True]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.detect_back_ticks_in_line(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print("detect_back_ticks_in_line_should_return_true_when_backticks_present")
        print("RESULTS  =>" + results_array)
        print("EXPECTED =>" + expected_results)
    return


def detect_back_ticks_in_line_should_return_false_when_backticks_not_present():
    # Arrange
    input_array = [
        "",
        " ",
        "woehfowfewfdsofosidjf",
        "hello",
        "#hello",
        "#hello",
        "1234",
        "12 34",
        "13 24",
    ]
    expected_results = [False, False, False, False, False, False, False, False, False]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.detect_back_ticks_in_line(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "detect_back_ticks_in_line_should_return_false_when_backticks_not_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


# remove_back_ticked_hashes
def remove_back_ticked_hashes_should_remove_hashes_within_backticks_when_present():
    # Arrange
    input_array = [
        "`#hello`",
        "`#`",
        " `#hello`",
        "something `#hello`",
        "something `# hello`",
        " something `#hello`",
        " #`#hello`",
        " # `# hello`",
    ]
    expected_results = [
        "`hello`",
        "``",
        " `hello`",
        "something `hello`",
        "something ` hello`",
        " something `hello`",
        " #`hello`",
        " # ` hello`",
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.remove_back_ticked_hashes(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "remove_back_ticked_hashes_should_remove_hashes_within_backticks_when_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


def remove_back_ticked_hashes_should_not_touch_line_when_hash_within_backtick_not_present():
    # Arrange
    input_array = [
        "`hello`",
        "``",
        " `hello`",
        "something `hello`",
        "something ` hello`",
        " something `hello`",
        " #`hello`",
        " # ` hello`",
    ]
    expected_results = [
        "`hello`",
        "``",
        " `hello`",
        "something `hello`",
        "something ` hello`",
        " something `hello`",
        " #`hello`",
        " # ` hello`",
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.remove_back_ticked_hashes(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "remove_back_ticked_hashes_should_not_touch_line_when_hash_within_backtick_not_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


# remove_multiline_back_ticked_blocks
def remove_multiline_back_ticked_blocks_should_remove_backticked_blocks_when_backticked_blocks_present():
    # Arrange
    input_array = [
        ["Hello", "```", "This is in backticks", "```"],
        ["```", "This is in backticks too", "```"],
        ["## This is a title", "```", "This is backticked", "```"],
        [
            "" "This one has a blank line at the start",
            "```",
            "As does the back ticks",
            "```",
        ],
        [
            "This has two back ticked lines",
            "```",
            "First one",
            "```",
            "```",
            "Second one",
            "```",
            "And then something after the back tics ",
        ],
    ]
    expected_results = [
        ["Hello"],
        [],
        ["## This is a title"],
        ["" "This one has a blank line at the start"],
        ["This has two back ticked lines", "And then something after the back tics "],
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.remove_multiline_back_ticked_blocks(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "remove_multiline_back_ticked_blocks_should_remove_backticked_blocks_when_backticked_blocks_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


def remove_multiline_back_ticked_blocks_should_not_remove_backticked_blocks_when_backticked_blocks_not_present():
    # Arrange
    input_array = [
        ["Hello"],
        [],
        ["## This is a title"],
        ["" "This one has a blank line at the start"],
        ["This has two back ticked lines", "And then something after the back tics "],
    ]
    expected_results = [
        ["Hello"],
        [],
        ["## This is a title"],
        ["" "This one has a blank line at the start"],
        ["This has two back ticked lines", "And then something after the back tics "],
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.remove_multiline_back_ticked_blocks(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "remove_multiline_back_ticked_blocks_should_not_remove_backticked_blocks_when_backticked_blocks_not_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


# handle_code_segments
def handle_code_segments_should_remove_backtick_hashes_when_backtick_hashes_present():
    # Arrange
    input_array = [
        [
            "`hello`",
            "``",
            " `hello`",
            "something `hello`",
            "something ` hello`",
            " something `hello`",
            " #`hello`",
            " # ` hello`",
        ]
    ]
    expected_results = [
        [
            "`hello`",
            "``",
            " `hello`",
            "something `hello`",
            "something ` hello`",
            " something `hello`",
            " #`hello`",
            " # ` hello`",
        ]
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.handle_code_segments(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "handle_code_segments_should_remove_backtick_hashes_when_backtick_hashes_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


def handle_code_segments_should_remove_backtick_blocks_when_backtick_blocks_present():
    # Arrange
    input_array = [
        ["Hello", "```", "This is in backticks", "```"],
        ["```", "This is in backticks too", "```"],
        ["## This is a title", "```", "This is backticked", "```"],
        [
            "" "This one has a blank line at the start",
            "```",
            "As does the back ticks",
            "```",
        ],
        [
            "This has two back ticked lines",
            "```",
            "First one",
            "```",
            "```",
            "Second one",
            "```",
            "And then something after the back tics ",
        ],
    ]
    expected_results = [
        ["Hello"],
        [],
        ["## This is a title"],
        ["" "This one has a blank line at the start"],
        ["This has two back ticked lines", "And then something after the back tics "],
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.handle_code_segments(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "handle_code_segments_should_remove_backtick_blocks_when_backtick_blocks_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


def handle_code_segments_should_not_remove_hashes_when_backtick_hashes_and_backtick_blocks_not_present():
    # Arrange
    input_array = [
        [
            "hello",
            "",
            " hello",
            "something hello",
            "something  hello",
            " something hello",
            " #hello",
            " #  hello",
        ]
    ]
    expected_results = [
        [
            "hello",
            "",
            " hello",
            "something hello",
            "something  hello",
            " something hello",
            " #hello",
            " #  hello",
        ]
    ]
    results_array = []

    # Act
    for var in input_array:
        results_array.append(main.handle_code_segments(var))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print(
            "handle_code_segments_should_not_remove_hashes_when_backtick_hashes_and_backtick_blocks_not_present"
        )
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


# System test
# create_TOC
def create_TOC_test_text_3_run():
    # Arrange
    text_loc = "C:/Users/SamReece/AppData/Local/Programs/Python/Python37-32/own_work_projects/createMDTOC/test_text_3.txt"
    input_array = main.get_text_lines(text_loc)
    expected_results = [
        [
            "  - [New Cruise](#new-cruise)",
            "    - [Setting up a Cruise server](#setting-up-a-cruise-server)",
            "      - [Set up a Puppet agent](#set-up-a-puppet-agent)",
            "      - [Configure the agent](#configure-the-agent)",
            "      - [Cicspuppet](#cicspuppet)",
            "      - [Cruise repository](#cruise-repository)",
            "      - [Run the following to start the agent](#run-the-following-to-start-the-agent)",
            "    - [Set up Cruise](#set-up-cruise)",
            "      - [Set up the cruise service](#set-up-the-cruise-service)",
            "      - [Set up a cron job to update the indexes](#set-up-a-cron-job-to-update-the-indexes)",
            "    - [Sourcing Code from Github](#sourcing-code-from-github)",
        ]
    ]
    results_array = []

    # Act
    results_array.append(main.create_TOC(input_array))

    # Assert
    try:
        assert results_array == expected_results
    except:
        print("create_TOC_test_text_3_run")
        print("RESULTS  =>", results_array)
        print("EXPECTED =>", expected_results)
    return


## Dummy Version
# Note, this framework is against a monad. If we have a diad/triad, we will want to test each
# argument in isolation to ensure that behaviour is good, so in:
# foo(var1, var2)
# ...we will likely want to test var1 with a good var2, then separately var2 with a good var1.
# This means writing tests ensuring each var works as expected.
def function_name_should_expected_behaviour_when_condition():
    # Arrange
    input_array = []  # Items to input to test functionality
    expected_results = (
        []
    )  # Manually worked out correct results to confirm efficacy against
    results_array = []  # Array that holds what is actually returned by the function

    # Act
    for var in input_array:  # Iterate through the inputs
        # Append the results to the results_array as we go...
        results_array.append(
            main.get_indent_lvl_from_banner_hashes(var)
        )  # ... giving the tested function the item you want.

    # Assert
    # We mix it up a bit with the assert. Rather than wait for the test to throw an AssertionException, we instead let it
    # pass on to the next stage - not for everyone, if you prefer to see the traceback then get rid of the try/except.
    try:
        assert (
            results_array == expected_results
        )  # Confirm that the results match what we want
    except:
        print(
            "function_name_should_expected_behaviour_when_condition"
        )  # Same as the test name so that we can easily see which test failed.
        print(
            "RESULTS  =>", results_array
        )  # Note the => ends at the same point, enabling easy side-by-side comparison of failed results
        print(
            "EXPECTED =>", expected_results
        )  # Note the => ends at the same point, enabling easy side-by-side comparison of failed results
    return


if __name__ == "__main__":
    isVerbose_should_return_False_when_called_no_change_command()
    isVerbose_should_return_true_when_called_with_true_change_command()
    get_indent_lvl_from_banner_hashes_should_return_correct_lvl_from_good_lines()
    get_indent_lvl_from_banner_hashes_should_return_0_when_lines_not_appropriate()
    create_indent_should_create_correctly_with_valid_input()
    create_indent_should_return_error_string_if_indent_lvl_0()
    extract_titles_should_create_valid_halves_when_input_good()
    extract_titles_should_fail_to_create_valid_halves_when_input_bad()
    create_full_indent_section_should_create_correctly_with_valid_input()
    create_full_indent_section_should_return_none_if_not_title_line()
    create_title_half_should_create_valid_halves_when_input_good()
    create_title_half_should_fail_to_create_valid_halves_when_input_bad()
    translate_to_lower_should_return_all_lower_case_when_input_good()
    remove_punctuation_should_return_without_any_punctuation_when_punctuation_present()
    remove_punctuation_should_return_same_as_input_when_no_punctuation_present()
    remove_punctuation_should_preserve_solo_dashes_when_present()
    convert_spaces_to_dashes_should_convert_spaces_to_dashes_when_spaces_present()
    convert_spaces_to_dashes_should_not_convert_anything_to_dashes_when_no_spaces_present()
    construct_link_section_should_return_prefixed_and_suffixed_linker_half()
    create_linker_half_should_return_correct_half_when_input_good()
    create_linker_half_should_return_none_when_input_bad()
    create_full_line_should_create_good_lines_when_input_good()
    create_TOC_should_create_good_toc_array_when_input_good()
    create_TOC_when_line_ends_with_a_hash()

    detect_back_ticks_in_line_should_return_true_when_backticks_present()
    detect_back_ticks_in_line_should_return_false_when_backticks_not_present()

    remove_back_ticked_hashes_should_remove_hashes_within_backticks_when_present()
    remove_back_ticked_hashes_should_not_touch_line_when_hash_within_backtick_not_present()

    remove_multiline_back_ticked_blocks_should_remove_backticked_blocks_when_backticked_blocks_present()
    remove_multiline_back_ticked_blocks_should_not_remove_backticked_blocks_when_backticked_blocks_not_present()

    handle_code_segments_should_remove_backtick_hashes_when_backtick_hashes_present()
    handle_code_segments_should_remove_backtick_blocks_when_backtick_blocks_present()
    handle_code_segments_should_not_remove_hashes_when_backtick_hashes_and_backtick_blocks_not_present()

    create_TOC_test_text_3_run()
    # full_test = True
    # if full_test == True:
    #  main.main()
