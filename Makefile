# This file contains a make script for the PathProwler application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/core/*.py
TEMPLATE_FILES=src/templates/*.html
RES_FILES=res/*.csv res/*.json
RES_SECRET_FILES=res/*.key res/*.crt

BUILD_DIR=bin/pathprowler
TEMPLATE_DIR=templates
RES_DIR=res
RES_SECRET_DIR=bin/secret

# This rule builds the application
build: $(SRC_FILES) $(DATA_FILES)
	mkdir -p $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)/$(TEMPLATE_DIR)
	mkdir -p $(BUILD_DIR)/$(RES_DIR)
	mkdir -p $(RES_SECRET_DIR)
	cp $(SRC_FILES) $(BUILD_DIR)
	cp $(TEMPLATE_FILES) $(BUILD_DIR)/$(TEMPLATE_DIR)
	cp $(RES_FILES) $(BUILD_DIR)/$(RES_DIR)
	cp $(RES_SECRET_FILES) $(RES_SECRET_DIR)

# This rule cleans the build directory
clean: $(BUILD_DIR)
	rm -r $(BUILD_DIR)/*
	rmdir $(BUILD_DIR)
	rm -r $(RES_SECRET_DIR)/*
	rmdir $(RES_SECRET_DIR)
