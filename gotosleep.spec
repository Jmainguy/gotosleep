%if 0%{?rhel} == 7
  %define dist .el7
%endif
%define _unpackaged_files_terminate_build 0
Name: gotosleep
Version: 0.1
Release:    1%{?dist}
Summary: A golang daemon for shutting computer down at a specified time of day.

License: GPLv2
URL: https://github.com/Jmainguy/gotosleep
Source0: gotosleep.tar.gz
Requires(pre): shadow-utils

%description
A golang daemon for shutting computer down at a specified time of day.

%prep
%setup -q -n gotosleep
%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -p $RPM_BUILD_ROOT/etc/gotosleep
install -m 0755 $RPM_BUILD_DIR/gotosleep/gotosleep %{buildroot}/usr/sbin
install -m 0644 $RPM_BUILD_DIR/gotosleep/service/gotosleep.service %{buildroot}/usr/lib/systemd/system
install -m 0644 $RPM_BUILD_DIR/gotosleep/config.yaml %{buildroot}/etc/gotosleep/

%files
/usr/sbin/gotosleep
/usr/lib/systemd/system/gotosleep.service
%dir /etc/gotosleep
%config(noreplace) /etc/gotosleep/config.yaml

%pre

%post
if [ -f /usr/bin/systemctl ]; then
  systemctl daemon-reload
fi

%changelog
