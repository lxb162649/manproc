%global debug_package %{nil}

Name:           manproc
Version:        1.0.0
Release:        2
Summary:        Man manual translation.

License:        GPLv3+
URL:            https://github.com/lxb162649/manproc
Source0:        %{name}-%{version}.tar.gz
Patch0:   cqos-fix-adjust-invalid-macro-removal-position.patch

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
* Fri Jun 27 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 1.0.0-2
- 更改移除无效宏操作的位置

* Thu Jun 26 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 1.0.0-1
- 整合 patch，升级版本到 1.0.0

* Thu Jun 26 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-8
- 修复缩进问题

* Wed Jun 25 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-7
- 修复获取man手册字符串数组

* Wed Jun 25 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-6
- 增加不包含man手册的处理

* Tue Jun 24 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-5
- 修复安装生成包后显示man手册路径问题

* Mon Jun 23 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-4
- 修复获取源码包去掉版本号名出错的问题

* Mon Jun 23 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-3
- 修复manproc中修改spec文件的问题

* Fri Jun 20 2025 lixuebing <lixuebing@cqsoftware.com.cn> - 0.0.1-2
- 优化代码

* Mon Jun 16 2025 Xuebing Li <lixuebing@cqsoftware.com.cn> - 0.0.1-1
- Initial release