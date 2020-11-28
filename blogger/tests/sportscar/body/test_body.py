from pytest import mark

@mark.body
def test_body_functions_as_expected():
    assert True

@mark.smoke
@mark.body
class BodyTests():

    def test_windshield(self):
        assert True

    def test_wippers(self):
        assert True

    @mark.smoke
    def test_steering(self):
        assert True

@mark.ui
def test_can_navigate_to_youtube_page(chrome_browser):
    chrome_browser.get("https://www.youtube.com")
    assert True
