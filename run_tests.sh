#!sh


set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function usage {
  echo "Usage: $0" 
  exit 0
}
#docker rm bigram_suggest_test 2>/dev/null
#docker run -it --name py_word_suggest_test --rm -v $(pwd)/:/code py_word_suggest py.test tests
#docker run -it --name py_word_suggest_test --rm -v $(pwd)/:/code py_word_suggest nosetests tests -v
py.test -vv "$SCRIPT_DIR//tests"
# nosetests -vv "$SCRIPT_DIR/app/tests"
