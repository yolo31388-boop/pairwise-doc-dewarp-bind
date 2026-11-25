# pairwise-doc-dewarp-bind

## 领域

游戏、图形与多媒体

## 主题

扫描书页弯曲矫正

## 说明

曲面网格建模、曲线行检测与双页拆分。

初始状态下 `imaging/doc_dewarp.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
