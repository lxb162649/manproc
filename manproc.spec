%global debug_package %{nil}

Name:           manproc
Version:        0.0.1
Release:        2
Summary:        Man manual translation.

License:        GPLv3+
URL:            https://github.com/lxb162649/manproc
Source0:        %{name}-%{version}.tar.gz
Patch0:   cqos-func-optimized-code.patch

Requires:  git 
Requires:  yum-utils
Requires:  wget
Requires:  rpm-build
Requires:  diffutils

%description
This project is used to handle the translation of man manuals under the CQ system.

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/*

%changelog
* Fri Jun 20 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-2
- 优化代码

* Mon Jun 16 2025 Xuebing Li <lixuebing@cqsoftware.com.cn> - 0.0.1-1
- Initial release