# Legends of Runeterra Loc-bin-file Reader & Writer
《符文之地》本地化二进制文件读取和写入工具
## 用法
    import bin
    bin.reader([ET].bin, [ET].txt)
    # 对比新老英文，参考繁中，维护简中词典
    bin.writer(E.bin, C.txt, C.bin)
## About LoR
* 和 LoR 打交道期间接触了不少有趣的东西，全部都没学精，但大致认识了一些知名或小众软件。
* 读取和写入工具是我的第一个 Python 项目。花了几分钟粗略了解`bin`文件结构后，装好多年没碰的 C++ 读二进制文件把自己搞晕了，转投从没用过的 Python 花半个晚上熟悉基础代码，随时查`struct`模块文档后，当天就写完了。
* 后来轻松从打包文件中提取`.wem`。
* 简中文件我维护到`2.18C修复85版.bin`(2021-10-25)，之后回想了一下和拳头的过往，决定不再维护。
  * 同样从Riot API进货，我获取的数据稍微多点，统计出了一年多来DAU的图表，发到英文社区就被封了。几个官方英文渠道和大陆渠道都假装回复，问违反了哪天规定又装死。最后都不了了之。这些数据本来就是你们给的，我坚持维护公平却被永封，创造不公平性的若干号却只是暂时封禁。
  * 我提交的5个issue中，有2个被答复`We're looking into it.`，5个全都不了了之。
  * 小语种官媒整活不止一次。
  * 客户端问题越来越多：残留N年的漏洞，强制只留一种配音，增加校验，繁中字库缺字……
# Riot API
(pending)
* 普通 app：每小时 100 次对局详情，200 次对局列表。
* 默认对局用假邮箱服务注册 600 个拳头账号，用临时密钥辅助查询对局，可突破部分瓶颈。
# lor.mobalytics.gg API
(pending)
# Magic Set Editor LoR mod
在 kinotherapy 第一次重构前我就改了亿点点，索性不管了。
[原项目](https://magicseteditor.boards.net/thread/988/lor-template-pack-worldwalker-update)
