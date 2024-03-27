be-dev:
	cd aws && cdk synth && cdklocal bootstrap && cdklocal deploy
be-deploy:
	cd aws && npx cdk bootstrap --profile nk aws://147123257637/ap-southeast-1 --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess && cdk deploy --profile nk
be-test:
	cd aws && cdk synth && python3 -m unittest tests/unit/test_common.py
be-mock:
	sh mock.sh
be-setup:
		cd aws &&  rm -rf ./.venv && \
		python3 -m venv .venv && \
		. .venv/bin/activate && \
		python3 -m pip install -r requirements.txt
fe-setup:
	cd fe && yarn
fe-deploy:
	echo "pushcode"