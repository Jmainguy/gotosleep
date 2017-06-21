# This expects a few requirements
# one, that https://github.com/Jmainguy/docker_rpmbuild is cloned into ~/Github/docker_rpmbuild
# two, that docker is installed and running
# three, that ~/Github/docker_rpmbuild/dockerbuild/build.sh centos7 has been run
rpm:
	@go build
	@tar -czvf ~/Github/docker_rpmbuild/rpmbuild/SOURCES/gotosleep.tar.gz ../gotosleep
	@cp gotosleep.spec ~/Github/docker_rpmbuild/rpmbuild/SPECS/gotosleep.spec
	@cd ~/Github/docker_rpmbuild/; ./run.sh centos7 gotosleep
	@ls -ltrh ~/Github/docker_rpmbuild/rpmbuild/RPMS/x86_64/gotosleep*
