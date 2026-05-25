import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app import app

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales Visualiser" in header.text

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    chart = dash_duo.find_element("#sales-chart")
    assert chart is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None