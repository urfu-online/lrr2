REQ_FILES = \
	requirements/base \
	requirements/dev \
	requirements/production

compile-requirements:
	pip-compile -v --upgrade -o requirements/pip-tools.txt requirements/pip-tools.in
	pip install -r requirements/pip-tools.txt

	for f in $(REQ_FILES); do \
		echo ; \
		echo "== $$f ===============================" ; \
		echo "pip-compile -v --rebuild --upgrade -o $$f.txt $$f.in"; \
		pip-compile -v --rebuild --upgrade -o $$f.txt $$f.in || exit 1; \
	done

dev-requirements: compile-requirements
	pip-sync requirements/dev.txt

prod-requirements: compile-requirements
	pip-sync requirements/production.txt