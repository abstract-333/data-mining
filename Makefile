.PHONY: run
run:
	uvicorn --factory src.app:app_factory --reload

.PHONY: android
android:
	uvicorn --factory src.app:app_factory --reload --host 0.0.0.0