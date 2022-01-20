from postmanrenderer.main import Url


def test_url_class_wo_protocol():
    url = Url("www.google.com")
    assert url.host == ["www", "google", "com"]
    assert url.raw == "www.google.com"
    assert url.protocol == None


def test_url_class_w_protocol():
    url = Url("https://www.google.com")
    assert url.host == ["www", "google", "com"]
    assert url.raw == "www.google.com"
    assert url.protocol == "https"
