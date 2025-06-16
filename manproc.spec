%global debug_package %{nil}

Name:           manproc
Version:        0.0.1
Release:        1
Summary:        Man manual translation.

License:        GPLv3+
URL:            https://github.com/lxb162649/manproc
Source0:        %{name}-%{version}.tar.gz

Requires:  git 
Requires:  yum-utils
Requires:  wget
Requires:  rpm-build
Requires:  diffutils

%description
This project is used to handle the translation of man manuals under the CQ system.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

make install \
    DESTDIR=$RPM_BUILD_ROOT \
    PREFIX=/usr \
    SYSCONFDIR=/etc

%files
%{_bindir}/*

%changelog
* Mon Jun 16 2025 Xuebing Li <lixuebing@cqsoftware.com.cn> - 0.0.1-1
- Initial release