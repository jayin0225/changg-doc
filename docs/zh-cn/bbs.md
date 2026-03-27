> [!TIP|style:callout|label:用户须知|iconVisibility:hidden]
    1、电影院还在**上映**的电影是没有资源的，站长也不会分享电影院里的录制版本（TC版）污眼睛  
    2、影视资源都可以保存到自己的网盘后**在线观看**,当然在**电视上安装TV版APP**也可以在线播放  
    3、高评分电影可以搜 **豆瓣TOP250** 或 **IMDB top250** 一般里面都有  
    4、资源失效、求资源可下方**留言**或进Q群@群主,留言最好说清楚,同名资源太多。站长也方便寻找  
    5、只分享绿色健康的资源,想要违规资源,免开尊口

---

<p align="center"><b><font color="red">如果留言板没打开,多等一会儿或按一下F5刷新</font></b></p>

## 留言板：

<head>
<!-- Waline 评论系统 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@waline/client@3/dist/waline.css" onerror="this.href='https://unpkg.com/@waline/client@v3/dist/waline.css'">
</head>
<body>
<div id="waline"></div>
<script src="https://cdn.jsdelivr.net/npm/@waline/client@3/dist/waline.umd.js" onerror="this.src='https://unpkg.com/@waline/client@v3/dist/waline.umd.js'">
</script>
<script>
    // 页面加载完成后初始化 Waline
    document.addEventListener('DOMContentLoaded', function() {
        console.log('[Waline] 尝试初始化...');
        
        const container = document.querySelector('#waline');
        console.log('[Waline] #waline 容器:', container);
        
        if (!container) {
            console.log('[Waline] 未找到 #waline 容器，跳过');
            return;
        }
        
        // 检查是否已初始化
        if (container.hasAttribute('data-waline-initialized')) {
            console.log('[Waline] 已经初始化过，跳过');
            return;
        }
        
        if (typeof Waline === 'undefined') {
            console.error('[Waline] Waline 对象未定义，初始化失败');
            return;
        }
        
    init({
                el: '#waline',
                serverURL: 'https://waline.haozy.top',
                lang: 'zh-CN',
                path: location.pathname,
                meta: ['nick', 'mail'],
                requiredMeta: ['nick'],
                avatar: 'none',
                pageSize: 6,
                commentSorting: 'latest',
                imageUploader: false,
                noCopyright: false,
                search: false,
                login: 'disable',
                reaction: false,
                recordIP: false,
                pageview: false,
                emoji: [
                    'https://cdn.jsdelivr.net/npm/@waline/emojis@1.4.0/qq',
                    'https://cdn.jsdelivr.net/npm/@waline/emojis@1.4.0/bilibili',
                ],
                locale: {
                    nickRequired: "请输入昵称",
                    nick: '昵称',
                    nickError: '昵称不能小于2字符',
                    mail: '邮箱',
                    mailError: '邮件地址不正确',
                    word: '字',
                    wordHint: '评论字数应在 $0 到 $1 字之间！\n当前字数：$2',
                    anonymous: '匿名',
                    placeholder: '留言请提供资源类型...',
                    spam: '评论内容包含广告或垃圾信息，已被删除',
                    submit: '提交',
                    reply: '回复',
                    cancelReply: '取消回复',
                    level0: '潜水',
                    level1: '冒泡',
                    level2: '吐槽',
                    level3: '活跃',
                    level4: '话痨',
                    level5: '传说',
                    refresh: '刷新',
                    more: '更多...',
                    preview: '预览',
                    emoji: '表情',
                    seconds: '秒前',
                    minutes: '分钟前',
                    hours: '小时前',
                    days: '天前',
                    now: '刚刚',
                    sticky: '置顶',
                    required: '必填项',
                    empty: '留言不能为空',
                    comment: '条留言',
                },
                highlighter: false,
                texRenderer: false,
            });
            container.setAttribute('data-waline-initialized', 'true');
            console.log('[Waline] 初始化成功');
        } catch (error) {
            console.error('[Waline] 初始化失败:', error);
        }
    });
</script>
</body>