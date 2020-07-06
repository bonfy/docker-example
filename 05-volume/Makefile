project_name=app-volume
username=bonfy
image_name=$(username)/$(project_name)
container_name=$(username)-$(project_name)
local_log_path=/tmp/volume/log

image:
	@echo Creating image $(image_name)...
	docker build -t $(image_name) .
run:
	@echo Creating container $(container_name)...
	docker run -v $(local_log_path):/log --name $(container_name) $(image_name) 
clean:
	@echo Remove container $(container_name)...
	docker rm -f $(container_name)
