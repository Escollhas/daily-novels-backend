.PHONY: publish-exchanges clean

.DEFAULT_GOAL := help

publish-exchanges:
	python3 backend/events/publishers.py

clean:
	@find ./ -type d -name 'dist' -exec rm -rf {} +;
	@find ./ -type d -name 'build' -exec rm -rf {} +;
	@find ./ -type d -name '*.egg-info' -exec rm -rf {} +;
	@find ./ -type d -name '.pytest_cache' -exec rm -rf {} +;
	@find ./ -type d -name '__pycache__' -exec rm -rf {} +;
	@find . -type d -name "__pycache__" -delete

help:
	@echo "Makefile Help"
	@echo "-----------------"
	@echo "Use make <target> where <target> is one of:"
	@echo "publish-exchanges Publish in RabbitMQ instance all exchanges"
