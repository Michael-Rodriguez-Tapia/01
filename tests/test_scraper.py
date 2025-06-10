import pathlib
import sys

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from scraper import scrape_data_directly, extract_data_from_soup

FIXTURE_DIR = pathlib.Path(__file__).parent / "fixtures"


def load_sample_html():
    return (FIXTURE_DIR / "sample.html").read_text()


def test_scrape_data_directly_non_empty():
    html = load_sample_html()
    data = scrape_data_directly(html)
    assert data, "scrape_data_directly should return non-empty result"


def test_extract_data_from_soup_non_empty():
    html = load_sample_html()
    data = extract_data_from_soup(html)
    assert data, "extract_data_from_soup should return non-empty result"
