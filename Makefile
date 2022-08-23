.PHONY: build build_search_engine_crawler build_search_engine_ui \
	test test_search_engine_crawler test_search_engine_ui \
	clean


build: build_search_engine_crawler build_search_engine_ui

build_search_engine_crawler: search_engine_crawler
	cd search_engine_crawler && docker build -t $(USERNAME)/search_engine_crawler .

build_search_engine_ui: search_engine_ui
	cd search_engine_ui && docker build -t $(USERNAME)/search_engine_ui .

search_engine_crawler:
	git clone git@github.com:$(USERNAME)/search_engine_crawler.git

search_engine_ui:
	git clone git@github.com:$(USERNAME)/search_engine_ui.git


test: test_search_engine_crawler test_search_engine_ui

test_search_engine_crawler:
	docker run --rm --entrypoint python $(USERNAME)/search_engine_crawler -m unittest discover -s tests/

test_search_engine_ui:
	docker run --rm $(USERNAME)/search_engine_ui python -m unittest discover -s tests/


clean:
	rm -rf search_engine_crawler search_engine_ui
