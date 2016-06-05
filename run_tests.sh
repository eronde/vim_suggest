#!sh


set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function usage {
  echo "Usage: $0" 
  exit 0
}
#docker rm bigram_suggest_test 2>/dev/null
#3docker run -it --name bigram_suggest_test --rm -v $(pwd)/:/code bigram_suggest py.test app/tests -vvv
# docker run -it --name bigram_suggest_test --rm -v $(pwd)/:/code bigram_suggest nosetests app/tests -v
py.test -vv "$SCRIPT_DIR/app/tests"
