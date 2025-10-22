.PHONY: install fmt lint test run clean help

# Default target
.DEFAULT_GOAL := help

# Python and Poetry executables
PYTHON := python3.11
POETRY := poetry
POETRY_RUN := $(POETRY) run

# Source directories
SRC_DIR := src
TEST_DIR := tests

# Help target
help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies using Poetry
	@echo "Installing dependencies..."
	$(POETRY) install --no-interaction --no-ansi
	@echo "✓ Dependencies installed"

install-dev: ## Install all dependencies including dev
	@echo "Installing all dependencies..."
	$(POETRY) install --with dev --no-interaction --no-ansi
	@echo "✓ All dependencies installed"

fmt: ## Format code with black and isort
	@echo "Formatting code with black..."
	$(POETRY_RUN) black $(SRC_DIR) $(TEST_DIR)
	@echo "Sorting imports with isort..."
	$(POETRY_RUN) isort $(SRC_DIR) $(TEST_DIR)
	@echo "✓ Code formatted"

fmt-check: ## Check code formatting without making changes
	@echo "Checking code format..."
	$(POETRY_RUN) black --check $(SRC_DIR) $(TEST_DIR)
	$(POETRY_RUN) isort --check-only $(SRC_DIR) $(TEST_DIR)

lint: ## Run all linters (ruff, mypy)
	@echo "Running ruff..."
	$(POETRY_RUN) ruff check $(SRC_DIR) $(TEST_DIR)
	@echo "Running mypy..."
	$(POETRY_RUN) mypy $(SRC_DIR)
	@echo "✓ Linting complete"

lint-fix: ## Run ruff with auto-fix
	@echo "Running ruff with auto-fix..."
	$(POETRY_RUN) ruff check --fix $(SRC_DIR) $(TEST_DIR)
	@echo "✓ Auto-fixes applied"

test: ## Run tests with pytest
	@echo "Running tests..."
	$(POETRY_RUN) pytest $(TEST_DIR) -v
	@echo "✓ Tests complete"

test-cov: ## Run tests with coverage report
	@echo "Running tests with coverage..."
	$(POETRY_RUN) pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term-missing --cov-report=html
	@echo "✓ Coverage report generated in htmlcov/"

test-watch: ## Run tests in watch mode
	@echo "Running tests in watch mode..."
	$(POETRY_RUN) pytest-watch $(TEST_DIR) -v

security: ## Run security checks with bandit
	@echo "Running security checks..."
	$(POETRY_RUN) bandit -r $(SRC_DIR) -c pyproject.toml
	@echo "✓ Security checks complete"

run: ## Run the application
	@echo "Starting inventory sync application..."
	$(POETRY_RUN) python -m src.cli

run-dev: ## Run the application in development mode
	@echo "Starting inventory sync application (dev mode)..."
	FLASK_ENV=development $(POETRY_RUN) python -m src.cli

clean: ## Clean up generated files and caches
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	rm -rf htmlcov/ .coverage coverage.xml
	@echo "✓ Cleanup complete"

check: fmt-check lint test ## Run all checks (format, lint, test)

all: clean install fmt lint test ## Clean, install, format, lint, and test

update: ## Update dependencies
	@echo "Updating dependencies..."
	$(POETRY) update
	@echo "✓ Dependencies updated"

lock: ## Generate poetry.lock file
	@echo "Generating lock file..."
	$(POETRY) lock --no-update
	@echo "✓ Lock file generated"

show: ## Show installed packages
	$(POETRY) show

shell: ## Open a poetry shell
	$(POETRY) shell
