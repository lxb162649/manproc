# 目录

- [简介](#简介)
- [引入说明](#引入说明)
- [使用场景](#使用场景)
- [常见用法](#常见用法)
- [修改及适配](#修改及适配)
	- [长擎定制修改](#长擎定制修改)
	- [适配其他系统](#适配其他系统)
- [注意事项](#注意事项)
- [参考链接](#参考链接)

# 简介

此项目用于处理CQ系统下的man手册翻译。

# 引入说明

暂不引入

# 使用场景

处理CQ系统下的man手册翻译

# 常见用法



## 步骤 1: 克隆包（克隆到当前目录下）

bash
```bash
manproc package -cl
```

**功能说明**：

- 若当前目录下不存在目标包，自动从指定仓库克隆该包到当前目录
- 若包已存在，则删除该包重新克隆

**执行逻辑**：

1. 检查当前目录是否存在目标包目录
2. 若不存在，则调用 `git clone` 从配置的仓库地址克隆
3. 若存在，则输出提示信息并跳过克隆

## 步骤 2: 解压 man 文件到 SOURCES/man 目录

bash
```bash
manproc package -e
```

**功能说明**：

- 从 spec 文件识别包含 man 手册的主包及子包
- 自动安装相关包并提取 man 手册路径
- 将 man 文件复制到 `SOURCES/man` 目录并解压

**执行逻辑**：

1. 解析 spec 文件，识别包含 `%{_mandir}` 的子包
2. 使用 `yum install` 或 `yum reinstall` 安装相关包
3. 通过 `rpm -ql` 命令查询 man 手册文件路径
4. 创建 `SOURCES/man` 目录
5. 复制 gzip 压缩的 man 文件到 `SOURCES/man` 目录并解压

### 步骤 3: 翻译 man 文件并更新 README.md

**操作说明**：

1. 手动翻译 `SOURCES/man` 目录下的 man 文件
2. 保持 man 手册语法格式（如 `.TH`、`.SH` 标签）
3. 更新项目 README.md

**翻译规范**：

- 翻译后文件需与原文件同名，存放路径保持一致
  （例如：原路径 `SOURCES/man/xxx.3`，翻译后仍存于此路径）

- 保持 man 手册特有的标记语法：

  plaintext
```plaintext
.TH "标题" "章节号" "日期" "版本" "手册名称"  # 文档头部
.SH "NAME"                                  # 名称章节
.SH "SYNOPSIS"                              # 概要章节
.SH "DESCRIPTION"                           # 描述章节
.IP "-f" "4"                                # 选项说明（缩进4格）
```

- 特殊符号（如 `-`、`.`）需保留原始格式

**README 更新**：

- 根据模板手动更新

### 步骤 4: 生成补丁并修改 SPEC 文件

bash
```bash
manproc package -p
```

**功能说明**：

1. 创建源码对比目录并整合翻译文件
2. 生成 diff 补丁文件
3. 自动修改 spec 文件（补丁引用、安装命令、版本号更新等）

**执行逻辑**：

1. 复制 `BUILD` 目录下的源码至 `BUILD/***-diff` 目录
2. 将翻译后的 man 文件移动至 `BUILD/***-diff` 对应位置
3. 执行 `diff -Nuar` 生成补丁文件（默认命名为 `cqos-func-add-chinese-man-page.patch`）
4. 修改 spec 文件：
   - 检查并移除无效宏（`anolis_release|rhel|fedora`）
   - 增加版本号（`release +1`）
   - 根据 spec 文件是否已存在补丁及打补丁方式（自动/手动），在最后一个 `Source` 行或 `Patchx` 行下添加编号递增的 Patch 行（如 Patch0 或 Patch (x+1)），并在手动打补丁的 `%setup` 行后添加对应 %patch 命令，自动打补丁则跳过命令添加
   - 在 `%install` 行下添加创建中文man手册目录及安装翻译后man文件的相关命令。
   - 在spec文件中，为每个以 `%{_mandir}` 开头的行追加对应的中文目录行（即在原路径后添加 `/zh_CN/`），确保中文man手册文件被正确包含在rpm包中。
   - 在spec文件的 `%changelog` 区块下自动添加包含当前日期、用户信息、版本号的更新日志，并提供可自定义的默认日志内容。

### 步骤 5: 编译

bash
```bash
manproc package -co
```

**功能说明**：

- 基于修改后的 spec 文件构建 rpm 包
- 成功编译则清理操作
- 展示构建好的 rpm 包
- 验证 man 手册是否正确安装

**执行逻辑**：

1. 执行 `rpmbuild -ba` 命令构建 rpm 包
2. 成功编译则执行 `rpmbuild -bp` 操作
3. 展示构建好的 rpm 包（分 `noarch` 及 `x86_64`）
4. 安装 rpm 包，通过 `rpm -ql` 及 `grep /usr/share/man` 查找 man 手册并打印其路径

### 步骤 6: 上传

bash
```bash
manproc package -u
```

**功能说明**：

- 将编译好的 rpm 包上传至指定仓库

**执行逻辑**：

1. 检查 `RPMS` 目录下是否存在目标 rpm 包
2. 根据配置的仓库地址，执行上传命令
3. 验证上传结果并输出状态信息

# 修改及适配

该项目为自研项目

# 注意事项

- 除克隆操作包的参数必须为包名外，其他操作包的参数可以为绝对路径，也可以为包名（此时此包应在当前目录）
- 如果 spec 文件为自动打补丁 `%autosetup` 模式，则根据情况判断是否需要在此行尾部增加 `-p1`
- 如果编译失败，报错找不到相关目录，需要查看 `%install` 下添加的命令，主要看如 `LWP-Protocol-https-%{version}` 是否为 BUILD 目录下的源码名，如果不是请修改，如果是请查找该行下面是否有删除 `$RPM_BUILD_ROOT` 的操作，如果有，将添加的命令放到该行下面

# 参考链接

- [manproc 官方网站](https://github.com/lxb162649/manproc)
