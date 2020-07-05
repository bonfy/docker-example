project_name=app-python
username=bonfy
image_name=$(username)/$(project_name)
container_name=$(username)-$(project_name)

image:
	@echo Creating image $(image_name)...
	docker build -t $(image_name) .
run:
	@echo Creating container $(container_name)...
	docker run --name $(container_name) $(image_name)
clean:
	@echo Remove container $(container_name)...
	docker rm -f $(container_name)
