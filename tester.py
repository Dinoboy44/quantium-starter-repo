from app import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header")

def test_graph(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#filteredfig")

def test_regionpick(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-filter")
