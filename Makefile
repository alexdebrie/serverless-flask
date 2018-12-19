
SDK_DIR=sdk

$(SDK_DIR):
	mkdir -p $(SDK_DIR)

generate-openapi: $(SDK_DIR)
	$(shell serverless invoke local -f openapi > $(SDK_DIR)/openapi.json)

generate-client: generate-openapi
ifdef lang
	mkdir -p $(SDK_DIR)/$(lang)
	docker run --rm -v "$(PWD)/$(SDK_DIR):/local" openapitools/openapi-generator-cli generate \
	-i /local/openapi.json \
	-g $(lang) \
	-o /local/$(lang)
	@echo "SDK output to $(SDK_DIR)/$(lang)"
else
	@echo "Please specify language with lang="
	@echo "Example: make lang=typescript-axios generate-client"
endif
