dev:
	cdk synth && cdklocal bootstrap && cdklocal deploy
deploy:
	npx cdk bootstrap --profile nk aws://147123257637/ap-southeast-1 --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess && cdk deploy --profile nk
test:
	cdk synth && python3 -m unittest tests/unit/test_common.py
mock:
	sh mock.sh
setup:
		rm -rf ./.venv && \
		python3 -m venv .venv && \
		. .venv/bin/activate && \
		python3 -m pip install -r requirements.txt