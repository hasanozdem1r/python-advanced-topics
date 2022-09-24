import unittest
import web_scraping_demo as wsd


def text_extract_displacement():
    displacement = wsd.extract_displacement("something 70.0 cubic inches")
    assert displacement == 70.0


text_extract_displacement()

# Processing online limits growth
# Processing offline is scalable
