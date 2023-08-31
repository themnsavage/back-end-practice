.PHONY: deploy build delete

build:
	@sam build

deploy: build
	@sam deploy --template-file template.yaml --stack-name back-end-practice --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

delete:
	@sam delete --stack-name back-end-practice
