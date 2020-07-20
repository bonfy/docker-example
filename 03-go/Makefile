project_name=app-go
username=bonfy
image_name=$(username)/$(project_name)
container_name=$(username)-$(project_name)

image:
	@echo Creating image $(image_name)...
	CGO_ENABLED=0 GOOS=linux go build -o app
	docker build -t $(image_name) .
	rm -f app
run:
	@echo Creating container $(container_name)...
	docker run -p 8889:8888 --name $(container_name) $(image_name)
clean:
	@echo Remove container $(container_name)...
	docker rm -f $(container_name)
