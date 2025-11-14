from unittest.mock import patch


def test_sync_sheets_full_demo_mode(client, monkeypatch):
    # Enable demo mode
    monkeypatch.setenv('DEMO_MODE', 'true')
    monkeypatch.setenv('GOOGLE_SHEET_NAME', 'Test Sheet')

    # Patch methods on the concrete repository to avoid network
    with (
        patch('src.infra.sheets_repo.SheetsRepository.get_config', return_value={'LowStockThreshold': 5}) as _cfg,
        patch('src.infra.sheets_repo.SheetsRepository.update_inventory') as upd,
        patch('src.infra.sheets_repo.SheetsRepository.update_restock_list') as upd_restock
    ):
        resp = client.post('/sync/sheets/full')
        assert resp.status_code == 200
        data = resp.get_json()
        assert data['status'] == 'success'
        assert data['demo_mode'] is True
        assert data['rows_written'] >= 1
        # Ensure inventory and restock writes were invoked
        assert upd.called
        assert upd_restock.called


def test_sync_sheets_full_live_not_implemented(client, monkeypatch):
    monkeypatch.delenv('DEMO_MODE', raising=False)
    resp = client.post('/sync/sheets/full')
    assert resp.status_code == 501
    data = resp.get_json()
    assert data['demo_mode'] is False
