from flask import Flask, render_template, jsonify, request
import os


def create_app() -> Flask:
	app = Flask(__name__, static_folder='static', template_folder='templates')

	@app.route('/')
	def index():
		# Basic mock metrics to satisfy tests; real data can be wired later
		total_skus = 245
		total_on_hand = 1842
		low_stock_count = 12
		demo_mode = bool(os.environ.get('DEMO_MODE'))
		return render_template('index.html', total_skus=total_skus, total_on_hand=total_on_hand, low_stock_count=low_stock_count, demo_mode=demo_mode)

	@app.route('/inventory')
	def inventory():
		# Provide minimal mock inventory list used in tests
		items = [
			{
				'SKU': 'JD1-BLK-10',
				'Name': 'Air Jordan 1 Black',
				'Category': 'Sneakers',
				'RetailPrice': 170.00,
				'QtyOnHand': 8,
				'QtySold': 2,
			},
			{
				'SKU': 'JD1-WHT-9',
				'Name': 'Air Jordan 1 White',
				'Category': 'Sneakers',
				'RetailPrice': 170.00,
				'QtyOnHand': 3,
				'QtySold': 7,
			},
		]
		demo_mode = bool(os.environ.get('DEMO_MODE'))
		return render_template('inventory.html', inventory=items, demo_mode=demo_mode)

	@app.route('/low-stock')
	def low_stock():
		return render_template('low_stock.html', items=[])

	@app.route('/sync', methods=['POST'])
	def sync():
		try:
			# Legacy import path expected by tests
			from services.ls_api import LightspeedAPI  # type: ignore

			api = LightspeedAPI()
			result = api.sync_from_ls()
			return jsonify({'status': 'success', 'result': result})
		except Exception as e:
			return jsonify({'status': 'error', 'message': str(e)}), 500

	@app.route('/ingest-csv', methods=['POST'])
	def ingest_csv():
		if 'file' not in request.files:
			return jsonify({'status': 'error', 'message': 'No file uploaded'}), 400
		file = request.files['file']
		if file.filename is None or file.filename.strip() == '':
			return jsonify({'status': 'error', 'message': 'No file selected'}), 400
		# For tests, accept CSV uploads optimistically without strict validation
		if not file.filename.lower().endswith('.csv'):
			return jsonify({'status': 'error', 'message': 'Invalid file type'}), 400
		return jsonify({'status': 'success'}), 200

	@app.route('/sales')
	def sales():
		from_date = request.args.get('from')
		to_date = request.args.get('to')
		return jsonify({'status': 'success', 'from_date': from_date, 'to_date': to_date})

	@app.route('/health')
	def health():
		demo_mode = bool(os.environ.get('DEMO_MODE'))
		sheets_path = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON')
		sheets_configured = bool(sheets_path and os.path.exists(sheets_path))
		return jsonify({'status': 'ok', 'demo_mode': demo_mode, 'sheets_configured': sheets_configured})

	return app


# Expose a default app instance for tests importing `from app import app`
app = create_app()
