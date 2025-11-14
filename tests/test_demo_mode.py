from unittest.mock import patch


def test_demo_mode_disables_http_calls(monkeypatch):
    # Ensure DEMO_MODE is on
    monkeypatch.setenv("DEMO_MODE", "true")
    from src.infra.lightspeed_client import LightspeedGateway

    # Mock requests.Session.get to verify it's never called
    with patch("src.infra.lightspeed_client.requests.Session.get") as mock_get:
        gw = LightspeedGateway(api_token="x", account_domain="demo")
        # Exercise multiple calls; these should read fixtures
        products = gw.get_products()
        inventory = gw.get_inventory()
        sales = gw.get_sales()

        assert isinstance(products, list)
        assert isinstance(inventory, list)
        assert isinstance(sales, list)
        mock_get.assert_not_called()


def test_demo_mode_banner_renders(client, monkeypatch):
    monkeypatch.setenv("DEMO_MODE", "true")
    # Dashboard
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Demo Mode Active" in resp.data
    # Inventory page
    resp2 = client.get("/inventory")
    assert resp2.status_code == 200
    assert b"Demo Mode Active" in resp2.data
