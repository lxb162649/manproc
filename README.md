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

```bash
# 步骤1: 克隆包
manproc package -cl

# 步骤2: 解压 man 文件到 SOURCES/man 目录
manproc package -e

# 步骤3: 翻译man文件并更新README.md

# 步骤4: 生成补丁并修改SPEC文件
manproc package -p

# 步骤5: 编译
manproc package -co

# 步骤6: 上传
manproc package -u
```

# 修改及适配

该项目为自研项目

# 注意事项

无

# 参考链接

- [manproc 官方网站](https://github.com/lxb162649/manproc)
