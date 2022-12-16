**Logging.conf**里配置日志等级，是否打印及控制台输出等

文件直接调用

```python
#t_log.py

import logging.config

logging.config.fileConfig("./logging.conf")
logger = logging.getLogger("spider")

logger.debug("this is a test")
```

可作为工程化项目日志使用