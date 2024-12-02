# FLA_AutoTester

目前踩的坑：

1. GPT让我用python:3.10-slim作为基础image，但是我无论从官方源还是国内docker镜像源都没法直接通过命令行运行docker build拉取（不排除是我自己网络问题）。之后考虑到大家应该更多会使用ubuntu环境，就手动在docker desktop上搜索了ubuntu:22.04然后pull下来了，以这个最基础的纯净ubuntu来构建整个实验环境，运行docker build(`docker build -t flask-test-server .`)是可行的。
2. docker build时配置ubuntu环境最好换源，目前dockerfile已修改换源，同时由于docker构建时一旦某一个环境配置出错就会终止，加上了--fix-missing参数来跳过失败项最后再尝试修复。



理论上，如果你可以build成功(我已经能build了)，后面运行一下就可以看看flask和自动测试的脚本gpt写的咋样了，不过我相信肯定还是有不少坑等着呢。

目前我就是完全遵照郭骁学长的路子走的，问了gpt他也觉得更好，最后我还附了我前期的gpt记录(GPT.md)，后续就是我push GPT微调dockerfile的过程，别的部分没有修改。