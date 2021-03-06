"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/pyflask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cid">Continuous Integration and Deployment</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/pyflask")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/cid")
    assert response.status_code == 200
    assert b"Continuous Integration and Deployment" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"Object Oriented Programming Concepts" in response.data

def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"What is AAA Testing?" in response.data

def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/pylin")
    assert response.status_code == 200
    assert b"Object Oriented Concepts in the calculator app" in response.data

def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404