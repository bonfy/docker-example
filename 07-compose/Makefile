project_name=app-pycompose
username=bonfy
image_name=$(username)/$(project_name)
container_name=$(username)-$(project_name)
container_port=9000

image:
	@echo Creating image $(image_name)...
	docker build -t $(image_name) .
run:
	@echo Creating container $(container_name)...
	docker run -p $(container_port):8888 --name $(container_name) $(image_name)
clean:
	@echo Remove container $(container_name)...
	docker rm -f $(container_name)
