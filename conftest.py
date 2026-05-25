import chromedriver_autoinstaller

def pytest_configure(config):
    chromedriver_autoinstaller.install()