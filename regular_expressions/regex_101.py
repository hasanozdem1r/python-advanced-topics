import re

text: str = "Python is a powerful programming language"

mka_quote = (
    "Heroes who shed their blood and lost their lives! You are now lying in the soil of a friendly country. Therefore rest in peace. "
    "There is no difference between the Johnnies and Mehmets to us where they lie side by side here in this country of ours. "
    "You, the mothers, who sent their sons from far away countries wipe away your tears; your sons are now lying in our bosom and are in peace. "
    "After having lost their lives on this land they have become our sons as well."
)


def check_start(pattern: str, source: str):
    # match() Determine if the RE matches at the beginning of the string.
    # if there is match return format  -> <re.Match object; span=(0, 6), match='Python'>
    # if there is no match return format -> None
    match_result = re.match(pattern, source)
    startswith_result = source.startswith(pattern)
    print(match_result, match_result.span(), match_result.group())
    print(startswith_result)
    print("-----------------------")


def search_all(pattern: str, source: str):
    # search() Scan through a string, looking for any location where this RE matches.
    search_res = re.search(pattern, source)
    print(search_res, search_res.span(), search_res.group())
    print("-----------------------")


def find_all_substrings(pattern: str, source: str):
    # Find all substrings where the RE matches, and returns them as a list.
    find_result = re.findall(pattern, source)
    print(find_result)
    print("-----------------------")


check_start("Python", text)
# check_start('who',mka_quote)

search_all("who shed their blood", mka_quote)

find_all_substrings("in", mka_quote)
