.PHONY: run
run:
	uvicorn src.app:app --reload

.PHONY: android
android:
	uvicorn src.app:app --reload --host 0.0.0.0