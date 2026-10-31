"""Exercise the distributed public source, without API credentials or private data."""
import importlib
import zipfile
from pathlib import Path


def test_archived_demo_approval_and_exports(tmp_path, monkeypatch):
    source = tmp_path / 'source'
    with zipfile.ZipFile(Path(__file__).resolve().parents[1] / 'ProductSense-reviewed-app-source.zip') as archive:
        archive.extractall(source)
    monkeypatch.syspath_prepend(str(source))
    monkeypatch.setenv('PRODUCTSENSE_DATA_DIR', str(tmp_path / 'runtime'))
    from fastapi.testclient import TestClient
    module = importlib.import_module('app.main')
    with TestClient(module.app) as client:
        assert client.get('/api/health').json() == {'status': 'ok'}
        response = client.post('/api/sessions/demo', json={'mode': 'demo'})
        assert response.status_code == 201
        sid = response.json()['id']
        assert client.post(f'/api/sessions/{sid}/approve', json={'opportunity_id': 'missing'}).status_code == 409
        assert client.post(f'/api/sessions/{sid}/analyze').status_code == 202
        state = client.get(f'/api/sessions/{sid}').json()
        assert state['opportunities'], state
        evidence = [rid for group in state['groups'] for rid in group['evidence_ids']]
        assert sorted(evidence) == sorted(row['id'] for row in state['feedback'])
        response = client.post(f'/api/sessions/{sid}/approve', json={'opportunity_id': state['opportunities'][0]['id']})
        assert response.status_code == 202
        state = client.get(f'/api/sessions/{sid}').json()
        assert state['prd_markdown'], state
        assert state['calls_used'] == 0
        assert client.get(f'/api/sessions/{sid}/history').status_code == 200
        markdown = client.get(f'/api/sessions/{sid}/export?format=md')
        word = client.get(f'/api/sessions/{sid}/export?format=docx')
        assert markdown.status_code == word.status_code == 200
        assert word.content.startswith(b'PK')
        assert client.get('/api/sessions/nonexistent').status_code == 404
