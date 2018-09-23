clean:
	rm -rf ./tests/*pyc ./tests/__pycache__ ./py_word_suggest/*pyc ./py_word_suggest/__pycache__

pytest:
	  docker-compose run --rm python366 bash run_tests.sh

dev:
	bash ./test_on_change.sh


shell:
	  docker-compose run --rm python366 bash
