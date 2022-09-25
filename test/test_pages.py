import pytest
from app import create_app

def success_response(client, path):
    rr = client.get(path)
    assert rr.status_code == 200


# def test_login_page():
#     flask_app = create_app()
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/login')
#         print(response)
#         assert response.status_code == 200
@pytest.fixture
def app():
    """An application for the tests."""
    _app = create_app()
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture
def client(app):
    return app.test_client()       

class TestBasicPageCanView:
    def test_404(self, client):
        rv = client.get("/404notfound")
        assert rv.status_code == 404

    def test_login(self, client):
        success_response(client, "/login")
        
    def test_login_post(self, client):
        rv = client.post("/login",data={'email':'demo@financialhouse.io','password':'cjaiU8CV'},follow_redirects=True)
        print("rvPrint",rv)
        assert rv.status_code == 200
                

        def test_dashboard(self, client):
            success_response(client, "/")