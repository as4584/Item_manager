# Lightspeed Retail (X-Series) API Overview

**Purpose:** Demonstrate how organizational, master, and transactional data from a real-world retail POS (DonxEra’s Lightspeed X-Series system) integrate into an IS344-style ERP framework.

| Data Type | Example Entity | Lightspeed Endpoint | App Module |
|------------|----------------|--------------------|-------------|
| Organizational | Store, Outlet, Register, User | `/outlets`, `/registers`, `/users` | `.env` + Scheduler Config |
| Master | Products, Brands, Categories, Variants | `/products`, `/categories`, `/brands` | Sheets “Inventory” Tab |
| Transactional | Sales, Returns, Stock Adjustments | `/sales`, `/inventory_movements` | `SalesLog` Tab, `InventoryService.reconcile_sales()` |

**Data Flow Diagram**



Lightspeed (API)
↓
LightspeedClient (Gateway/Adapter)
↓
SyncService (Application Logic)
↓
Google Sheets (Master + Transactional)
↓
Flask Dashboard (Presentation)


**Demo Mode**

If `DEMO_MODE=true`, the system loads mock JSON fixtures from `/sample_data/lightspeed/` to simulate live API responses for academic demonstration.


That one page + your .env is enough to make your professor go, “Wow, this student understands enterprise data integration.”

🤖 Copilot Prompt — “Refine Project for Academic Demo & ERP Data Mapping”

Prompt:
Refine the Inventory Manager for an IS344/IS218 academic showcase.

Goals:
1️⃣ Update .env.example to separate variables by Organizational, Master, and Transactional Data sections, as in the ERP model.
2️⃣ Add support for DEMO_MODE=true so that the Lightspeed client reads local fixtures from sample_data/lightspeed/*.json instead of calling the API.
3️⃣ Create docs/lightspeed_api_overview.md summarizing endpoint-to-data-type mapping, data flow, and demo mode behavior.
4️⃣ Display a “Demo Mode Active” banner on the Flask dashboard.
5️⃣ Ensure all tests still pass in demo mode; add a test that asserts no network call occurs when DEMO_MODE=true.

Acceptance:

.env.example organized and documented by ERP data type.

docs/lightspeed_api_overview.md present and formatted.

Demo mode fully functional; no HTTP requests made.

Tests green and CI clean.
